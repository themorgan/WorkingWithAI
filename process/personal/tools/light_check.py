#!/usr/bin/env python3
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
     process/personal/README.md §18, which is what actually tracks it (an
     upstream repo/commit, per-file hashes) so it can be kept current and
     audited like any other vendored tree. Also flags any entry whose
     recorded local_path doesn't exist on disk (a partial or stale
     install). This check is repo-wide and runs every time, independent of
     which files changed — a plain `cp -r` wouldn't necessarily touch
     process/manifest_personal.json at all, so scoping it to changed files
     would miss exactly the mistake it exists to catch.

Checks 1-5 are gates (FAIL, exit 1); check 6 is a warning; check 7 is a
gate. Checks 1-6 use the same scoping convention as doc_lint.py: by
default, files changed vs the default branch (committed + working tree);
explicit paths scan exactly those; --all scans every tracked text file and
never fails (backlog report only). Check 7 ignores file scoping — it
always inspects the whole repo, in every mode including --all, though
--all still keeps it non-fatal per that mode's own contract.

Run:  python3 process/personal/tools/light_check.py            # changed-vs-default-branch, gate
      python3 process/personal/tools/light_check.py --all       # whole repo, report-only
"""
import ast, json, pathlib, re, subprocess, sys

def _git(args, cwd=None):
    return subprocess.run(['git'] + args, cwd=cwd, capture_output=True, text=True).stdout.strip()

ROOT = pathlib.Path(_git(['rev-parse', '--show-toplevel'],
                         cwd=pathlib.Path(__file__).resolve().parent)
                    or pathlib.Path(__file__).resolve().parents[3])

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
            "process/personal/README.md §18 (which tracks it: an upstream "
            "repo/commit, per-file hashes). Install it properly, or if this "
            "IS the pack's own source repo, add the self-hosting manifest "
            "(upstream.repo/commit null, per §18 step 6).")
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
            "registered as installed. See process/personal/README.md §18.")
        return
    for entry in entries:
        local_path = entry.get('local_path')
        if local_path and not (ROOT / local_path).exists():
            fails.append(
                f"PACK NOT VENDORED: {rel_manifest} entry "
                f"'{entry.get('practice', '?')}' records local_path "
                f"'{local_path}', which doesn't exist -- partial or stale "
                "install.")

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
