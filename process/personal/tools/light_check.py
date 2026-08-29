#!/usr/bin/env python3
# Last updated: 2026-08-28 22:40:00 (Buenos Aires) by Morgan F, to version 5
"""light_check.py — personal-pack sanity net, beyond BestPractice's doc_lint.py.

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
  7. PACK PRESENT BUT NOT VENDORED: process/personal/ exists on disk but
     process/manifest_personal.json is missing, unparseable, or has no
     `entries` — the signature of the personal pack having been copied in
     by hand (or otherwise dropped in place) rather than installed per
     process/personal/README.md#install, which is what actually tracks it (an
     upstream repo/commit, per-file hashes) so it can be kept current and
     audited like any other vendored tree. Also flags any entry whose
     recorded local_path doesn't exist on disk (a partial or stale
     install). This check is repo-wide and runs every time, independent of
     which files changed — a plain `cp -r` wouldn't necessarily touch
     process/manifest_personal.json at all, so scoping it to changed files
     would miss exactly the mistake it exists to catch.
  8. PENDING DRIFT REVIEWS (warning only): TODO.md's "## Pending Drift
     Reviews" section (process/personal/README.md#drift-notice, maintained by
     pack_sync.py's `record`/`resolve` subcommands) still has an open,
     unchecked entry — a session-start freshness notice that fired but was
     never actually reviewed. Repo-wide and runs every time, like check 7:
     the point is that this warning keeps showing up on every commit,
     including ones that never touch TODO.md, for as long as the entry
     stays open — a stdout-only notice a session can read past once and
     never see again is exactly the failure mode this exists to catch
     (origin: a session in a dependent repo missed a BestPractice-drift
     notice for a full task, 2026-08-27 — real name kept out of this
     vendored file, per the private-repo-scrub rule; see
     process/personal/README.md#drift-notice and this repo's own TODO.md).
  9. PRIVATE REPO NAME LEAK: any name from
     process/personal/private_repo_blocklist.txt showing up inside
     process/personal/ or NEW_REPO_SETUP.md — content that vendors
     byte-for-byte into every repo the personal pack is installed into
     (process/personal/README.md#private-repo-scrub). Two rules leaked a
     private repo's real name and link this way before this check existed
     (2026-08-28). Repo-wide and runs every time, like checks 7 and 8 —
     the leak isn't scoped to whatever files a given commit happens to
     touch.

 10. RULE CITATION FORM: a rule of the personal pack cited by its
     positional number (a bare "§N") instead of its permanent slug, or a
     cited slug that doesn't resolve to an anchor in
     process/personal/README.md. The pack's rules are cited as
     `[`slug`](process/personal/README.md#slug)` and never by heading
     number, because the numbers move whenever the file is reorganized and
     the slugs never do (process/personal/README.md#rule-links). A "§N"
     whose own source file is named right beside it -- "INSTALL.md §2",
     BestPractice's own numbering -- is fine and is what the check looks
     for before flagging. Repo-wide, like checks 7-9; process/upstream/ is
     skipped (a mirror, with its own numbering).

Checks 1-5 are gates (FAIL, exit 1); check 6 is a warning; check 7 is a
gate; check 8 is a warning; checks 9 and 10 are gates. Checks 1-6 use the same
scoping convention as doc_lint.py: by default, files changed vs the
default branch (committed + working tree); explicit paths scan exactly
those; --all scans every tracked text file and never fails (backlog
report only). Checks 7, 8, and 9 ignore file scoping — they always
inspect the whole repo, in every mode including --all, though --all still
keeps them non-fatal per that mode's own contract.

Run:  python3 process/personal/tools/light_check.py            # changed-vs-default-branch, gate
      python3 process/personal/tools/light_check.py --all       # whole repo, report-only
"""
import ast, json, pathlib, re, subprocess, sys

def _git(args, cwd=None):
    return subprocess.run(['git'] + args, cwd=cwd, capture_output=True, text=True).stdout.strip()

