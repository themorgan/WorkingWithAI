<!-- Last updated: 2026-09-01 16:35:00 (Buenos Aires) by Morgan F, to version 15 -->

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
runs the company on — it passes through three stages, each with its own
document, and each stage has to actually earn the idea's way to the next
one:

1. **Learn how to work with AI as a partner-in-thought.** Get oriented in
   the method before the rules: read [OUR_PHILOSOPHY.md](docs/OUR_PHILOSOPHY.md)
   for the underlying ideas, [COMPANY_BUILDING_RULES.md](docs/COMPANY_BUILDING_RULES.md)
   for the principles to build a company around, [AGENTS.md](AGENTS.md) for
   the rules AI agents actually follow here, and
   [REASONS_WHY.md](docs/REASONS_WHY.md) for the less obvious benefits those
   ideas produce.
2. **Try it for real — [RULES_NOW_TESTING.md](docs/RULES_NOW_TESTING.md).** The
   practical checklist actually in force in real work right now, each rule
   tagged *Trial* until it's proven, *Ready to promote* once it is, or
   *Promoted* once it's landed at stage 3 — these are the rules we've
   baked into our own repos so far, and you might want to bake them into
   yours too.
3. **Roll it out everywhere — [BestPractice](https://github.com/alex137/BestPractice)
   and [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences).**
   Once a rule in [RULES_NOW_TESTING.md](docs/RULES_NOW_TESTING.md) has proven
   itself, a genuinely generic rule gets exported into BestPractice first,
   where any repo can pick it up, and a rule that's specifically Morgan's
   own gets ported into his personal pack in RepoPersonalPreferences, for
   automatic installation into every project he starts — see
   [RULES_NOW_TESTING.md](docs/RULES_NOW_TESTING.md)'s own "Promotion" section
   for the mechanics.

The point of keeping these separate: nothing becomes company-wide policy
just because it sounded good in a brainstorm session, or even because an
essay argued for it well. It has to survive stage 2, in this repo, first.
For what running this pipeline looks like from inside one session —
spark, argue, GitHub, rule — see
[OUR_PHILOSOPHY.md](docs/OUR_PHILOSOPHY.md)'s "The working loop" section.

## What's here

- [OUR_PHILOSOPHY.md](docs/OUR_PHILOSOPHY.md) — the underlying theoretical ideas
  everything else here assumes, named and explained on their own terms, for
  anyone who wants to understand this at the theory level before diving
  into the brainstorm itself.
- [REASONS_WHY.md](docs/REASONS_WHY.md) — OUR_PHILOSOPHY.md's companion: the
  less obvious benefits those ideas produce in practice.
- [HUMANS_AT_OUR_BEST.md](docs/HUMANS_AT_OUR_BEST.md) — the one list of what
  humans are good at, referenced in shorter form from several of these
  documents.
- [RANDOM_NOTES.md](docs/RANDOM_NOTES.md) — the brainstorm itself: one entry per idea, prompt,
  workflow, or observation, loosely grouped.
- [COMPANY_BUILDING_RULES.md](docs/COMPANY_BUILDING_RULES.md) — a full essay
  promoted out of the brainstorm (pipeline stage 1).
- [AI_GOVERNANCE_TO_COCREATE.md](docs/AI_GOVERNANCE_TO_COCREATE.md) — another
  full essay promoted out of the brainstorm (pipeline stage 1).
- [RULES_NOW_TESTING.md](docs/RULES_NOW_TESTING.md) — the practical rules
  actually being tried right now, and candidates for promotion to
  RepoPersonalPreferences (pipeline stage 2).
- [THE_REVOLUTIONARY_FORMULA.md](docs/THE_REVOLUTIONARY_FORMULA.md) —
  one-page pitch: the three ideas this repo argues are unique specifically
  taken together.

  These main content documents live in `docs/`, kept apart from the
  technical documents below about running the repo itself.

- `process/upstream/` — the vendored [BestPractice](https://github.com/alex137/BestPractice)
  copy, unmodified.
- `process/personal/` — Morgan's personal pack, vendored from
  [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences)
  (pipeline stage 3's destination).
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
