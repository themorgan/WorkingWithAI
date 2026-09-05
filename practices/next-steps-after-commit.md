---
slug:        next-steps-after-commit
title:       A reply that commits closes with an explicit Next Steps line
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "ending a reply in which I committed something"
gates:       ["reply"]
index_clause: "after a commit, close the reply by naming what I still need to do"
checked_by:  null
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-09-04
approved_by: "Morgan F"
---
## Rule
Any reply that made a commit ends with an explicit **Next Steps** statement addressed to me: what, if anything, I need to do now. If there's nothing left for me to do, say so directly -- "There is nothing else you need to do" or equivalent -- rather than leaving it implied. This holds even when the reply already asked me a question or mentioned an action item earlier in its body: restate it at the end anyway, because the end is the part I'm least likely to miss.

## Detail
This isn't a request for a summary of what changed -- that's the commit message and diff's job. It's specifically about *my* follow-on actions: approve something, review a PR, run a command, answer a question the reply raised, wait on something else, or nothing at all. A reply with no commit in it doesn't need this -- it's the commit that makes the omission costly, since a commit is exactly the kind of action whose loose ends (a push still pending, a PR still to open, a check still red) are easy to bury in a long reply and easy for me to miss.

## Why
I write long replies, and the important trailing detail -- a question I asked, a step I flagged as still needed -- gets lost in the length even when it was stated clearly earlier in the same message. Restating it as a short, explicit closing line costs little and means I never have to re-read a whole reply to find out whether anything is still on me.

## Story
Raised directly, as a standing personal preference, rather than in response to a specific missed handoff.

## Install
No mechanical check, for the same reason `go-merge` has none: this governs how a reply gets *written*, not any property of the repo tree, a commit, or a diff. There's no artifact after the fact that distinguishes a reply that correctly named "nothing else to do" from one that just happened not to need anything -- both leave an identical commit behind, and the one place the omission is visible is the conversation transcript itself, which a repo-scoped check script has no access to.
