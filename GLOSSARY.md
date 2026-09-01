<!-- Last updated: 2026-09-01 16:35:00 (Buenos Aires) by Morgan F, to version 10 -->

# Canonical names

The one list of names for this repo's own vocabulary. **Use these names;
don't invent new ones.** If two documents disagree with this file, this file
wins — fix the documents.

| Name | What it is | Defined in |
|---|---|---|
| **the brainstorm** | This repo's one deliverable: the running list of ideas, prompts, and workflows for working with AI. | [RANDOM_NOTES.md](docs/RANDOM_NOTES.md) |
| **the revolutionary formula** | The three ideas — groups of people collaborating (not individuals working alone with a model), protocols generated automatically, chat as the only intermediary for touching any document or artifact — that this repo argues are unique specifically when combined. | [THE_REVOLUTIONARY_FORMULA.md](docs/THE_REVOLUTIONARY_FORMULA.md) |
| **the pipeline** (three-stage) | How a brainstorm idea becomes company-wide policy: discover (the brainstorm) → try it for real (**the rules now testing**) → roll out everywhere (RepoPersonalPreferences's personal pack). | [README.md](README.md) |
| **the rules now testing** | Pipeline stage 2: the practical checklist actually in force in real work now, each rule tagged Trial, Ready to promote, or Promoted. | [RULES_NOW_TESTING.md](docs/RULES_NOW_TESTING.md) |
| **promote** / **promotion** | Moving a rule from *Trial* to *Ready to promote* to landed as its own section in RepoPersonalPreferences's personal pack — pipeline stage 2 to stage 3. | [RULES_NOW_TESTING.md](docs/RULES_NOW_TESTING.md) "Promotion" |
| **the voice guidelines** | [HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md), vendored from [SoundHuman](https://github.com/themorgan/SoundHuman): the "don't sound like an LLM" ruleset this repo's own writing follows, chat replies included. | [AGENTS.md](AGENTS.md) "Voice" |
| **the voice guidelines sync** | The scheduled GitHub Actions workflow (weekly by default) that keeps [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) current with SoundHuman. | [AGENTS.md](AGENTS.md) "A third scheduled check keeps the voice guidelines current" |
| **BestPractice** | The public upstream practice layer this repo vendors and follows. | [process/upstream/README.md](process/upstream/README.md) |
| **the personal pack** | Morgan's own layer of setup rules, vendored from [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences). | [process/personal/README.md](process/personal/README.md) |
| **the BestPractice sync** | The scheduled GitHub Actions workflow (weekly by default) that keeps `process/upstream/` current with the public BestPractice repo. | [`bestpractice-sync`](process/personal/README.md#bestpractice-sync) |
| **the pack sync** | The BestPractice sync's sibling: keeps `process/personal/` current with RepoPersonalPreferences. Needs its own repository secret, `PERSONAL_PACK_TOKEN`. | [`pack-sync`](process/personal/README.md#pack-sync) |
| **the light check** | The personal pack's fast sanity check (conflict markers, syntax, obvious secrets, broken doc links) run on every commit path, beyond [doc_lint.py](process/upstream/tools/doc_lint.py). | [process/personal/tools/light_check.py](process/personal/tools/light_check.py) |
| **the session-start notice** | `tools/bootstrap.sh` comparing both vendored trees against their sources on every session start and printing a notice only when one has moved. | [`drift-notice`](process/personal/README.md#drift-notice) |
