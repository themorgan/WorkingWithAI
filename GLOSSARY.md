<!-- Last updated: 2026-08-26 13:00:00 (Buenos Aires) by Morgan F, to version 1 -->

# Canonical names

The one list of names for this repo's own vocabulary. **Use these names;
don't invent new ones.** If two documents disagree with this file, this file
wins — fix the documents.

| Name | What it is | Defined in |
|---|---|---|
| **the brainstorm** | This repo's one deliverable: the running list of ideas, prompts, and workflows for working with AI. | [IDEAS.md](IDEAS.md) |
| **BestPractice** | The public upstream practice layer this repo vendors and follows. | [process/upstream/README.md](process/upstream/README.md) |
| **the personal pack** | Morgan's own layer of setup rules, vendored from [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences). | [process/personal/README.md](process/personal/README.md) |
| **the BestPractice sync** | The scheduled GitHub Actions workflow (weekly by default) that keeps `process/upstream/` current with the public BestPractice repo. | [process/personal/README.md](process/personal/README.md) §14 |
| **the pack sync** | The BestPractice sync's sibling: keeps `process/personal/` current with RepoPersonalPreferences. Needs its own repository secret, `PERSONAL_PACK_TOKEN`. | [process/personal/README.md](process/personal/README.md) §15 |
| **the light check** | The personal pack's fast sanity check (conflict markers, syntax, obvious secrets, broken doc links) run on every commit path, beyond [doc_lint.py](process/upstream/tools/doc_lint.py). | [process/personal/tools/light_check.py](process/personal/tools/light_check.py) |
| **the session-start notice** | `tools/bootstrap.sh` comparing both vendored trees against their sources on every session start and printing a notice only when one has moved. | [process/personal/README.md](process/personal/README.md) §16 |
