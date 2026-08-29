<!-- Last updated: 2026-08-29 15:12:22 (Buenos Aires) by Morgan F, to version 7 -->

# Rules for building a company around AI

*The "why" half of this repo's stage-1 pair — the case for running a
company this way at all. [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)
is the "how" half, one level down: what it takes to build the AI systems
themselves so this becomes the default, rather than something a
disciplined person has to manufacture by hand every session. Neither essay
is itself a checklist anyone follows day to day —
[RULES_NOW_TESTING.md](RULES_NOW_TESTING.md) is where an idea from either
one gets tried in real work before it's ready to be called a rule. Source
essay for the brainstorm — see [IDEAS.md](IDEAS.md) for how this connects
to the rest and for follow-on discussion. Promoted to its own document per
the "reorganize once a group gets big enough" rule in [IDEAS.md](IDEAS.md),
since it's a single sustained argument rather than a loose list of
entries.*

Every founder, every operator, every manager, every person anywhere who has
ever tried to get something done through other people knows one thing and has
never had a reason to write it down: almost nothing that made the work come
out right was ever in the work. It was in somebody's head, and then the head
went to lunch. Survivable for the entire history of commerce. It stopped
being survivable the week a machine could read everything you own, and the
rules below all fall out of that, grouped by where they bite: the case
itself, then how you actually work with the model day to day, then how you
ship and run things, then who you hire and keep.

## Foundations

<a id="capital-asset"></a>

**1. Context is the capital asset.**

The scarce input isn't hours anymore — it's the tacit, never-written-down
stuff that makes a task come out right: why the last vendor failed, what
the customer actually meant, which option you already killed and why.
Capturing that is capital expenditure now, not overhead. A *corpus* is a
body, and a body dies when you stop feeding it. Your competitor rents the
same models by Thursday; what nobody can rent is yours.

<a id="transcribe-everything"></a>

**2. Transcribe everything, past the point of comfort.**

Meetings, calls, site visits, the argument that got resolved and the one
that didn't — transcribe it, don't erase it. Picture a colleague who's
been there since the founding, remembers everything, never sleeps, and
has no eyes or ears, only text. Call it the Ghost — the most experienced
employee in the building, unable to attend anything. Every meeting you
leave untranscribed is one more organ you've removed from it. Most
companies do the easy 5%; the number that matters is nearer 90%, and
closing that gap is cultural — people need to hear *compounding*, not
*recorded*.

<a id="own-every-word"></a>

**3. You own every word you pass on.**

If you didn't read something closely enough to defend it, it doesn't
leave your hands — not to a colleague, a customer, or a deck someone else
presents while you're on a plane. What actually kills a company is four
handoffs where everyone skimmed and assumed the person before had read it
closely. The error surfaces at the customer, the most expensive room and
the last one you hear about. If you can't answer a question about the
fourth paragraph, you haven't finished the work.

## Working with the model

<a id="ai-chat-as-intermediary"></a>

**4. Treat the AI Chat as the intermediary for the work itself, not a tool you consult on the side.**

Every plan and decision worth a moment's thought runs through it before
it runs through anyone else — not because it produces the output, but
because it's the partner that pushes back: the hole in the logic, the
option you haven't considered, the version that's actually better. That
same layer is what pushes things into happening — the commit, the
message, the next step — instead of a good idea that never left
somebody's head. Put a model between intent and action, and arguing
before you commit becomes the habit, for free.

<a id="co-create-dont-delegate"></a>

**5. Co-create; don't delegate.**

The low-value mode is "produce this for me and I'll edit it." The
high-value mode is thinking with the model in real time — arguing the
opposite side, asking for the hole in your logic before you've committed
to it. The tell that someone's crossed over: their sessions read like
fights, not requests. Research and drafting are the beginner uses; the
real gain is catching your own error an hour after you made it, not three
weeks later in front of the client.

<a id="three-questions"></a>

**6. Three questions, asked until they're reflexes.**

A long checklist buys you people who spend the day interrogating their
work instead of doing it. So: three questions, drilled until nobody
notices they're asking them, because this is what the AI is doing too:

- What rules or protocols should come from this?
- Have I done this shape before, or will I again? If yes, it's a
  workflow, and you're doing it by hand.
- Is there a way Claude could make this better? Not faster — better.

*Faster* makes people think about the work they already do. *Better*
makes them notice the work they'd quietly stopped proposing years ago.

<a id="think-in-workflows"></a>

**7. Think in workflows — and in the protocols and rules that fall out of them.**

Stopping to systematize a one-off is procrastination in a nice suit. First
time, do it by hand, with the model. Third time you've seen the shape,
stop — that repetition just handed you the spec for free. The same
reflex runs one level up: every correction and judgment call is itself a
repeating shape, so capture it as a rule the moment it does, automatically,
a byproduct of the work rather than a separate write-up. Never
systematize and you stay fast forever; systematize everything, workflow
and rule alike, and you ship nothing, beautifully diagrammed.

