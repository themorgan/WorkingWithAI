---
slug:        content-directory
title:       A content/ directory keeps working files apart from repo machinery
tier:        on-demand
severity:    advisory
applies_to:  ["**"]
occasion:    "laying out a repo's root directory, or a root that's grown crowded with agent/tooling files"
gates:       []
index_clause: "put working files in content/ so they don't mix with agent/tooling files"
checked_by:  null
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-09-04
approved_by: "Morgan F, 2026-09-04"
source_practice_number: null
---
## Rule
When a repo's root directory is carrying so much machinery for managing agents -- `AGENTS.md`/`CLAUDE.md`, tool scripts, hooks, config -- that the files actually being worked on and referenced get lost among them, put those working files in a `content/` directory rather than the root. This is a default I fall back to when the repo doesn't already define its own layout convention, not a mandate: an existing, established structure (a `docs/`, `src/`, or whatever the repo already uses) wins over this every time.

## Why
The root of a repo like this one already does a specific job -- it's where an agent looks first for `AGENTS.md`, tool scripts, and config -- and piling the actual content being worked on into that same directory makes both harder to scan: the machinery gets lost among the content, and the content gets lost among the machinery. Separating them keeps each directory legible for what it's for.

## Story


## Install
No mechanical check -- this is a layout preference, not a property a script can verify against arbitrary repo content. Reached by occasion only: when starting a repo's directory layout, or restructuring a root that's become crowded, check whether the repo already has its own convention before defaulting to `content/`.
