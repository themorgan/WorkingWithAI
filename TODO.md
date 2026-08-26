<!-- Last updated: 2026-08-26 14:00:00 (Buenos Aires) by Morgan F, to version 2 -->

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
  15 wants a real year for "the way you'd have read it in [YEAR]." Both are
  intentionally left as placeholders rather than filled with something
  generic — replace them only when a real specific comes to mind.
- [ ] **Look for contradictions across [IDEAS.md](IDEAS.md) entries**, per
  the meta-note at the bottom of that file (e.g. rule 9's "build five, kill
  four" against rule 5's "don't systematize a one-off") — worth a
  dedicated pass once there's enough material for real tensions to show up.

## Verify before external use

## Decisions (user's call)

- [ ] **Force deeper AI engagement, or just permit it?** See
  [IDEAS.md](IDEAS.md) §"Why BestPractice specifically works" → "Open
  question." Candidate mechanisms: Claude pushing back harder on direct
  instructions by default, more visible/frequent reminders of the deeper
  co-creation mode, making automatic rule-extraction more visible so people
  notice it happening, or having Claude proactively resurface a relevant
  extracted rule in a new context. Undecided — needs Morgan's call on how
  paternalistic this repo's own tooling should be toward less technical
  users.