ROOT = pathlib.Path(_git(['rev-parse', '--show-toplevel'],
                         cwd=pathlib.Path(__file__).resolve().parent)
                    or pathlib.Path(__file__).resolve().parents[3])

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pack_sync  # noqa: E402 -- sibling tool; shares the pending-drift-entry format

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

def check_pack_vendored(fails):
    pack_dir = ROOT / 'process' / 'personal'
    if not pack_dir.is_dir() or not any(pack_dir.iterdir()):
        return  # pack not installed here at all -- nothing to check
    manifest_path = ROOT / 'process' / 'manifest_personal.json'
    rel_manifest = 'process/manifest_personal.json'
    if not manifest_path.exists():
        fails.append(
            f"PACK NOT VENDORED: process/personal/ exists but {rel_manifest} "
            "is missing -- looks copied in rather than installed per "
            "process/personal/README.md#install (which tracks it: an upstream "
            "repo/commit, per-file hashes). Install it properly, or if this "
            "IS the pack's own source repo, add the self-hosting manifest "
            "(upstream.repo/commit null, per process/personal/README.md#install step 6).")
        return
    try:
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        fails.append(f"PACK NOT VENDORED: {rel_manifest} is not valid JSON: {e}")
        return
    entries = manifest.get('entries')
    if not entries:
        fails.append(
            f"PACK NOT VENDORED: {rel_manifest} has no 'entries' -- "
            "process/personal/ is present but nothing is actually "
            "registered as installed. See process/personal/README.md#install.")
        return
    for entry in entries:
        local_path = entry.get('local_path')
        if local_path and not (ROOT / local_path).exists():
            fails.append(
                f"PACK NOT VENDORED: {rel_manifest} entry "
                f"'{entry.get('practice', '?')}' records local_path "
                f"'{local_path}', which doesn't exist -- partial or stale "
                "install.")

PRIVATE_REPO_BLOCKLIST = 'process/personal/private_repo_blocklist.txt'
# Files under process/personal/ or named here at the repo root are the
# content that actually vendors elsewhere (process/personal/README.md#install
# step 1, and NEW_REPO_SETUP.md is copy-pasted directly) — the scope the private-repo-scrub rule's
# check covers. Nothing outside that scope is scanned: a private repo name
# is fine in TODO.md, this repo's own AGENTS.md, or a commit message, all
# of which never leave this repo (process/personal/README.md#private-repo-scrub's own carve-out).
VENDOR_SURFACE_ROOTS = ('process/personal/',)
VENDOR_SURFACE_FILES = ('NEW_REPO_SETUP.md',)

def _load_private_repo_patterns():
    path = ROOT / PRIVATE_REPO_BLOCKLIST
    if not path.exists():
        return []
    pats = []
    for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        try:
            pats.append((line, re.compile(line)))
        except re.error:
            pass  # a malformed blocklist line is doc_lint/light_check's own
                   # problem to catch elsewhere, not a reason to crash here
    return pats

def check_private_repo_names(fails):
    pats = _load_private_repo_patterns()
    if not pats:
        return
    for rel in tracked_text():
        if rel == PRIVATE_REPO_BLOCKLIST:
            continue  # the blocklist itself necessarily names what it blocks
        if not (rel.startswith(VENDOR_SURFACE_ROOTS) or rel in VENDOR_SURFACE_FILES):
            continue
        text = (ROOT / rel).read_text(encoding='utf-8', errors='ignore')
        for i, line in enumerate(text.splitlines(), 1):
            for name, pat in pats:
                if pat.search(line):
                    fails.append(
                        f"PRIVATE REPO NAME LEAK: {rel}:{i}: matches blocklist "
                        f"entry '{name}' — this path vendors into every repo "
                        "the personal pack installs into "
                        "(process/personal/README.md#private-repo-scrub). "
                        "Scrub to a general description; keep "
                        "the real name only in this repo's own TODO.md decision "
                        "record.")
                    break

