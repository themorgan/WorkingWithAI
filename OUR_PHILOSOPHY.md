<!-- Last updated: 2026-08-29 14:42:50 (Buenos Aires) by Morgan F, to version 22 -->

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
   (item 1 below).
3. Most of that arguing happens on GitHub in the open, and the decision
   and reasoning is tracked there — a pull request, not a secret chat
   log (items 2 and 3 below).
4. The AI Assistant produces all the output; you only guide it (items 4
   and 7 below).
5. The decisions, small to big, turn into learnings and shared rules
   and protocols automatically (items 5 and 6 below), staying visible
   to whichever session opens this repo next.

## The 7 Core Philosophies

**1. Coworking with a model means arguing with it.** State a half-formed
position, let the model push back, push back on its answer — keep going
until the exchange settles it, not either side alone. Instructing makes
a typist; polling for an opinion makes an oracle. Quality is one payoff:
agreement just hands back your blind spots ([rule 4](COMPANY_BUILDING_RULES.md),
[rule 5](COMPANY_BUILDING_RULES.md);
[AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)'s "argue in
the open").

**2. Context is capital.** Models produce competent output on demand, so
hours stopped being scarce. What's still scarce never got commoditized:
why the last vendor failed, what the customer meant, which option got
killed and why. Capturing that thinking is capital — an asset no
competitor can rent by Thursday ([rule 1](COMPANY_BUILDING_RULES.md)). The
same logic covers language: what someone writes in whatever tongue comes
naturally, with the AI carrying the translation into the shared record,
keeps the real thinking — a version forced through an unfamiliar language
on the way in would have been thinner ([REASONS_WHY.md](REASONS_WHY.md)
item 7).

**3. Processes should be visible, not locked in one person's brain.** A
workflow whose only interface is "email me and I'll handle it" is
invisible to everyone else. Bigger than tidiness ([rule 8](COMPANY_BUILDING_RULES.md)):
real intelligence is what anyone with the record can check, not what one
person knows. Every dark process trades convenience now for a
compounding blind spot.

**4. People manage; agents execute.** The human contribution is
planning, taste, judgment — deciding what gets built and whether it
works, the way defining a system beats hand-running it. Brief the model
like an individual contributor, stay engaged, adjust the plan as soon as
the first attempt reveals what the brief missed ([rule 13](COMPANY_BUILDING_RULES.md))
— same posture as item 1, applied to management.

**5. Protocols, rules, and preferences get generated automatically.** The
AI Assistant distills them straight out of the human-AI interaction —
the guidance, the correction, the back-and-forth of the working loop —
into a reusable rule the next session inherits automatically, no one
having sat down to write a policy. `process/personal/` is that mechanism
running continuously, not a document someone drafted once
([AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)'s "automatic
rule extraction";
[practice 20](process/upstream/PRACTICES.md#20-mistakes-become-rules-root-cause-the-miss-then-encode-the-prevention)
is the same move done by hand).

**6. Every decision carries the situation that produced it.** However
small the call, the record states what case prompted it — a bare
"always do X" invites relitigation from anyone who wasn't there. The
case also tests the rule: one that wouldn't have caught it is theater.
BestPractice already requires this
([practice 5](process/upstream/PRACTICES.md#5-conventions-cite-the-incident-that-created-them),
[practice 20](process/upstream/PRACTICES.md#20-mistakes-become-rules-root-cause-the-miss-then-encode-the-prevention));
capture is the
agents' job, pulled from the work as it happens (item 5's rule
extraction).

**7. Humans should do what humans do best.** Machines produce; people
bring judgment, relationships, instinct: reading a room, sensing what a
client meant but didn't say, pushing someone harder when the moment
calls for it. Optimizing a person to act like a fast, tireless model
optimizes away what they're for ([rule 15](COMPANY_BUILDING_RULES.md)) —
hold them to that standard, not a machine's.

See [REASONS_WHY.md](REASONS_WHY.md) for what these ideas actually buy in
practice.
