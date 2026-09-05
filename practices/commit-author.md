---
slug:        commit-author
title:       Commit author is always `Morgan F`
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "making the first commit in a fresh clone or session"
gates:       []
index_clause: "git config user.name/email to Morgan F, don't ask"
checked_by:  tools/checks/check_commit_author.py
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-08-31
approved_by: "Morgan F, migrated from RepoPersonalPreferences by the private-set migration session"
---
## Rule
Set `git config user.name "Morgan F"` and `git config user.email "morgan@westegg.com"` once per clone, before the first commit -- don't ask who the author is first. The email is my own address, used to identify me as the author of every commit.

## Detail
This replaces only the *identity* half of the generic default of asking before the first commit. It says nothing about co-authorship: a host's own `Co-Authored-By:` trailer naming the assistant still applies undisturbed alongside it.

The same identity extends past the git config lines themselves: commits, PRs, and any GitHub-side attribution are mine under the `themorgan` account, and where a document refers to me by name or pronoun, use "Morgan" and he/him.

## Why
The identity is already decided, every time -- there is nothing to ask about, and asking on every fresh clone is pure friction for a fact that never changes.

## Story
Written down after the identity question got asked, and answered the same way, often enough that answering it was clearly more session time than the fact was worth.

## Install
A one-time `git config` at the start of a session, in whatever repo I'm working in. Where a repo's own bootstrap step runs automatically at session start, this belongs there so it never needs to be typed by hand.

Checked mechanically by [`tools/checks/check_commit_author.py`](../tools/checks/check_commit_author.py): every commit reachable from HEAD in this repo must carry `Morgan F <morgan@westegg.com>` as its recorded author. Scope is `tree` -- this repo's own history is what's checked, since a check living in a private set has no visibility into any other repo this practice also governs. Two-direction tested in [`tools/checks/tests/test_commit_author.sh`](../tools/checks/tests/test_commit_author.sh): a scratch copy with a planted wrong-author commit fails the check; the real, current history stays clean. The check's `GRANDFATHERED_SHAS` mechanism exists to exempt a pre-existing commit from before this check existed, by SHA, rather than rewriting already-published history to silence it -- see `no-rewrite-for-warnings` (BestPractice universal). Two commits used that mechanism (`ac525c9`, `0016903`) until Morgan's own explicit instruction on 2026-09-03 turned rewriting them from forbidden into allowed; both were rewritten in place and the list is empty again. Every commit made after the mechanism was added is still fully checked.
