---
slug:        fail-gracefully
title:       Always fail gracefully
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "writing code that depends on something outside its own control, or handling a part that could not run"
gates:       []
index_clause: "keep going on a missing config, file, call or credential — and tell the session's human"
checked_by:  null
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-08-31
approved_by: "Morgan F, migrated from RepoPersonalPreferences by the private-set migration session"
---
## Rule
Any code written or set up here anticipates its own common failure modes rather than letting them surface as an unhandled crash. Failing gracefully means **two** things, and one without the other is still a violation:

1. **Keep going.** The work continues. A part that cannot run does not stop the session, abort the surrounding task, or take the rest of the system down with it: check for the absence or failure case on purpose and carry on with a documented fallback, a reduced scope, or that one part skipped -- never a raw stack trace, a hang, or an abort of work that did not depend on the thing that failed.
2. **Say so, to the person in the session.** Every degraded path announces itself where the human running the session will see it, naming what could not run, what that means for the result they are about to trust, and what would fix it. Silence is not grace. A quiet fallback, an empty result reported as a clean one, a swallowed exception -- each of these is a *worse* failure than the crash, because the crash at least told someone.

The failure mode this rule forbids is not "an error happened." It is **a result that looks complete and is not**, or **a stop that did not have to happen**.

## Detail
Three shapes recur, all of them "graceful" by the narrow reading and violations by this one:

- **The silent fallback.** A missing optional dependency, a config that did not load, a network call that failed -- handled, defaulted, and never mentioned. The next reader has no way to know the result is partial.
- **The empty scan reported as clean.** A check whose input did not exist, whose parser is not installed, or whose history was too shallow to reach what it walks, printing the same "OK" it prints when it genuinely looked and found nothing. "Could not check" and "checked, nothing wrong" must never render identically.
- **The stop that need not be one.** One part failing takes down a whole run that had many independent parts, when the honest outcome was to skip that part, say which, and finish the rest.

Where a tool has an exit status, "keep going" applies to the *work*, not to the status: a run that could not check something still reports that honestly rather than exiting 0, and a run whose one purpose could not be served at all may still exit non-zero -- as long as it says why, in words naming the fix.

## Why
The point of degrading is to leave the person better off than a crash would.
A crash is loud, so it gets fixed. A silent degrade is *quieter than success*,
so it accumulates: the fallback becomes the normal path, nobody remembers it
is a fallback, and the first person to depend on the missing piece finds out
years later. Between the two, the crash is the safer bug -- which is why grace
has to be measured against the human's understanding, not against whether the
process survived.

## Story
Two halves of this, both on 2026-09-06, in the same audit.

The stop half: fourteen mechanical check scripts across two practice sets
shared a `rule_text()` that read a practice file with no guard. Run in a
repository where that file was absent, each one detected its violation
correctly, printed it correctly, and then raised `FileNotFoundError` **from
inside the violation printer** -- burying a real finding under a traceback and
making a working check look broken.

The silence half, found the same day and worse: `doc_sync.py`'s
`owned_figures()` caught every exception from importing the script it reads
and returned `[]`. A crashing emitter was therefore indistinguishable from a
deliberate opt-out, so the restatement scan examined nothing and the gate
printed green. Nothing crashed. Nobody was told. That is the failure this
rule's second clause exists to name -- and it was the third time the same
shape had been found in this project, after an under-fetched `git log`
returning no commits and three inherited audits printing `OK` on having
inspected nothing.


## Install
No mechanical check, and this is the second attempt rather than an
assumption (practice `checkable-gets-checked`).

**Clause 1** -- whether code "anticipates its own common failure modes" and
keeps going -- is a judgment about error-handling adequacy across arbitrary
code in any language, not a fixed syntactic pattern: a bare `except:` is
sometimes exactly wrong and sometimes a deliberate, documented catch-all. At
this scope (`applies_to: ["**"]`, no language or shape specified) no static
rule is both broad enough to catch real violations and narrow enough not to
flood.

**Clause 2** -- the silent degrade -- looked more promising, because it has a
shape: an `except` handler whose body neither raises, nor prints or logs, nor
exits, but returns a default. Measured 2026-09-06 against Precedent's own
`tools/` (37 scripts, the most heavily audited Python in this project): **67
hits**, the large majority of them legitimate -- a narrow `except ValueError:
continue` inside a parser loop is correct and has nothing to announce. At that
signal-to-noise ratio the check would be turned off within a week, which is
worse than not having it, so this stays advisory and the measurement is
recorded here rather than re-derived by the next session that has the same
idea.

What IS enforceable is the specific case, not the general one. Where a
particular family of scripts must distinguish "could not check" from "checked,
nothing wrong," that family's own check can assert it -- `check_deep_check.py`
does exactly this for the check scripts in this set, and Precedent's own
harness asserts it for its gates. The general rule stays a review judgment;
each place it actually bites gets its own narrow check.
