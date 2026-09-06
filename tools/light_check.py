#!/usr/bin/env python3
# Last updated: 2026-09-03 (Buenos Aires) by a Precedent beta-test session, to version 2
"""light_check.py — this repo's own sanity net, beyond BestPractice's doc_lint.py.

Repo-owned tool, per precedent-team-maintainers's `light-check` practice
Detail section ("a repo that vendors this set would extend the check with
that piece itself"): under Precedent, a team practice set is resolved live
from a sibling clone rather than vendored, so there is no shared
`light_check.py` to inherit — each consuming repo keeps its own, informed by
the team practice's Rule but adapted to what this repo actually has on disk.

This replaces the pre-Precedent version that lived at
process/personal/tools/light_check.py (vendored from RepoPersonalPreferences,
retired 2026-09-02 — see process/PRECEDENT_MIGRATION.md). Checks 7-10 of that
version (personal-pack-vendored, pending-drift, private-repo-name-leak,
rule-citation-by-slug) all assumed a `process/personal/` vendored tree with
its own `README.md` anchors; that surface no longer exists under the
three-source model, so those checks are dropped rather than carried forward
broken. Check 7 below is their honest replacement, pointed at the config
surfaces this repo actually has now: `process/manifest.json` (still a real
vendored install) and `precedent.json` (new).

doc_lint.py (process/upstream/tools/doc_lint.py) is Markdown-specific. This
runs on every changed file, of every type, looking for the class of mistake
that isn't a style violation so much as "something obviously went wrong":

  1. MERGE-CONFLICT MARKERS left in a tracked file (a resolve that missed one).
  2. INVALID JSON in a changed .json file.
  3. INVALID YAML in a changed .yml/.yaml file (skipped with a notice if
     PyYAML isn't installed — same graceful-degradation pattern as doc_lint's
     cmark-gfm check).
  4. INVALID PYTHON SYNTAX in a changed .py file (ast.parse).
  5. SECRET-SHAPED STRINGS: an AWS-style access key ID, a private-key PEM
     header, or a GitHub-style token — coarse and conservative on purpose, to
     keep false positives near zero.
  6. BROKEN RELATIVE DOC LINKS (warning only): a markdown link whose target
     isn't a URL, an anchor, or a file that actually exists.
  7. PRACTICE SOURCES NOT TRACKED: process/manifest.json (the process/upstream/
     vendor tracking) is missing an expected field, unparseable, or records a
     local_path that doesn't exist on disk; or precedent.json is unparseable,
     a source is missing its 'path' field, or a source declares an
     individual-level set (the one thing a shared repo's tracked config must
     never do — see AGENTS.md's "Practice sources" section). Repo-wide, runs
     every time regardless of which files changed, the same way the old
     personal-pack-vendored check did: a `cp -r` or a hand-edited path
     wouldn't necessarily touch any file this run happens to be scoped to.
     A precedent.json source whose declared path just isn't checked out
     here (a sibling clone CI never has, or a session that hasn't fetched it
     yet) is a WARNING, not part of this gate — that's an environment fact,
     not a repo-content defect, and every CI run would otherwise fail on
     something CI can never satisfy.
  8. ON-DEMAND PRACTICES MATCHED (informational only, never a gate): for each
     changed file, which on-demand practices' `applies_to` glob matches it —
     the same lookup `tools/precedent_paths.py FILE` does by hand, run here
     automatically so it doesn't depend on a session remembering to ask.
     Added after a session reorganizing content/HUMANS_AT_OUR_BEST.md
     mis-capitalized a new header: `header-caps` matched the edited file and
     would have caught it, but nothing surfaced the rule because the session
     never ran precedent_paths.py against that file, only recalling a few
     slugs from memory instead. This closes that gap by making the surfacing
     automatic rather than something a session has to remember to trigger —
     see [`checkable-gets-checked`](../practices/checkable-gets-checked.md):
     a genuine mechanical check (the header-caps script) already exists for
     part of the rule, but the earlier miss was never reaching the rule's
     text at all, which no downstream mechanical check can catch after the
     fact.

Checks 1-5 and 7 are gates (FAIL, exit 1); check 6 is a warning, and so is
the "not checked out here" case within check 7 (see above). Check 8 never
fails or warns — it's a reminder to go read a Rule, not a defect. Checks 1-6
and 8 use the same scoping convention as doc_lint.py: by default, files
changed vs the default branch (committed + working tree); explicit paths
scan exactly those; --all scans every tracked text file and never fails
(backlog report only). Check 7 ignores file scoping — it always inspects the
whole repo, in every mode including --all, though --all still keeps it
non-fatal per that mode's own contract.

Run:  python3 tools/light_check.py            # changed-vs-default-branch, gate
      python3 tools/light_check.py --all       # whole repo, report-only
"""
import ast, json, pathlib, re, subprocess, sys

import precedent_paths

def _git(args, cwd=None):
    return subprocess.run(['git'] + args, cwd=cwd, capture_output=True, text=True).stdout.strip()

