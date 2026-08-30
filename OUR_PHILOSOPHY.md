<!-- Last updated: 2026-08-30 18:50:50 (Buenos Aires) by Morgan F, to version 32 -->

# Our philosophy

*The theoretical layer underneath everything else in this repo, not a new
argument. [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) makes the
case for running a company this way; [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)
makes the case for building the AI systems that way. Both assume a handful
of ideas about memory, judgment, and how work actually produces quality.
This document names those ideas and explains them on their own terms,
without re-arguing for them. It's an account of the theory, not a pitch
for it.*

## The working loop

The same five steps repeat every time, in order:

1. A spark — an idea, new data, an incoming request, a changed system
   message.
2. Argue it out with an AI Assistant that has this repo attached, so
   the argument runs against the actual record instead of a guess
   ([`arguing-with-the-model`](#arguing-with-the-model)).
3. Most of that arguing happens on GitHub in the open, and the decision
   and reasoning is tracked there — a pull request, not a secret chat
   log ([`context-is-capital`](#context-is-capital),
   [`processes-should-be-visible`](#processes-should-be-visible)).
4. The AI Assistant produces all the output; you only guide it
   ([`people-manage-agents-execute`](#people-manage-agents-execute),
   [`humans-do-what-humans-do-best`](#humans-do-what-humans-do-best)).
5. The decisions, small to big, turn into learnings and shared rules
   and protocols automatically
   ([`rules-generated-automatically`](#rules-generated-automatically),
   [`decisions-carry-their-situation`](#decisions-carry-their-situation)),
   staying visible to whichever session opens this repo next.

## The 8 Core Philosophies

<a id="context-is-capital"></a>

**1. Context is core.** [`capital-asset`](COMPANY_BUILDING_RULES.md#capital-asset)
makes the case for capturing this. What matters is the residue, not
the deliverable — the option tried and killed, the correction only
legible against the draft it corrected. One document carries that
forward for the next session; another reaches the same conclusion and
reads as if it had always been obvious. Language works the same way:
the AI carrying the translation keeps thinking real, not thinned
([`second-language-stops-costing-quality`](REASONS_WHY.md#second-language-stops-costing-quality)).

<a id="arguing-with-the-model"></a>

**2. Coworking with a model means arguing with it.** State a half-formed
position, let the model push back, push back on its answer — keep going
until the exchange settles it, not either side alone. Instructing makes
a typist; polling for an opinion makes an oracle. Quality is one payoff:
agreement just hands back your blind spots
([`ai-chat-as-intermediary`](COMPANY_BUILDING_RULES.md#ai-chat-as-intermediary),
[`co-create-dont-delegate`](COMPANY_BUILDING_RULES.md#co-create-dont-delegate);
[`argue-in-the-open`](AI_GOVERNANCE_TO_COCREATE.md#argue-in-the-open)).

<a id="processes-should-be-visible"></a>

**3. Processes should be visible, not locked in one person's brain.** A
workflow whose only interface is "email me and I'll handle it" is
invisible to everyone else. Bigger than tidiness
([`no-dark-processes`](COMPANY_BUILDING_RULES.md#no-dark-processes)):
real intelligence is what anyone with the record can check, not what one
person knows. Every dark process trades convenience now for a
compounding blind spot.

<a id="people-manage-agents-execute"></a>

**4. People manage; agents execute.** The human contribution is
planning, taste, judgment — deciding what gets built and whether it
works, the way defining a system beats hand-running it. Brief the model
like an individual contributor, stay engaged, adjust the plan as soon as
the first attempt reveals what the brief missed
([`manager-of-agents`](COMPANY_BUILDING_RULES.md#manager-of-agents))
— same posture as [`arguing-with-the-model`](#arguing-with-the-model),
applied to management. (Full list:
[HUMANS_AT_OUR_BEST.md](HUMANS_AT_OUR_BEST.md).)

<a id="rules-generated-automatically"></a>

**5. Protocols, rules, and preferences get generated automatically.**
What's automatic is the finding: the AI Assistant surfaces the pattern
every time, without anyone having to remember to look. Turning it into
a standing rule is a human call, routed by this repo's own rules to
whoever's responsible — and a spotted pattern always gets surfaced,
never left unremarked. `process/personal/` runs that mechanism
continuously
([`automatic-rule-extraction`](AI_GOVERNANCE_TO_COCREATE.md#automatic-rule-extraction);
[practice 20](process/upstream/PRACTICES.md#20-mistakes-become-rules-root-cause-the-miss-then-encode-the-prevention)
is the same move done by hand).

<a id="decisions-carry-their-situation"></a>

**6. Every decision carries the situation that produced it.** However
small the call, the record states what case prompted it — a bare
"always do X" invites relitigation from anyone who wasn't there. The
case also tests the rule: one that wouldn't have caught it is theater.
BestPractice already requires this
([practice 5](process/upstream/PRACTICES.md#5-conventions-cite-the-incident-that-created-them),
[practice 20](process/upstream/PRACTICES.md#20-mistakes-become-rules-root-cause-the-miss-then-encode-the-prevention));
capture is the
agents' job, pulled from the work as it happens
([`rules-generated-automatically`](#rules-generated-automatically)'s
rule extraction).

<a id="humans-do-what-humans-do-best"></a>

**7. Humans should do what humans do best.** Machines produce; people
bring judgment, relationships, instinct: reading a room, sensing what a
client meant but didn't say, pushing someone harder when the moment
calls for it. Optimizing a person to act like a fast, tireless model
optimizes away what they're for
([`structurally-human`](COMPANY_BUILDING_RULES.md#structurally-human)) —
hold them to that standard, not a machine's. (Full list:
[HUMANS_AT_OUR_BEST.md](HUMANS_AT_OUR_BEST.md).)

<a id="explicit-ownership-not-hidden-in-the-model"></a>

**8. Protocols, documents, and knowledge should be explicitly owned by
the team, not hidden inside Claude.** Claude and ChatGPT already infer
your implicit patterns as you work — the question is where that
inference lives afterward: locked inside a vendor's private session
state, gone the moment you switch tools, or pulled into files the team
can read, edit, and hand to a different model entirely.
[`rules-generated-automatically`](#rules-generated-automatically) does
the pulling; left inside the chat, a rule benefits no one once that
conversation ends
([`owned-rules-outlast-the-chat`](REASONS_WHY.md#owned-rules-outlast-the-chat)).

See [REASONS_WHY.md](REASONS_WHY.md) for what these ideas actually buy in
practice.
