---
slug:        go-merge
title:       "\"Go merge\" authorizes sync, confirm branch, commit, and merge"
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "my message ends on the standing merge-authorization phrase"
gates:       ["merge"]
index_clause: "\"Go merge\" alone at the end means sync, confirm branch, commit, and merge"
checked_by:  null
defines:     []
status:      active
supersedes:  []
overrides:   merge-authorization-keyword
added:       2026-08-31
approved_by: "Morgan F, migrated from RepoPersonalPreferences by the private-set migration session; revised 2026-09-04, Morgan F, to a single phrase with an explicit sync/branch-confirmation step"
---
## Rule
If my message, at a point where you've said you're ready to commit (or ready to commit and merge), ends with `Go merge` standing alone as its own sentence -- case-insensitive, whether that's the whole message on one line or the last sentence of a longer one, set off by ordinary sentence-ending punctuation -- treat it as my authorization, right there, to: sync your local branch with origin, confirm out loud which branch you're merging into, commit the pending work, and merge it, using the repo's usual conventions, without asking again first.

## Detail
"That was perfect. Go merge", "Go merge.", and a lone line reading `GO MERGE` all count; "let's go merge those two lists" and "go check the logs, then merge the report" don't, because there the words are part of a longer sentence, not standing alone as the message's last one. Where context leaves it ambiguous whether the trailing phrase is this shorthand or just part of the sentence's own meaning -- or where multiple pending items make it unclear what "merge" would even apply to -- don't assume: ask.

This phrase replaces the three separate triggers (`go`, `merge`, `PR & merge`) this practice used before 2026-09-04. `go` doubled as ordinary language for "let's build this" too often to trust as a standing keyword, and `merge` alone was tangled up with real confusion about *which* branch a merge would target. The sync-and-confirm-branch step is spelled out here, not left implicit inside "usual conventions", so it's something I actually see happen on every merge, not something I have to trust happened silently.

## Why
This names one specific fixed phrase for the general standing merge-authorization mechanism, which is exactly the choice that mechanism leaves to each repo -- it's shorthand for the same authorization "merge only when the user says so" already asks for, not a new kind of permission. Naming the sync-and-branch-confirmation step explicitly closes a real gap: that check already happens as part of "usual conventions" in any repo that documents it, but leaving it implicit means it's easy to trust it happened without seeing it happen.

## Story
Originally my own shorthand from typing `go`/`merge`/`PR & merge` session after session. Revised 2026-09-04, prompted by two confusions that surfaced in the same conversation while working in BestPractice: a session's local branch there turned out to be badly stale relative to origin, and -- a separate, earlier incident already on record in that repo -- a PR once merged silently into the wrong branch ([merge-target-is-beta-branch](https://github.com/alex137/BestPractice/blob/precedent-beta-v01/local/practices/merge-target-is-beta-branch.md)). Neither incident happened in this repo, but both come down to the same gap: a keyword whose Rule says "using the repo's usual conventions" trusts the sync-and-correct-branch check invisibly. I asked, in that same conversation, to collapse `go`/`merge`/`PR & merge` into one phrase -- I use "go" and "merge" too often as ordinary words to trust either alone as a keyword -- and to have the sync/branch check spoken out loud on every merge.

## Install
No mechanical check, and not for lack of trying: this practice governs how a chat message gets *read*, not any property of a diff, a commit, or the repo tree. There is no artifact after the fact that distinguishes "the assistant correctly recognized `Go merge` as authorization and merged" from "the assistant merged on its own initiative and `Go merge` happened to be the last words typed" -- both leave the identical commit and merge behind. The one place the distinction is visible is the conversation transcript itself, which isn't something a repo-scoped check script has access to, and even there it's a judgment call about intent (per the Rule's own "don't assume: ask" clause for ambiguous phrasing), not a mechanical signature a script could pattern-match reliably. This is the same class `mistakes-become-rules`' proportionality guard already names as resistant to checking.
