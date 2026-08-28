<!-- Last updated: 2026-08-28 12:58:31 (Buenos Aires) by Morgan F, to version 5 -->

# Our philosophy

*The theoretical layer underneath everything else in this repo, not a new
argument. [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) makes the
case for running a company this way; [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)
makes the case for building the AI systems that way. Both assume a handful
of ideas about memory, judgment, and how work actually produces quality.
This document names those ideas and explains them on their own terms,
without re-arguing for them. It's an account of the theory, not a pitch
for it.*

**1. If it isn't written down, it doesn't exist.** A decision made in a
hallway survives only as long as the people who were there remember it.
Treat text as the substrate of memory, not a record of it: a thing
counts as done only once it's written, since "done in someone's head"
behaves like "not done." That's what makes transcribing past the point
of comfort rational, not obsessive (rule 2), and makes "it doesn't leave
your hands until you'd defend it" coherent (rule 3). A full written
record also stays checkable against reality rather than only against
itself — you can re-read it for contradictions, or hand it to a fresh
session and ask whether it could reconstruct a live decision from the
record alone (the coldstart test), which is what catches a summary that
has drifted while still reading as coherent (rule 13).

**2. Context is capital. Hours are not.** For most of business history
the scarce input was time — pay enough hours and the work got done. That
stopped being true once a model could produce competent output on
demand. What stayed scarce is what never got commoditized: why the last
vendor failed, what the customer meant versus what they said, which
option got killed and why — material that lived in one person's head. A
conclusion written down without the thinking behind it is nearly as
opaque as no decision at all. Capturing that thinking is capital
expenditure: an asset a competitor can't rent by Thursday afternoon
(rule 1).

**3. Every decision carries the situation that produced it.** However
small the call, the record says what specific case prompted it. A bare
instruction — "always do X" — invites relitigation from anyone who
wasn't in the room and misapplication by everyone else, because nothing
in it says what it was protecting against. The originating case gives a
later reader what they need to judge whether the rule still applies to
the situation in front of them, and it doubles as the rule's own test:
a guard that wouldn't have caught the case that created it is theater,
and you can only see that when the case sits next to it. This is the
practice layer's own standard, not a preference of ours — BestPractice
requires conventions to cite the incident that created them, and
requires a mistake to be root-caused into a dated rule carrying that
incident ([PRACTICES.md](process/upstream/PRACTICES.md) practices 5 and
20). Doing it by hand loses to whatever's due today, so the capture is
the agents' job, pulled out of the work as it happens
([IDEAS.md](IDEAS.md)'s automatic rule extraction).

**4. Quality comes from disagreement, not compliance.** A model that
complies with whatever you propose just gives back your own thinking,
blind spots included. The fix is a mechanism, not a nicer tone: make the
model argue the other side, find the hole in the logic before you've
committed (rule 4; [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)'s
"argue in the open"). "Co-create as partners" undersells this — the
useful version is disagreement, deliberately introduced, since agreement
with yourself can't catch what agreement with yourself produced.

**5. Processes should be intensely visible, not locked in one person's
brain.** A workflow whose entire interface is "email me and I'll handle
it" is invisible to everyone but that person. The idea behind "no dark
processes" (rule 10) is bigger than tidiness: an organization's actual
intelligence is what's checkable by anyone with access to the record,
not what one person knows. Every dark process trades convenience now for
a blind spot that compounds.

**6. People manage; agents execute.** The distinctly human contribution
isn't producing the draft — it's the planning, creativity, and taste
that decide what gets built and whether it's actually working, the way
defining a system well beats hand-running each step of it. Treat the
model as an individual contributor: brief it clearly, stay engaged while
it works, adjust the plan the moment the first attempt reveals what the
brief missed — not a spec handed off once and picked up at the end (rule
14). Same posture as "co-create" (item 4), applied to managing the work.

**7. Humans should do what humans do best.** Machines are for
production; people are for judgment, relationships, instinct, and the
parts of a situation nobody wrote down — reading a room, sensing what a
client meant but didn't say, pushing a colleague harder because the
moment calls for it. Optimizing a person to act like a fast, tireless
model optimizes away what they're actually good for (rule 15). The
standard isn't "be a better machine." It's "be a good human."

See [REASONS_WHY.md](REASONS_WHY.md) for what these ideas actually buy in
practice.
