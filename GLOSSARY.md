<!-- Last updated: 2026-09-04 10:49:37 (Buenos Aires) by Morgan F, to version 14 -->

# Canonical names

The one list of names for this repo's own vocabulary. **Use these names;
don't invent new ones.** If two documents disagree with this file, this file
wins — fix the documents.

| Name | What it is | Defined in |
|---|---|---|
| **the brainstorm** | This repo's one deliverable: the running list of ideas, prompts, and workflows for working with AI. | [RANDOM_NOTES.md](content/RANDOM_NOTES.md) |
| **the revolutionary formula** | The three ideas — groups of people collaborating (not individuals working alone with a model), protocols generated automatically, chat as the only intermediary for touching any document or artifact — that this repo argues are unique specifically when combined. | [THE_REVOLUTIONARY_FORMULA.md](content/THE_REVOLUTIONARY_FORMULA.md) |
| **the pipeline** (three-stage) | How a brainstorm idea becomes company-wide policy: discover (the brainstorm) → try it for real (**the rules now testing**) → roll out everywhere (precedent-team-maintainers, or precedent-individual for the rare Morgan-specific rule). | [README.md](README.md) |
| **the rules now testing** | Pipeline stage 2: the practical checklist actually in force in real work now, each rule tagged Trial, Ready to promote, or Promoted. | [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) |
| **promote** / **promotion** | Moving a rule from *Trial* to *Ready to promote* to landed in precedent-team-maintainers (or precedent-individual) — pipeline stage 2 to stage 3. | [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) "Promotion" |
| **the voice guidelines** | [HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md), vendored from [SoundHuman](https://github.com/themorgan/SoundHuman): the "don't sound like an LLM" ruleset this repo's own writing follows, chat replies included. | [AGENTS.md](AGENTS.md) "Voice" |
| **the voice guidelines sync** | The scheduled GitHub Actions workflow (weekly by default) that keeps [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) current with SoundHuman. | [GETTING_STARTED.md](GETTING_STARTED.md) "A second scheduled check keeps the voice guidelines current" |
| **BestPractice** | The public upstream practice layer this repo vendors and follows. | [process/upstream/README.md](process/upstream/README.md) |
| **the team practice source** | Morgan and Alex's own working conventions, resolved live from a sibling clone of [precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers). | [precedent.json](precedent.json) |
| **the individual practice source** | Morgan's own person-specific facts (commit identity, timezone, file-header naming, the `go`/`merge` shorthand), resolved from [precedent-individual](https://github.com/themorgan/precedent-individual) via his user-level config — never declared in this repo's own tracked files. | [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md) |
| **the BestPractice sync** | The scheduled GitHub Actions workflow (weekly by default) that keeps `process/upstream/` current with the public BestPractice repo. Paused for the precedent-beta-v01 beta test. | [`bestpractice-sync`](https://github.com/themorgan/precedent-individual/blob/main/practices/bestpractice-sync.md) |
| **the light check** | This repo's own fast sanity check (conflict markers, syntax, obvious secrets, broken doc links, and now the `precedent.json`/`process/manifest.json` sources) run on every commit path, beyond [doc_lint.py](process/upstream/tools/doc_lint.py). | [tools/light_check.py](tools/light_check.py) |
| **the session-start notice** | `tools/bootstrap.sh` comparing the vendored `process/upstream/` tree and the voice guidelines file against their sources on every session start and printing a notice only when one has moved (the BestPractice half is currently paused — see [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)). | [`drift-notice`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/drift-notice.md) |