## Shipping and process

<a id="no-dark-processes"></a>

**8. No dark processes.**

Any workflow you can only trigger by emailing a person becomes the
bottleneck for everything downstream of it — expense approvals and shift
scheduling as much as anything an engineer would call a system. Go
process by process and kill the ones whose only interface is somebody's
inbox: "just email me and I'll take care of it" is the sound of a process
going dark. It sounds technical and is almost entirely political — every
dark process is dark for a reason, and the reason usually has a name and
a desk.

<a id="build-five-kill-four"></a>

**9. Build five, kill four.**

When an option costs nearly nothing to create, deliberating before
building it is a bad trade. Bring several working versions to the meeting
instead of a deck arguing for one — the killing is the point, not the
count. This only works where killing work carries zero social cost, which
is a culture problem, not a tooling one: you can't ask for five built and
four killed in a company where being the person whose version got killed
follows you into your review.

<a id="digitize-the-edge"></a>

**10. Digitize the edge, where the atoms are.**

If you make, move, install, or repair physical things, the untouched
value sits at the analog frontier, precisely because reaching it is
annoying: photos of every job, sensor logs, the technician's voice note
before driving to the next call. The Ghost can't climb the ladder or
smell the burnt wiring — it only knows what somebody said into a phone
before driving off. Convert your physical reality into text at high
fidelity and the other rules become available to you. Don't, and you're
running on anecdote and calling it experience.

<a id="no-ai-voice"></a>

**11. Nothing you ship may sound like it came from an AI.**

The default register — the throat-clearing opener, "it's not just X, it's
Y," the bolded summary nobody asked for — reads as nobody being home, and
erodes trust faster than a typo. It's also evidence: generic output is
output nobody rewrote, and output nobody rewrote is output nobody
thought hard about — the style rule enforces the thinking rule. It's
positioning too: what you sound like is the only claim about you a reader
can check without doing any work. Everything ships rewritten in your own
voice, stripped of anything you wouldn't say out loud to someone you
respect.

## People

<a id="hire-for-drive"></a>

**12. Hire for drive, "Getting Shit Done," relationships, and taste.**

The bottleneck isn't making things anymore, it's judging them fast and
pushing them into the world — production is the trait models absorbed
first. Hire the person who figures out how to get things done without
being managed into it, who builds relationships a counterparty actually
trusts, and who has taste — one part of that picture, not the headline.
Test taste directly: hand the candidate twenty drafts. Somebody like
[NAME OF THE SHARPEST EDITOR MORGAN HAS WORKED WITH — CHECK], who rejects
nineteen for a reason they can name, does something the person who
produces three cannot do at any volume.

<a id="manager-of-agents"></a>

**13. Give the agents a manager — a human over the loop, not in it.**

"In the loop" quietly became jargon for a rubber stamp — a person
clicking approve on every step, since nobody scrutinizes step four
thousand the way they scrutinized step one. What's missing isn't more
approval clicks, it's someone whose job is the fleet of agent-run
processes itself: watching where they drift, retuning prompts and
guardrails, deciding when a step needs a human again. Call the role
Manager of Agents or don't, but staff it — agents left running on the
strength of the day they were configured degrade quietly, until something
downstream breaks.

<a id="human-only-zones"></a>

**14. Protect human-only zones on purpose, and put them on the calendar.**

If everyone consumes only summaries, nobody can detect the moment the
summaries start to drift — everything keeps reading as coherent. So
mandate raw contact as permanent ritual: founders reading unfiltered
complaints instead of the sentiment rollup, managers watching real work
for an afternoon and saying nothing, somebody reading the actual source
the way you'd have read it in [YEAR]. It will feel like deliberate
inefficiency. Keep it anyway — it's the only part of the system that can
tell you the rest has started lying to you.

<a id="structurally-human"></a>

**15. Reserve the permanent hire for what's structurally human.**

Follow every rule on this list to where it leads and they land in the
same place: the roles worth making permanent are built on something a
model can't do at all. Judgment when the rules run out. Taste that
catches the one paragraph in twenty that's quietly wrong. Relationships a
counterparty trusts because of who's on the other end of them.
Accountability that lands on one name, not a process nobody can point to.
The human spark that makes someone worth working for, not merely
alongside. And, increasingly, the discipline of running a fleet of
agent-driven processes — pushing one further than it would push itself,
and pulling it back before it overreaches. (Full list:
[HUMANS_AT_OUR_BEST.md](HUMANS_AT_OUR_BEST.md).)

That list is shorter than it was five years ago. It isn't going to zero.
Build the permanent roster around it.

---

**Open placeholders (see [TODO.md](TODO.md)):** [`hire-for-drive`](#hire-for-drive)
has an unfilled `[NAME OF THE SHARPEST EDITOR...]` bracket;
[`human-only-zones`](#human-only-zones) has an unfilled `[YEAR]` bracket.
Both are intentional — fill them in with real specifics when they come to
mind rather than inventing something generic to close the bracket.
