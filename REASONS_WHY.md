<!-- Last updated: 2026-08-28 19:46:33 (Buenos Aires) by Morgan F, to version 10 -->

# Reasons why

*Not "AI produces better results" and not "collaboration beats solo work"
— both true and both said so often they've stopped meaning anything.
These are the more specific, less obvious effects of actually working the
way [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) and the rest of this repo
describe: the kind that only show up once you've been doing it a while.*

**1. Being wrong gets cheap while it's still small.** Catching an error
the same hour costs one correction; catching it three weeks later costs
the correction plus a meeting reconstructing who approved what
([COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) rule 4). The gain
isn't the time saved — a wrong idea dies before it acquires allies.
Drift is the same failure in slow motion, caught by raw contact with the
work ([COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) rule 13) and
periodic contradiction-checks
([RULES_NOW_TESTING.md](RULES_NOW_TESTING.md#7-contradiction-scanning-across-the-corpus-as-a-recurring-job--trial)
item 7).

**2. Writing things down stops competing with getting things done.**
Documenting usually loses to the real work competing for the same hour.
Pulling the record out as a byproduct of working in the open — rules,
open items, reasoning — instead of a follow-up chore
([IDEAS.md](IDEAS.md)'s automatic extraction) removes that tax: the
writing already happened while the task did.

**3. Attaching the situation to a decision heads off the confusions
nobody sees coming.** This repo's merge runbook says never hand-merge
`process/upstream/` — as a bare instruction it loses the day
hand-resolving looks competent and breaks the mirror. Stating the
reason — this directory stays byte-identical — settles it before the
pull request, not three merges later. Every rule with its origin case
attached is that same trade
([OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) item 6).

**4. The power of documentation is almost magical — since no one finds
the time, AI will.** Everyone agrees a good record is worth having, but
writing it up always loses to whatever's due today. Making the record a
background part of the work agents already do — captured as it
happens, not scheduled — delivers on that. Knowledge that outlives any
employment relationship
([COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) rule 2's Ghost)
turns someone leaving into a staffing change.

**5. The deepest problems get caught by instinct, not by a checklist.**
A model flags what fails its own checks — a broken link, a number that
doesn't add up. It can't notice a client's answer felt off, or a plan
that's technically sound yet wrong for reasons nobody wrote down. That
catch is instinct, not checklist — judgment-heavy work this repo routes
to people, not models
([COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) rule 8).

**6. AI is superhuman at building rule lists, and at keeping them
current.** Turning an incident into a rule, checking it against
everything already on the list, and renumbering cross-references when
an entry moves — a person skips this once it's tedious, and the list
rots. A model runs the whole chain every pass, at any scale, without
getting bored or leaving a stale reference behind.

**7. Working in a second language stops costing quality.** Someone
forced to compose in an unfamiliar language spends part of their
attention on translation, and the record gets a thinner version of
their actual thinking. Letting people write and think in whatever
language comes naturally, with the AI carrying the translation into the
repo's shared working language, gets the real version into the record
instead ([IDEAS.md](IDEAS.md)).

**8. A private chat with an LLM is knowledge the company never gets.**
People already work through problems by talking to a model. When that
stays in a private chat window, the reasoning and the discarded options
leave with the chat history, and the company never had them. Doing the
same thinking in the open, in this repo, turns that habit into
information the company actually keeps (item 4 above).

**9. An intermediate AI layer in front of every action delivers
benefits nobody asked for.** Put a model between intent and the action
— a commit, a message, a purchase — and side benefits appear that
weren't the point: speaking an instruction works as well as typing one,
a half-formed plan gets contradicted before it fires, and the layer
holds the trace of why, so the rule that catches it next time falls out
for free (item 4 above).

See [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) for the theory behind why these
particular things happen.
