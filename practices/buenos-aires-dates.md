---
slug:        buenos-aires-dates
title:       Every date is Buenos Aires local time
tier:        resident
severity:    default
applies_to:  ["**"]
occasion:    "writing a date or timestamp anywhere"
gates:       []
index_clause: "dates and commit timestamps are Buenos Aires time, not UTC"
checked_by:  tools/checks/check_buenos_aires_dates.py
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-08-31
approved_by: "Morgan F, migrated from RepoPersonalPreferences by the private-set migration session"
---
## Rule
Every date is my own Buenos Aires local calendar date, never the session container's system clock and never UTC. Two mechanisms: a prose date (a doc's "as of" note, a last-updated header) uses the Buenos Aires calendar date on the day the text was written; a git commit gets the right offset by running the commit itself under `TZ="America/Argentina/Buenos_Aires"` -- git resolves the offset from `TZ` at commit time, so no manual arithmetic is needed.

## Detail
Argentina has held UTC-3 year-round, with no daylight saving, since 2009 *(verified 2026-08-21)*. If that ever changes, every mechanism keyed to it -- this rule, and any scheduled workflow's cron line written against Buenos Aires time -- needs re-deriving; treat this note as a standing reminder to re-check the fact the next time this practice is touched.

## Why
It's my own timezone, and a document or commit timestamped in whatever timezone a session container happens to be running in is a fact about the infrastructure, not about when I actually did the work.

## Story


## Install
TZ="America/Argentina/Buenos_Aires" git commit -m "..."

for commits; for prose, resolve "today" in that timezone before writing a date into a document.

Checked mechanically, but only half of it: [`tools/checks/check_buenos_aires_dates.py`](../tools/checks/check_buenos_aires_dates.py) verifies every commit reachable from HEAD carries a `-0300` author-date offset (`tree` scope, this repo's own history). That's the git-commit mechanism in full -- `TZ` at commit time is recorded verbatim, so a wrong offset is a hard, unambiguous signature. The prose-date mechanism has no such signature: nothing in the repo independently tells a check what the actual Buenos Aires wall-clock date was when a line of prose was written, so a check can't tell a correct date from a wrong one, only that *some* date-shaped string is present -- checking format wouldn't be checking the rule. It's covered partially by `file-header`'s own timestamp-format and version-continuity check for files that carry that header, but the general case stays a judgment call. Two-direction tested in [`tools/checks/tests/test_buenos_aires_dates.sh`](../tools/checks/tests/test_buenos_aires_dates.sh). The check exempts two named, pre-existing commits from before this check existed (`GRANDFATHERED_SHAS` in the script itself) rather than rewriting already-published history to silence it -- see `no-rewrite-for-warnings` (BestPractice universal). Every commit made after that exemption was added is still fully checked.
