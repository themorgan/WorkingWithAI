<!-- Last updated: 2026-08-29 07:56:08 (Buenos Aires) by Morgan F, to version 6 -->

# AI governance to co-create

*Governance for the AI systems themselves: how to configure, build, and
run them so co-creation — rule 4 of
[COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md), arguing with the
model in real time rather than delegating to it — is the default outcome,
not something a disciplined person has to manufacture by hand every
session. COMPANY_BUILDING_RULES.md is this repo's stage-1 "why" half — the
case for running a company this way at all; this document is one level
down, about the systems rather than the company. "Co-creation" here is
used as the umbrella term for that whole healthy pattern, not narrowly
rule 4 alone — a judgment call; flag it if the scope should split.
Promoted out of [IDEAS.md](IDEAS.md), same pattern as
COMPANY_BUILDING_RULES.md before it. Neither essay is itself a checklist
anyone follows day to day — [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md)
is where an idea from either one gets tried in real work before it's
ready to be called a rule.*

## Memory & context

**Persistent, versioned, greppable state should be the default shape, not
a special case.** Context only behaves like capital (rule 1) if it
outlives the session that made it — durable, diffable state should beat
ephemeral chat by default.

**Automatic rule extraction should be a standing capability, not a manual
habit.** Distill protocols, rules, and preferences straight out of the
interaction — the guidance, the correction — instead of waiting for
someone to write policy by hand; `process/personal/` runs this
continuously (IDEAS.md's 3a).

**A coldstart test, run like any other check.** Can a fresh session, given
only the memory store, reconstruct the current state of any live
decision? If not, the transcription (rule 2) failed somewhere specific
and locatable.

**Resurfacing should be active, not just searchable.** A system that only
answers when asked misses what nobody thought to ask — the better version
notices "you decided X six weeks ago" unprompted, when it's relevant now.

## Interaction design

**Push-back as a configuration switch, not a personality quirk.** Argue a
genuine counter-case on writing/thinking work, comply on technical
execution — the switch should track task shape, not sit fixed at the
system level.

**The two reflexes from rule 6 belong in the system prompt, not just a
human's habit.** An agent that asks itself "have I done this shape
before" mid-task, and says so, does more of rule 5's work than a person
remembering to ask.

**Argue in the open.** An AI reviewer that holds a half-formed position
and invites disagreement, rather than posting a clean finished-looking
suggestion, keeps the disagreement itself in the record.

## Interface

**Chat is the primary interface to every document, not a shortcut around
them.** The AI constantly creates, tracks, and organizes documents and
thoughts, and a human can always go read or edit them directly — but most
human work will be asking the AI questions answered in the docs and
brainstorming with the AI on what to do, then guiding the AI to do it,
not reading, writing, or editing docs directly. The docs are the AI's
working memory; chat is where the human actually works.

## Verification

**Confidence should look non-uniform, because it isn't.** If every claim
reads with the same even prose confidence, rule 8's "find the one false
paragraph" skill has nothing to grab onto. Flag the weaker claims — a
hedge, a citation, an assumption — so a verifier has a place to start.

## Workflow & cost sensitivity

**Automatic workflow-candidate detection.** Mine the history itself —
commits, sessions, transcripts — for recurring task shapes instead of
relying on a human noticing "this is the third time." Turns rule 5's
judgment call into a standing job.

**Cost-awareness should be situational, inferred by the system, not a
fixed global policy.** Whether cost discipline is even the right posture
varies by person, project, and moment — sometimes you want rule 9's
"build five, kill four" lavishness instead. The harder problem is the
system inferring which situation it's in — from a budget mention, project
stage, or stated intent — rather than applying one policy everywhere.

## Voice & output

**A structural "sounds like AI" check.** Rule 11 names the actual
fingerprints — the throat-clearing opener, "not just X, it's Y," the
bolded summary nobody asked for. Those are mechanical enough to check for
before publishing, rather than relying on a human catching it every time.

## Surfacing blind spots

**Configure the AI to hunt its own dark processes.** Have it periodically
list workflows whose only interface is a human inbox — including its own
— and propose an addressable alternative, per rule 10.

**Rotation and temp workflows get periodic check-ins, not baked-in
expiry.** A hard sunset date, taken literally from rule 15, forces an end
even when a workflow is going well. Better: a recurring, low-cost
reminder — "is this still needed, still the right shape?"

## Keeping the corpus honest

**Contradiction-scanning as a recurring job, not a one-off pass.** A
compounding corpus (rule 1's own metaphor) rots quietly if nothing
re-reads it for internal disagreement — worth standing up as a periodic
pass, not something that only runs once someone thinks of it.

**Provider-neutrality is a hedge on rule 1, not a preference.** Context
built against one vendor's tooling shouldn't be strandable by a provider
switch — the capital asset is the context, not the platform it's sitting
in today.

---

**Set aside this thread, not carried forward:** a mandatory eval-file gate
before any output ships (unclear how it generalizes past code, where
"eval" has an obvious technical meaning); having the AI itself pick which
raw, unfiltered sample a human reviews for rule 13's human-only zones
(the idea didn't land clearly enough in discussion to write down yet —
worth re-raising once it's sharper, rather than forcing it in now).
