---
slug:        go-merge
title:       "`go`, `merge`, or `PR & merge` authorizes commit + merge"
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "my message ends on a standing merge-authorization word"
gates:       ["merge"]
index_clause: "\"go\"/\"merge\"/\"PR & merge\" alone at the end means merge"
checked_by:  null
defines:     []
status:      active
supersedes:  []
overrides:   merge-authorization-keyword
added:       2026-08-31
approved_by: "Morgan F, migrated from RepoPersonalPreferences by the private-set migration session"
---
## Rule
If my message, at a point where you've said you're ready to commit (or ready to commit and merge), ends with `go`, `merge`, or `PR & merge` standing alone as its own sentence -- case-insensitive, whether that's the whole message on one line or the last sentence of a longer one, set off by ordinary sentence-ending punctuation -- treat it as my authorization, right there, to commit the pending work and merge it, using the repo's usual conventions, without asking again first.

## Detail
"That was perfect. merge", "Go.", a lone line reading `MERGE`, and a closing "PR & merge" all count; "let's merge the two lists" and "go check the logs" don't, because there the word is part of a longer sentence, not standing alone as the message's last one. `PR & merge` names the same authorization spelled out through the step a repo's own workflow takes to get there -- open the PR, then merge it -- and its ordinary variants (`PR and merge`, `PR then merge`) count the same way. Where context leaves it ambiguous whether the trailing phrase is this shorthand or just part of the sentence's own meaning -- or where multiple pending items make it unclear what "merge" would even apply to -- don't assume: ask.

## Why
This names one specific fixed word for the general standing merge-authorization mechanism, which is exactly the choice that mechanism leaves to each repo -- it's shorthand for the same authorization "merge only when the user says so" already asks for, not a new kind of permission.

## Story
This exact wording is my own shorthand, from actually typing it this way session after session -- not something to expect or require from anyone else.

## Install
No mechanical check, and not for lack of trying: this practice governs how a chat message gets *read*, not any property of a diff, a commit, or the repo tree. There is no artifact after the fact that distinguishes "the assistant correctly recognized `go` as authorization and merged" from "the assistant merged on its own initiative and `go` happened to be the last word typed" -- both leave the identical commit and merge behind. The one place the distinction is visible is the conversation transcript itself, which isn't something a repo-scoped check script has access to, and even there it's a judgment call about intent (per the Rule's own "don't assume: ask" clause for ambiguous phrasing), not a mechanical signature a script could pattern-match reliably. This is the same class `mistakes-become-rules`' proportionality guard already names as resistant to checking.

