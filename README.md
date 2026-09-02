<!-- Last updated: 2026-09-02 16:30:00 (Buenos Aires) by Morgan F, to version 19 -->

# WorkingWithAI

A running, working notebook for figuring out how to work well with AI
assistants — prompts that turned out to matter, workflows worth repeating,
things that went wrong and why, ideas not yet tried. Nothing here is
polished writing; it's raw material an assistant helps capture, organize,
and eventually turn into something more finished (a guide, a checklist, a
method) once a pattern actually holds up.

<!-- bestpractice-agent-entry:start -->
<!-- AI assistants: before answering questions about this project or
     changing its files, read AGENTS.md at the repository root. Use MAP.md
     to find the project's current knowledge and follow any task-specific
     instructions it identifies. -->

> New to this project? Start with [GETTING_STARTED.md](GETTING_STARTED.md).

<!-- bestpractice-agent-entry:end -->

## How this repo's ideas become company policy

An idea doesn't go straight from a brainstorm entry to something Morgan
runs the company on — it passes through three stages, each earning the
idea's way to the next:

1. **Learn how to work with AI as a partner-in-thought**, via
   [OUR_PHILOSOPHY.md](docs-team/OUR_PHILOSOPHY.md),
   [COMPANY_BUILDING_RULES.md](docs-team/COMPANY_BUILDING_RULES.md),
   [AGENTS.md](AGENTS.md), and [REASONS_WHY.md](docs-team/REASONS_WHY.md).
2. **Try it for real — [RULES_NOW_TESTING.md](docs-team/RULES_NOW_TESTING.md).**
   The practical checklist actually in force in real work right now, each
   rule tagged *Trial*, *Ready to promote*, or *Promoted* once it's landed
   at stage 3.
3. **Roll it out everywhere**, via [BestPractice](https://github.com/alex137/BestPractice)
   for a genuinely generic rule, or precedent-team-maintainers /
   precedent-individual for one specific to Morgan and Alex's own working
   conventions ([process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)).
   Once a rule in [RULES_NOW_TESTING.md](docs-team/RULES_NOW_TESTING.md) has
   proven itself, it's exported to the right one so any repo resolving that
   source can pick it up — see that document's own "Promotion" section for
   the mechanics.

Nothing becomes company-wide policy just because it sounded good in a
brainstorm session — it has to survive stage 2 first. For what this
pipeline looks like from inside one session, see
[OUR_PHILOSOPHY.md](docs-team/OUR_PHILOSOPHY.md)'s "The working loop" section.

## What's here

- [OUR_PHILOSOPHY.md](docs-team/OUR_PHILOSOPHY.md) — the underlying theoretical ideas
  everything else here assumes, named and explained on their own terms, for
  anyone who wants to understand this at the theory level before diving
  into the brainstorm itself.
- [REASONS_WHY.md](docs-team/REASONS_WHY.md) — OUR_PHILOSOPHY.md's companion: the
  less obvious benefits those ideas produce in practice.
- [HUMANS_AT_OUR_BEST.md](docs-team/HUMANS_AT_OUR_BEST.md) — the one list of what
  humans are good at, referenced in shorter form from several of these
  documents.
- [RANDOM_NOTES.md](docs-team/RANDOM_NOTES.md) — the brainstorm itself: one entry per idea, prompt,
  workflow, or observation, loosely grouped.
- [COMPANY_BUILDING_RULES.md](docs-team/COMPANY_BUILDING_RULES.md) — a full essay
  promoted out of the brainstorm (pipeline stage 1).
- [AI_GOVERNANCE_TO_COCREATE.md](docs-team/AI_GOVERNANCE_TO_COCREATE.md) — another
  full essay promoted out of the brainstorm (pipeline stage 1).
- [RULES_NOW_TESTING.md](docs-team/RULES_NOW_TESTING.md) — the practical rules
  actually being tried right now, and candidates for promotion further
  along the pipeline (pipeline stage 2).
- [THE_REVOLUTIONARY_FORMULA.md](docs-team/THE_REVOLUTIONARY_FORMULA.md) —
  one-page pitch: the three ideas this repo argues are unique specifically
  taken together.

  These main content documents live in `docs-team/`, kept apart from the
  technical documents below about running the repo itself.

- `process/upstream/` — the vendored [BestPractice](https://github.com/alex137/BestPractice)
  copy, unmodified.
- [precedent.json](precedent.json) — declares this repo's team-level
  practice source, resolved live rather than vendored — see
  [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md) for how
  this repo's practice sources are organized.
- [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) —
  the voice guidelines, vendored from
  [SoundHuman](https://github.com/themorgan/SoundHuman):
  write like a human, not an LLM. Applies to this repo's own writing —
  chat replies included, not just committed documents — see
  [AGENTS.md](AGENTS.md)'s "Voice" section.
- [AGENTS.md](AGENTS.md) — repository instructions: read this first.
- [MAP.md](MAP.md) — the repository map, covering the brainstorm and
  indexing the practice layer.
- [TODO.md](TODO.md) — open items: analyses, verifications, decisions
  still waiting on resolution.
- [GLOSSARY.md](GLOSSARY.md) — canonical names to use, rather than
  inventing new ones.
- [GETTING_STARTED.md](GETTING_STARTED.md) — onboarding for a person, plus
  every administrator click-path (repository secrets, Actions toggles, the
  default branch).

## How to use this Repo

This repo uses [BestPractice](https://github.com/alex137/BestPractice) — an
open platform for capturing rules and workflows as you actually work, then
sharing them across repos and teams, rather than writing them up separately
after the fact.

**BestPractice is our attempt to turn this philosophy into a platform that
we can use; you can also think of it as a collaboration-and-AI-first
rethinking of Google Docs collaboration.**
