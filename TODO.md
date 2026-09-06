<!-- Last updated: 2026-09-06 09:25:00 (Buenos Aires) by Morgan F, to version 57 -->

# Repo TODO — open analyses, verifications, and decisions

Working list of open items that span sessions. Convention: one line each, with
the deliverable/section it blocks and the kind of work (**analysis** =
agent-doable from the desk; **verify** = source-check before external use;
**physical** = needs hardware/vendor/test; **decision** = the user's call).
Prune when done; large completed items get a one-line "done → doc" entry, then
drop off next cycle.

**Push-time gate (personal pack):** before every push, re-read this list
against what the branch actually discussed — add ideas that came up but
never got a line here, remove/check items this branch already implements.
See [AGENTS.md](AGENTS.md) merge runbook step 0c.

## Pending drift reviews

Auto-maintained by `pack_sync.py record` / `resolve`
([`drift-notice`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/drift-notice.md)) -- a
session-start freshness notice lands here, not just on stdout, so it
can't lose a priority fight against whatever task is already in front
of a session and go unaddressed. `light_check.py` warns on every commit
while an entry below stays unchecked. Check an item off (or run
`pack_sync.py resolve <source>`) once its drift has actually been
reviewed -- the update taken, or deliberately deferred with a reason.

- [x] **personal-pack** (2026-08-29): NOTICE: the personal pack's source has moved (1e06a5349a43; your base d436be779be1) — review at the next session (https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/drift-notice.md). -- resolved 2026-08-29: taken via WorkingWithAI RPP sync, this session
- [x] **personal-pack** (2026-08-29): NOTICE: the personal pack's source has moved (570f86c520fc; your base b10c163a96dd) — review at the next session (https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/drift-notice.md). -- resolved 2026-08-29: taken via RPP sync: durable-list-anchors + brainstorm-citations, this session
- [x] **personal-pack** (2026-08-29): NOTICE: the personal pack's source has moved (b54461560435; your base 9793691dcecb) — review at the next session (https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/drift-notice.md). -- resolved 2026-08-29: taken via RPP sync: derived-file-marker + doc-recipe + rule-scope-ask + list-restraint, this session
- [x] **personal-pack** (2026-09-02): COULD NOT VERIFY: couldn't reach the personal pack's source (https://github.com/themorgan/RepoPersonalPreferences) to check freshness — `git ls-remote` failed (fatal: could not read Username for 'https://github.com': terminal prompts disabled). This is NOT the same as 'confirmed fresh': if you need to know, verify directly instead of trusting this silence (https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/fresh-check-escalation.md). -- resolved 2026-09-02: moot. `process/personal/` and RepoPersonalPreferences tracking were retired the same day in the Precedent migration below — there is no personal-pack source left to check freshness against.
- [x] **bestpractice** (2026-09-02): NOTICE: BestPractice upstream has moved (558b16a62030; your base c76f06f87e52) — review at the next check-in (process/upstream/INSTALL.md sec.2/sec.4). -- resolved 2026-09-02: superseded, not taken as a normal update. The same-day Precedent migration below re-vendored `process/upstream/` from `alex137/BestPractice`'s `precedent-beta-v01` branch instead (a deliberate beta-test pin, not this notice's own default-branch head at 558b16a62030) — see [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md). The BestPractice sync is paused until the beta branch merges to main, at which point this repo should take a normal update against whatever main's head is by then, not against this now-stale commit.
- [x] **bestpractice** (2026-09-04): re-vendored `process/upstream/` from `alex137/BestPractice`'s `precedent-beta-v01` at `16a9becf` to `3d03afd` (~30 commits, PRs #83-#98) via the same one-off manual mirror (`checkin.py` still can't track a non-default branch). -- resolved 2026-09-04: taken, this session → [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)'s "2026-09-04 follow-up" section.

## Recurring

- [ ] **BestPractice check-in:** review `diverged` entries in
  [process/manifest.json](process/manifest.json) and the vendored tree's
  accumulated changes; propose upstream per
  [process/upstream/INSTALL.md](process/upstream/INSTALL.md) §4 (scrub audit
  first). Include the `practice_audit.py --update-baseline` bug found
  2026-09-04 (below) as one of the proposed fixes.

## Analyses (agent-doable)

- [x] **Populate [RANDOM_NOTES.md](content/RANDOM_NOTES.md) with real content.** Done
  2026-08-26 → [RANDOM_NOTES.md](content/RANDOM_NOTES.md) now holds the first real brainstorm
  batch, plus [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) promoted out as its own
  document. The three original placeholder sections (prompts, workflows,
  incidents) are still empty and open for the next batch.
- [x] **Restructure [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md):
  drop the count from the title, cut a rule, reword two, and group the
  rest into named sections.** Done 2026-08-29 → doc. Seven changes,
  Morgan's, in one pass. (1) Title "Fifteen rules for building a company
  around AI" → "Rules for building a company around AI" — a count in a
  title drifts every time a rule is added or cut, so it's gone from the
  title, the opening paragraph, and every cross-reference that named it
  (this file, [AGENTS.md](AGENTS.md), [RANDOM_NOTES.md](content/RANDOM_NOTES.md),
  [MAP.md](MAP.md)) — the file's own
  [`no-stale-counts`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/no-stale-counts.md).
  (2) Rule 1's title dropped ", Labor isn't" — read as needlessly
  dismissive of labor; the body already makes the point without it.
  (3) The old rule 6 rewritten from two reflexes to three, adding "What
  rules or protocols should come from this?" as the first question —
  the reflex that generates a rule live, matching rule 7's own point
  about capturing corrections automatically.
  (4) The old rule 7, "own the spec and the eval before you own the
  output," removed — Morgan flagged it sits in tension with rule 9's
  "build five, kill four" (commit to a definition of good before
  building vs. building fast and killing most of it). Not resolved,
  just cut; logged as a 2026-08-29 entry in [RANDOM_NOTES.md](content/RANDOM_NOTES.md) to
  revisit later — is it a real contradiction or two rules for two
  different situations that needed sharper scoping instead.
  (5) The hiring rule retitled "Hire for drive, 'Getting Shit Done,'
  relationships, and taste" (was "hire for taste and verification, not
  production") — Morgan's emphasis is specifically people who figure
  out how to get things done, with taste as one part of that picture,
  not the headline; the blunter ", not production" framing is gone.
  (6) A new rule, "treat the AI Chat as the intermediary for the work
  itself, not a tool you consult on the side" — the partner that pushes
  back before a plan commits and pushes it into happening once it
  does — added and placed early (new rule 4) rather than at the end,
  since Morgan called it core.
  (7) The full list regrouped under four named sections — Foundations;
  Working with the model; Shipping and process; People — ordered so the
  "various roles of humans" rule (permanent hire, what's structurally
  human) stays last, as Morgan asked. Removing rule 7 and moving rule 16
  meant renumbering the whole list; every "(rule N)" citation across
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md), [REASONS_WHY.md](content/REASONS_WHY.md),
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md), and
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) was updated to match;
  historical "Revised Nth time" log entries elsewhere in this file were
  left alone, per this file's own precedent of not rewriting the record
  of what was true when it was written.
  Judgment calls made: (1) kept rules as bold paragraphs rather than
  real Markdown headings even with the new section structure, since
  giving each rule its own heading was a bigger typographic change than
  asked and would have obsoleted [AGENTS.md](AGENTS.md)'s citation-style
  reasoning ("no heading to anchor to") for the whole file, not just this
  edit; (2) named the four sections descriptively (not numbered) rather
  than inventing punchier titles, to keep them from reading as a second
  numbering scheme competing with the rules' own; (3) kept the hiring
  rule's phrase "Getting Shit Done" close to Morgan's own wording rather
  than softening it, since the whole point of that edit was to state the
  emphasis (drive, execution) more directly, not less.

  Session: https://claude.ai/code/session_017Zg3sdbyAygn4L3ShpxTKw

- [x] **Shorten every rule paragraph in [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)
  to roughly 60% of its original length.** Done 2026-08-29 → doc.
  Morgan's. Trimmed the opening paragraph and all 15 rule paragraphs in
  two passes — the first pass under-cut rules 8-15 (they landed closer
  to 80-85% of original length), caught and fixed in a second pass once
  Morgan flagged it. Kept every anchor, link, and the two open
  placeholder brackets (`hire-for-drive`, `human-only-zones`) intact.

  Session: https://claude.ai/code/session_019JL6ufKp3vdHv6n1drNYoz

- [x] **Fill in the two open brackets in [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md).**
  Done 2026-09-01 → doc's. Rule 12's "sharpest editor" bracket (and the
  "test taste directly: hand the candidate twenty drafts..." sentences it
  sat in) is gone — cut on Morgan's instruction rather than filled in.
  Rule 14 still wants a real year for "the way you'd have read it in
  [YEAR]," intentionally left as a placeholder — replace it only when a
  real specific comes to mind. **Superseded 2026-09-01:** Morgan decided
  to drop the year as an input entirely rather than fill it in — rule 14
  rewritten without one, and the "Open placeholders" footer this entry
  refers to is gone.

  Session: https://claude.ai/code/session_013PVX4o1GAgFzfbvgUZuM1S

