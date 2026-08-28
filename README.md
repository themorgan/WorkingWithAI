<!-- Last updated: 2026-08-28 14:17:07 (Buenos Aires) by Morgan F, to version 9 -->

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

1. **Discover — [IDEAS.md](IDEAS.md).** Raw material: prompts, workflows,
   observations, dropped in as they come up, loosely grouped. When a
   cluster of entries turns into one sustained argument, it gets promoted
   to its own essay — [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md)
   (why to run a company this way) and
   [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md) (how
   the AI systems themselves should be built so that way of working is the
   default) both started as brainstorm entries here.
2. **Try it for real — [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md).** The
   practical checklist actually in force in real work right now, each rule
   tagged *Trial* until it's proven, *Ready to promote* once it is, or
   *Promoted* once it's landed at stage 3. This is where an essay's idea
   gets tested against actual sessions before it becomes a standing rule
   anywhere else.
3. **Roll out everywhere — [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences).**
   Once a rule in [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md) has proven
   itself, it gets ported into Morgan's personal pack there, for automatic
   installation into every project he starts — see
   [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md)'s own "Promotion" section
   for the mechanics.

The point of keeping these separate: nothing becomes company-wide policy
just because it sounded good in a brainstorm session, or even because an
essay argued for it well. It has to survive stage 2, in this repo, first.
For what running this pipeline looks like from inside one session —
spark, argue, GitHub, rule — see
[OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md)'s "The working loop" section.

## What's here

- [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) — the underlying theoretical ideas
  everything else here assumes, named and explained on their own terms, for
  anyone who wants to understand this at the theory level before diving
  into the brainstorm itself. [REASONS_WHY.md](REASONS_WHY.md) is its
  companion: the less obvious benefits those ideas produce in practice.
- [IDEAS.md](IDEAS.md) — the brainstorm itself: one entry per idea, prompt,
  workflow, or observation, loosely grouped.
- [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md), [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md) —
  full essays promoted out of the brainstorm (pipeline stage 1).
- [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md) — the practical rules
  actually being tried right now, and candidates for promotion to
  RepoPersonalPreferences (pipeline stage 2).
- `process/upstream/` — the vendored [BestPractice](https://github.com/alex137/BestPractice)
  copy, unmodified.
- `process/personal/` — Morgan's personal pack, vendored from
  [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences)
  (pipeline stage 3's destination).
- [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) —
  the voice guidelines, vendored from
  [SoundHuman](https://github.com/themorgan/VoiceGuidelinesToSoundHuman):
  write like a human, not an LLM. Applies to this repo's own writing —
  chat replies included, not just committed documents — see
  [AGENTS.md](AGENTS.md)'s "Voice" section.
- [AGENTS.md](AGENTS.md), [MAP.md](MAP.md), [TODO.md](TODO.md),
  [GLOSSARY.md](GLOSSARY.md) — this repo's own instantiated BestPractice
  documents.
- [GETTING_STARTED.md](GETTING_STARTED.md) — onboarding for a person, plus
  every administrator click-path (repository secrets, Actions toggles, the
  default branch).
