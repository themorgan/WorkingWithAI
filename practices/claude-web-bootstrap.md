---
slug:        claude-web-bootstrap
title:       My individual set resolves automatically in Claude Code Web
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "installing Precedent into a project I'll work on from Claude Code Web"
gates:       []
index_clause: "wire the SessionStart hook so this set clones and configures itself"
checked_by:  tools/checks/check_claude_web_bootstrap.py
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-08-31
approved_by: "Morgan F, in the session that raised it"
---
## Rule
Every project set up with Precedent for me to work on from Claude Code Web gets a `SessionStart` hook that clones or updates `precedent-individual` and writes `~/.config/precedent/config.json`, before the session's first tool call. I never run a command myself for this -- not to clone the repo, not to write the config -- so the individual source is already resolvable the moment work starts.

## Detail
The hook is synchronous, not async, on purpose: an early tool call resolving practices before the individual source exists would silently degrade (correctly, per the resolver's own contract -- but not what should happen every single session). Synchronous removes the race outright, at the cost of a small, fixed amount of session-start latency for a small clone.

It fails gracefully rather than failing the session: if this environment can't reach `precedent-individual` (no credential, no network), the hook says so on stderr and exits 0 -- team and universal still resolve, and the missing-source message is the same one `precedent_resolve.py` already prints for any absent source, not a special case.

This is a per-project install step, not a one-time global setting -- `SessionStart` hooks live in a project's own `.claude/settings.json`, so each project that wants this needs the hook installed once, the same way it needs Precedent's `precedent.json` installed once. See `precedent-team-maintainers/practices/install.md` for where this step belongs in that procedure. The actual script content must be **copied** into the target project's own `.claude/hooks/`, not referenced by a path under `$HOME` -- on a brand-new container nothing under `$HOME` exists yet, so the hook that creates `$HOME/precedent-individual` can't itself live inside it.

## Why
Most of what a personal preference layer like this ever needs from me is nothing at all -- and for anyone this pattern serves who isn't a developer, "clone a repo and write a config file" was never a reasonable one-time cost, let alone a per-project one. The friction was a bootstrapping gap in an otherwise sound design (a separate private repo, never vendored into a shared project), not a reason to weaken the privacy separation itself.

## Story
Raised directly in a conversation where testing this against a fresh repo turned out to be blocked by this session's own repo scoping -- which is what surfaced that a session-level "add a repo" capability isn't actually wired up in this environment, separately from the bootstrap question itself.

## Install
The canonical script and settings snippet live in this repo, at [`bootstrap/session-start.sh`](../bootstrap/session-start.sh) and [`bootstrap/settings.snippet.json`](../bootstrap/settings.snippet.json). Installing into a project:

1. Copy `bootstrap/session-start.sh`'s content into the target project as `.claude/hooks/precedent-individual-bootstrap.sh` (executable).
2. Merge `bootstrap/settings.snippet.json`'s `hooks.SessionStart` entry into the project's own `.claude/settings.json` (create it if missing; append to an existing `SessionStart` array rather than replacing it).
3. Commit both as tracked files in the project -- this only works because they're present the instant the container starts, before anything else runs.

Validated end-to-end 2026-08-31: a fresh clone, an idempotent re-run (pull path), and the non-remote no-op all behaved as described, and `precedent_resolve.py` picked up the individual source afterward with no other setup.

Checked mechanically by [`tools/checks/check_claude_web_bootstrap.py`](../tools/checks/check_claude_web_bootstrap.py), scope `tree`, with a deliberate limit: the practice's actual claim -- "every project gets this hook installed" -- is about *other* projects' `.claude/` trees, which a check living in this repo can't see. What it verifies instead is that the two canonical artifacts this repo publishes for other projects to copy still hold the structural invariants this file's own Detail section requires: `bootstrap/session-start.sh` is git-tracked executable and never exits non-zero (fail-gracefully, not fail-the-session), and `bootstrap/settings.snippet.json` is valid JSON whose hook command doesn't reference `$HOME` and whose hook entry isn't marked `"async": true`. If either file regresses on any of those, every project that copied it breaks the same way. Two-direction tested in [`tools/checks/tests/test_claude_web_bootstrap.sh`](../tools/checks/tests/test_claude_web_bootstrap.sh), one planted violation per invariant.