ROOT = pathlib.Path(_git(['rev-parse', '--show-toplevel'],
                         cwd=pathlib.Path(__file__).resolve().parent)
                    or pathlib.Path(__file__).resolve().parents[1])

# This file's own path is excluded from the secret scan below — it is the
# only file in the repo whose job is to spell out the patterns it looks for.
SELF = pathlib.Path(__file__).resolve().relative_to(ROOT).as_posix()

TEXT_EXT = {'.md', '.py', '.sh', '.json', '.txt', '.yml', '.yaml', '.toml', '.template'}

def _declared_base_branch(root):
    """The branch this repo's work is measured against, as DECLARED in
    precedent.json's `base_branch` -- not inferred from `origin/HEAD`.

    Two different questions with usually the same answer, which is why asking
    the wrong one survives so long. `origin/HEAD` answers "what does GitHub
    show first"; callers here mean "what lineage does this work belong to".
    They diverge the moment a repo pins its work to a branch that is not the
    configured default, and then every inference is quietly wrong with nothing
    failing. Returns None when undeclared or unreadable, so callers fall back
    to the old inference rather than breaking (practice: fail-gracefully).
    Enforced by precedent_check.py's `declared-base-branch`.
    """
    try:
        import json as _json, pathlib as _pathlib
        v = _json.loads((_pathlib.Path(root) / 'precedent.json')
                        .read_text(encoding='utf-8')).get('base_branch')
        return v if isinstance(v, str) and v.strip() else None
    except Exception:
        return None

def default_branch():
    declared = _declared_base_branch(ROOT)
    if declared:
        return declared
    head = _git(['symbolic-ref', 'refs/remotes/origin/HEAD'], cwd=ROOT)
    if head:
        return head.rsplit('/', 1)[-1]
    for cand in ('main', 'master'):
        if _git(['rev-parse', '--verify', '--quiet', f'origin/{cand}'], cwd=ROOT):
            return cand
    return 'HEAD'

def tracked_text():
    out = []
    for f in _git(['ls-files'], cwd=ROOT).split('\n'):
        if f and pathlib.PurePath(f).suffix.lower() in TEXT_EXT:
            out.append(f)
    return out

def changed_text():
    ref = f'origin/{default_branch()}'
    base = _git(['merge-base', 'HEAD', ref], cwd=ROOT) or ref
    committed = _git(['diff', '--name-only', '--diff-filter=d', base], cwd=ROOT).split('\n')
    worktree = _git(['diff', '--name-only', '--diff-filter=d'], cwd=ROOT).split('\n')
    staged = _git(['diff', '--name-only', '--diff-filter=d', '--cached'], cwd=ROOT).split('\n')
    files = {f for f in committed + worktree + staged
             if f and pathlib.PurePath(f).suffix.lower() in TEXT_EXT}
    return sorted(files)

try:
    import yaml
    HAVE_YAML = True
except Exception:
    HAVE_YAML = False

CONFLICT_RE = re.compile(r'^(<{7} |={7}$|>{7} )')

