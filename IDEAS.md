<!-- Last updated: 2026-08-27 21:00:00 (Buenos Aires) by Morgan F, to version 5 -->

# Ideas — how to work with AI

One entry per idea, prompt, workflow, or observation. Loosely grouped;
reorganize once a group gets big enough to need its own document (link it
from [MAP.md](MAP.md) when that happens).

**How to use this file (proposed — see the meta-note at the bottom):** each
entry below is raw material dropped in from a session, lightly organized.
Treat it as a standing agenda, not a finished write-up — the point of doing
this in a repo instead of a doc is that any thread can pick up one entry,
argue it out with Claude (per [FIFTEEN_RULES.md](FIFTEEN_RULES.md) rule 4),
and push the sharpened version back in.

## Frameworks

- **Fifteen rules for building a company around AI** — a full essay, promoted
  to its own document because it's one sustained argument rather than a
  loose list: [FIFTEEN_RULES.md](FIFTEEN_RULES.md). Covers context as the
  scarce capital asset, transcription discipline (the "Ghost"), owning
  every word you pass on, co-creating instead of delegating, building
  workflows only once work actually repeats, hiring for verification over
  production, giving agents a human manager over the loop, killing "dark
  processes," and voice/style as evidence that someone actually thought.
- **Building AI systems for co-creation** — one level down from the above:
  how the AI systems themselves should be configured, built, and run so
  the healthy pattern is the default rather than something a disciplined
  user has to manufacture by hand:
  [COCREATION_DESIGN.md](COCREATION_DESIGN.md). Covers durable memory as
  the default substrate, push-back as a config switch keyed to task shape,
  arguing in the open instead of posting finished-looking suggestions,
  visibly non-uniform confidence, situational (not fixed) cost-awareness,
  a structural check for AI-sounding prose, and self-surfacing of dark
  processes.
- **Where an idea from either essay actually goes next** —
  [OPERATING_RULES.md](OPERATING_RULES.md), added 2026-08-27. Neither essay
  above is itself a set of rules anyone follows day to day; this is the
  document that turns an argument into a checklist actually in force, and
  tracks which of those checklist items have proven themselves enough to
  become real company-wide policy in [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences).
  See [README.md](README.md)'s pipeline explanation and this file's own
  meta section below for why that middle step exists at all.

## Why BestPractice specifically works (semi-organized brainstorm)

*The premise: BestPractice — the practice layer this repo vendors under
`process/upstream/` — is being used here as a live case study of rule 4 and
rule 2 from [FIFTEEN_RULES.md](FIFTEEN_RULES.md): forced co-creation, forced
transcription. The observations below are about* why *it works, not just
that it does.*

1. It's a structure for working with AI as a partner-in-thought, rather
   than the two usual extremes for non-dev work: blindly handing it
   everything, or using it lightly for research/writing and nothing more.
2. It forces "think in process" / "think in the how" — a way of working
   that's enormously powerful and very hard for most non-technical
   ("normie") employees to adopt voluntarily. This structure gives them no
   other option. (This is the "Nix approach" — see the open question
   below.)
3. Key information, learnings, and intentions are normally trapped inside
   private AI chat conversations. This surfaces them granularly and
   effectively, while still keeping the conversations themselves private.
   - **3a.** Corollary of #2 + #3 together: it doesn't just put learnings
     into the shared GitHub repo — it purposefully extracts *the rules*
     (this repo's own [AGENTS.md](AGENTS.md)/`process/` layer is itself an
     instance of that), which amounts to automatic documentation generated as a
     side effect of doing the work.
   - **3b.** Consequence of 3a: it also extracts the TODOs, which
     otherwise get lost constantly unless someone is unusually organized.
     (Compare [TODO.md](TODO.md)'s push-time gate in this repo — that's
     this exact mechanism, installed.)
4. Multiple people can work the same issue simultaneously — version
   control plus AI-assisted merging beats one-person-at-a-time editing.

### Open question: forcing deeper engagement, not just permitting it

For points 2 and 3: "normie" employees might default to the shallow use —
simple prompting — and never discover the deeper mode, unless something
pushes them there. Candidate mechanisms, none decided yet (this is a
**decision**-class item, see [TODO.md](TODO.md)):

- Have Claude push back harder than its default on direct instructions —
  question them instead of just complying.
- Constant, visible reminders of the deeper mode, rather than a one-time
  onboarding note.
- Make the automatic rule-extraction (3a) more "in your face" — if people
  *see* the rules being generated live, the "wow" reaction itself teaches
  them the system has more to offer than a simple prompt box.
- Have Claude proactively surface a previously-extracted rule when it's
  relevant in a new context, rather than leaving it inert in a file
  nobody re-reads.

Push-back mode (the first candidate above) is decided and promoted — see
[OPERATING_RULES.md](OPERATING_RULES.md) item 1. The rest — visible
reminders, in-your-face rule-extraction, proactive resurfacing — remain
open; proactive resurfacing specifically also shows up as one of
[COCREATION_DESIGN.md](COCREATION_DESIGN.md)'s "Memory & context" ideas,
tracked as a not-yet-ready item in
[OPERATING_RULES.md](OPERATING_RULES.md) pending real infrastructure.

## Observations from other conversations

**Visibility as an incentive mechanism.** When contributions live in
version control, you can ask the AI to help you evaluate whether a given
person's contribution is good — and because the contributor knows that's
coming, they can (and will) ask the AI to help them tune their work toward
what you'll value. This only works cleanly if you've set explicit goals and
rules of the road in advance for them to tune toward. Performance on this
front becomes visible in the history, for that person and for everyone else
on the team simultaneously — a much stronger and more continuous signal
than a periodic review.

