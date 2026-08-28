<!-- Last updated: 2026-08-28 09:30:00 (Buenos Aires) by Morgan F, to version 6 -->

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

## Recurring

- [ ] **BestPractice check-in:** review `diverged` entries in
  [process/manifest.json](process/manifest.json) and the vendored tree's
  accumulated changes; propose upstream per
  [process/upstream/INSTALL.md](process/upstream/INSTALL.md) §4 (scrub audit
  first).

## Analyses (agent-doable)

- [x] **Populate [IDEAS.md](IDEAS.md) with real content.** Done
  2026-08-26 → [IDEAS.md](IDEAS.md) now holds the first real brainstorm
  batch, plus [FIFTEEN_RULES.md](FIFTEEN_RULES.md) promoted out as its own
  document. The three original placeholder sections (prompts, workflows,
  incidents) are still empty and open for the next batch.
- [ ] **Fill in the two open brackets in [FIFTEEN_RULES.md](FIFTEEN_RULES.md).**
  Rule 8 wants the name of the sharpest editor Morgan has worked with; rule
  14 wants a real year for "the way you'd have read it in [YEAR]." Both are
  intentionally left as placeholders rather than filled with something
  generic — replace them only when a real specific comes to mind.
- [ ] **Look for contradictions across [IDEAS.md](IDEAS.md) entries**, per
  the meta-note at the bottom of that file (e.g. rule 9's "build five, kill
  four" against rule 5's "don't systematize a one-off") — worth a
  dedicated pass once there's enough material for real tensions to show up.
  Now also item 7 of [OPERATING_RULES.md](OPERATING_RULES.md) — this line
  and that item are the same recurring job, described from two sides.
- [ ] **Design real infrastructure for active/proactive resurfacing** —
  "you decided X six weeks ago, unprompted" (COCREATION_DESIGN.md's
  "Memory & context", [OPERATING_RULES.md](OPERATING_RULES.md)'s "Not yet
  ready" list). Needs something that mines and ranks prior decisions rather
  than only answering when asked; no design proposed yet. **analysis.**
- [ ] **Design automatic workflow-candidate detection** — mining
  commit/session history for a recurring task shape, instead of relying
  solely on [OPERATING_RULES.md](OPERATING_RULES.md) item 4's
  human-triggered reflex. **analysis.**
- [ ] **Work out situational, inferred cost-awareness** — COCREATION_DESIGN.md
  records that a fixed "surface spend per outcome" policy was already
  proposed and rejected; the open half is inferring *which* posture
  applies (explicit budget mention, project stage, stated intent) rather
  than applying one policy everywhere. Passive cost logging is the one
  piece already worth keeping regardless. **analysis.**
- [ ] **Formalize the coldstart test as a periodic check** — can a fresh
  session, given only the memory store, reconstruct the state of any live
  decision? Currently just a manual audit idea in
  [OPERATING_RULES.md](OPERATING_RULES.md); worth deciding whether it
  becomes a recurring item here (like the BestPractice check-in) or stays
  ad hoc. **decision.**

## Verify before external use

## Decisions (user's call)

- [x] **Vendor the voice guidelines in, with their own weekly sync and
  session-start check.** Decided 2026-08-28 → done, doc. A prior session
  had flagged item 5 of [OPERATING_RULES.md](OPERATING_RULES.md) ("a
  structural check for AI-sounding prose") as reinventing something that
  might already exist. It did: a real repo,
  [VoiceGuidelinesToSoundHuman](https://github.com/themorgan/VoiceGuidelinesToSoundHuman),
  already maintains [HUMAN_VOICE_RULES.md](https://github.com/themorgan/VoiceGuidelinesToSoundHuman/blob/main/HUMAN_VOICE_RULES.md), in production use by
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
  documents — and [OPERATING_RULES.md](OPERATING_RULES.md) item 5 now
  points at it instead of the ad hoc fingerprint list it started with.
  [MAP.md](MAP.md), [GLOSSARY.md](GLOSSARY.md) (new terms: **the voice
  guidelines**, **the voice guidelines sync**), [README.md](README.md), and
  [GETTING_STARTED.md](GETTING_STARTED.md) (the new
  `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN` secret disclosure) all updated to
  match. Judgment calls made: (1) reused
  `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN` as the secret name rather than
  inventing a new one, since VoiceGuidelinesToSoundHuman's own docs already
  establish that name for its other consumers (VoiceDefinitionMorgan,
  VoiceDefinitionCelia) — one less name for that ecosystem to track; (2)
  tracked only [HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) itself in
  [process/manifest_voice.json](process/manifest_voice.json), not the new
  workflow file — the workflow is this repo's own infrastructure, not
  something vendored from anywhere upstream, so a manifest entry for it
  would misrepresent what "vendored" means here; (3) kept
  [OPERATING_RULES.md](OPERATING_RULES.md) item 5 at *Trial* rather than
  jumping to *Promoted*, since this is the ruleset's first use on general
  assistant output (chat replies, not just WriteLike's voice-pack
  rewrites) — a new use worth testing here before it becomes a
  RepoPersonalPreferences default, same pipeline discipline as everything
  else in this document; (4) left `WriteLike` (the separate rewriting-app
  repo, added to this session while confirming which repo was the actual
  rules source) unvendored — it's the wrong repo for this purpose, kept
  only for reference.
- [x] **Give this repo an explicit third stage — [OPERATING_RULES.md](OPERATING_RULES.md)
  — between the brainstorm/essays and RepoPersonalPreferences.** Decided
  2026-08-27 → done, doc. A session recommending changes to
  RepoPersonalPreferences straight from this repo's ideas had skipped the
  step this repo exists to provide: trying an idea in real work before it
  becomes company-wide policy. Morgan's correction: (1) discover in
  [IDEAS.md](IDEAS.md) / the promoted essays, (2) try it for real in a new
  document, (3) only then port proven rules into RepoPersonalPreferences
  for rollout everywhere. Landed as
  [OPERATING_RULES.md](OPERATING_RULES.md) (new document, seeded with
  items 1-2 already promoted from a prior session, items 3-7 as trial
  rules pulled straight from [COCREATION_DESIGN.md](COCREATION_DESIGN.md)
  and [FIFTEEN_RULES.md](FIFTEEN_RULES.md), and a "not yet ready" section
  for ideas that need real infrastructure first — see the five new items
  above this one), a new "How this repo's ideas become company policy"
  section in [README.md](README.md), updated [MAP.md](MAP.md) and
  [GLOSSARY.md](GLOSSARY.md) (new terms: **the pipeline**, **the operating
  rules**, **promote**/**promotion**), [AGENTS.md](AGENTS.md)'s quick
  index, and a new dated entry plus an updated open-question note in
  [IDEAS.md](IDEAS.md). Judgment calls made: (1) named
  [OPERATING_RULES.md](OPERATING_RULES.md) that rather than
  something like `COMPANY_RULES.md` —
  "operating" reads as closer to "what's actually run on" than "company,"
  which could be misread as employee-facing policy; (2) picked five of
  COCREATION_DESIGN.md's ideas as concrete enough to state as Trial rules
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
  [§19 of the personal pack](https://github.com/themorgan/RepoPersonalPreferences/blob/main/process/personal/README.md)
  ([PR #24](https://github.com/themorgan/RepoPersonalPreferences/pull/24)).
  On writing-and-thinking work only (never code/technical work): argue a
  genuine counter-case before building on a stated stance, and flag a
  serious unresolved disagreement before calling a piece done — not a
  quota, never manufactured, and explicitly distinct from a judgment call
  or a clarifying question. This resolves the narrower "should Claude push
  back harder" question from the original brainstorm; the broader
  "normie"-employee-adoption question (visible rule-extraction, proactive
  resurfacing of rules) is still open — see [IDEAS.md](IDEAS.md)
  §"Why BestPractice specifically works" → "Open question" for the rest of
  it. Once the personal-pack sync pulls §19 into this repo's own
  `process/personal/` and re-weaves `AGENTS.md`, this repo picks up
  push-back mode automatically.
