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
#
# aa2155d (2026-09-04, "next-steps-after-commit: also close with
# branch-deletion recommendations") landed as `Claude <noreply@anthropic.com>`
# because the session never ran `git config user.name`/`user.email` before
# committing -- a one-off session mistake, not a gap in this check or a
# case for rewriting: the commit was already published (merged into main)
# by the time it was noticed, and Morgan's explicit instruction on
# 2026-09-04 was to grandfather it rather than rewrite.
# 2026-09-06: three more, from two sessions on 2026-09-05/06 that committed
# without setting `git config user.name`/`user.email` (and so without the
# Buenos Aires TZ either) -- the same one-off session mistake aa2155d was,
# not a gap in this check. All three were already merged into `main` and
# pushed by the time the pre-launch audit ran this check, so they are
# published history: `no-rewrite-for-warnings` reserves a rewrite for an
# explicit human instruction and none was given for these, so they are
# grandfathered rather than rewritten. Left permanently red, this check is
# a check nobody runs, which is the failure mode the exemption mechanism
# exists to prevent.
#   7fb401f  Correct v2: the retry loop cannot close the SessionStart/add_repo gap
#   b40a903  Retry the SessionStart bootstrap clone instead of trying once
#   977e360  Spell out push and PR as explicit go-merge steps
GRANDFATHERED_SHAS: set[str] = {
    "aa2155d2098c831fea3248ff50dc44741ace76e5",
    "7fb401f294638d38c4495117ca7f608d3e9d6492",
    "b40a903c8444b7052bfdf1a9470317ceee2804ca",
    "977e3607cd679c4056cd763733abfbe7565c2aaf",
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