def check_pending_drift(warns):
    if not pack_sync.TODO.exists():
        return
    text = pack_sync.TODO.read_text(encoding='utf-8', errors='ignore')
    for source, date, notice in pack_sync.open_entries(text):
        warns.append(
            f"PENDING DRIFT REVIEW: TODO.md — '{source}' notice from {date} is "
            f"still unresolved ({notice[:80]}{'…' if len(notice) > 80 else ''}). "
            f"Review it (process/personal/README.md#drift-notice), then "
            f"`pack_sync.py resolve {source}`.")

PACK_README = 'process/personal/README.md'
RULE_ANCHOR_RE = re.compile(r'<a id="([a-z0-9][a-z0-9-]*)"></a>')
# A "§N" is BestPractice's own numbering when the file it belongs to is named
# right before it (same line or the one above): "INSTALL.md §2", "[SETUP.md](…) §5".
# Local adaptation for this repo: also recognizes HUMAN_VOICE_RULES.md, this
# repo's third vendored pack (process/voice/, from SoundHuman) -- it carries
# its own independent §N numbering, unrelated to the personal pack's, and
# this repo's own AGENTS.md/TODO.md/RULES_NOW_TESTING.md legitimately cite
# it by number the same way BestPractice's own files are cited. Re-apply
# this addition after any future mirror from RepoPersonalPreferences.
UPSTREAM_SECTION_RE = re.compile(
    r'(INSTALL|SETUP|PRACTICES|GIT|MOBILE|GITHUB_ACTIONS|METHOD|HUMAN_VOICE_RULES)\.md[^\n]{0,60}$')
SLUG_CITATION_RE = re.compile(r'README\.md#([a-z0-9][a-z0-9-]*)')
# `#slug` is the placeholder the docs use when spelling out the citation form
# itself ("[`slug`](process/personal/README.md#slug)"), not a real citation.
PLACEHOLDER_SLUGS = {'slug'}

def pack_rule_slugs():
    """Every slug the pack's README actually defines, or None if it isn't here."""
    p = ROOT / PACK_README
    if not p.exists():
        return None
    return set(RULE_ANCHOR_RE.findall(p.read_text(encoding='utf-8', errors='ignore')))

def check_rule_citations(fails):
    slugs = pack_rule_slugs()
    if slugs is None:
        return  # no pack installed here — nothing to cite
    for rel in tracked_text():
        # process/voice/ is also skipped here: this repo's third vendored
        # pack (from SoundHuman), with its own independent §N numbering --
        # local adaptation, same reasoning as process/upstream/'s own skip.
        if rel.startswith(('process/upstream/', 'process/voice/')) or rel == SELF:
            continue
        text = (ROOT / rel).read_text(encoding='utf-8', errors='ignore')
        lines = text.splitlines()
        for i, line in enumerate(lines, 1):
            for m in re.finditer(r'§(\d+)', line):
                before = line[:m.start()]
                prev = lines[i - 2] if i >= 2 else ''
                if UPSTREAM_SECTION_RE.search(before) or UPSTREAM_SECTION_RE.search(prev):
                    continue
                fails.append(
                    f"RULE CITED BY NUMBER: {rel}:{i}: '§{m.group(1)}' — the "
                    "pack's rules are cited by their permanent slug, "
                    "[`slug`](process/personal/README.md#slug), never by "
                    "heading number (process/personal/README.md#rule-links). "
                    "If this is BestPractice's own numbering, name its file "
                    "next to it (\"INSTALL.md §2\").")
            for m in SLUG_CITATION_RE.finditer(line):
                if m.group(1) in PLACEHOLDER_SLUGS:
                    continue
                if m.group(1) not in slugs:
                    fails.append(
                        f"UNKNOWN RULE SLUG: {rel}:{i}: '#{m.group(1)}' doesn't "
                        f"match any rule anchor in {PACK_README}. Slugs are "
                        "permanent; check the spelling, or add the anchor.")

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
    check_pack_vendored(fails)
    check_pending_drift(warns)
    check_private_repo_names(fails)
    check_rule_citations(fails)

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
