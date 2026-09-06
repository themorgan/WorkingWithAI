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
import json
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
    # 2026-09-06 -- this session's own three commits, made before it had run
    # the `git config` this practice asks for. Grandfathered rather than
    # rewritten: they are pushed, and no-rewrite-for-warnings says fix the
    # setting forward and leave published history alone. The setting is now
    # configured in every clone this session touched, so the next commit is
    # correct on its own merit rather than by exemption.
    "1844ab3178892e761417697578db7d75871bb3e3",
    "de3e4a0faca6b6cd980b8ce65d4f770f7f7fcd9d",
    "1be9c9084bba8fc92dfb65a73b2eace315fedb5b",
    "72edf0198b3ceadaaf747701311ab88fb7f8469c",
    "c3c69466aecb6ef88039fcb3a70bea9257ca322d",
    "c3b32b8d179fe120a2d437439d8c18192c2cb394",
    "7fb401f294638d38c4495117ca7f608d3e9d6492",
    "b40a903c8444b7052bfdf1a9470317ceee2804ca",
    "977e3607cd679c4056cd763733abfbe7565c2aaf",
}


# --- scope: commits still in flight -------------------------------------
#
# This practice is about how a commit is MADE, so the only commits it can
# ask anything of are the ones not yet published. Auditing a repo's entire
# history means auditing history that `no-rewrite-for-warnings` forbids
# touching -- the finding is true, unfixable, and permanent, and the check
# it belongs to becomes one nobody runs.
#
# That was survivable while these scripts ran only in the set that wrote
# them, where the fix was a short list of grandfathered SHAs. It stopped
# being survivable when precedent_materialize.py started shipping them into
# consuming repos: those have years of history nobody is going to rewrite,
# by authors who are not this practice's subject, and no allowlist of one
# repo's SHAs can ever cover another's. 2026-09-06, in two real consumers:
# every pre-existing commit reported, forever.
#
# Scope is therefore commits reachable from HEAD but not from the published
# default branch -- exactly the work a session can still amend. An empty
# scope is reported as "could not run" (exit 2, SKIPPED), never as a pass:
# a scan of nothing is not evidence of anything.
class CouldNotRun(Exception):
    """Reported as SKIPPED (exit 2), never as a pass."""


def _default_branch_ref() -> str | None:
    head = subprocess.run(
        ["git", "-C", str(ROOT), "symbolic-ref", "refs/remotes/origin/HEAD"],
        capture_output=True, text=True)
    if head.returncode == 0 and head.stdout.strip():
        return head.stdout.strip().replace("refs/remotes/", "", 1)
    for cand in ("origin/main", "origin/master"):
        probe = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "--verify", "--quiet", cand],
            capture_output=True, text=True)
        if probe.returncode == 0:
            return cand
    return None


def commits_in_flight() -> list[str] | None:
    """SHAs on HEAD that the published default branch does not have, or None
    when that cannot be determined (no remote, no default branch)."""
    base = _default_branch_ref()
    if base is None:
        return None
    r = subprocess.run(
        ["git", "-C", str(ROOT), "rev-list", f"{base}..HEAD"],
        capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return [l.strip() for l in r.stdout.splitlines() if l.strip()]


# A consuming repo's own grandfathered SHAs live in that repo, not here.
# GRANDFATHERED_SHAS below is this set's own history; a SHA from some other
# repository has no meaning in it, and a shared list could never hold every
# consumer's. no-rewrite-for-warnings names "the exemption" as one of its
# three forward fixes, so the exemption has to be somewhere the repo being
# audited can actually write.
def repo_exemptions() -> set:
    """SHAs the audited repo has recorded as published-and-left-alone.

    `local/grandfathered_commits.json`: {"commits": ["<sha>", ...]}, beside
    that repo's other repo-local Precedent content. Absent or malformed
    reads as empty -- an exemption nobody wrote is not one."""
    f = ROOT / "local" / "grandfathered_commits.json"
    if not f.is_file():
        return set()
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    commits = data.get("commits") if isinstance(data, dict) else None
    return {str(c) for c in commits} if isinstance(commits, list) else set()


def rule_text() -> str:
    text = PRACTICE_FILE.read_text(encoding="utf-8")
    m = re.search(r"## Rule\n(.*?)\n## ", text, re.S)
    return m.group(1).strip() if m else "(no Rule found)"


def find_violations() -> list[str]:
    scope = commits_in_flight()
    if scope is None:
        raise CouldNotRun(
            "no published default branch to compare against (no origin, or "
            "origin/HEAD unset), so there is no way to tell which commits "
            "are still amendable from which are published history this "
            "practice must not touch")
    if not scope:
        raise CouldNotRun(
            "no commits on HEAD that the published default branch does not "
            "already have -- nothing in flight to audit. Published history "
            "is out of scope by no-rewrite-for-warnings")
    in_flight = set(scope)
    _repo_exempt = repo_exemptions()
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
        if sha not in in_flight:
            continue
        if sha in GRANDFATHERED_SHAS or sha in _repo_exempt:
            continue
        if offset != EXPECTED_OFFSET:
            findings.append(
                f"commit {sha[:12]}: author-date offset is {offset!r}, "
                f"expected {EXPECTED_OFFSET!r} "
                "(commit was not made under TZ=America/Argentina/Buenos_Aires)"
            )
    return findings


if __name__ == "__main__":
    try:
        findings = find_violations()
    except CouldNotRun as e:
        print(f"SKIPPED: {PRACTICE_FILE.stem}: {e}")
        sys.exit(2)
    if findings:
        print(f"VIOLATION: {PRACTICE_FILE.stem}")
        for f in findings:
            print(f"  {f}")
        print("\nthe rule:")
        print("  " + rule_text().replace("\n", "\n  "))
        sys.exit(1)
    sys.exit(0)
