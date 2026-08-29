#!/usr/bin/env python3
# Last updated: 2026-08-29 15:18:36 (Buenos Aires) by Morgan F, to version 2
"""check_file_mention_links.py — mechanical backstop for
process/personal/README.md#file-mention-links on its one automatable
surface: a Claude Code chat reply.

Invoked by .claude/hooks/stop-file-links-check.sh as a Stop hook. Claude
Code hands a Stop hook a JSON blob on stdin naming the transcript file for
this session (`transcript_path`, JSONL — one message per line); this script
reads that transcript and pulls out the text of the final reply that is
about to end the turn — the last contiguous run of assistant text blocks,
stopping the moment it walks back into a tool call (a tool_use block) or a
real user message. A turn is typically many tool calls interleaved with
short progress narration, then a final wrap-up reply; only that trailing
run is checked, deliberately excluding the narration — narration was never
meant as a citable deliverable the way the closing reply is, and holding it
to the same bar added real friction for no benefit (found the day this
script shipped: it first walked the *whole* turn since the last real user
message, and immediately flagged a batch of "now let's update X..."
progress notes instead of anything in the actual summary). Checks it for a
mention of a real, tracked file in this repo that isn't already wrapped in
a `[...](...)` markdown link.

Scope, matching the rule's own text:
  - Only mentions outside fenced (```) code blocks count — a markdown link
    can't render inside one anyway, so a path or filename there is a
    literal value, not a reference.
  - A mention inside a single-backtick code span still counts — the rule's
    own "even inside code" carve-out.
  - A bare pasted URL that happens to contain the filename counts as
    already linked (autolinked), even without `[text](url)` syntax.

This is a heuristic, not a perfect reader of intent — documented plainly in
the rule itself: it can occasionally flag a mention that was never meant as
a reference to this repo's own file. Fails open (exit 0) on anything that
looks like infrastructure trouble — no transcript, unparseable JSON, no git
— rather than blocking a turn over a problem unrelated to what the reply
actually said (process/personal/README.md#fail-gracefully).

Run standalone for testing: pipe a Stop-hook-shaped JSON blob in on stdin,
or pass a transcript path directly:
  python3 process/personal/tools/check_file_mention_links.py [transcript.jsonl]
"""
import json, pathlib, re, subprocess, sys

def _git(args, cwd):
    return subprocess.run(['git'] + args, cwd=cwd, capture_output=True, text=True).stdout.strip()

def repo_root():
    here = pathlib.Path(__file__).resolve().parent
    out = _git(['rev-parse', '--show-toplevel'], cwd=here)
    return pathlib.Path(out) if out else None

TEXT_EXT = {'.md', '.py', '.sh', '.json', '.yml', '.yaml', '.txt', '.template'}

def tracked_basenames(root):
    out = _git(['ls-files'], cwd=root)
    names = set()
    for f in out.split('\n'):
        if not f:
            continue
        p = pathlib.PurePosixPath(f)
        if p.suffix.lower() in TEXT_EXT or f.endswith('.md.template'):
            names.add(p.name)
    return names

FENCE_RE = re.compile(r'```.*?```', re.DOTALL)
MD_LINK_RE = re.compile(r'\[[^\]]*\]\([^)]*\)')
BARE_URL_RE = re.compile(r'https?://\S+')

def strip_linked_and_fenced(text):
    text = FENCE_RE.sub(' ', text)
    text = MD_LINK_RE.sub(' ', text)
    text = BARE_URL_RE.sub(' ', text)
    return text

def unlinked_mentions(text, basenames):
    remaining = strip_linked_and_fenced(text)
    found = []
    for name in sorted(basenames):
        # No word char or hyphen on either side, so "TODO.md" doesn't match
        # inside a longer name like "TODO.md-old" or "xTODO.md". Deliberately
        # NOT excluding a trailing/leading '.' -- basenames already end in
        # one (".md", ".py"), and a sentence ending right after a mention
        # ("...touched TODO.md.") is the common case, not the rare one
        # (found 2026-08-29: the stricter version silently dropped every
        # mention immediately followed by sentence punctuation).
        pattern = r'(?<![\w-])' + re.escape(name) + r'(?![\w-])'
        if re.search(pattern, remaining):
            found.append(name)
    return found

def last_turn_assistant_text(entries):
    """The final reply about to end this turn: every 'text' block from the
    trailing, unbroken run of assistant entries, oldest first — split
    across several assistant entries only if nothing but text separates
    them. Walking backward from the end, this stops the moment it reaches
    an assistant entry containing a tool_use block (a tool call — anything
    before it belongs to an earlier step, not the closing reply) or any
    user entry (a real message, or a tool_result, which itself always
    means a tool_use came just before it). Deliberately excludes
    progress narration written between tool calls earlier in the same
    turn — never meant as a citable deliverable the way the closing reply
    is."""
    texts = []
    for entry in reversed(entries):
        if entry.get('type') == 'assistant':
            msg = entry.get('message') or {}
            content = msg.get('content')
            blocks = content if isinstance(content, list) else (
                [{'type': 'text', 'text': content}] if isinstance(content, str) else [])
            has_tool_use = any(isinstance(b, dict) and b.get('type') == 'tool_use' for b in blocks)
            for b in blocks:
                if isinstance(b, dict) and b.get('type') == 'text':
                    texts.append(b.get('text', ''))
            if has_tool_use:
                break
        else:
            break
    return '\n\n'.join(reversed(texts))

def load_transcript(path):
    entries = []
    with open(path, encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return entries

def main(argv):
    if len(argv) > 1:
        transcript_path = argv[1]
    else:
        try:
            payload = json.loads(sys.stdin.read() or '{}')
        except json.JSONDecodeError:
            return 0
        transcript_path = payload.get('transcript_path')

    if not transcript_path or not pathlib.Path(transcript_path).exists():
        return 0

    root = repo_root()
    if root is None:
        return 0

    try:
        entries = load_transcript(transcript_path)
    except OSError:
        return 0

    reply_text = last_turn_assistant_text(entries)
    if not reply_text.strip():
        return 0

    basenames = tracked_basenames(root)
    if not basenames:
        return 0

    hits = unlinked_mentions(reply_text, basenames)
    if not hits:
        return 0

    names = ', '.join(f'`{h}`' for h in hits)
    print(
        f"Unlinked file mention(s) in this reply: {names}. Per "
        "process/personal/README.md#file-mention-links, every mention of a "
        "real repo file in a chat reply is a clickable GitHub link "
        "(https://github.com/<owner>/<repo>/blob/<branch>/<path>), even "
        "inside a code span. Add the missing link(s) before ending this "
        "turn. (If a name above isn't actually a reference to this repo's "
        "own file, that's a false positive from a heuristic check — adding "
        "a link anyway is the cheaper fix.)",
        file=sys.stderr,
    )
    return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
