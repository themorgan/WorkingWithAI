#!/usr/bin/env python3
"""check_commit_author.py -- the mechanical check for practices/commit-author.md.

# practice: commit-author

Scope: tree. Every commit reachable from HEAD in this repo must be authored
as "Morgan F <morgan@westegg.com>" -- both the git-recorded author name and
email, which is what `git config user.name`/`user.email` actually produces
on every subsequent commit once set correctly.

Exit 0 and print nothing when clean. Exit 1 and print the practice's own
Rule text (never a paraphrase) plus the specific finding(s) on a violation.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PRACTICE_FILE = ROOT / "practices" / "commit-author.md"

EXPECTED_NAME = "Morgan F"
EXPECTED_EMAIL = "morgan@westegg.com"

# practice: no-rewrite-for-warnings -- these two commits predate this check
# and landed before the identity was enforced. Rewriting already-published
# history to silence a check is exactly what that practice forbids ("fix
# the setting forward... do not rebase, amend, or force-push to satisfy the
# warning"); its own Install section calls for scoping the check instead,
# which is what this list does. Found and left as a noted, unfixed backlog
# item 2026-09-03, while adding this check's own regeneration to this repo.
# Every commit made after this list was added is still fully checked --
# this exempts exactly these two SHAs, nothing else, ever.
GRANDFATHERED_SHAS = {
    "ac525c90017b5cc2bc18ac9e048af8bae7324f87",  # 2026-09-02, pre-check
    "0016903c1ec8e818826cabe34858cc133899e365",  # 2026-09-02, pre-check
}


def rule_text() -> str:
    text = PRACTICE_FILE.read_text(encoding="utf-8")
    m = re.search(r"## Rule\n(.*?)\n## ", text, re.S)
    return m.group(1).strip() if m else "(no Rule found)"


def find_violations() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "log", "--format=%H|%an|%ae"],
        capture_output=True,
        text=True,
        check=True,
    )
    findings = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        sha, name, email = line.split("|", 2)
        if sha in GRANDFATHERED_SHAS:
            continue
        if name != EXPECTED_NAME or email != EXPECTED_EMAIL:
            findings.append(
                f"commit {sha[:12]}: author is {name!r} <{email}>, "
                f"expected {EXPECTED_NAME!r} <{EXPECTED_EMAIL}>"
            )
    return findings


if __name__ == "__main__":
    findings = find_violations()
    if findings:
        print(f"VIOLATION: {PRACTICE_FILE.stem}")
        for f in findings:
            print(f"  {f}")
        print("\nthe rule:")
        print("  " + rule_text().replace("\n", "\n  "))
        sys.exit(1)
    sys.exit(0)
