<!-- Last updated: 2026-09-02 12:40:00 (Buenos Aires) by Morgan F, to version 1 -->

# Migrating this repo from BestPractice-only to Precedent (2026-09-02)

This is the record of moving `WorkingWithAI` from BestPractice's original
single-vendor-plus-personal-pack model to
[Precedent](https://github.com/alex137/BestPractice/tree/precedent-beta-v01)'s
three-source model — the first real test of the `precedent-beta-v01` branch
against a repo that already had BestPractice installed. Kept here per this
repo's own `repo-is-memory` habit: a session's chat thread is disposable,
so what a future session needs to understand this change lives in a
committed file, not a transcript. See [TODO.md](../TODO.md)'s "Decisions"
section for the same change as a one-paragraph decision-log entry, and
[AGENTS.md](../AGENTS.md)'s "Practice sources (Precedent)" section for the
resulting day-to-day rules.

## Before → after

| | Before | After |
|---|---|---|
| Universal practices | Vendored at `process/upstream/`, tracking `alex137/BestPractice`'s `main` branch | Vendored at `process/upstream/`, now tracking the `precedent-beta-v01` branch (a deliberate beta pin — see "Why a vendored copy, still" below) |
| Team / personal conventions | Vendored at `process/personal/`, mirrored from the private repo `themorgan/RepoPersonalPreferences` (46 rules, one flat file, `process/personal/README.md`) | Resolved **live** from a sibling clone of the now-real [precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers) (41 practices), declared in the new [precedent.json](../precedent.json) — not vendored at all |
| Morgan-specific facts | Mixed into the same `process/personal/` pack, flagged only by convention (`morgan-scope`) | Split into [precedent-individual](https://github.com/themorgan/precedent-individual) (6 practices), resolved from Morgan's own user-level config, **never** named in this repo's tracked files |
| Sync automation | Three scheduled workflows: BestPractice sync, personal-pack sync, voice-guidelines sync | Two: BestPractice sync (paused for the beta) and voice-guidelines sync (unaffected). Personal-pack sync retired outright — there is nothing left to vendor-and-sync for the team/individual sources |
| `AGENTS.md` | A "Personal setup rules (Morgan's pack)" section with all ~40 rules copied in full | A "Practice sources (Precedent)" section: explains the three sources, points at `precedent_resolve.py` for the real merged set, and hand-curates only the resident + most-frequently-needed practices (see "Known gap" below for why it isn't fully automatic) |

`process/personal/`, `process/manifest_personal.json`, and the two
retired-tools-that-were-really-generic-utilities
(`process/personal/tools/light_check.py`,
`process/personal/tools/report_automation_issue.py`, now at
[tools/light_check.py](../tools/light_check.py) and
[tools/report_automation_issue.py](../tools/report_automation_issue.py))
are all gone from this repo's tree as of this change.
RepoPersonalPreferences itself was already split into the two new repos in
an earlier session — see
[spec/PRIVATE_SETS_BRIEF.md](https://github.com/alex137/BestPractice/blob/precedent-beta-v01/spec/PRIVATE_SETS_BRIEF.md)
in BestPractice for that side of the story ("Done, 2026-09-01" — closed
before this repo ever consumed either new repo).

## Why a vendored copy, still

Precedent's own `precedent.json` (BestPractice is its own first consumer)
declares its universal source as `path: "."` — itself. A generic dependent
repo can't do that: it needs `process/upstream/` to keep working offline,
for a collaborator or a CI runner without a sibling `BestPractice` checkout,
and for `process/manifest.json`'s per-file drift tracking, none of which a
live path reference provides. So universal stayed vendored; only team
(now a real repo with its own maintainers, not a domain-scoped pack
without one yet) moved to the live-sibling-clone pattern.

## Why a beta branch, and what that costs

`process/manifest.json`'s `upstream.branch` is `precedent-beta-v01`, not
BestPractice's own default branch. That is the entire point of this
exercise, but it breaks one piece of existing automation:
`tools/checkin.py`'s `fresh`/`update`/`record` commands all resolve the
remote's **default-branch** HEAD unconditionally (`_default_branch()` reads
`refs/remotes/origin/HEAD`) — there is no way to tell them "track this named
branch instead." Left alone, the BestPractice sync workflow would either
print a false "upstream has moved" notice every session (comparing our
beta-branch commit against `main`'s HEAD) or, worse, try to merge `main`'s
tree over this repo's deliberately beta-pinned vendored copy the next time
it ran unattended.

**What was done about it:** the vendoring for this change was a one-off
manual mirror (the vendored tree replaced wholesale from a checkout of
`precedent-beta-v01`, not `checkin.py update`), `.github/workflows/bestpractice-upstream-sync.yml`'s
schedule is commented out (manual `workflow_dispatch` still works, with a
guard in its own prompt telling it to stand down if `upstream.branch` isn't
the default branch), and `tools/bootstrap.sh`'s freshness notice for
BestPractice is replaced with a static explanation instead of a live
`checkin.py fresh` call. All three carry a pointer back to this document.
**What isn't done:** a real three-way merge of the branch's changes against
each `process/manifest.json` entry's own adaptation (INSTALL.md §2 step 2)
— the tree was replaced wholesale ("tree-identical" to `precedent-beta-v01`,
the same end state `checkin.py update` would reach on a normal sync), so a
manifest entry whose `upstream_path` moved or was renamed on the beta
branch may now be stale. Not checked entry-by-entry in this pass; worth a
light audit before this beta pin is lifted.

**Recommended pattern for BestPractice itself, going forward:** this whole
section — the branch-tracking gap in `checkin.py`, the paused-sync
workaround, and the general shape of retiring a vendored personal pack in
favor of the new three-source model — is written up generically upstream at
[spec/MIGRATING_EXISTING_INSTALLS.md](https://github.com/alex137/BestPractice/blob/precedent-beta-v01/spec/MIGRATING_EXISTING_INSTALLS.md),
using this repo as the worked example, so the next dependent repo doing
this same migration doesn't have to rediscover it.

## The validation: running `precedent_resolve.py` for real

[spec/PRIVATE_SETS_BRIEF.md](https://github.com/alex137/BestPractice/blob/precedent-beta-v01/spec/PRIVATE_SETS_BRIEF.md)'s
own "Done when" checklist named one item that had never happened: running
the resolver against the real two private sets from a real consumer repo,
with a real `precedent.json` and a real user config, rather than the
verification harness's synthetic fixtures. This repo is that consumer repo.
Setup (the first two steps are per-environment, not committed to this
repo — see `AGENTS.md`'s own privacy note on why the individual source is
never named here):

```
# ~/.config/precedent/config.json (outside any repo, never committed):
{
  "format_version": 1,
  "individual": {"name": "precedent-individual", "path": "<local precedent-individual checkout>"}
}
```

`precedent.json` (committed, in this repo's root) declares universal
(`process/upstream`) and team (`../precedent-team-maintainers`, a sibling
clone). Result, 2026-09-02:

```
$ python3 process/upstream/tools/precedent_resolve.py --repo .
resolved 99 practice(s) from 3 source(s): 6 individual, 41 team, 52 universal
  overridden: doc-references-are-links -- team (precedent-team-maintainers) replaces universal (precedent)
  overridden: merge-authorization-keyword -- individual (precedent-individual) replaces universal (precedent)
resident block across all sources: ~659 of 2000 token budget (10 practice(s): bold-key-phrases (team), buenos-aires-dates (individual), environment-gotchas (universal), nonblocking-questions (team), orientation-map (universal), quick-index (universal), reply-links-files (universal), repo-is-memory (universal), small-calls (team), verify-postcondition (universal))
$ echo $?
0
```

No missing sources, no blocked overrides, no slug collisions, and the
combined resident block (from all three sources at once — the
cross-source cap `precedent_resolve.py`'s own `resident_stats()` added
specifically because no single source's own build had ever seen the whole
picture) comes in at under a third of the 2,000-token budget. `--explain`
on both overridden slugs confirms the precedence reads correctly:

```
$ python3 process/upstream/tools/precedent_resolve.py --repo . --explain go-merge
go-merge: in force from the individual source (precedent-individual), .../practices/go-merge.md
  overrides the universal practice 'merge-authorization-keyword' at .../process/upstream/practices/merge-authorization-keyword.md
```

This closes the one open item `spec/PRIVATE_SETS_BRIEF.md` and
`spec/PHASE5_DEEPCHECK.md` both flagged as unfinished: the resolver and the
cross-source resident cap were tested against fixtures and the frozen
example set, never against the real 46-rules-split in a real repo, until
now.

## Known gap: no cross-source Rule-text loading channel yet

`precedent_resolve.py` genuinely merges all three sources — it is the tool
this document's validation run used, and it is what `AGENTS.md` tells a
session to run to see the real in-force set. The *other* loader tools —
`precedent_show.py` (pulls one slug's `## Rule` text into context),
`precedent_paths.py` (path-triggered loading), `precedent_gate.py`
(moment-triggered loading) — are all single-source as of the
`precedent-beta-v01` branch: each hardcodes `ROOT` to its own repo and only
ever reads `<that repo>/practices/`. Running
`process/upstream/tools/precedent_show.py SOME-TEAM-SLUG` from this repo
resolves `ROOT` to `process/upstream` and silently looks for the slug in
BestPractice's own catalogue, not `precedent-team-maintainers`'s — there is
no built extractor today that reads a slug from an arbitrary resolved
source.

Practically, this means the automatic, low-effort part of the loader
design (a session's context gets the right `## Rule` text without anyone
having to go find it) doesn't fully exist yet for a three-source consumer
repo — only for BestPractice auditing itself. `AGENTS.md`'s "Practice
sources (Precedent)" section hand-curates the resident and most-frequently-
needed on-demand practices as a stopgap for exactly this gap, explicitly
labeled as one, rather than either leaving nothing (a real regression from
the old fully-inlined personal pack) or silently pretending the automatic
channel already reaches every source.

This is the same gap `spec/PHASE5_BRIEF.md`'s "what phase 6 inherits"
language anticipates in general terms; this migration is the first place
it was actually hit by a real consumer repo, not a fixture. Recorded
upstream too, in
[spec/MIGRATING_EXISTING_INSTALLS.md](https://github.com/alex137/BestPractice/blob/precedent-beta-v01/spec/MIGRATING_EXISTING_INSTALLS.md),
so it isn't only visible from this repo's own side.

## A real finding: `practice_audit.py`'s scrub check does not cleanly pass

Running `python3 process/upstream/tools/practice_audit.py` after the
re-vendor gives **53 SCRUB failures, all inside `process/upstream/`
itself** — not in anything this repo added. This is worth recording
plainly rather than working around, and worth NOT "fixing" by editing
`process/upstream/` (forbidden — it must stay byte-identical to the vendored
branch) or by quietly deleting blocklist entries to make the audit pass.

**What's actually happening:** `process/scrub_blocklist.txt` is Morgan's
own private-vocabulary list for this repo, whose own header explains its
purpose precisely — "never let these appear in `process/upstream/` (the
public BestPractice repo would receive them on the next check-in)". It
includes broad patterns (`themorgan`, `Buenos Aires`,
`America/Argentina/Buenos_Aires`) alongside much more specific ones
(`morgan@westegg\.com`, `westegg\.com`, `morganfriedman`, `6497032`).
`precedent-beta-v01`'s own spec docs and decision records
(`PRACTICE_ENGINE_PLAN.md`, `spec/PRIVATE_SETS_BRIEF.md`,
`spec/PHASE5_DEEPCHECK.md`, `decisions/2026-09-01-relax-private-repo-isolation.md`,
and others) legitimately, publicly document Morgan's real GitHub handle and
Buenos Aires timezone as part of narrating the real work of populating
`precedent-individual` and `precedent-team-maintainers` — because in this
story Morgan is a genuine, disclosed, named contributor to the public
Precedent project itself, not someone whose identity BestPractice is
supposed to keep out of its own docs.

**Confirmed by checking exactly which patterns fired:** all 53 hits match
only `themorgan` (28), `Buenos Aires` (22), and
`America/Argentina/Buenos_Aires` (3) — none of the more specific,
genuinely sensitive entries (`morgan@westegg\.com`, `westegg\.com`,
`morganfriedman`, `6497032`, `Morgan F`, `WorkingWithAI`) fired at all.
That is exactly the shape a legitimate disclosure collision should have:
the identifiers BestPractice's own public docs disclose about their real
contributor overlap with this repo's *broadest* private-vocabulary
patterns, and nothing more specific leaked.

**Why this isn't a WorkingWithAI leak, and why it isn't something to
silently patch:** the scrub check's own design assumption is that anything
under `process/upstream/` should already be public-safe *because it mirrors
a public repo verbatim* — it has no way to distinguish "this term arrived
already-public, disclosed by upstream itself" from "this term leaked in via
our own local edit or a bad merge." Both this repo's blocklist and
BestPractice's own `practice_audit.py` are working exactly as designed;
they simply weren't designed for the case where the *same person* is both
a dependent repo's private owner and a disclosed, named contributor to the
public upstream project. Weakening the blocklist to silence this would
also weaken it against the scenario it actually exists for — a future
accidental leak of the *specific* identifiers, which correctly did not fire
here. Left as a known, understood FAIL for this beta-tracked vendored
tree; **flagged upstream** in
[spec/MIGRATING_EXISTING_INSTALLS.md](https://github.com/alex137/BestPractice/blob/precedent-beta-v01/spec/MIGRATING_EXISTING_INSTALLS.md)
as a real gap `practice_audit.py`'s scrub check has no answer for today
(a diff-against-last-recorded-upstream-snapshot design, the same shape
`tools/leak_gate.py`'s push-time check already uses instead of scanning a
whole snapshot, would resolve it — not built here).

## Files touched

See [TODO.md](../TODO.md)'s "Decisions" entry for this change (dated
2026-09-02) for the full list; the shape, not repeated here to avoid a
second copy that can drift out of sync with the first
([`no-duplication`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/no-duplication.md),
generalized past BestPractice specifically).
