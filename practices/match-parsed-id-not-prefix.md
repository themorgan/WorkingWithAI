---
slug:        match-parsed-id-not-prefix
title:       Match the parsed identifier, not a filename-prefix glob
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "counting or matching entries by name against other entries that may share a prefix"
gates:       []
index_clause: "When counting how many files or entries share a name (recurrence, a duplicat..."
checked_by:  null
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-09-02
approved_by: "Morgan F, 2026-09-02"
source_practice_number: null
---
## Rule
When counting how many files or entries share a name (recurrence, a duplicate check, a registry lookup), match on each entry's own parsed identifier field, never a filename-prefix or substring glob. A longer, differently-named entry that merely shares the shorter one's prefix (`foo-bar` alongside `foo`) will silently match too, and the miscount is invisible until something adversarial or coincidental actually produces the collision.

## Why
Raised via Precedent's creation pipeline (Stage 1 signal: review-found-defect), promoted at individual level, approved by Morgan F on 2026-09-02.

## Story
Deep-checking Precedent's phase-5 creation pipeline before phase 6 (per spec/PHASE5_BRIEF.md's own request for adversarial pressure), found that tools/precedent_promote.py's check_recurrence_or_cost() counted same-slug candidate files with cand_dir.glob(f'{slug}-*.md'). That glob also matches a DIFFERENTLY-slugged candidate that merely shares a name prefix: raising a one-time candidate named 'foo' alongside an unrelated candidate named 'foo-bar' made 'foo' silently read as having recurred twice, letting it pass Stage 3's recurrence-or-cost criterion without a real second occurrence ever happening. Fixed by parsing each file's own frontmatter slug field and comparing that, never the filename.

## Install
No mechanical check yet -- reached via occasion only, per checkable-gets-checked's own standing rule, a real check should still be attempted before this stays null indefinitely.
