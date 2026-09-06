---
slug:        my-identity-is-not-private
title:       My name, city and timestamps are never private
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "adding a term to a scrub or leak blocklist, or flagging an author or date as a disclosure risk"
gates:       []
index_clause: "never blocklist my name, city, timezone or timestamps; never warn about them"
checked_by:  tools/checks/check_my_identity_is_not_private.py
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-09-06
approved_by: "Morgan F"
---
## Rule
My display name (**Morgan F**), my GitHub owner name (**themorgan**), my
city and timezone (**Buenos Aires**, **America/Argentina/Buenos_Aires**),
and the dates and timestamps in file headers are **not private and are
never treated as a disclosure risk**. They never go on a scrub blocklist,
a leak blocklist, or any other denylist, and a session never raises them
as a concern, a risk, or something to review before publishing.

Their presence is the **point**. I want every file I edit to say who
edited it and exactly when, timestamp included, and that attribution is
supposed to travel with the file wherever it goes.

Still private, and not covered by this: my email address
(`morgan@westegg.com`, `westegg.com`), my other handles, and numeric
account identifiers. This practice is about the attribution that appears
in a file header, not about every string that happens to name me.

## Why
These terms went onto a blocklist in the first place *to stop sessions
flagging them*, and produced the exact opposite. They appear in the
upstream practice layer's own date headers, so they arrive in a consuming
repo from upstream rather than leaking to it — which meant the gate
reported failures no edit in that repo could ever clear. One repo sat at
116 of them. A gate that can only be ignored is worse than no gate: it
trains everyone to skip the one check that would have caught a real leak.

The cost landed on me directly. Half my working time went to correcting
sessions that flagged my own name in my own file headers as a risk, in
repos I own, on files I had just written.

## Story
2026-09-06. A pre-launch audit found `themorgan/WorkingWithAI`'s scrub
gate at 116 failures, every one of them `Morgan F`, `Buenos Aires`,
`America/Argentina/Buenos_Aires` or `themorgan` matching upstream's own
`<!-- Last updated: ... -->` headers. That repo's own instructions said
the audit "must pass before committing anything that touches
`process/`" — a rule that had been impossible to follow for as long as
the terms had been on the list. The terms came off, the gate went green
for the first time, and the rule became true again.

This practice exists so the fix does not have to be rediscovered per
repository. It was written in the individual set on purpose: it is a fact
about me, it travels to every repo I work in, and no team or project gets
to re-decide it.

## Install
`tools/checks/check_my_identity_is_not_private.py` reads every blocklist
file in the repo — `process/scrub_blocklist.txt`, any `leak-blocklist.txt`,
anything else named like a blocklist — and fails if a protected term is
listed. It skips vendored and materialized trees, and it skips the
upstream `*.template` files, which document the blocklist format rather
than configuring anything.