- [x] **Trim [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)'s
  intro, reword rule 1, reorder rules 6/7, and drop the closing
  "shorter than five years ago" line; add "and" to
  [REASONS_WHY.md](content/REASONS_WHY.md) rule 9; shrink the README's
  "How this repo's ideas become company policy" section by half and add a
  closing "How to use this Repo" section.** Done 2026-09-02 → docs.
  Morgan's. In [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md):
  cut the italic intro's meta-commentary about the essay/checklist
  relationship and the "Every founder..." paragraph that followed it;
  retitled rule 1 from "Context is the capital asset" to "Context is
  king" (anchor `capital-asset` kept); swapped
  [`think-in-workflows`](content/COMPANY_BUILDING_RULES.md#think-in-workflows)
  and [`three-questions`](content/COMPANY_BUILDING_RULES.md#three-questions)
  into rules 6 and 7 respectively (anchors unaffected, per
  `durable-list-anchors`; fixed the one stale "rule 7" reference this
  broke, further down this file); dropped the closing "That list is
  shorter than it was five years ago" sentence after rule 15. In
  [REASONS_WHY.md](content/REASONS_WHY.md), added "and" before "get
  caught" in rule 9. In the README, condensed the three-stage pipeline
  section and dropped its
  [precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers)/[precedent-individual](https://github.com/themorgan/precedent-individual)
  name-drops — public-facing docs point to
  [BestPractice](https://github.com/alex137/BestPractice) only, never to
  the team- or individual-level source repos by name; added a closing
  "How to use this Repo" section pointing readers at BestPractice.

  Session: https://claude.ai/code/session_01W8YVaDduub3yidsxj6f5es

- [ ] **`process/upstream/tools/practice_audit.py --update-baseline` silently
  flips a manifest entry's `status` from `diverged` to `synced`** whenever
  the recorded `local_sha256` doesn't match the file's current hash — even
  when the mismatch is just a stale recorded hash (nothing about the file
  actually changed), not a real re-baseline event. Hit 2026-09-04 running
  `--update-baseline` after a `process/upstream/` re-vendor: it flipped
  `.claude/settings.json` and `tools/bootstrap.sh` from `diverged` to
  `synced`, silently discarding the deliberate "never export this
  as-is" marking both entries' own notes explain — fixed by hand in
  [process/manifest.json](process/manifest.json), not by editing
  `process/upstream/`. Blocked on a check-in session (upstream repo access)
  to actually propose the fix (the guard at
  `practice_audit.py`'s line ~172 should require the caller to name which
  entries are intentionally being re-baselined, or at minimum warn loudly
  on any `diverged → synced` flip instead of doing it silently).
- [ ] **Look for contradictions across [RANDOM_NOTES.md](content/RANDOM_NOTES.md) entries**, per
  the meta-note at the bottom of that file (e.g. rule 9's "build five, kill
  four" against [`think-in-workflows`](content/COMPANY_BUILDING_RULES.md#think-in-workflows)'s
  "don't systematize a one-off") — worth a
  dedicated pass once there's enough material for real tensions to show up.
  Now also item 7 of [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) — this line
  and that item are the same recurring job, described from two sides.
- [ ] **Design real infrastructure for active/proactive resurfacing** —
  [`active-resurfacing`](content/AI_GOVERNANCE_TO_COCREATE.md#active-resurfacing)'s
  "you decided X six weeks ago, unprompted" test,
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md)'s "Not yet
  ready" list. Needs something that mines and ranks prior decisions rather
  than only answering when asked; no design proposed yet. **analysis.**
- [ ] **Design automatic workflow-candidate detection** — mining
  commit/session history for a recurring task shape, instead of relying
  solely on [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) item 4's
  human-triggered reflex. **analysis.**
- [ ] **Work out situational, inferred cost-awareness** —
  [`cost-awareness-situational`](content/AI_GOVERNANCE_TO_COCREATE.md#cost-awareness-situational)
  records that a fixed "surface spend per outcome" policy was already
  proposed and rejected; the open half is inferring *which* posture
  applies (explicit budget mention, project stage, stated intent) rather
  than applying one policy everywhere. Passive cost logging is the one
  piece already worth keeping regardless. **analysis.**
- [ ] **Formalize the coldstart test as a periodic check** — can a fresh
  session, given only the memory store, reconstruct the state of any live
  decision? Currently just a manual audit idea in
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md); worth deciding whether it
  becomes a recurring item here (like the BestPractice check-in) or stays
  ad hoc. **decision.**
## Verify before external use

## Decisions (user's call)

- [x] **Re-vendor `process/upstream/` to pick up the cross-source
  consumer-repo generator (`tools/precedent_sync_views.py`); vendor the
  loader-engine tools to this repo's own top-level `tools/`; regenerate
  `AGENTS.md`'s loader block for real.** Decided 2026-09-03 → done, full
  record in [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)'s
  "2026-09-03 follow-up" section. Closes the "Known gap" the original
  migration below flagged and explicitly did not build a fix for: the
  hand-curated resident/on-demand stopgap list in `AGENTS.md` is gone,
  replaced by a real `<!-- BEGIN/END GENERATED: precedent-loader -->` block
  regenerated from all four sources (universal/team/individual/repo-local)
  by `python3 tools/precedent_sync_views.py --repo .` — confirmed
  byte-identical on a second `--check` run. Re-vendored `process/upstream/`
  to `precedent-beta-v01` commit `16a9becf` (previously `8c3b02dd`);
  `process/manifest.json` updated. Evaluated repo-local per practice 23's
  decision rule — not adopted, nothing in this repo's own `AGENTS.md` rose
  to a portable rule distinct from its subject-matter docs. Found and
  documented, not silently patched: a real path-doubling bug in the
  vendored `precedent_materialize.py`'s `MANIFEST.json` output (cosmetic —
  actual file writes are correct); `.claude/settings.json`'s permission
  allowlist left un-updated for the two new script paths (blocked by the
  session's own auto-mode classifier, a self-granting-permissions change
  correctly left for a human). `practice_audit.py`'s scrub-collision count
  unchanged at 63 (matches the previously recorded count exactly).

- [x] **Re-vendor `process/upstream/` to pick up `migration-scrubs-vocabulary`.**
  Decided 2026-09-03 → done. Upstream added a new practice, mechanical
  check, and harness case: a repo migrating off an old practice system now
  scrubs that system's vocabulary in the same migration, not on request —
  the exact gap this repo's own RepoPersonalPreferences migration hit a
  day before it was caught. Adds an opt-in, tree-scoped check keyed off a
  declared `process/retired_vocabulary.json` (this repo hasn't declared
  one, so it reports `NotApplicable`) and strengthens
  `spec/MIGRATING_EXISTING_INSTALLS.md`'s step 5 to require it before a
  migration counts as done. `process/manifest.json`'s `upstream.commit`/
  `_note` updated; scrub-collision count unchanged.

- [x] **Strip old-system vocabulary and instructions (RepoPersonalPreferences,
  "the personal pack", `process/personal/`) out of every day-to-day
  document, leaving them only where they're genuinely migration content.**
  Decided 2026-09-03 → done. Morgan asked directly: our vocabulary
  shouldn't keep defining words for concepts we've already retired, except
  where migration itself needs them. Trimmed `AGENTS.md` (the "Practice
  sources" intro, the merge-runbook's export gate and `process/personal/`
  step, the "rest of RepoPersonalPreferences' 46 rules" paragraph, the
  scheduled-syncs list's tombstone bullet for the already-deleted
  personal-pack sync), `GETTING_STARTED.md` (a whole paragraph teaching a
  new member about a workflow that was retired before they ever saw this
  repo — replaced with just the current fact), `GLOSSARY.md` (three
  entries that defined "the personal pack" inline instead of just pointing
  at the migration record), `MAP.md` (three rows with the same pattern),
  `content/RULES_NOW_TESTING.md` (one paragraph), `precedent.json` (one
  comment), and all three `.github/workflows/*.yml` header comments.
  Along the way, fixed a real numbering bug this same cleanup exposed:
  removing the dead "personal-pack sync" bullet left "the second scheduled
  check" (BestPractice sync) and "the third" (voice guidelines sync)
  correctly as first and second — both `AGENTS.md` and `GETTING_STARTED.md`
  updated, plus a stale cross-reference in `AGENTS.md` that named "this
  file" for a heading that has only ever lived in `GETTING_STARTED.md`.
  Also fixed two accuracy bugs surfaced along the way: `GLOSSARY.md` and
  `GETTING_STARTED.md` still linked `bestpractice-sync` to
  `precedent-team-maintainers`, not its actual new home in
  `precedent-individual` (from the 2026-09-03 move). Checked
  `alex137/BestPractice` for the same pattern and found none needed — its
  own RepoPersonalPreferences mentions are already confined to genuine
  migration/design-history documents (`spec/MIGRATING_EXISTING_INSTALLS.md`,
  `spec/PRIVATE_SETS_BRIEF.md`, `decisions/*`, `PRACTICE_ENGINE_PLAN.md`),
  and `layered-practice-packs` (the "practice pack" GLOSSARY.md term) is a
  different, still-`active` concept, not a retired one — so no upstream PR
  this round, only this repo's own cleanup. Left untouched, deliberately:
  `TODO.md` and `content/RANDOM_NOTES.md` (both explicitly historical
  logs, not living instructions), `process/manifest.json`'s own
  per-entry provenance notes (a legitimate audit trail), and
  `process/PRECEDENT_MIGRATION.md` itself (the migration record this
  content now lives in instead).

- [x] **Re-vendor `process/upstream/` to pick up `code-cites-practice`'s
  finished retrofit; add the same slug markers to this account's own two
  private practice sources.** Decided 2026-09-03 → done. Morgan asked
  directly whether the retrofit had actually reached universal, team, and
  individual — it hadn't finished for universal (only the one motivating
  example, `disclose-landing`, had been fixed) and hadn't started for the
  two private sets. Closed all three: BestPractice converted over thirty
  stale position-number citations across ten `tools/*.py` files to slugs,
  and widened the check to flag a bare `practice N` mention on sight, not
  only an existing-but-wrong slug; `precedent-team-maintainers` and
  `precedent-individual` (no session access needed beyond what this repo
  already has via `add_repo`) each got the same `# practice: SLUG` marker
  added to every one of their own check scripts' docstrings, for
  consistency, even though neither had an actual drift risk (their check
  scripts were built under the slug-based model from the start).
  `process/manifest.json`'s `upstream.commit`/`_note` updated; scrub-count
  unchanged at 62.

- [x] **Move `bestpractice-sync` from `precedent-team-maintainers` to
  `precedent-individual`; add `code-cites-practice` and
  `spec/MOVING_PRACTICES.md` upstream; re-vendor.** Decided 2026-09-03 →
  done. Morgan asked two design questions and one concrete correction:
  1. Does code implementing a practice cite it back by slug? No — fixed
     upstream with a new practice, `code-cites-practice`, and a real
     mechanical check in `precedent_check.py` that flags a citation naming
     a slug that doesn't exist or has been retired.
  2. Is moving an already-active practice between levels a documented
     process? No — fixed upstream with `spec/MOVING_PRACTICES.md`.
  3. `bestpractice-sync` was migrated to `precedent-team-maintainers` by
     the original RepoPersonalPreferences split's blanket "default to
     team" rule, without checking whether it actually belonged there. It
     didn't: unattended, auto-merging automation is Morgan's own
     preference about his own projects, not something Alex separately
     agreed his repos should run. Moved to `precedent-individual`
     following the new documented pattern (land at destination, retire at
     source, in that order) — retired, not deleted, in
     `precedent-team-maintainers`, with a `## Story` note pointing to the
     new location. `AGENTS.md`'s own `bestpractice-sync` link updated to
     match. `process/manifest.json`'s `upstream.commit`/`_note` updated;
     scrub-collision count moved 61 → 62 (`spec/MOVING_PRACTICES.md`'s own
     file-header date, same already-disclosed-upstream reasoning as the
     rest of that known exception).

- [x] **Re-vendor `process/upstream/` again to pick up the new
  `disclose-landing` practice.** Decided 2026-09-03 → done. Morgan asked
  directly whether a session clearly tells the human when a practice lands
  or is proposed, and clearly names where (individual, which named team, or
  universal) -- the honest answer was no, so it got fixed upstream:
  `precedent_land.py` and `precedent_candidate.py` now print an
  unconditional "DISCLOSE TO THE HUMAN:" line naming the level, location,
  approver, and in-force status every time, and the new
  `practices/disclose-landing.md` makes this a real, checkable practice
  rather than only narrative intent in the design plan.
  `process/manifest.json`'s `upstream.commit`/`_note` updated to the new
  tip (`d226f6e`). Scrub-collision count unchanged at 61 -- the new
  practice file introduces no private-vocabulary collision.

- [x] **Re-vendor `process/upstream/` again to pick up the session-repo-access
  fix and the rewritten `ADOPTING.md` approval-lifecycle section.** Decided
  2026-09-03 → done. Two more upstream commits: `f990a98` closes the exact
  session-repo-access gap this repo's own `AGENTS.md` hit and fixed locally
  first (proactive `add_repo`, never "ask if the clone fails") — now baked
  into `INSTALL.md`, `spec/MIGRATING_EXISTING_INSTALLS.md`, and
  `templates/AGENTS.md.template` so every future install gets it right from
  day one, not just this repo. `3a9d497` rewrites `ADOPTING.md`'s approval
  lifecycle as "How an idea becomes a practice" — the plain-language
  explanation of individual/team/universal approval Morgan asked to have
  written down. `process/manifest.json`'s `upstream.commit`/`_note` updated
  to the new tip (`b81b6b9`). Scrub-collision count moved 60 → 61 (the
  re-vendored `ADOPTING.md` carries its own "Buenos Aires" file-header
  date, same already-disclosed-upstream reasoning as the rest of that known
  exception) — `AGENTS.md` and `process/PRECEDENT_MIGRATION.md` updated to
  match.

- [x] **Re-vendor `process/upstream/` to pick up two new BestPractice
  `precedent-beta-v01` commits: a `doc_lint.py` acronym false-positive fix,
  and team candidates that can become a GitHub Issue.** Decided 2026-09-02
  → done. Morgan made a separate fix directly on `BestPractice`
  (`06b1fcf`, unrelated to this repo); separately, the same session had
  just built and merged `48047e3` upstream (`alex137/BestPractice#72`):
  `precedent_candidate.py create --level team --as-issue true` drafts a
  team candidate as a GitHub Issue on that team repo instead of a
  `candidates/*.md` file, for the case a non-approver raises one — a quiet
  file nobody's watching for doesn't get anyone's actual yes, the same
  reasoning universal candidates already use. `process/manifest.json`'s
  `upstream.commit`/`_note` updated to the new tip
  (`29f14c0`). `practice_audit.py`'s known scrub-collision count moved
  from 53 to 60 (the newly-vendored `spec/MIGRATING_EXISTING_INSTALLS.md`
  itself names `themorgan/WorkingWithAI` and Buenos Aires, same
  already-disclosed-upstream reasoning as the rest of that known
  exception) — both `AGENTS.md` and `process/PRECEDENT_MIGRATION.md`
  updated to the new count. No action needed on this repo's own
  `AGENTS.md` "Practice sources (Precedent)" section beyond the count: the
  new `--as-issue` capability is universal-source tooling, already
  documented where a session would look for it
  (`process/upstream/spec/CANDIDATE_FORMAT.md`), not a team-specific rule
  this repo's own hand-curated stopgap list needs to restate.

- [x] **Fix two CI red X's on every push since the Precedent migration, and
  re-add team-source auto-cloning to `tools/bootstrap.sh` at Morgan's
  explicit request.** Decided 2026-09-02 → done. Morgan noticed the red X
  on GitHub and asked; investigating found two real, distinct bugs, both
  introduced by the migration:
  1. **"Light check" failed every run.** `tools/light_check.py`'s new
     `check_precedent_sources` treated a missing `../precedent-team-maintainers`
     sibling clone as a gate failure — but GitHub Actions checks out only
     this one repo, so that sibling structurally never exists in CI.
     Softened to a warning, matching `precedent_resolve.py`'s own
     "degrade gracefully, don't fail" design for a missing source.
  2. **"bestpractice-upstream-sync.yml" failed every run, with zero jobs.**
     Pausing its schedule had left `schedule:` present with every
     `- cron:` line commented out underneath it — an empty `schedule:` key
     is invalid, which invalidates the whole workflow file (GitHub reports
     that as an immediate failure, unrelated to what the workflow does).
     Fixed by removing the `schedule:` key entirely rather than emptying
     it; the reactivation snippet moved into a comment.
  Separately, Morgan asked to re-add automatic cloning of
  `precedent-team-maintainers` in `tools/bootstrap.sh` — the exact thing
  reverted earlier this same day after he pointed out that
  `precedent.json`'s schema has no git URL field, so a generic script
  can't safely guess one. This time it's back, explicitly: the URL is
  still hardcoded, but as WorkingWithAI's own disclosed, current fact
  (matching how `precedent-individual`'s own bootstrap script hardcodes
  its own URL), with the coupling risk spelled out in the script's own
  comment rather than silently accepted. `AGENTS.md`'s "Build-environment
  gotchas" updated to match, and to state plainly that declaring or
  cloning a source is read-only and one-directional — it doesn't grant
  Alex, or anyone else with access to `precedent-team-maintainers`, any
  access back to this repo, regardless of whether Alex has access to
  WorkingWithAI himself.

- [x] **Fix the session-scoping gap the Precedent migration below left open:
  a fresh Claude Code Remote/Cloud session on this repo alone has no git
  access to precedent-team-maintainers or precedent-individual until
  explicitly granted.** Decided 2026-09-02 → done. Morgan asked how a new
  session picks these up; the honest answer exposed an asymmetry —
  precedent-individual's own bootstrap hook clones/pulls it automatically
  once access exists, but `tools/bootstrap.sh` only pulled an *existing*
  team sibling clone, never created one. First attempt hardcoded a clone
  URL for precedent-team-maintainers in `tools/bootstrap.sh` — Morgan
  caught that this was wrong: `precedent.json`'s source schema is
  `{level, name, path}`, never a git URL, so a generic script has no
  authoritative way to know which repo a path corresponds to; guessing
  would silently clone the wrong thing if the source ever moved. Fixed by
  having `tools/bootstrap.sh` only pull-if-present and clearly report
  "not checked out yet" otherwise, and documenting the real two-step fix
  in `AGENTS.md`'s "Build-environment gotchas": add the repo via
  `add_repo`, then clone it using the URL `AGENTS.md`'s own "Practice
  sources" section documents — a session-level action informed by this
  repo's own docs, not something a shell script should infer. Added the
  same one-time ask to `GETTING_STARTED.md`'s Claude Code onboarding steps
  for a human starting a session.

- [x] **Migrate this repo from BestPractice-only to Precedent's three-source
  model (the first real test of `alex137/BestPractice`'s
  `precedent-beta-v01` branch against a repo that already had BestPractice
  installed).** Decided 2026-09-02 → done, full record in
  [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md). Re-vendored `process/upstream/` from
  `precedent-beta-v01` (not `main` — a deliberate beta pin;
  `process/manifest.json` records both the commit and why). Retired
  `process/personal/` and `process/manifest_personal.json` (the vendored
  RepoPersonalPreferences copy) entirely: its 46 rules were already split,
  in an earlier session, into
  [precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers)
  (team) and
  [precedent-individual](https://github.com/themorgan/precedent-individual)
  (Morgan-specific facts) — this session wired this repo up as their first
  real consumer: added `precedent.json` (universal → `process/upstream/`,
  team → a sibling clone of precedent-team-maintainers), and
  `.claude/hooks/precedent-individual-bootstrap.sh` (+ `.claude/settings.json`
  wiring) so the individual source resolves automatically at session start
  without ever being named in this repo's own tracked config — the privacy
  boundary the three-source split exists to enforce. Relocated the two
  generic tools that were living under `process/personal/tools/`
  (`light_check.py`, `report_automation_issue.py`) to this repo's own
  `tools/`, since they were never personal-pack *content*; rewrote
  `light_check.py`'s pack-specific checks (which assumed a vendored
  `process/personal/` tree) into a `precedent.json` / `process/manifest.json`
  validity check instead. Rewrote `AGENTS.md`'s "Personal setup rules"
  section into "Practice sources (Precedent)": explains the three sources,
  points at `precedent_resolve.py --repo .` for the full merged set, and
  hand-curates the resident + most-used on-demand practices as a stopgap
  for a real gap this session found and did not build a fix for (see
  below). Retired the personal-pack sync workflow; paused the BestPractice
  sync workflow (its `checkin.py`-based commands assume default-branch
  tracking, which would either spam a false drift notice or, worse, try to
  merge `main`'s tree over this repo's deliberately beta-pinned vendored
  copy). Repointed the "pipeline stage 3" references in `README.md`,
  `GLOSSARY.md`, `MAP.md`, and `content/RULES_NOW_TESTING.md` from
  RepoPersonalPreferences to the two new repos; left `content/RANDOM_NOTES.md`'s
  own brainstorm-history mentions of RepoPersonalPreferences untouched
  (append-only raw material, accurate as of when written).

  **Judgment calls made:** (1) kept `process/upstream/` a real vendored
  copy rather than switching universal to a live sibling-clone reference
  too — a dependent repo needs the vendored copy for collaborators and
  environments without that sibling checked out, unlike Precedent's own
  self-referential `precedent.json` which can afford `path: "."`. (2) Did
  not attempt to build the missing cross-source `precedent_show`/`paths`/
  `gate` extractor this migration surfaced (team/individual slugs have no
  automatic Rule-text loading channel yet, only `precedent_resolve.py`
  resolves all three sources) — flagged upstream instead
  ([process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md), and `spec/MIGRATING_EXISTING_INSTALLS.md`
  in BestPractice itself) as a real gap this repo's own daily operation now
  depends on closing, rather than scope-creeping a new loader feature into
  a migration task. (3) Hand-curated a short resident + on-demand list in
  `AGENTS.md` rather than either reproducing all ~47 team/individual
  practices verbatim (exactly the duplication the split exists to avoid)
  or leaving nothing at all (a real regression from having the full pack's
  text inline) — a deliberate middle ground, not the resolver actually
  running automatically at session start. (4) Ran
  `python3 process/upstream/tools/precedent_resolve.py --repo .` for real
  against this repo's own `precedent.json` plus a user-level config
  pointing at the local precedent-individual checkout — see
  [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md) for the output — satisfying
  `spec/PRIVATE_SETS_BRIEF.md`'s own "done when" checklist item that this
  had never actually been run against the real two private sets from a
  real consumer repo.

- [x] **Take the pending personal-pack update (RepoPersonalPreferences @
  b5446156).** Decided 2026-08-29 → done. Ran
  `pack_sync.py update ../RepoPersonalPreferences --force` — the only
  local drift `update` found was this repo's own documented
  `PENDING_HEADING` sentence-case adaptation in
  `process/personal/tools/pack_sync.py` (expected; re-applied by hand
  right after, per the note already on that line). Mirrored
  `process/personal/README.md`,
  `process/personal/templates/AGENTS_ADDENDUM.md.template`, and
  `process/personal/tools/pack_sync.py` verbatim (plus two new files:
  `process/personal/tools/check_file_mention_links.py` and
  `process/personal/templates/claude-code/hooks/stop-file-links-check.sh.template`);
  re-wove [AGENTS.md](AGENTS.md)'s "Personal setup rules" section to
  match — replaced `generated-file-marker` with `derived-file-marker`,
  added its new `doc-recipe` sibling, inserted `rule-scope-ask` after
  `small-calls`, and `list-restraint` after `list-item-parity`, all in
  reading-order position. `process/manifest_personal.json` (retired with the pack it tracked)
  records the new upstream commit and the re-weave. Judgment call made:
  the template's `file-mention-links` bullet also grew a new
  "mechanically enforced" paragraph (a Claude Code Stop hook) in this
  same upstream update — left unwoven, since this repo never adopted
  `file-mention-links` at all in any earlier sync (a pre-existing gap,
  not something this update introduced) and installing it means more
  than re-weaving text: copying the hook script into `.claude/hooks/`
  and wiring `.claude/settings.json`. Tracked as its own item below
  rather than folded into this one.

- [ ] **Adopt `file-mention-links` (currently missing entirely from this
  repo).** [AGENTS.md](AGENTS.md) has never carried this pack rule —
  every mention of a repo file in chat/PR/commit text becomes a
  clickable absolute GitHub URL — even though
  [process/personal/README.md](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/file-mention-links.md)
  has documented it for a while and RepoPersonalPreferences now
  mechanically enforces it on itself via a Claude Code Stop hook
  (`process/personal/tools/check_file_mention_links.py`, wired through
  `process/personal/templates/claude-code/hooks/stop-file-links-check.sh.template`).
  Installing it here means: weave the rule's text into
  [AGENTS.md](AGENTS.md) in reading-order position (right after
  `rule-links`, its parent rule), copy the hook template into
  `.claude/hooks/stop-file-links-check.sh`, and wire it into
  `.claude/settings.json`'s `Stop` hooks. Found while re-weaving the
  2026-08-29 personal-pack sync above — deliberately not done in that
  same pass, since it's an install step, not a text mirror.

- [x] **Close the gap [`hire-for-drive`](content/COMPANY_BUILDING_RULES.md#hire-for-drive)
  left out of the "what humans are good at" consolidation, and check the
  rest of [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) for
  similar missing links.** Decided 2026-08-29 → done, doc. The earlier
  "Pull the scattered 'what humans are good at' lists into one document"
  entry above found three source spots for
  [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md) and missed a fourth:
  [`hire-for-drive`](content/COMPANY_BUILDING_RULES.md#hire-for-drive) itself
  names three of that list's own entries (drive/"Getting shit done,"
  relationships, taste) without linking there, the exact gap
  HUMANS_AT_OUR_BEST.md's own "Keeping this current" section asks each
  source list to close. Added the missing parenthetical there. Reviewed
  every other rule in the document for a similarly clear, already-argued
  case (a concept the rule names that some other document treats as the
  actual mechanism, not just an echo) — found one more:
  [`no-ai-voice`](content/COMPANY_BUILDING_RULES.md#no-ai-voice) argues for the
  style rule but never pointed at what enforces it, so it now also links
  [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md)
  and [`write-like-a-human`](content/RULES_NOW_TESTING.md#write-like-a-human).
  Judgment calls made: (1) left the many rules other documents already
  cite *from* (`ai-chat-as-intermediary`, `manager-of-agents`,
  `think-in-workflows`, and the rest) unchanged — that citation already
  runs the useful direction, and this document staying the
  heavily-cited-from essay rather than linking back out to every citing
  document is the existing, working pattern (see [TODO.md](TODO.md)'s
  own record below on why rule citations point *at* it); (2) didn't add
  a "Ghost"/"AI Chat"/"Manager of Agents" glossary entry or cross-link —
  none of the three is a canonical [GLOSSARY.md](GLOSSARY.md) term, and
  other documents already link back to this file's own definitions of
  them rather than the reverse.

- [x] **Give [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md)
  the same permanent slugs
  [`durable-list-anchors`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/durable-list-anchors.md)
  already requires of its sibling essay lists.** Decided 2026-08-29 →
  done, doc. Morgan noticed [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) item 1
  cited AI_GOVERNANCE_TO_COCREATE.md's "argue in the open" by quoted
  phrase instead of a slug link, and asked whether
  AI_GOVERNANCE_TO_COCREATE.md should get the same `<a id="slug"></a>`
  treatment as [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) —
  it was the one essay list
  [`durable-list-anchors`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/durable-list-anchors.md)'s
  own [AGENTS.md](AGENTS.md) bullets had left off their named list, an
  oversight rather than a deliberate exemption. All sixteen items across
  its eight thematic sections now carry a running number and a permanent
  slug, matching [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)'s
  format exactly. [AGENTS.md](AGENTS.md)'s two `durable-list-anchors`
  bullets now name it alongside the other four lists. Every
  quoted-phrase citation of one of its ideas elsewhere in the repo was
  converted to the slug form:
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) items 1 and 5,
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md)'s "Not yet ready" list,
  and two open items in this file. Also checked
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) itself for the
  same problem, per Morgan's follow-up question — every existing
  reference to it already uses the slug form, so nothing needed changing
  there. Companion change: RepoPersonalPreferences'
  [GLOSSARY.md](https://github.com/themorgan/RepoPersonalPreferences/blob/main/GLOSSARY.md)
  picked up a general **slug** entry, since its existing "rule slug"
  entry only covered the personal pack's own rules, not this pattern
  generalized to any repo's durable lists.
  **Judgment calls made:** (1) picked one slug per item from its own
  wording rather than asking Morgan to name all sixteen
  (`durable-state-default`, `automatic-rule-extraction`,
  `coldstart-test`, `active-resurfacing`, `push-back-as-config-switch`,
  `three-reflexes-in-system-prompt`, `argue-in-the-open`,
  `chat-is-primary-interface`, `non-uniform-confidence`,
  `automatic-workflow-detection`, `cost-awareness-situational`,
  `structural-ai-voice-check`, `ai-hunts-dark-processes`,
  `periodic-checkins-not-expiry`, `contradiction-scanning-recurring`,
  `provider-neutrality-hedge`); (2) reused the literal slug
  `argue-in-the-open` even though
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) already has its own
  anchor of that name for the trial-rule version of the same idea — the
  two are the same concept at two pipeline stages, and every citation's
  file name already disambiguates which one it points to; (3) numbered
  continuously 1–16 straight through the eight thematic headings rather
  than restarting per section, matching how
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)'s own four
  sections number straight through; (4) left the "Set aside this
  thread" closing note at the bottom of the file unslugged — it's
  explicitly marked as dropped material, not part of the list.

- [x] **Cite every durable numbered list by permanent slug, not position —
  [`durable-list-anchors`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/durable-list-anchors.md).**
  Decided 2026-08-29 → done, doc. Direct follow-on from the
  brainstorm-citations fix below: giving REASONS_WHY.md item 7's idea a
  home in [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) required a corollary
  bolted onto an existing item specifically to avoid renumbering every
  "item N" cross-reference a clean insertion would have forced — Morgan
  flagged that as the same problem the personal pack's own
  [`rule-links`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/rule-links.md) already solved
  for its own rules (cite by slug, never by number), generalized. New
  personal-pack rule (companion PR against RepoPersonalPreferences, its
  own TODO.md decision record); pulled into this repo via a personal-pack
  sync in the same session, along with the still-pending
  [`brainstorm-citations`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/brainstorm-citations.md)
  sync from the last one. Implemented here on the four lists it names:
  every rule in [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)
  (15), every item in [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) (7) and
  [REASONS_WHY.md](content/REASONS_WHY.md) (9), and every rule in
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) (7, already headed — still
  needed an explicit anchor, since GitHub's own auto-generated heading
  anchor bakes the position number in too) now carries a permanent
  `<a id="slug"></a>`. Every existing "rule N"/"item N" citation across
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md),
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md), [REASONS_WHY.md](content/REASONS_WHY.md),
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md),
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md),
  [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md), and [RANDOM_NOTES.md](content/RANDOM_NOTES.md)
  (its own numbered brainstorm list left unslugged — see judgment call
  below) was converted to the slug form in the same pass — this repo's
  own version of the "unlinked numbered-list citations" backlog item
  above, now closed by construction rather than by a separate linking
  pass. [AGENTS.md](AGENTS.md)'s "Doc references are links" convention
  rewritten to state the unified rule, superseding its old
  "anchored-headings vs. bare-file" split. **Judgment calls made:** (1)
  did not add anchors to [RANDOM_NOTES.md](content/RANDOM_NOTES.md)'s own numbered brainstorm
  list (points 1–5, with 3a/3b) — it's append-only by this repo's own
  convention, so position-drift risk is much lower than the essay lists,
  and [`brainstorm-citations`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/brainstorm-citations.md)
  already discourages a *formal* document from citing it by position
  going forward, reducing the practical need; did update the plain "rule
  N" mentions inside [RANDOM_NOTES.md](content/RANDOM_NOTES.md) itself that cite
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) to the new slug
  form, since those were already citation-convention violations
  independent of this rule. (2) Rejected the "§ + filename + slug"
  citation form Morgan floated when asking for this — kept "§" meaning
  exactly what it already means in this repo (BestPractice's own
  independently-numbered `practice N`), and used
  [`rule-links`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/rule-links.md)'s existing
  `` `slug` (file.md#slug) `` form as-is for this repo's own lists; see
  RepoPersonalPreferences' own TODO.md for the same call made there,
  where the rule itself was written. (3) Also brought this repo's
  vendored `process/personal/` tree current with RepoPersonalPreferences
  (commit `9793691d`, up from `b10c163a96d`) as part of the same session,
  since the new rule had to exist there before it could be applied here —
  re-wove `AGENTS.md` with both new bullets, and manually re-applied this
  repo's own `PENDING_HEADING` sentence-case adaptation in
  `process/personal/tools/pack_sync.py` after the mirror (a documented,
  recurring manual step — the automatic `update` command refused to
  overwrite it precisely because it's a real, intentional divergence, not
  drift).

- [x] **Pull the scattered "what humans are good at" lists into one
  document, and link the originals to it.** Decided 2026-08-29 → done,
  doc. Morgan noticed several documents each carry their own short list
  of what humans should focus on, and asked for one consolidated
  document plus a parenthetical link back to it from each existing list,
  leaving the existing text unchanged. Found three spots: [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md)
  item 4 (planning, taste, judgment), [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md)
  item 7 (judgment, relationships, instinct — reading a room, sensing the
  unspoken, pushing harder), and [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)
  rule 15 (judgment, taste, relationships, accountability, the human
  spark, and running a fleet of agent-driven processes). Landed as
  [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md), gathering all of it
  into one deduplicated list, each entry citing which source document
  and item/rule it came from. Each of the three spots above got one new
  parenthetical sentence pointing at the new document; no other wording
  in any of the three changed. Wired into [MAP.md](MAP.md),
  [README.md](README.md)'s "What's here," and [AGENTS.md](AGENTS.md)'s
  quick index. Judgment calls made: (1) treated [REASONS_WHY.md](content/REASONS_WHY.md)
  item 5 ("the deepest problems get caught by instinct, not a checklist")
  as out of scope — it makes one argument about instinct versus
  checklists, not a multi-item list of human strengths, so it didn't get
  a parenthetical link; (2) didn't add a new [GLOSSARY.md](GLOSSARY.md)
  entry — "Humans at our best" is a document title, not a term reused
  elsewhere in the repo's own vocabulary; (3) placed the new document
  right after [REASONS_WHY.md](content/REASONS_WHY.md) in each index, since it's
  the same kind of small companion reference rather than a top-level
  essay; (4) added a "Keeping this current" note to the new document
  itself, so a future new list of the same kind knows to fold in here
  rather than start a fourth copy.

- [x] **Stop citing a specific point inside [RANDOM_NOTES.md](content/RANDOM_NOTES.md) (the
  brainstorm) as justification from a formal doc — cite the promoted
  formal-doc treatment instead.** Decided 2026-08-29 → done, doc. Morgan
  flagged [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md)'s
  "automatic rule extraction" bullet citing "IDEAS.md's 3a" — an unvetted
  brainstorm entry doesn't earn the weight of backing a claim in a formal
  document. Re-pointed it at [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) item 5
  and [REASONS_WHY.md](content/REASONS_WHY.md) item 2, which already state the same
  idea formally. Fixed the same pattern everywhere else it showed up:
  OUR_PHILOSOPHY.md item 6's own "(IDEAS.md's rule extraction)" now points
  at its own item 5; REASONS_WHY.md item 2's "(IDEAS.md's automatic
  extraction)" now points at OUR_PHILOSOPHY.md item 5. REASONS_WHY.md item 7
  (working in a second language) had no formal-doc home yet for its
  IDEAS.md citation, so folded a short corollary into OUR_PHILOSOPHY.md item
  2 ("context is capital" extends to language) and re-pointed the citation
  there. The general rule this establishes — a formal doc cites another
  formal doc, never a specific brainstorm entry; add the idea to a formal
  doc first, then link — is now a new rule in
  [the personal pack](https://github.com/themorgan/RepoPersonalPreferences/blob/main/process/personal/README.md)
  (slug `brainstorm-citations`; lands here on the next personal-pack sync),
  so this gets caught going forward rather than needing another sweep
  later. Judgment call: picked OUR_PHILOSOPHY.md item
  2 (context is capital) as the language idea's new home, since "capturing
  real thinking instead of a diminished version" is the same logic the item
  already argues, rather than opening it as its own numbered core
  philosophy (which would force renumbering every "item N" cross-reference
  that depends on the current seven).

- [x] **Flip the pre-rename VoiceGuidelinesToSoundHuman URLs to
  SoundHuman.** Done 2026-08-29 → doc. The rename landed on GitHub
  2026-08-27; every functional link/URL/repo-name reference across this
  repo (`process/manifest_voice.json`'s `upstream.repo`,
  `.github/workflows/voice-guidelines-sync.yml`'s header comment,
  `process/voice/tools/voice_sync.py`'s docstring, and the SoundHuman
  links in [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md), [MAP.md](MAP.md),
  [GLOSSARY.md](GLOSSARY.md), [README.md](README.md),
  [GETTING_STARTED.md](GETTING_STARTED.md), [AGENTS.md](AGENTS.md), and
  this file) now point at `themorgan/SoundHuman`. Left untouched, on
  purpose: the `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN` secret name (kept
  permanently, per its own decision record above) and every note that
  narrates the rename event itself (`process/manifest_voice.json`'s and
  `process/manifest.json`'s own `_note`/notes fields, and this repo's
  workflow-comment history) — rewriting "renamed X -> Y" to "renamed Y ->
  Y" would make those sentences nonsensical.

- [x] **Add a theory-level intro pair: what this is and why it's worth
  doing, deeper than "co-create as partners."** Decided 2026-08-28 → done,
  doc. Morgan asked for two documents: one naming and explaining the
  handful of underlying philosophies this repo's essays assume (not a
  defense, an explanation), and one listing the less obvious benefits —
  not generic "better results" or "collaboration is better." Landed as
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) (seven named ideas, current
  titles: if it isn't written down it doesn't exist, context is capital
  and hours are not, quality comes from disagreement not compliance,
  judgment is scarce and production is not, processes should be intensely
  visible not locked in one person's brain, records should be checked
  against reality not just against themselves, and direction must be
  continuous not a one-time handoff) and [REASONS_WHY.md](content/REASONS_WHY.md) (seven subtler benefits: cheap early
  failure, killing ideas losing its social cost, documentation as a
  byproduct, continuous depersonalized evaluation, institutional memory
  outliving any one person, judgment work becoming the promotion path, and
  drift caught before a customer does). Both cross-link each other and
  cite back to specific rules in
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md),
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md), and
  [RANDOM_NOTES.md](content/RANDOM_NOTES.md) rather than restating them. Wired into
  [MAP.md](MAP.md), [README.md](README.md), [AGENTS.md](AGENTS.md)'s quick
  index, and [GETTING_STARTED.md](GETTING_STARTED.md) as the theory-level
  entry point for a newcomer. Judgment calls made: (1) used Morgan's
  suggested filenames verbatim rather than inventing alternatives; (2)
  picked seven items per document rather than a strict "couple" — enough
  to cover the corpus without any one entry being superficial, which was
  the specific thing Morgan flagged as missing from "co-create as
  partners" alone; (3) didn't add new [GLOSSARY.md](GLOSSARY.md) entries —
  the seven names in each document are paragraph headers local to that
  document, not canonical vocabulary reused elsewhere in the repo; (4)
  linked both from every index file even though doc_lint's findability
  gate doesn't technically require it for a document with no generated
  numbers, since these are meant to be the first thing a newcomer reads.
  **Revised same day** — Morgan flagged item 7 (the pipeline's earned-trust
  point) as the weakest of the seven and asked to swap it for a different
  core idea: that people need to constantly instruct, guide, tweak, and
  fix an agent as it creates, not hand off a brief once and collect the
  result. Landed as the new item 7, "direction is continuous, not a single
  handoff." He also asked for "understanding the thinking behind the
  work" — usually the first thing lost when work changes hands — folded
  into the context paragraph (item 2) rather than made its own item, since
  it's a specific consequence of that same point rather than a separate
  idea. **Revised again same day** — Morgan's next note: most of the seven
  bolded titles read as too chatty and not strong enough, and gave one
  rewrite as the model to follow — "a process only one person can run is a
  process nobody can see" tightened to "processes should be intensely
  visible, not locked in one person's brain." Applied the same tightening
  to the rest: plainer subject-predicate claims instead of riddle-shaped
  reversals, matching the direct, punchy style
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)'s own bolded
  openers already use (its rule 4, "Co-create; don't delegate.", was the
  clearest precedent already in the repo). Two line-wrap artifacts left
  over from the previous edit pass (an orphaned word on its own line in
  items 2 and 5) were cleaned up in the same pass. **Revised again
  2026-08-28** — two content swaps plus a length pass. In
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md): item 4 ("judgment is scarce,
  production is not") became "humans should do what humans do best" —
  judgment, relationships, instinct, reading what's unspoken, pushing
  people when the moment calls for it, cited to rule 15 ("reserve the
  permanent hire for what's structurally human") instead of rules 7-8;
  item 7 dropped "direction must be continuous" for "people manage;
  agents execute" — plan and oversee like Nix defines a system rather than
  hand-running it, treating the model as an individual contributor
  (IC), cited to rule 14 ("give
  the agents a manager") instead of standing alone. All seven items were
  also cut to roughly half their prior length, titles and rule citations
  otherwise unchanged. In [REASONS_WHY.md](content/REASONS_WHY.md): item 2
  ("killing a bad version stops being a referendum on the person who made
  it") was dropped outright, and the rest renumbered 1-6. The old item 5
  (institutional memory survives a departure) became "the power of
  documentation is almost magical — nobody ever finds the time, so it's
  now a background part of the process agents do," with the
  departure-survives-knowledge point folded in as one example rather than
  the headline. The old item 6 (judgment work becomes more interesting,
  not less) became "the deepest problems get caught by instinct, not a
  checklist" — what a model's checks can't see (a felt-off answer, a
  disengaging teammate) versus what instinct built on experience catches.
  Judgment calls made: (1) picked rule 15 and rule 14 as the new
  citations for items 4 and 7 rather than leaving them uncited, since both
  rules match the new content more precisely than the ones they replaced;
  (2) kept each item's opening bold title short enough to match the
  tightened style from the prior revision, rather than let the halving
  pass produce a longer title to compensate for a shorter body; (3) left
  [REASONS_WHY.md](content/REASONS_WHY.md)'s own length alone — Morgan asked for
  the halving pass only on [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md).
  **Revised a third time 2026-08-28** — three changes to
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) and one to
  [REASONS_WHY.md](content/REASONS_WHY.md), all Morgan's. Philosophy gained a new
  item, "every decision carries the situation that produced it" (however
  small the call, the record says what specific case prompted it), placed
  third and cited to BestPractice practices 5 and 20, which already
  require exactly this — Morgan checked that understanding first and it
  held. The old item 6 (records checked against reality) was dropped as a
  standalone and folded into item 1 as one sentence, since it is a detail
  of what a full written record lets you do. "Humans should do what humans
  do best" moved from item 4 to last, so the order now runs: written
  record, context is capital, decisions carry their situation,
  disagreement over compliance, visible processes, people manage / agents
  execute, humans do what humans do best. In
  [REASONS_WHY.md](content/REASONS_WHY.md), item 3 ("how someone's doing stops
  being a once-a-year guess") was cut as confusing and weak, and replaced
  in place with the benefit side of the new philosophy item — attaching
  the situation to a decision heads off confusions nobody sees coming.
  Judgment calls made: (1) placed the new philosophy item third, directly
  after "context is capital," since it is that idea's operational form,
  rather than first as its criticality might suggest; (2) illustrated the
  new [REASONS_WHY.md](content/REASONS_WHY.md) item with this repo's own
  never-hand-merge-`process/upstream/` rule, per Morgan's "PR & merge"
  steer, rather than inventing an outside example; (3) renumbered the
  internal cross-reference in "people manage; agents execute" (item 3 →
  item 4) to follow the reorder.
  **Revised a fourth time 2026-08-28** — two more edits to
  [REASONS_WHY.md](content/REASONS_WHY.md), both Morgan's. Item 4's opening line
  ("the problem was never doubting that, it was finding the time") lost
  the middle clause, now reading "The power of documentation is almost
  magical — it was finding the time." Items 1 ("being wrong gets cheap
  while it's still small") and 6 ("drift gets caught before a customer
  does") were merged into one, keeping item 1's text as the surviving
  point and folding item 6's drift-detection content in as an example of
  the same underlying mechanism (catching a problem while it's still
  small) rather than a separate benefit — Morgan's own framing. The list
  is now five items, renumbered 1-5 (items 2-5 kept their existing
  numbers; only the old 6 was removed). Judgment calls made: (1) placed
  the folded-in drift example at the end of item 1's paragraph, after the
  existing citation to rule 4, rather than interleaving it mid-paragraph,
  so the original point stays intact and the example reads as an
  addition; (2) kept item 6's own citations (rule 13,
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) item 7) attached to the
  folded-in sentences rather than dropping them.
  **Revised a fifth time 2026-08-28** — one change to
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md), Morgan's. Item 4 ("quality comes
  from disagreement, not compliance") became "coworking with a model
  means arguing with it" — the headline moved off disagreement-produces-
  quality and onto the working relationship itself: don't instruct the
  model (typist) and don't just poll it for an opinion (oracle), argue
  with it and let it argue back until the exchange, not either side
  alone, settles the question. Disagreement's payoff for quality stays in
  the paragraph as one reason among several, not the whole point. The
  rule 4 and [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md)
  "argue in the open" citations carried over unchanged. Judgment calls
  made: (1) kept the paragraph close to its prior length rather than
  cutting further, since the typist/oracle contrast needed the room to
  land; (2) kept the plain subject-predicate title style from the third
  revision's pass rather than reintroducing a riddle-shaped reversal.
  **Revised a sixth time 2026-08-28** — one typo fix to
  [REASONS_WHY.md](content/REASONS_WHY.md), Morgan's. Item 4's title had been left
  a broken fragment by the fourth revision's trim — "The power of
  documentation is almost magical — it was finding the time," missing the
  clause that made "it was finding the time" make sense on its own. Fixed
  to "The power of documentation is almost magical — since no one finds
  the time, AI will," which states the item's actual point (the record
  gets made because the agents make it a background part of the work, not
  because anyone finds an hour for it) directly in the title instead of
  leaving it implicit in the body.
  **Revised a seventh time 2026-08-28** — a new item added to
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md), not a rewrite of an existing
  one. Morgan described a four-step working loop — a spark (an idea, new
  data, an incoming request, a changed system message), argued out with
  an assistant that has this repo attached, mostly (not entirely) in the
  open on GitHub, settling into a rule with its case attached that
  everyone can see — and asked where it should live and what he thought
  of the framing. Landed as new item 8, "the same four steps repeat every
  time, in order," placed last as a synthesis rather than inserted
  earlier and forcing a renumber, citing back to items 1, 3, 4, 5 instead
  of restating them, and cross-linking [README.md](README.md)'s
  three-stage pipeline as the same shape seen from the document side —
  which picked up one sentence pointing back. Judgment calls made: (1)
  put it in [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) rather than a new
  standalone document — the framing is theory-register ("the new way of
  working we envision"), and a fourth top-level intro doc would mostly
  duplicate this file and [README.md](README.md)'s pipeline section
  rather than add anything a cross-reference couldn't; (2) genericized
  "Claude/LLM" to "an assistant," matching this repo's platform-neutral
  terminology ([GETTING_STARTED.md](GETTING_STARTED.md) covers Claude,
  Codex, ChatGPT, and Gemini as first-class); (3) no new
  [GLOSSARY.md](GLOSSARY.md) entry, following this file's own precedent
  above — the eight names in [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) are
  paragraph headers local to that document, not canonical vocabulary
  reused elsewhere in the repo.
  **Revised an eighth time 2026-08-28** — Morgan's correction to the
  seventh revision, same day. Item 8 read fine on its own but he judged
  the four steps as a preface, not a peer of the seven ideas — an easier,
  clearer way to bring several of them together before the reader hits
  the list, not an eighth idea alongside it. Item 8 removed; the same
  four steps now open a new "The working loop" section right after the
  intro paragraph and before item 1, restored to Morgan's original
  numbered-step shape (plain `1.`-`4.` list, not the bold-title paragraph
  style the seven ideas use) rather than folded into that style. Internal
  references swapped from "item 4"/"item 5" (ambiguous once the loop has
  its own steps 1-4) to "item 4 below"/"item 5 below." [README.md](README.md)'s
  cross-link updated from "item 8" to the section name. Judgment calls
  made: (1) kept the loop unheaded as its own numbered list rather than
  bold-paragraph style like items 1-7, since Morgan's own complaint was
  that the paragraph style buried the steps; (2) didn't add a matching
  header above the seven ideas for parallelism — Morgan asked only for
  the new section, and adding one to the existing list wasn't part of
  that ask.
  **Revised a ninth time 2026-08-28** — three more tweaks to "The working
  loop" section, all Morgan's, same day. A new step inserted between the
  old steps 3 and 4: the AI Assistant produces all the output, the human
  only guides it (item 6 below, "people manage; agents execute") — the
  list is now five steps, not four. "Assistant" became "AI Assistant"
  throughout the section, to read unambiguously as the software rather
  than a human role. The closing paragraph that mapped the steps onto
  [README.md](README.md)'s three-stage pipeline was dropped — Morgan
  called it confusing and out of place for what this section is, a
  plain-language lead-in to the seven ideas — and replaced with one
  transition sentence, "Here is a boildown of the principles guiding
  us:". Judgment calls made: (1) inserted the new step as position 4
  (between GitHub and the written-rule step) exactly where Morgan asked,
  rather than at the end, even though it means the written-rule step's
  citations ("items 1 and 3 below") now sit one position later in the
  list; (2) kept "AI Assistant" capitalized as given rather than
  lowercasing to match this repo's usual "the assistant" style
  elsewhere (GETTING_STARTED.md, README.md) — Morgan's ask was
  specifically to make this section read unambiguously, and scoped it
  to "assistant," not the rest of the repo's terminology; (3) used
  Morgan's transition sentence verbatim, including its wording, rather
  than silently correcting what may be a typo ("boildown") — flagged it
  back to him instead of guessing.
  **Revised a tenth time 2026-08-28** — four more changes to
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md), Morgan's, same day. Step 3 of
  the working loop (arguing on GitHub) was the one step citing no idea
  below, even though it's the mechanism that makes item 2 ("context is
  capital") real — added that citation alongside the existing one.
  Reordered the seven ideas to match the order the loop's steps first
  cite them (old 4, 2, 5, 6, 1, 3, with 7 — never cited by the loop —
  kept last), renumbering every citation in the loop and the one
  internal cross-reference inside the new item 4 to match; also
  repointed [REASONS_WHY.md](content/REASONS_WHY.md)'s citation of the old item
  3 to the new item 6. Item 2's opening line, "Context is capital, hours
  are not," lost its second half — Morgan didn't want the document read
  as saying hours don't matter. Every "(rule N)" citation naming a
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) rule (as
  against a BestPractice practice or a
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) rule, both cited
  elsewhere in the same document) became a link to that file — Morgan
  had been searching this document itself for rules cited by number and
  not finding them. Judgment calls made: (1) Morgan asked for a new
  header reading "The 5 Core Philosophies" after the loop; the list
  holds seven ideas, not five, so titled it "The 7 Core Philosophies"
  instead of shipping a header that contradicts its own list, and
  flagged the correction back to him; (2) the reorder was posed as an
  open question, not an instruction — did it anyway, since it makes the
  loop's citations read in ascending order and the only cost outside
  this file was the one stale reference in
  [REASONS_WHY.md](content/REASONS_WHY.md), fixed above; (3) linked every rule
  citation to the bare file rather than a specific anchor —
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)'s fifteen
  rules are bold paragraph text, not headings, so GitHub can't generate
  a per-rule anchor without restructuring that file, which wasn't asked
  for.
  **Revised an eleventh time 2026-08-28** — one more change to
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md), Morgan's, same day. Step 4 of
  the working loop ("the AI Assistant produces all the output; you only
  guide it") cited only item 4 ("people manage; agents execute"); Morgan
  pointed out it's equally item 7 ("humans should do what humans do
  best") — the AI producing the output is exactly the part humans don't
  do, which is what makes room for the part they do. Added that second
  citation, which means every one of the seven ideas is now cited by at
  least one step of the loop.
  **Revised a twelfth time 2026-08-28** — three more changes, Morgan's,
  same day. First, a new [AGENTS.md](AGENTS.md) convention: every
  numbered-list citation elsewhere in the repo (a rule, a practice, an
  item) is always a link to its source — anchored to the specific entry
  when the source list uses real headings
  ([RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md),
  [process/upstream/PRACTICES.md](process/upstream/PRACTICES.md)), or to
  the bare file when it doesn't
  ([COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md)'s bold
  paragraphs). Brought into compliance immediately:
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) item 6's `(practices 5, 20)`,
  and every practice citation already inside
  [AGENTS.md](AGENTS.md) itself (nine of them, plus its one
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) item citation). Second, a
  new sixth [REASONS_WHY.md](content/REASONS_WHY.md) reason: AI is superhuman at
  turning an incident into a rule, checking it against everything else on
  the list, and renumbering every cross-reference when an entry moves —
  upkeep a person defers the moment it gets tedious but a model runs on
  every pass, at any scale, without leaving a stale reference behind.
  Third, all five existing [REASONS_WHY.md](content/REASONS_WHY.md) reasons
  (plus the new sixth) shortened to roughly half their prior length,
  matching [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md)'s own brevity — kept
  every citation and the core claim, cut the worked examples and
  restatement. Judgment calls made: (1) didn't sweep the rest of the
  repo's unlinked numbered-list citations
  ([RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md)'s own self-references,
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md)'s and
  [RANDOM_NOTES.md](content/RANDOM_NOTES.md)'s `rule N` mentions) into this same change — logged
  as its own open item below instead, since it touches several documents
  Morgan didn't name; (2) picked word-count targets of roughly 45-55% of
  each reason's original length rather than a strict half, since a couple
  of the originals didn't compress cleanly to exactly 50% without cutting
  a citation; (3) for the new sixth reason, cited this very thread's own
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) renumbering work as the concrete
  instance, rather than a hypothetical example.
