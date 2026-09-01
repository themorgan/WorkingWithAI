<!-- Last updated: 2026-09-01 16:46:35 (Buenos Aires) by Morgan F, to version 1 -->

# Recipe: GLOSSARY.md

- **Always stays at the repo root — never move it into `docs/` or any
  other subdirectory.** Not a style choice: it's one of BestPractice's
  own living documents, installed from
  [process/upstream/templates/GLOSSARY.md.template](../process/upstream/templates/GLOSSARY.md.template)
  per [process/manifest.json](../process/manifest.json)'s `local_path`.
  [process/upstream/tools/doc_lint.py](../process/upstream/tools/doc_lint.py)
  hardcodes `GLOSSARY_PATH = ROOT / 'GLOSSARY.md'` for its ungapped-acronym
  check — moving the file wouldn't error, it would silently disable that
  check repo-wide, since the tool treats a missing file at that exact path
  as "this repo has no glossary yet."
