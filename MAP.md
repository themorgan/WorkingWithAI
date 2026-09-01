<!-- Last updated: 2026-09-01 15:56:02 (Buenos Aires) by Morgan F, to version 14 -->

# Repository map — where to find things

**Purpose:** orientation for any thread picking up work here. This repo's
one deliverable is **the brainstorm** — [RANDOM_NOTES.md](RANDOM_NOTES.md), a running list
of prompts, workflows, and observations about working with AI — plus the
three-stage pipeline (see [README.md](README.md)) that turns the ideas
which prove out into company-wide policy. Everything else here is the
practice layer that keeps the repo itself well-run: BestPractice (vendored,
unmodified) plus Morgan's personal pack on top.

Companions: [AGENTS.md](AGENTS.md) (workflow + conventions), [TODO.md](TODO.md)
(open items across sessions).

## Top-level layout

| Path | What it is |
|---|---|
| [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) | Orientation for a newcomer: the handful of underlying theoretical ideas everything else here assumes, named and explained on their own terms. |
| [REASONS_WHY.md](REASONS_WHY.md) | Orientation's companion: the less obvious benefits those ideas actually produce in practice. |
| [THE_REVOLUTIONARY_FORMULA.md](THE_REVOLUTIONARY_FORMULA.md) | One-page pitch: the three ideas — from [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) and [REASONS_WHY.md](REASONS_WHY.md) — that this repo argues are unique specifically taken together. |
| [HUMANS_AT_OUR_BEST.md](HUMANS_AT_OUR_BEST.md) | The one list of what humans are good at, gathered from the shorter versions scattered across [OUR_PHILOSOPHY.md](OUR_PHILOSOPHY.md) and [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md). |
| [RANDOM_NOTES.md](RANDOM_NOTES.md) | **The deliverable.** The brainstorm itself — pipeline stage 1. |
| [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) | Standalone essay promoted out of the brainstorm: rules for building a company around AI. |
| [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md) | Standalone doc promoted out of the brainstorm: how AI systems themselves should be configured, built, and run to make the healthy pattern the default. |
| [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md) | Pipeline stage 2 — the practical rules actually being tried in real work right now, tagged Trial / Ready to promote / Promoted. |
| [GLOSSARY.md](GLOSSARY.md) | Canonical names — the one list. Use its names; don't invent new ones. |
| [GETTING_STARTED.md](GETTING_STARTED.md) | Human-facing onboarding, including administrator click-paths (secrets, toggles, default branch). |
| [README.md](README.md) | What this repo is, in a paragraph, plus the pipeline explanation and the agent-entry block. |
| `process/upstream/` | Vendored copy of the public BestPractice repo — see [process/manifest.json](process/manifest.json). |
| `process/personal/` | Morgan's personal pack, vendored from RepoPersonalPreferences — see [process/personal/README.md](process/personal/README.md) and [process/manifest_personal.json](process/manifest_personal.json). Pipeline stage 3's destination lives in that repo, not here. |
| [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) | The voice guidelines — write like a human, not an LLM — vendored from [SoundHuman](https://github.com/themorgan/SoundHuman); see [AGENTS.md](AGENTS.md)'s "Voice" section and [process/manifest_voice.json](process/manifest_voice.json). Governs chat replies, not just committed documents. |
| [.github/workflows/](.github/workflows/) | The five installed checks: Markdown lint, the light check, the BestPractice sync, the pack sync, and the voice guidelines sync. |
| [TODO.md](TODO.md) | Cross-session open items. |
| `doc-recipes/` | Standing rules for individual documents, one `.recipe.md` file per document — see [`doc-recipe`](process/personal/README.md#doc-recipe). |

## The brainstorm and its pipeline

| Part | Backed by |
|---|---|
| Frameworks (full essays) — stage 1 | [COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md), [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md), linked from [RANDOM_NOTES.md](RANDOM_NOTES.md) |
| Why BestPractice works, observations, meta-notes on this repo's own use | [RANDOM_NOTES.md](RANDOM_NOTES.md) |
| Prompts and phrasing | [RANDOM_NOTES.md](RANDOM_NOTES.md) |
| Workflows | [RANDOM_NOTES.md](RANDOM_NOTES.md) |
| Things that went wrong, and why | [RANDOM_NOTES.md](RANDOM_NOTES.md) |
| Rules actually in force, and promotion candidates — stage 2 | [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md) |
| Rules rolled out to every project — stage 3 | [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences) (a separate repo) |
