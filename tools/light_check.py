#!/usr/bin/env python3
# Last updated: 2026-09-02 (Buenos Aires) by a Precedent beta-test session, to version 1
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
     vendor tracking) or precedent.json (the universal/team source
     declarations) is missing an expected field, unparseable, or points at a
     path that doesn't exist on disk — the signature of a vendored tree or a
     source declaration having drifted from what it claims to track. Repo-wide,
     runs every time regardless of which files changed, the same way the old
     personal-pack-vendored check did: a `cp -r` or a hand-edited path
     wouldn't necessarily touch any file this run happens to be scoped to.

Checks 1-5 and 7 are gates (FAIL, exit 1); check 6 is a warning. Checks 1-6
use the same scoping convention as doc_lint.py: by default, files changed vs
the default branch (committed + working tree); explicit paths scan exactly
those; --all scans every tracked text file and never fails (backlog report
only). Check 7 ignores file scoping — it always inspects the whole repo, in
every mode including --all, though --all still keeps it non-fatal per that
mode's own contract.

Run:  python3 tools/light_check.py            # changed-vs-default-branch, gate
      python3 tools/light_check.py --all       # whole repo, report-only
"""
import ast, json, pathlib, re, subprocess, sys

def _git(args, cwd=None):
    return subprocess.run(['git'] + args, cwd=cwd, capture_output=True, text=True).stdout.strip()

ROOT = pathlib.Path(_git(['rev-parse', '--show-toplevel'],
                         cwd=pathlib.Path(__file__).resolve().parent)
                    or pathlib.Path(__file__).resolve().parents[1])

# This file's own path is excluded from the secret scan below — it is the
# only file in the repo whose job is to spell out the patterns it looks for.
SELF = pathlib.Path(__file__).resolve().relative_to(ROOT).as_posix()

TEXT_EXT = {'.md', '.py', '.sh', '.json', '.txt', '.yml', '.yaml', '.toml', '.template'}

def default_branch():
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

def check_precedent_sources(fails):
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
            fails.append(
                f"PRECEDENT SOURCE NOT TRACKED: {rel} source {entry.get('name')!r} "
                f"(level {level!r}) points at '{path}', which doesn't exist here "
                f"({resolved}) — a sibling clone that hasn't been checked out, or a stale path.")

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

    fails, warns = [], []
    for f in files:
        check_file(f, fails, warns)
    check_upstream_manifest(fails)
    check_precedent_sources(fails)

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