**Rethinking an ad campaign AI-first — a conversation with Claude.** Prompted
by thinking through what it would mean to run an ad campaign in a truly
AI-first way. The framing generalizes well past ads:

> That changes my advice, and I'll retract part of the caution — but keep
> one piece of it.
>
> The part I'll keep: the campaign being real is exactly what makes this a
> good learning vehicle. Real money, real API failures, real dirty data,
> real consequences for being wrong. A todo app teaches you nothing about
> verification because nothing breaks. So don't let the campaign degrade —
> not because the campaign is the only goal, but because a live campaign is
> the thing generating the feedback you're trying to learn from.
>
> **What "partner, not lookup tool" actually cashes out to.** Mostly three
> things, and none of them are prompting tricks.
>
> *Context is the whole game.* The reason chat feels like a lookup tool is
> that I arrive at every conversation with nothing. I can't disagree with
> you usefully because I don't know enough to have a view. Working in a
> repo changes this: the repo *is* the shared context. So the
> highest-leverage thing you can do is write things down in files I'll read
> — a `CONTEXT.md` describing the business and the campaign, a
> `DECISIONS.md` with one line per architectural choice and why. Investing
> in context isn't housekeeping; it's what buys you a collaborator who can
> push back instead of one who can only comply. Related: explicitly invite
> disagreement. "Here's my plan, build it" gets you compliance. "Here's my
> plan, what's wrong with it" gets you something better.
>
> *Specification, not instruction.* The mode shift is from "write a
> function that does X" to "here are the constraints, here's how we'll
> know it's correct." Writing good specs is a real skill and it transfers
> — you'll write better issues and better docs as a side effect.
>
> *Verification is the bottleneck.* Generating code is nearly free now;
> knowing whether it's right is the constraint, and it's *your* constraint.
> Build the checking apparatus early: recorded fixtures so you can test
> without hitting live APIs, a dry-run mode, an assertion that running
> apply twice produces no second diff. Then hold one rule absolutely —
> never merge code you can't explain.
>
> **Habits worth adopting deliberately:** keep a failure log (when
> generated output is wrong, write down whether it was missing context, a
> bad spec, or genuine model error — after twenty entries you'll have a
> calibrated sense of where the leverage actually is); build one module
> twice, once mostly by hand and once with heavy AI involvement, and
> compare; keep commits small and reviewable, because long AI-generated
> diffs are where review discipline dies.

**Morgan's synthesis on the above:** this is implicitly what BestPractice is
already suggesting, just framed more sharply. Running an ad campaign — or
most operational work — normally means constantly tweaking options,
constantly pushing buttons, and never recording why any button got pushed.
The BestPractice approach forces recording every small decision and its
reason, and it does this *automatically*, purely as a side effect of the
system's shape: the only interface is prompting Claude, and Claude tracks
everything via the repo. Same mechanism as 3a/3b above. The other point
worth keeping from that conversation: having the AI push back harder,
explicitly, rather than defaulting to compliance — connects directly to the
open question above.

## Meta: using this repo as "Google Docs on steroids" for brainstorming

Proposal, not yet decided (flag any of this you don't want — this is your
call as much as mine):

- **One entry per session, appended, not rewritten.** Keep the append-only
  discipline this repo already uses for [TODO.md](TODO.md); resist the urge
  to silently smooth over an earlier, rougher version of an idea — better to
  add a dated follow-up entry that supersedes it, so the disagreement with
  your past self stays visible instead of vanishing.
- **Turn open questions into TODO.md decision items as soon as they're
  identifiable**, the way the "forcing deeper engagement" question above
  just did — that's the mechanism in 3a/3b, applied to this repo's own
  practice of self-reflection, not just to code.
- **Use PR review comments as the argument, not just the record.** Rule 4
  (co-create, don't delegate) suggests the highest-value use of this repo
  isn't "paste a finished thought" but "open a PR with a half-formed one and
  have the back-and-forth happen as review comments" — the transcript of
  the disagreement becomes part of the corpus (rule 1), not just the
  conclusion.
- **When a topic outgrows a bullet, promote it**, exactly as
  [FIFTEEN_RULES.md](FIFTEEN_RULES.md) just was. A dedicated file gets its
  own version history, so you can watch one idea sharpen over many sessions
  instead of only ever seeing its latest state.
- **Periodically ask Claude to look for contradictions across entries.**
  Loosely-grouped brainstorm entries accumulated over many sessions will
  eventually disagree with each other (e.g., rule 9's "kill four of five
  built" against rule 5's "don't systematize a one-off") — that tension is
  often more interesting than either entry alone, and it's the kind of
  thing a single session won't notice but a deliberate re-read will.

**2026-08-27 entry — the pipeline needed a name and a middle stage.** A
session asked to recommend RepoPersonalPreferences changes based on this
repo's ideas went straight from brainstorm to "add this to the personal
pack." Morgan's correction: this repo's actual job is to *try* an idea in
real work first — going straight from an essay here to a rule that rolls
out to every project skips the step that's supposed to catch a good-sounding
idea that doesn't actually hold up. The fix wasn't a new rule, it was
naming the stage that was missing: [OPERATING_RULES.md](OPERATING_RULES.md),
sitting between the essays here and RepoPersonalPreferences, holding
whatever's currently on trial. See [README.md](README.md)'s new pipeline
section and [TODO.md](TODO.md) for the decision record.

## Prompts and phrasing

- [ ] *(seed this with real prompts as they come up)*

## Workflows

- [ ] *(seed this with real workflows as they come up)*

## Things that went wrong, and why

- [ ] *(seed this with real incidents as they come up)*
