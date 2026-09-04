#!/usr/bin/env python3
"""check_buenos_aires_dates.py -- the mechanical check for
practices/buenos-aires-dates.md.

# practice: buenos-aires-dates

Scope: tree. Covers only the mechanically checkable half of the practice:
the git-commit mechanism. `git` records each commit's author-date UTC
offset verbatim from the environment's `TZ` at commit time, so a commit
made under `TZ="America/Argentina/Buenos_Aires"` always carries a fixed
"-0300" offset (Argentina has held UTC-3 with no DST since 2009 -- see the
practice's own Detail section). Every commit reachable from HEAD must carry
that offset.

The prose-date mechanism ("a doc's as-of note uses the Buenos Aires
calendar date on the day the text was written") has no mechanical
signature: nothing in the repo lets a check independently know what the
actual Buenos Aires wall-clock date was at write time, so it cannot be
verified here. See the practice file's own Install section for this split.

Exit 0 and print nothing when clean. Exit 1 and print the practice's own
Rule text (never a paraphrase) plus the specific finding(s) on a violation.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PRACTICE_FILE = ROOT / "practices" / "buenos-aires-dates.md"

EXPECTED_OFFSET = "-0300"

# practice: no-rewrite-for-warnings -- the two commits formerly exempted
# here (ac525c9, 0016903) were rewritten in place on 2026-09-03. 9ad366a
# (the commit that first added this exemption) quoted the practice as
# reserving a rewrite "for an explicit human instruction, never inferred
# from a tool's output" -- Morgan gave that instruction today, supplying
# the one condition that was missing. Both commits now carry the correct
# offset on their own merit, so the exemption list is empty rather than
# removed outright -- the mechanism stays in place for the next real
# pre-check commit that needs it.
GRANDFATHERED_SHAS: set[str] = set()


def rule_text() -> str:
    text = PRACTICE_FILE.read_text(encoding="utf-8")
    m = re.search(r"## Rule\n(.*?)\n## ", text, re.S)
    return m.group(1).strip() if m else "(no Rule found)"


def find_violations() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "log", "--format=%H|%ad", "--date=format:%z"],
        capture_output=True,
        text=True,
        check=True,
    )
    findings = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        sha, offset = line.split("|", 1)
        if sha in GRANDFATHERED_SHAS:
            continue
        if offset != EXPECTED_OFFSET:
            findings.append(
                f"commit {sha[:12]}: author-date offset is {offset!r}, "
                f"expected {EXPECTED_OFFSET!r} "
                "(commit was not made under TZ=America/Argentina/Buenos_Aires)"
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