# Deliberately coarse and conservative — a handful of unmistakable shapes,
# not a general secret scanner.
SECRET_PATTERNS = [
    ('AWS access key ID', re.compile(r'AKIA[0-9A-Z]{16}')),
    ('private-key PEM header', re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----')),
    ('GitHub token', re.compile(r'gh[pousr]_[A-Za-z0-9]{36}')),
]

LINK_RE = re.compile(r'\[[^\]]*\]\(([^)]+)\)')

def check_conflicts(path, text, fails):
    for i, line in enumerate(text.splitlines(), 1):
        if CONFLICT_RE.match(line):
            fails.append(f"CONFLICT MARKER: {path}:{i}: {line.strip()[:80]}")

def check_json(path, text, fails):
    try:
        json.loads(text)
    except json.JSONDecodeError as e:
        fails.append(f"INVALID JSON: {path}: {e}")

def check_yaml(path, text, fails, warns):
    if not HAVE_YAML:
        return
    try:
        list(yaml.safe_load_all(text))
    except Exception as e:
        fails.append(f"INVALID YAML: {path}: {e}")

def check_python(path, text, fails):
    try:
        ast.parse(text, filename=path)
    except SyntaxError as e:
        fails.append(f"INVALID PYTHON: {path}:{e.lineno}: {e.msg}")

def check_secrets(path, text, fails):
    if path == SELF:
        return
    for name, pat in SECRET_PATTERNS:
        m = pat.search(text)
        if m:
            fails.append(f"SECRET-SHAPED STRING: {path}: looks like a {name} ({m.group(0)[:12]}…)")

def check_links(path, text, warns):
    base = (ROOT / path).parent
    for m in LINK_RE.finditer(text):
        target = m.group(1).strip()
        if not target or target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        target = target.split('#', 1)[0]
        if not target:
            continue
        if not (base / target).exists() and not (ROOT / target.lstrip('/')).exists():
            warns.append(f"BROKEN LINK: {path}: -> {target}")

def check_upstream_manifest(fails):
    manifest_path = ROOT / 'process' / 'manifest.json'
    rel = 'process/manifest.json'
    if not manifest_path.exists():
        return  # nothing vendored under process/upstream/ at all
    try:
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        fails.append(f"UPSTREAM NOT TRACKED: {rel} is not valid JSON: {e}")
        return
    upstream = manifest.get('upstream') or {}
    if not upstream.get('commit'):
        fails.append(f"UPSTREAM NOT TRACKED: {rel} has no upstream.commit recorded.")
    entries = manifest.get('entries')
    if not entries:
        fails.append(f"UPSTREAM NOT TRACKED: {rel} has no 'entries'.")
        return
    for entry in entries:
        local_path = entry.get('local_path')
        if local_path and not (ROOT / local_path).exists():
            fails.append(
                f"UPSTREAM NOT TRACKED: {rel} entry '{entry.get('practice', '?')}' "
                f"records local_path '{local_path}', which doesn't exist — "
                "partial or stale install.")

def check_precedent_sources(fails, warns):
    cfg_path = ROOT / 'precedent.json'
    rel = 'precedent.json'
    if not cfg_path.exists():
        return  # Precedent not wired into this repo (or not yet)
    try:
        cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        fails.append(f"PRECEDENT SOURCE NOT TRACKED: {rel} is not valid JSON: {e}")
        return
    for entry in cfg.get('sources', []):
        level = entry.get('level')
        if level == 'individual':
            fails.append(
                f"PRECEDENT SOURCE LEAK: {rel} declares an individual source "
                f"({entry.get('name')!r}) — a shared repo's tracked config must "
                "never name a person's individual set (leaks its existence and "
                "location to everyone with read access). Move it to the "
                "person's own user-level config instead.")
            continue
        path = entry.get('path')
        if not path:
            fails.append(f"PRECEDENT SOURCE NOT TRACKED: {rel} source {entry.get('name')!r} has no 'path'.")
            continue
        resolved = (ROOT / path).resolve()
        if not resolved.is_dir():
            # Warning, not a gate: a sibling clone is an ENVIRONMENT fact, not
            # a repo-content fact -- CI checks out only this one repo, so a
            # team source's sibling path is structurally never present there,
            # same as any other CI runner or fresh clone that hasn't fetched
            # it yet. precedent_resolve.py's own design treats a missing
            # source as "report it, don't fail" for exactly this reason
            # (PRACTICE_ENGINE_PLAN.md: "degrading gracefully is part of the
            # contract, not an error path"); this check follows suit instead
            # of gating every CI run on something CI can never satisfy.
            warns.append(
                f"PRECEDENT SOURCE NOT CHECKED OUT: {rel} source {entry.get('name')!r} "
                f"(level {level!r}) points at '{path}', which doesn't exist here "
                f"({resolved}) — a sibling clone that hasn't been checked out yet "
                "(expected in CI; see AGENTS.md's 'Build-environment gotchas' if "
                "this is a session that should have it), or a stale path.")

def check_applicable_practices(files, notes):
    # practice: checkable-gets-checked
    # matches_for_paths already returns at most one (slug, path) pair per
    # slug -- no dedup needed here.
    for slug, path in precedent_paths.matches_for_paths(files):
        notes.append(f"{slug} — {path}")

def check_file(rel, fails, warns):
    p = ROOT / rel
    if not p.exists() or not p.is_file():
        return
    text = p.read_text(encoding='utf-8', errors='ignore')
    suf = p.suffix.lower()
    check_conflicts(rel, text, fails)
    check_secrets(rel, text, fails)
    if suf == '.json':
        check_json(rel, text, fails)
    elif suf in ('.yml', '.yaml'):
        check_yaml(rel, text, fails, warns)
    elif suf == '.py':
        check_python(rel, text, fails)
    elif suf == '.md':
        check_links(rel, text, warns)

def main():
    args = sys.argv[1:]
    if '--all' in args:
        files, gate = tracked_text(), False
    elif [a for a in args if not a.startswith('-')]:
        files, gate = [a for a in args if not a.startswith('-')], True
        missing = [f for f in files if not (ROOT / f).exists()]
        if missing:
            for f in missing:
                print(f"light_check FAIL: file not found under repo root {ROOT}: {f}")
            return 2
    else:
        files, gate = changed_text(), True

    if not HAVE_YAML:
        print("light_check: PyYAML not installed — YAML syntax check SKIPPED (pip install pyyaml).")

    fails, warns, notes = [], [], []
    for f in files:
        check_file(f, fails, warns)
    check_upstream_manifest(fails)
    check_precedent_sources(fails, warns)
    check_applicable_practices(files, notes)

    if notes:
        print("On-demand practices matched by these changes (read before committing):")
        for n in notes:
            print(f"  {n}")
    for w in warns:
        print(f"WARN: {w}")
    for f in fails:
        print(f"FAIL: {f}")

    if not fails and not warns:
        print(f"light_check OK: {len(files)} file(s) checked — no conflict markers, "
              f"invalid syntax, secret-shaped strings, or broken doc links.")
    elif not fails:
        print(f"light_check OK (with warnings): {len(files)} file(s) checked, {len(warns)} warning(s).")

    if gate and fails:
        print(f"\nlight_check FAIL — {len(fails)} error(s).")
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
