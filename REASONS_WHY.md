<!-- Last updated: 2026-08-28 13:41:04 (Buenos Aires) by Morgan F, to version 5 -->

# Reasons why

*Not "AI produces better results" and not "collaboration beats solo work"
— both true and both said so often they've stopped meaning anything.
These are the more specific, less obvious effects of actually working the
way [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) and the rest of this repo
describe: the kind that only show up once you've been doing it a while.*

**1. Being wrong gets cheap while it's still small.** Catching an error
the same hour you make it costs one correction. Catching it three weeks
later in front of a client costs the correction plus the meeting where
everyone tries to remember who approved what and why nobody caught it
sooner. Arguing a claim out with the model in real time, before it
becomes a deliverable anyone downstream builds on, moves most mistakes
from the second bucket into the first
([COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) rule 4). The time
saved is real but almost beside the point — the actual gain is that a
wrong idea gets killed before it has time to acquire allies. Drift is one
shape this takes: a system where everyone downstream sees only the
polished summary has no way to notice the summary has started drifting
from what's true, because a slightly wrong summary reads exactly as
coherent as a correct one. Keeping some raw, unfiltered contact with the
actual work on purpose
([COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) rule 13), and
periodically checking the record against itself for contradictions
([RULES_NOW_TESTING.md](RULES_NOW_TESTING.md) item 7), gives an
early-warning channel most organizations don't have: one that can report
a problem before it shows up as a complaint.

**2. Writing things down stops competing with getting things done.** Most
organizations under-document not because nobody values it, but because
documenting is a separate task competing for the same hour as the real
work, and the real work usually wins. When the record gets pulled out as
a byproduct of doing the work in the open, the rules, the open items, the
reasoning, instead of as a follow-up chore
([IDEAS.md](IDEAS.md)'s automatic rule- and TODO-extraction), that tax
mostly disappears. Nobody has to choose between finishing the task and
writing it up, because the writing already happened while the task did.

**3. Attaching the situation to a decision heads off the confusions
nobody sees coming.** This repo's merge runbook says never hand-merge
`process/upstream/` — re-run the sync instead. As a bare instruction it
loses the first time someone hits a real conflict there: resolving it by
hand is the obvious, competent-looking move, and the vendored copy
quietly stops matching upstream, so the next sync throws a conflict
nobody can account for and the audit trail says the two were identical
all along. Carrying the reason inline — this directory is a byte-for-byte
mirror, and editing it breaks the thing the mirror is for — settles that
in one read, before the pull request is opened rather than three merges later when
somebody has to reconstruct what happened. Every rule with its origin
case attached is that same trade: a sentence written once against a
problem that would otherwise get diagnosed from scratch by whoever
inherits it ([OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) item 3).

**4. The power of documentation is almost magical — since no one finds
the time, AI will.** Everyone already agrees a good record is worth having: decisions
that don't get re-litigated,
work that survives whoever made it, a fresh reader who can answer their
own question instead of cornering someone. What never actually happens
is someone doing it, because writing it up always loses the hour to
whatever's due today. Making the record a background part of the
process the agents already do — pulled out of the work as it happens,
not scheduled as a follow-up nobody gets to — is what finally delivers
on that, instead of just agreeing it would be nice. A company whose
knowledge outlives any one employment relationship
([COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) rule 2's Ghost)
is one case of this, not the whole of it: the person leaving becomes a
staffing change instead of a memory-loss event, same as any other
decision nobody has to reconstruct from memory.

**5. The deepest problems get caught by instinct, not by a checklist.**
A model can flag what fails its own checks — a broken link, a number
that doesn't add up, a claim that contradicts an earlier one. It has no
way to notice that a client's answer felt off, that a quiet teammate is
disengaging, that a plan is technically sound and still wrong for
reasons nobody wrote down. That kind of catch comes from instinct built
on experience no record holds — a sense that something's wrong before
anyone can say why. That instinct is exactly what the senior,
judgment-heavy work this repo keeps routing to people, not models,
actually runs on
([COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) rule 8), so the
skill and the work that needs it end up in the same hands.

See [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) for the theory behind why these
particular things happen.
