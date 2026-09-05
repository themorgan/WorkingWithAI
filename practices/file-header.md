---
slug:        file-header
title:       A last-updated timestamp, author, and version at the top of files
tier:        on-demand
severity:    default
applies_to:  ["**/*.md"]
occasion:    "editing a markdown file that carries this header"
gates:       []
index_clause: "markdown files get a last-updated/by-me/version header"
checked_by:  tools/checks/check_file_header.py
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-08-31
approved_by: "Morgan F, migrated from RepoPersonalPreferences by the private-set migration session"
---
## Rule
A markdown file I maintain gets `<!-- Last updated: YYYY-MM-DD HH:MM:SS (Buenos Aires) by Morgan F, to version N -->` as its first line -- a full timestamp (hour, minute, second), not just a calendar date, since a bare date can't tell two same-day edits apart. `N` is a plain integer counter private to that one file: 1 the first time the header is added, +1 each subsequent time the file's content changes. Update the line whenever the file's content changes, not its formatting alone -- same trigger for bumping `N`.

## Detail
The "to version N" phrasing names that one file's own version, not a repo-wide release number, so bumping it is a one-file edit. This also means the rule doesn't mean retrofitting a header onto every existing file at once -- a file only picks up (or bumps) its header when it's actually being edited for some other reason, never a repo-wide sweep. A script or config format with comments gets the equivalent in that syntax; skip it where a leading comment would break the file (JSON has none) or where the file is a byte-for-byte mirror of something else and must never be hand-edited.

## Why
`NAME` here is always "Morgan F" when I'm the one making the edit -- the same name every commit is already authored as -- so the header settles who last touched the file without a reader needing to go check `git blame`.

## Story


## Install
Checked mechanically by [`tools/checks/check_file_header.py`](../tools/checks/check_file_header.py) against every tracked `*.md` file. A file only carries an obligation once its first line already looks like the header -- files that never had one aren't flagged, matching the Detail section's "only when actually being edited" rule. For a file that does carry it: the header line must match the exact format, and version `N` must increase from the parent commit exactly when the file's body changed, and stay put exactly when it didn't. Scope is `change` (compares each commit against its parent). Two-direction tested in [`tools/checks/tests/test_file_header.sh`](../tools/checks/tests/test_file_header.sh), covering both a malformed header line and a content change with no version bump.

