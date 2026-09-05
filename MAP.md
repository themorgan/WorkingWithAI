<!-- Last updated: 2026-09-05 09:13:36 (Buenos Aires) by Morgan F, to version 21 -->

# Repository map — where to find things

**Purpose:** orientation for any thread picking up work here. This repo's
one deliverable is **the brainstorm** — [RANDOM_NOTES.md](content/RANDOM_NOTES.md), a running list
of prompts, workflows, and observations about working with AI — plus the
three-stage pipeline (see [README.md](README.md)) that turns the ideas
which prove out into company-wide policy. Everything else here is the
practice layer that keeps the repo itself well-run: BestPractice (vendored,
currently the precedent-beta-v01 branch — see
[process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)) plus
Morgan and Alex's team practices, resolved live from a sibling clone.

Companions: [AGENTS.md](AGENTS.md) (workflow + conventions), [TODO.md](TODO.md)
(open items across sessions).

## Top-level layout

| Path | What it is |
|---|---|
| `content/` | This repo's main content documents — the brainstorm, its promoted essays, and the theory behind them — kept apart from the technical documents below about running the repo itself. |
| [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) | Orientation for a newcomer: the handful of underlying theoretical ideas everything else here assumes, named and explained on their own terms. |
| [REASONS_WHY.md](content/REASONS_WHY.md) | Orientation's companion: the less obvious benefits those ideas actually produce in practice. |
| [THE_REVOLUTIONARY_FORMULA.md](content/THE_REVOLUTIONARY_FORMULA.md) | One-page pitch: the three ideas — one each from [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md), [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md), and [REASONS_WHY.md](content/REASONS_WHY.md) — that this repo argues are unique specifically taken together. |
| [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md) | The one list of what humans are good at, gathered from the shorter versions scattered across [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) and [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md). |
| [RANDOM_NOTES.md](content/RANDOM_NOTES.md) | **The deliverable.** The brainstorm itself — pipeline stage 1. |
| [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) | Standalone essay promoted out of the brainstorm: rules for building a company around AI. |
| [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md) | Standalone doc promoted out of the brainstorm: how AI systems themselves should be configured, built, and run to make the healthy pattern the default. |
| [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) | Pipeline stage 2 — the practical rules actually being tried in real work right now, tagged Trial / Ready to promote / Promoted. |
| [GLOSSARY.md](GLOSSARY.md) | Canonical names — the one list. Use its names; don't invent new ones. Stays at root, not `content/` — see [content/doc-recipes/GLOSSARY.recipe.md](content/doc-recipes/GLOSSARY.recipe.md). |
| [GETTING_STARTED.md](GETTING_STARTED.md) | Human-facing onboarding, including administrator click-paths (secrets, toggles, default branch). |
| [README.md](README.md) | What this repo is, in a paragraph, plus the pipeline explanation and the agent-entry block. |
| `process/upstream/` | Vendored copy of the public BestPractice repo, currently the `precedent-beta-v01` branch — see [process/manifest.json](process/manifest.json) and [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md). |
| [precedent.json](precedent.json) | Declares this repo's team practice source, [precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers) — resolved live from a sibling clone, not vendored. Pipeline stage 3's other destination, [precedent-individual](https://github.com/themorgan/precedent-individual) for Morgan-specific facts, is never declared here. |
| [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) | The voice guidelines — write like a human, not an LLM — vendored from [SoundHuman](https://github.com/themorgan/SoundHuman); see [AGENTS.md](AGENTS.md)'s "Voice" section and [process/manifest_voice.json](process/manifest_voice.json). Governs chat replies, not just committed documents. |
| [.github/workflows/](.github/workflows/) | The installed checks: Markdown lint, the light check, the BestPractice sync (paused during the beta), and the voice guidelines sync. |
| [TODO.md](TODO.md) | Cross-session open items. |
| `doc-recipes/`, `content/doc-recipes/` | Standing rules for individual documents, one `.recipe.md` file per document, living beside the document it governs — see [`doc-recipe`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/doc-recipe.md). |
| [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md) | The 2026-09-02 record of this repo's move from BestPractice-only to Precedent's three-source model: what changed, why, the `precedent_resolve.py` validation run, and what still doesn't work. |

## The brainstorm and its pipeline

| Part | Backed by |
|---|---|
| Frameworks (full essays) — stage 1 | [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md), [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md), linked from [RANDOM_NOTES.md](content/RANDOM_NOTES.md) |
| Why BestPractice works, observations, meta-notes on this repo's own use | [RANDOM_NOTES.md](content/RANDOM_NOTES.md) |
| Prompts and phrasing | [RANDOM_NOTES.md](content/RANDOM_NOTES.md) |
| Workflows | [RANDOM_NOTES.md](content/RANDOM_NOTES.md) |
| Things that went wrong, and why | [RANDOM_NOTES.md](content/RANDOM_NOTES.md) |
| Rules actually in force, and promotion candidates — stage 2 | [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) |
| Rules rolled out to every project — stage 3 | [precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers) and [precedent-individual](https://github.com/themorgan/precedent-individual) (separate repos) |
