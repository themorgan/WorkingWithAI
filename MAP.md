<!-- Last updated: 2026-08-27 11:40:00 (Buenos Aires) by Morgan F, to version 4 -->

# Repository map — where to find things

**Purpose:** orientation for any thread picking up work here. This repo's
one deliverable is **the brainstorm** — [IDEAS.md](IDEAS.md), a running list
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
| [IDEAS.md](IDEAS.md) | **The deliverable.** The brainstorm itself — pipeline stage 1. |
| [FIFTEEN_RULES.md](FIFTEEN_RULES.md) | Standalone essay promoted out of the brainstorm: fifteen rules for building a company around AI. |
| [COCREATION_DESIGN.md](COCREATION_DESIGN.md) | Standalone doc promoted out of the brainstorm: how AI systems themselves should be configured, built, and run to make the healthy pattern the default. |
| [OPERATING_RULES.md](OPERATING_RULES.md) | Pipeline stage 2 — the practical rules actually in force in real work right now, tagged Trial / Ready to promote / Promoted. |
| [GLOSSARY.md](GLOSSARY.md) | Canonical names — the one list. Use its names; don't invent new ones. |
| [GETTING_STARTED.md](GETTING_STARTED.md) | Human-facing onboarding, including administrator click-paths (secrets, toggles, default branch). |
| [README.md](README.md) | What this repo is, in a paragraph, plus the pipeline explanation and the agent-entry block. |
| `process/upstream/` | Vendored copy of the public BestPractice repo — see [process/manifest.json](process/manifest.json). |
| `process/personal/` | Morgan's personal pack, vendored from RepoPersonalPreferences — see [process/personal/README.md](process/personal/README.md) and [process/manifest_personal.json](process/manifest_personal.json). Pipeline stage 3's destination lives in that repo, not here. |
| [.github/workflows/](.github/workflows/) | The four installed checks: Markdown lint, the light check, the BestPractice sync, and the pack sync. |
| [TODO.md](TODO.md) | Cross-session open items. |

## The brainstorm and its pipeline

| Part | Backed by |
|---|---|
| Frameworks (full essays) — stage 1 | [FIFTEEN_RULES.md](FIFTEEN_RULES.md), [COCREATION_DESIGN.md](COCREATION_DESIGN.md), linked from [IDEAS.md](IDEAS.md) |
| Why BestPractice works, observations, meta-notes on this repo's own use | [IDEAS.md](IDEAS.md) |
| Prompts and phrasing | [IDEAS.md](IDEAS.md) |
| Workflows | [IDEAS.md](IDEAS.md) |
| Things that went wrong, and why | [IDEAS.md](IDEAS.md) |
| Rules actually in force, and promotion candidates — stage 2 | [OPERATING_RULES.md](OPERATING_RULES.md) |
| Rules rolled out to every project — stage 3 | [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences) (a separate repo) |
