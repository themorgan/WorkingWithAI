---
slug:        assorted-notes
title:       content/ASSORTED_NOTES.md holds notes never referenced elsewhere
tier:        on-demand
severity:    advisory
applies_to:  ["**"]
occasion:    "creating a repo's content/ directory, or migrating a legacy BRAINSTORM.md/NOTES.md/IDEAS.md into the new system"
gates:       []
index_clause: "a default content/ASSORTED_NOTES.md holds notes never referenced elsewhere"
checked_by:  tools/checks/check_assorted_notes.py
defines:     ["ASSORTED_NOTES.md"]
status:      active
supersedes:  []
overrides:   null
added:       2026-09-04
approved_by: "Morgan F, 2026-09-04"
source_practice_number: null
---
## Rule
When a repo uses a `content/` directory ([content-directory](content-directory.md)), it defaults to a single file there, `content/ASSORTED_NOTES.md`, for random notes, observations, comments, and things to use later -- content not yet organized or ready to be pointed to. When upgrading a legacy repo that already has an equivalent file under a different name (`BRAINSTORM.md`, `NOTES.md`, `IDEAS.md`, or similar), rename it to `content/ASSORTED_NOTES.md`, keeping its content, for consistency across repos. Nothing anywhere else in the repo may reference or link to `content/ASSORTED_NOTES.md` or cite anything inside it -- the file exists precisely for things not yet ready to be referenced; the moment something in it needs to be pointed to from elsewhere, it has graduated out of that file into wherever referenceable content actually belongs.

## Why
One consistently named catch-all for not-yet-formed thoughts, kept apart from anything actually referenced, means a note can be dropped there freely without it quietly turning into a citation something else comes to depend on. A consistent filename across repos also means a session upgrading any of them knows exactly what to look for and what to rename.

## Story


## Install
Reached via occasion, alongside [content-directory](content-directory.md). Checked mechanically by [`tools/checks/check_assorted_notes.py`](../tools/checks/check_assorted_notes.py): a markdown link anywhere in the tracked tree, outside this practice file and the notes file itself, whose target path ends in `ASSORTED_NOTES.md` (or one of the legacy names it replaces) fails the check. Scope is `tree`. It can't catch a bare prose reference with no link -- only the linked form, which is the catchable case in a repo whose own standing convention is to always link ([doc-references-are-links](https://github.com/alex137/BestPractice/blob/precedent-beta-v01/practices/doc-references-are-links.md), universal). Two-direction tested in [`tools/checks/tests/test_assorted_notes.sh`](../tools/checks/tests/test_assorted_notes.sh).