- [x] **Rename OPERATING_RULES.md, FIFTEEN_RULES.md, and COCREATION_DESIGN.md
  — all three names read as unclear about what they cover.** Decided
  2026-08-27 → done, doc. Morgan's complaint: `OPERATING_RULES` implies
  something more like company operating procedures than "what's currently
  on trial"; `FIFTEEN_RULES` doesn't say rules for what; `COCREATION_DESIGN`
  keeps the right word (co-creation) but leaves DESIGN ambiguous about
  which aspect it's designing. Renamed to
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md),
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md), and
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md) respectively,
  each file's title and opening paragraph rewritten (not just the filename)
  to state its role in the stage-1/stage-2 pair explicitly, cross-linking
  the other two by their new names. Every reference across
  [AGENTS.md](AGENTS.md), [GLOSSARY.md](GLOSSARY.md), [MAP.md](MAP.md),
  [README.md](README.md), [RANDOM_NOTES.md](content/RANDOM_NOTES.md), and this file updated to
  match, including the canonical term **the operating rules** →
  **the rules now testing** in [GLOSSARY.md](GLOSSARY.md) (kept in step with
  the file it names). Judgment calls made: (1) picked
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) for the middle document —
  Morgan's own suggestion (`STYLE_NOW_TESTING`) didn't fit content that
  isn't about style, so kept his "current state of what we're trying"
  framing and swapped in the actual subject; (2) used his suggested
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) and
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md) verbatim for
  the other two; (3) while
  rewriting [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md)'s opening
  paragraph, fixed a pre-existing error found in the same sentence — it
  called itself "the third stage" of the pipeline, but
  [README.md](README.md) and [MAP.md](MAP.md) both established it as stage
  2 (RepoPersonalPreferences is stage 3); (4) left the historical
  2026-08-27 decision entry below (the one that originally landed
  `OPERATING_RULES.md`) narrating the old name for its own reasoning, with
  its links repointed to the new filename and a bracketed note so the
  record stays readable rather than rewritten.
