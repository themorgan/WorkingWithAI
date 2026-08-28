<!-- Last updated: 2026-08-28 09:08:29 (Buenos Aires) by Morgan F, to version 3 -->

# Our philosophy

*The theoretical layer underneath everything else in this repo, not a new
argument. [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) makes the
case for running a company this way; [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)
makes the case for building the AI systems that way. Both assume a handful
of ideas about memory, judgment, and how work actually produces quality.
This document names those ideas and explains them on their own terms,
without re-arguing for them. It's an account of the theory, not a pitch
for it.*

**1. If it isn't written down, it doesn't exist.** A decision made in a hallway
and never written down exists exactly as long as the people who were in
the hallway remember it, which in practice means it stops existing the day
the wrong person forgets or moves on. Treat text as the actual substrate
of organizational memory rather than a record of it, and something
follows: a thing counts as done only once it's written, because "done in
someone's head" behaves like "not done" from every vantage but one. That
premise is what makes transcribing past the point of comfort rational
instead of obsessive (rule 2), and what makes "if you didn't read it
closely enough to defend it, it doesn't leave your hands" a coherent
standard rather than a strict one (rule 3). Both only make sense once what
isn't text has stopped counting as something the organization actually
knows.

**2. Context is capital. Hours are not.** For most of business history the
scarce input was time: pay for enough hours and the work got done. That
stopped being true the week a model could produce competent output on
demand. Hours are close to unlimited now, and nearly free. What stayed
scarce is the material that never got commoditized in the first place —
why the last vendor actually failed, what the customer meant versus what
they said, which option got killed and why. That material was always
locked inside one person's head, a form of scarcity no amount of hiring
solves. The conclusion alone doesn't fix this — a decision written down
without the thinking that produced it is nearly as opaque as no decision
at all, because nobody downstream, human or model, can tell whether the
reasoning still holds once the situation has moved. Capturing it is
capital expenditure in the literal sense: it produces an asset a
competitor can't buy, because renting the same model
from the same vendor by Thursday afternoon doesn't hand them your reasons
(rule 1). Counting effort in licenses activated measures the one input
that was never actually scarce.

**3. Quality comes from disagreement, not compliance.** A model that
complies with whatever you propose gives back your own thinking, blind
spots included; asking it to produce something and then editing the
result never surfaces what you didn't already believe. The alternative is
a specific mechanism, not a nicer working relationship: making the model
argue the other side, ask for the hole in the logic before you've
committed to it, hold a genuine counter-position instead of a polished
suggestion. What the model answers matters less than what surviving its
objection does to the claim you started with (rule 4; [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)'s
"argue in the open"). This is why "co-create as partners" undersells the
idea. The useful version isn't partnership as a warm tone; it's
disagreement, deliberately introduced, because agreement with yourself
can't catch what agreement with yourself produced.

**4. Judgment is scarce. Production is not.** When a first
draft costs nothing, having ten of them stops being an advantage, and the
entire question becomes which one is actually right. That question is
harder than it looks, because this era's characteristic failure is output
that's confidently, plausibly wrong and reads fine on a casual pass. The
skill that catches it, reading twenty drafts and knowing which paragraph
is quietly false and why, is rare and testable, and not what most hiring
and career paths were built to reward (rules 7 and 8). An organization
still optimizing for who produces the most is optimizing a metric that
stopped being the bottleneck. The constraint moved to whoever can tell a
right answer from a good-sounding one, fast, and that's where the
interesting work sits now too.

**5. Processes should be intensely visible, not locked in one person's
brain.** Any workflow whose entire interface is "email me and I'll handle
it" is invisible to everyone but that one person, since the only
description of how it works lives in the same place the work happens —
nothing gets written down, so nothing can be inspected or improved. The
idea underneath "no dark processes" (rule 10) is bigger than tidiness. An
organization's actual intelligence isn't the sum of what any person in it
knows; it's the sum of what's addressable, reachable and checkable by
anyone with access
to the record, human or otherwise. Every dark process trades a little
convenience now for a blind spot that compounds the same way the corpus
does, in the opposite direction.

**6. Records should be checked against reality, not just against
themselves.** Any system where everyone downstream consumes only the digest
loses the one thing that would let it notice its own drift, because a
summary of something slightly wrong reads exactly as coherent as a
summary of something right. The distortion doesn't show up until someone
checks the digest against the raw thing underneath it. That's the
reasoning behind protecting unfiltered contact on purpose (rule 13),
re-reading the corpus periodically for entries that have started to
disagree with each other, and asking whether a fresh, contextless session
could reconstruct the state of a live decision from the record alone (the
coldstart test, [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)'s
"Memory & context" and "Keeping the corpus honest"). None of this is
quality-control theater. It's the only channel left that can report the
record has started lying to itself, and a system that never checks has no
way of finding out before a customer does.

**7. Direction must be continuous, not a one-time handoff.** "Co-create" (item 3)
names the posture — argue, don't comply — but there's a separate, more
basic shift underneath it in what making something with a model actually
looks like day to day. The old shape is a handoff: describe what you want,
walk away, come back to a finished thing and edit it. The shape that
actually works is instructing, guiding, tweaking, and fixing the output
while it's still being made, not after — catching the wrong turn on
paragraph two instead of discovering it on paragraph twenty, adjusting the
plan mid-draft instead of re-briefing from scratch once the whole thing
has to be redone. A model given a broad brief and left alone commits early
to one reading of it and runs with that reading, confidently, all the way
to the end. Staying present through the making, not just at the start and
the end of it, is what keeps the output converging on the actual intent
instead of a plausible guess at it.

See [REASONS_WHY.md](REASONS_WHY.md) for what these ideas actually buy in
practice.
