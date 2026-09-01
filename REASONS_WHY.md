<!-- Last updated: 2026-09-01 15:56:02 (Buenos Aires) by Morgan F, to version 19 -->

# Reasons why

*Not "AI produces better results" and not "collaboration beats solo work"
— both true and both said so often they've stopped meaning anything.
These are the more specific, less obvious effects of actually working the
way [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) and the rest of this repo
describe: the kind that only show up once you've been doing it a while.*

## Knowledge that stays yours

<a id="private-chat-is-lost-knowledge"></a>

**1. A private chat with an LLM is knowledge the company never gets.**
People already work through problems by talking to a model. When that
stays in a private chat window, the reasoning and the discarded options
leave with the chat history, and the company never had them. Doing the
same thinking in the open, in this repo, turns that habit into
information the company actually keeps
([`protocols-generated-not-just-documented`](#protocols-generated-not-just-documented)
below).

<a id="owned-rules-outlast-the-chat"></a>

**2. Rules hidden in a model benefit the company behind the model, not
yours.** Claude and ChatGPT already reconstruct your implicit
preferences and patterns as you go — that's a real part of what makes
them feel like they "get" you. Left inside the vendor's own session
state, that inference resets next conversation, doesn't transfer to a
teammate, and disappears the day you switch tools. Pulled out into this
repo's own files instead, the same inference becomes a rule anyone can
read, edit, and hand to a different model entirely
([`explicit-ownership-not-hidden-in-the-model`](OUR_PHILOSOPHY.md#explicit-ownership-not-hidden-in-the-model)).

## Records and rules that write themselves

<a id="intermediary-layer-side-benefits"></a>

**3. An intermediate AI layer in front of every action improves output
& allows context sharing.** Put a model between intent and the action
— a commit, a message, a purchase — and side benefits appear that
weren't the point: speaking an instruction works as well as typing one,
a half-formed plan gets contradicted before it fires, and the layer
holds the trace of why, so the rule that catches it next time falls out
for free
([`protocols-generated-not-just-documented`](#protocols-generated-not-just-documented)
below;
[`ai-chat-as-intermediary`](COMPANY_BUILDING_RULES.md#ai-chat-as-intermediary)).

<a id="writing-stops-competing-with-doing"></a>

**4. Team Members rarely document protocols, patterns, why they did what
they did, because they always have more important work to do.**
Documenting usually loses to the real work competing for the same hour.
Pulling the record out as a byproduct of working in the open — rules,
open items, reasoning — instead of a follow-up chore
([`rules-generated-automatically`](OUR_PHILOSOPHY.md#rules-generated-automatically)'s
automatic extraction) removes that tax: the writing already happened
while the task did.

<a id="protocols-generated-not-just-documented"></a>

**5. The power isn't documentation — it's protocols generated
automatically, since no one finds the time to write them by hand.** This
reason is one third of
[THE_REVOLUTIONARY_FORMULA.md](THE_REVOLUTIONARY_FORMULA.md)'s case for
what makes this repo's approach unique.
Everyone agrees a good record is worth having, but writing it up always
loses to whatever's due today, and a static record wouldn't be the real
prize anyway. What pays off is the same background work turning into
rules and protocols the next session inherits — captured as it happens,
not scheduled
([`rules-generated-automatically`](OUR_PHILOSOPHY.md#rules-generated-automatically)).
Knowledge that outlives any employment relationship
([`transcribe-everything`](COMPANY_BUILDING_RULES.md#transcribe-everything)'s
Ghost) turns someone leaving into a staffing change.

<a id="situation-heads-off-confusion"></a>

**6. Decisions with the reason attached prevent regressions.**
This repo's merge runbook says never hand-merge
`process/upstream/` — as a bare instruction it loses the day
hand-resolving looks competent and breaks the mirror. Stating the
reason — this directory stays byte-identical — settles it before the
pull request, not three merges later. Every rule with its origin case
attached is that same trade
([`decisions-carry-their-situation`](OUR_PHILOSOPHY.md#decisions-carry-their-situation)).

## Working across languages

<a id="second-language-stops-costing-quality"></a>

**7. Working in a second language stops costing quality.** Someone
forced to compose in an unfamiliar language spends part of their
attention on translation, and the record gets a thinner version of
their actual thinking. Letting people write and think in whatever
language comes naturally, with the AI carrying the translation into the
repo's shared working language, gets the real version into the record
instead ([`context-is-capital`](OUR_PHILOSOPHY.md#context-is-capital)).

## Catching problems while they're still small

<a id="wrong-gets-cheap-early"></a>

**8. Being wrong gets cheap while it's still small.** Catching an error
the same hour costs one correction; catching it three weeks later costs
the correction plus a meeting reconstructing who approved what
([`co-create-dont-delegate`](COMPANY_BUILDING_RULES.md#co-create-dont-delegate)).
The gain isn't the time saved — a wrong idea dies before it acquires
allies. Drift is the same failure in slow motion, caught by raw contact
with the work
([`human-only-zones`](COMPANY_BUILDING_RULES.md#human-only-zones)) and
periodic contradiction-checks
([`contradiction-scanning`](RULES_NOW_TESTING.md#contradiction-scanning)).

<a id="instinct-catches-what-checklists-miss"></a>

**9. The biggest problems, that go to the core of why you're there, get
caught by instinct, never by smart checklists.**
A model flags what fails its own checks — a broken link, a number that
doesn't add up. It can't notice a client's answer felt off, or a plan
that's technically sound yet wrong for reasons nobody wrote down. That
catch is instinct, not checklist — judgment-heavy work this repo routes
to people, not models
([`hire-for-drive`](COMPANY_BUILDING_RULES.md#hire-for-drive)).

See [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) for the theory behind why these
particular things happen.
