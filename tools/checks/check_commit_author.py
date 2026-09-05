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

# practice: no-rewrite-for-warnings -- the two commits formerly exempted
# here (ac525c9, 0016903) were rewritten in place on 2026-09-03. 9ad366a
# (the commit that first added this exemption) quoted the practice as
# reserving a rewrite "for an explicit human instruction, never inferred
# from a tool's output" -- Morgan gave that instruction today, supplying
# the one condition that was missing. Both commits now carry the correct
# author on their own merit, so the exemption list is empty rather than
# removed outright -- the mechanism stays in place for the next real
# pre-check commit that needs it.
GRANDFATHERED_SHAS: set[str] = set()


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