- [x] **Vendor the voice guidelines in, with their own weekly sync and
  session-start check.** Decided 2026-08-28 → done, doc. A prior session
  had flagged item 5 of [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) ("a
  structural check for AI-sounding prose") as reinventing something that
  might already exist. It did: a real repo,
  [SoundHuman](https://github.com/themorgan/SoundHuman),
  already maintains [HUMAN_VOICE_RULES.md](https://github.com/themorgan/SoundHuman/blob/main/HUMAN_VOICE_RULES.md), in production use by
  VoiceDefinitionMorgan, VoiceDefinitionCelia, and the WriteLike app.
  Morgan asked for it in this repo's usual vendoring shape: pulled in and
  vendored at [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md)
  (tracked in [process/manifest_voice.json](process/manifest_voice.json)),
  a weekly sync
  ([.github/workflows/voice-guidelines-sync.yml](.github/workflows/voice-guidelines-sync.yml),
  [voice_sync.py](process/voice/tools/voice_sync.py)) mirroring the
  personal-pack sync's shape, and a third session-start freshness line in
  [tools/bootstrap.sh](tools/bootstrap.sh). [AGENTS.md](AGENTS.md) gained a
  new "Voice" section making it the actual standard for everything a
  session writes here — chat replies included, not only committed
  documents — and [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) item 5 now
  points at it instead of the ad hoc fingerprint list it started with.
  [MAP.md](MAP.md), [GLOSSARY.md](GLOSSARY.md) (new terms: **the voice
  guidelines**, **the voice guidelines sync**), [README.md](README.md), and
  [GETTING_STARTED.md](GETTING_STARTED.md) (the new
  `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN` secret disclosure) all updated to
  match. Judgment calls made: (1) reused
  `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN` as the secret name rather than
  inventing a new one, since SoundHuman's own docs already
  establish that name for its other consumers (VoiceDefinitionMorgan,
  VoiceDefinitionCelia) — one less name for that ecosystem to track; (2)
  tracked only [HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) itself in
  [process/manifest_voice.json](process/manifest_voice.json), not the new
  workflow file — the workflow is this repo's own infrastructure, not
  something vendored from anywhere upstream, so a manifest entry for it
  would misrepresent what "vendored" means here; (3) kept
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) item 5 at *Trial* rather than
  jumping to *Promoted*, since this is the ruleset's first use on general
  assistant output (chat replies, not just WriteLike's voice-pack
  rewrites) — a new use worth testing here before it becomes a
  RepoPersonalPreferences default, same pipeline discipline as everything
  else in this document; (4) left `WriteLike` (the separate rewriting-app
  repo, added to this session while confirming which repo was the actual
  rules source) unvendored — it's the wrong repo for this purpose, kept
  only for reference.
- [x] **Give this repo an explicit third stage — [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md)
  — between the brainstorm/essays and RepoPersonalPreferences.** Decided
  2026-08-27 → done, doc. A session recommending changes to
  RepoPersonalPreferences straight from this repo's ideas had skipped the
  step this repo exists to provide: trying an idea in real work before it
  becomes company-wide policy. Morgan's correction: (1) discover in
  [RANDOM_NOTES.md](content/RANDOM_NOTES.md) / the promoted essays, (2) try it for real in a new
  document, (3) only then port proven rules into RepoPersonalPreferences
  for rollout everywhere. Landed as
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) (new document, seeded with
  items 1-2 already promoted from a prior session, items 3-7 as trial
  rules pulled straight from [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md)
  and [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md), and a "not yet ready" section
  for ideas that need real infrastructure first — see the five new items
  above this one), a new "How this repo's ideas become company policy"
  section in [README.md](README.md), updated [MAP.md](MAP.md) and
  [GLOSSARY.md](GLOSSARY.md) (new terms: **the pipeline**, **the operating
  rules** [renamed **the rules now testing** in the 2026-08-27 rename below],
  **promote**/**promotion**), [AGENTS.md](AGENTS.md)'s quick
  index, and a new dated entry plus an updated open-question note in
  [RANDOM_NOTES.md](content/RANDOM_NOTES.md). Judgment calls made: (1) named it
  `OPERATING_RULES.md` (since renamed to
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md), see below) rather than
  something like `COMPANY_RULES.md` —
  "operating" reads as closer to "what's actually run on" than "company,"
  which could be misread as employee-facing policy; (2) picked five of
  AI_GOVERNANCE_TO_COCREATE.md's ideas as concrete enough to state as Trial rules
  now (argue in the open, the two reflexes, the AI-voice check, the
  dark-process self-audit, contradiction-scanning) and left the rest —
  active resurfacing, workflow-candidate mining, situational cost
  inference, the coldstart test, deeper normie-engagement mechanisms — as
  open TODO items instead of rules, on the view that they need real
  infrastructure or more testing before they're checkable the way a Trial
  rule should be; (3) explicitly did not touch RepoPersonalPreferences in
  this pass, since promotion only happens once a Trial rule proves itself
  here, not on day one.
- [x] **Force deeper AI engagement, or just permit it?** Decided
  2026-08-26 → done, for the specific form Morgan asked for: **push-back
  mode**, landed as
  [`push-back` of the personal pack](https://github.com/themorgan/RepoPersonalPreferences/blob/main/process/personal/README.md#push-back)
  ([PR #24](https://github.com/themorgan/RepoPersonalPreferences/pull/24)).
  On writing-and-thinking work only (never code/technical work): argue a
  genuine counter-case before building on a stated stance, and flag a
  serious unresolved disagreement before calling a piece done — not a
  quota, never manufactured, and explicitly distinct from a judgment call
  or a clarifying question. This resolves the narrower "should Claude push
  back harder" question from the original brainstorm; the broader
  "normie"-employee-adoption question (visible rule-extraction, proactive
  resurfacing of rules) is still open — see [RANDOM_NOTES.md](content/RANDOM_NOTES.md)
  §"Why BestPractice specifically works" → "Open question" for the rest of
  it. Once the personal-pack sync pulls
  [`push-back`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/push-back.md) into this repo's own
  `process/personal/` and re-weaves `AGENTS.md`, this repo picks up
  push-back mode automatically.
- [x] **Halve [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md)'s and
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md)'s numbered items, and cut
  the op-ed voice out of them.** Decided 2026-08-28 → done, doc. Morgan's
  complaint: the items ran long and leaned on scene-setting rhetoric this
  repo's own voice guidelines already ban — his example, item 2's opener
  "For most of business history the scarce input was time — pay enough
  hours and the work got done," a historical windup before the actual
  point. Rewrote all seven [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) items
  and all seven [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) rules,
  bringing the combined word count of the items themselves from 1,315
  words to 708 (≈54%) — titles, status tags, and rule/practice citations
  kept, narrative padding and restated context cut. Item 4 of
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) (from the prior session's
  rewrite, "coworking with a model means arguing with it") got the same
  pass. Judgment calls made: (1) didn't touch either document's intro
  paragraphs, status key, "Not yet ready," or "Promotion" sections —
  Morgan said "items," and those aren't numbered items, though the
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) intro has the same
  "not settled policy, not a finished essay, but X" triplet shape and is
  worth a look if he wants it too; (2) didn't edit
  [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md)
  itself — it's vendored from SoundHuman and can't be hand-merged (this
  file's own merge runbook), and HUMAN_VOICE_RULES.md already bans exactly
  what Morgan flagged (§1 Selectivity, §5.1's banned "not X, it's Y"
  contrast, HUMAN_VOICE_RULES.md's §12 "does the opening state the point,
  or clear its throat first?"); the
  gap was this repo not yet applying that rule rigorously to long-form
  essay content, not a hole in the rule itself; (3) dropped rule 1's
  "Origin: this repo, 2026-08-26" line and rule 5's superseded-draft
  history from [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) — that
  provenance still lives in this file's own history, and
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) is the current-state
  checklist, not the log; (4) cut rule 6's "email Morgan to change this
  config" example and a few secondary citations for length, keeping the
  rule-number cite on every item.
- [x] **Write [THREE_PILLARS.md](content/THREE_PILLARS.md)
  and add a new [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) point for
  group collaboration.** Decided 2026-09-01 → done, doc. Promoted
  [RANDOM_NOTES.md](content/RANDOM_NOTES.md)'s three-part uniqueness thesis into a
  one-page pitch, linked from
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md),
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md), and
  [REASONS_WHY.md](content/REASONS_WHY.md). Morgan's first-round correction: the
  formula's first bullet isn't
  [`co-create-dont-delegate`](content/COMPANY_BUILDING_RULES.md#co-create-dont-delegate)
  restated (one person co-creating with the model) — the actual claim is
  that this repo targets *groups* of people collaborating with each other,
  which the crowded field of individual-AI-productivity advice doesn't
  cover. That didn't have a home anywhere yet, so it became a new
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) point,
  [`groups-not-individuals`](content/OUR_PHILOSOPHY.md#groups-not-individuals),
  in a new "Groups, not individuals" section ahead of "Working with the
  model" — which meant renumbering that document's other eight items by
  one, same as the precedent above. The formula's first bullet now cites
  the new point instead of `co-create-dont-delegate`.
- [x] **Move the main content documents into `docs/`, add uniform
  "See also" sections, drop the `[YEAR]` placeholder, and move
  [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md)'s upkeep rule into a
  doc-recipe.** Decided 2026-09-01 → done, doc. Five separate asks in one
  round:

  (1) [THREE_PILLARS.md](content/THREE_PILLARS.md)'s
  second bullet is now "Protocols Generated Automatically (Then Reviewed
  By Humans)."

  (2) [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md) rule 14
  ("protect human-only zones") rewritten short, dropping the unfilled
  `[YEAR]` bracket entirely rather than filling it in — the "Open
  placeholders" footer that tracked it is gone, and the TODO.md entry
  above that recorded it as an intentional placeholder is marked
  superseded rather than rewritten.

  (3) [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md)'s "Keeping this
  current" section (the instruction to fold in new "what humans are good
  at" items when they show up elsewhere) moved out of the document body
  into [content/doc-recipes/HUMANS_AT_OUR_BEST.recipe.md](content/doc-recipes/HUMANS_AT_OUR_BEST.recipe.md) — a standing rule
  about the file, not part of its content, which is exactly what
  [`doc-recipe`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/doc-recipe.md) is for.

  (4) [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md)'s `groups-not-individuals`
  point cut to roughly 40% of its prior length; item 8's "not hidden
  inside Claude" changed to "not hidden inside an AI Assistant"
  (provider-neutral wording, matching
  [`llm-neutral`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/llm-neutral.md)'s spirit even
  though that rule is scoped to LLM-*integrations*, not repo prose), and
  its paragraph also cut to roughly 40%.

  (5) Every main content document
  ([OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md),
  [REASONS_WHY.md](content/REASONS_WHY.md),
  [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md),
  [RANDOM_NOTES.md](content/RANDOM_NOTES.md),
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md),
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md),
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md),
  [THREE_PILLARS.md](content/THREE_PILLARS.md)) now
  ends with a uniform "## See also" section listing the other seven,
  replacing whatever one-off closing pointer (or none) it had before.
  Then all eight moved into a new `docs/` subdirectory, so this repo's
  actual argument stops being mixed in at root alongside the technical
  documents about running the repo itself (`AGENTS.md`, `MAP.md`,
  `TODO.md`, `GLOSSARY.md`, `GETTING_STARTED.md`, `README.md`) — every
  link repo-wide updated to match, including this file's own history.

  Judgment calls made: (1) which documents count as "main content" for
  both the `docs/` move and the "See also" lists — the eight above, based
  on this pack's own existing
  [`content-subdirs`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/content-subdirs.md)
  recommendation and [README.md](README.md)'s pre-existing "What's here"
  split; `GLOSSARY.md` stayed at root as a cross-cutting reference used by
  both halves of the repo, not itself an essay. **Confirmed 2026-09-01:**
  Morgan says this one isn't a judgment call at all — `GLOSSARY.md` is a
  primary BestPractice-mandated living document, and the reason turns out
  to be load-bearing, not stylistic:
  [process/upstream/tools/doc_lint.py](process/upstream/tools/doc_lint.py)
  hardcodes `GLOSSARY_PATH = ROOT / 'GLOSSARY.md'` for its ungapped-acronym
  check, and [process/manifest.json](process/manifest.json)'s `local_path`
  for the glossary template is `GLOSSARY.md` at root. Moving it would have
  silently disabled that check repo-wide rather than erroring. Recorded as
  [content/doc-recipes/GLOSSARY.recipe.md](content/doc-recipes/GLOSSARY.recipe.md)
  so this doesn't get re-litigated as a tidiness call next time root looks
  cluttered; (2) gave
  [THREE_PILLARS.md](content/THREE_PILLARS.md)'s own
  "See also" bare links with no descriptions, unlike the other seven,
  since a full description list would work against that document's own
  point of being very short; (3) `TODO.md`'s own historical entries got
  their links repointed to `docs/` (a broken link is a broken link
  regardless of when the prose was written) without touching any of the
  historical wording itself; (4) added
  [THREE_PILLARS.md](content/THREE_PILLARS.md) to
  [README.md](README.md)'s "What's here" list, missing since that
  document was created — an oversight from the earlier round, not a new
  ask this round.
- [x] **Rename `docs/` to `content/`.** Decided 2026-09-02 → done, same
  day. Morgan's reasoning: "docs" is ambiguous — internal or external,
  meta-documentation about running the repo or the repo's actual
  substance — where "content" names what the directory holds (this
  repo's main content documents) unambiguously. All eight content
  documents and [content/doc-recipes/HUMANS_AT_OUR_BEST.recipe.md](content/doc-recipes/HUMANS_AT_OUR_BEST.recipe.md)
  moved via `git mv`; every repo-wide link updated to match
  ([AGENTS.md](AGENTS.md), [MAP.md](MAP.md), [GLOSSARY.md](GLOSSARY.md),
  [README.md](README.md), [GETTING_STARTED.md](GETTING_STARTED.md), and
  this file's current-state links). This file's own historical entry
  above (the earlier root-→`docs/` move) kept its prose describing
  `docs/` by that name — it's a record of what that move actually did —
  while its own links to the moved files were repointed to `content/`
  to keep resolving, same precedent as that entry's own judgment call
  (3).
- [x] **Rename `THE_REVOLUTIONARY_FORMULA.md` to `THREE_PILLARS.md`.**
  Decided 2026-09-05 → done, same day. Morgan's ask: the old name read as
  a sales pitch rather than a description of what the document actually
  is — three named ideas. File renamed via `git mv`, title changed from
  "The revolutionary formula" to "Three pillars" (only the title, per the
  file's own brevity — the body already reads fine either way), file
  header version bumped. Every reference updated to match:
  [AGENTS.md](AGENTS.md), [GLOSSARY.md](GLOSSARY.md) (canonical term
  **the revolutionary formula** → **the three pillars**), [MAP.md](MAP.md),
  [README.md](README.md), and this file's own historical entries above
  (links repointed, same precedent as the `docs/`→`content/` move above —
  a broken link is a broken link regardless of when the prose was
  written), plus every "See also" cross-link in
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md),
  [REASONS_WHY.md](content/REASONS_WHY.md),
  [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md),
  [RANDOM_NOTES.md](content/RANDOM_NOTES.md),
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md),
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md), and
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md). Same round, Morgan
  also asked to standardize content docs on `_` rather than a mix of `_`
  and `-` between words in filenames — checked every filename under
  `content/` plus the root-level content-adjacent docs
  ([AGENTS.md](AGENTS.md), [GLOSSARY.md](GLOSSARY.md), [MAP.md](MAP.md),
  [README.md](README.md), [TODO.md](TODO.md),
  [GETTING_STARTED.md](GETTING_STARTED.md)): all already use `_` between
  words. The only `-` in this area is `content/doc-recipes/` (and root
  `doc-recipes/`), which stays as-is — that directory name is fixed by the
  [`doc-recipe`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/doc-recipe.md)
  practice itself (`doc-recipes/<name>.recipe.md`), not a naming choice
  local to this repo, and durable-list anchor slugs (e.g.
  `groups-not-individuals`), which are hyphenated by the
  [`durable-list-anchors`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/durable-list-anchors.md)
  practice's own convention. Nothing else needed changing.
- [x] **Fix `python3 tools/precedent_gate.py merge|push|reply|review` —
  every invocation failed with `FileNotFoundError: tools/routing_scope.json`.**
  Decided 2026-09-05 → done, same day. Found while running the merge-time
  gate check for the rename above. Root cause: `tools/precedent_gate.py`
  and `tools/split_practices.py` were vendored into this repo's own
  `tools/` (byte-identical to `process/upstream/tools/`) so AGENTS.md's
  standing instruction to run the gate at named moments actually works —
  but `tools/routing_scope.json`, the data file `precedent_gate.py`
  hardcodes as `ROOT / 'tools' / 'routing_scope.json'`
  (`tools/precedent_gate.py` line 46), was never copied alongside them; only
  the `process/upstream/tools/routing_scope.json` copy existed.
  [tools/precedent_sync_views.py](tools/precedent_sync_views.py)'s own
  docstring confirms this class of file (the engine scripts, listed by
  name) has to already be sitting together in `tools/` — it isn't something
  a sync regenerates — so this was a real, incomplete vendoring gap, not a
  deliberate omission. Fixed by copying
  `process/upstream/tools/routing_scope.json` to `tools/routing_scope.json`
  (same as the existing `precedent_gate.py`/`split_practices.py` copies).
  Verified: all four gates (`merge`, `push`, `reply`, `review`) now resolve
  their practices correctly, confirmed via `--list` and by invoking each one
  directly. No manifest entry added — this file isn't part of the tracked
  BestPractice check-in list (`process/manifest.json`), same as its two
  sibling engine scripts.
