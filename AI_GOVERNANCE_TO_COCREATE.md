<!-- Last updated: 2026-08-27 23:09:41 (Buenos Aires) by Morgan F, to version 3 -->

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
a special case.** This repo's own repo-as-memory pattern is the proof:
context only behaves like capital (rule 1) if it survives past the
session that created it. The general claim is that any AI system meant to
compound should default to durable, diffable state over ephemeral chat.

**A coldstart test, run like any other check.** Can a brand-new session,
given only the memory store and no human in the loop, reconstruct the
current state of any live decision? If not, the transcription (rule 2)
failed somewhere specific and locatable — which makes it testable rather
than just aspirational.

**Resurfacing should be active, not just searchable.** A system that only
answers when asked misses the cases nobody thought to ask about. The
better version notices "you decided X six weeks ago" unprompted, when it's
relevant to what's happening now — this is IDEAS.md's open question about
proactive resurfacing, generalized past this one repo.

## Interaction design

**Push-back as a configuration switch, not a personality quirk.** The
personal pack's distinction — argue a genuine counter-case on
writing/thinking work, comply on technical execution — is a general
pattern worth naming on its own: most AI configurations pick one register
globally (always-comply or always-argue) and both are wrong for some
fraction of what they're used for. The switch should track task shape, not
be fixed at the system level.

**The two reflexes from rule 6 belong in the system prompt, not just in a
human's habit.** An agent that asks itself "have I done this shape before"
mid-task, and says so, does more of rule 5's work than a human remembering
to ask periodically.

**Argue in the open.** An AI reviewer that holds a half-formed position and
invites disagreement, instead of posting a clean finished-looking
suggestion, keeps the disagreement itself in the record — this is
IDEAS.md's "PR comments as argument" idea, generalized past pull requests
to any AI-reviewed artifact.

## Verification

**Confidence should look non-uniform, because it isn't.** If every claim in
an output reads with the same even prose confidence, rule 8's "find the
one false paragraph" skill has nothing to grab onto. Output that flags its
own weaker claims — a hedge, a citation, an explicit assumption — gives a
verifier a place to start instead of forcing them to re-derive everything
from scratch.

## Workflow & cost sensitivity

**Automatic workflow-candidate detection.** Instead of relying on a human
noticing "this is the third time," mine the history itself — commits,
sessions, transcripts — for recurring task shapes and surface the
candidate. Turns rule 5's judgment call into a standing job rather than a
thing that only happens if someone happens to notice.

**Cost-awareness should be situational, inferred by the system, not a
fixed global policy.** Earlier draft of this idea proposed surfacing spend
per outcome the way CI surfaces test results, framed as a straightforward
cost-discipline win. The objection that landed: whether cost discipline is
even the right posture varies by person, project, and moment — sometimes
you're watching spend closely, sometimes you deliberately want to indulge
rule 9's "build five, kill four" and let generation be cheap and lavish.
Making cost visibility a default pressure gets that wrong in whichever
direction the situation doesn't call for. The harder and more interesting
design problem is the system inferring *which* situation it's in — reading
signals like an explicit budget mention, the project's stage (exploring
vs. shipping), or stated intent ("throw a bunch of options at this" vs.
"keep this efficient") — rather than applying one policy everywhere. Plain
cost logging (the passive record, not an optimization target) is still
worth keeping regardless of which mode is active.

## Voice & output

**A structural "sounds like AI" check.** Rule 12 names the actual
fingerprints — the throat-clearing opener, "not just X, it's Y," the
bolded summary nobody asked for. Those are mechanical enough to check for
before publishing, rather than relying on a human catching it every time,
which is exactly the kind of single-point-of-failure rule 10 warns about
elsewhere.

## Surfacing blind spots

**Configure the AI to hunt its own dark processes.** Have it periodically
list workflows whose only interface is a human inbox — including its own
("email Morgan to change this config" counts) — and propose an addressable
alternative, per rule 10.

**Rotation and temp workflows get periodic check-ins, not baked-in
expiry.** Earlier draft proposed a hard sunset date written into the
process file at creation (rule 11's "temporary-on-purpose" framing, taken
literally). Objection: if a workflow is going well, there's no reason it
should have to end — the goal isn't churn, it's making sure it's still
earning its place. The better version is a recurring, low-cost reminder —
"is this still needed, still the right shape?" — rather than a deadline
that forces a decision whether or not one is actually due.

## Keeping the corpus honest

**Contradiction-scanning as a recurring job, not a one-off pass.** A
compounding corpus (rule 1's own metaphor) rots quietly if nothing ever
re-reads it looking for internal disagreement. Worth standing up as a
periodic pass in any system holding this kind of accumulated brainstorm,
not just running once when someone thinks of it.

**Provider-neutrality is a hedge on rule 1, not a preference.** The
personal pack already requires this for LLM integrations in this repo.
Stated as a general principle: context built against one vendor's tooling
shouldn't be strandable by a provider switch — the capital asset is the
context, not the platform it happens to be sitting in today.

---

**Set aside this thread, not carried forward:** a mandatory eval-file gate
before any output ships (unclear how it generalizes past code, where
"eval" has an obvious technical meaning); having the AI itself pick which
raw, unfiltered sample a human reviews for rule 14's human-only zones
(the idea didn't land clearly enough in discussion to write down yet —
worth re-raising once it's sharper, rather than forcing it in now).
