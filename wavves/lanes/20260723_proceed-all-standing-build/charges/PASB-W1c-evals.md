# PASB-W1c — proceed-all-standing evals + fixtures

```text
ROLE: charge worker PASB-W1c. One charge only. Not orch. Not moderator.
HOME: /Users/gilraitses/wavves_build/wavves/lanes/20260723_proceed-all-standing-build/
REPO: /Users/gilraitses/wavves_build
TIP: de75b4c4118c78dcc0164fdaa916bbc53f99225f
OWNS (only): evals/check_proceed_all_standing.py
             evals/fixtures/proceed-all-standing-*/
DO NOT TOUCH: skills/**, README.md, examples/, wavves/standing/ (runtime only)

AUTHORITY (do not reopen):
  - LOCKS: wavves/lanes/20260723_proceed-all-standing-check/decisions/LOCKED-DECISIONS.md
  - FR PS-10 + fail ids (PROC-PROCEED-*)
  - COMMIT-AUTH-GRAIN = C; SCOPE-FALLBACK = A; bare shrug non-widen

MISSION:
  Ship mechanical checker + fixtures covering at least:
    - no queue file → FAIL (PROC-PROCEED-NO-STANDING-QUEUE)
    - blocked lock → operator_gate not dispatch (PROC-PROCEED-FORCE-BLOCKED-LOCK /
      PROC-PROCEED-SILENT-SKIP-LOCK as applicable)
    - open dispatchable → background dispatch class
    - already PASS → skip_done with cite
    - bare shrug with leftover chat → AUTH-10 only (PROC-PROCEED-SHRUG-WIDEN if widened)
    - commit without files: → FAIL (PROC-PROCEED-COMMIT-WITHOUT-AUTH)
    - stale standing file without remasure → FAIL (PROC-PROCEED-STALE-QUEUE)
  Stdlib only. Mirror style of evals/check_wave_orchestrator_fanout.py where useful.
  Fixtures under evals/fixtures/proceed-all-standing-<case>/ with expected.md
  (+ input/trace as needed). Checker must be runnable:
    python3 evals/check_proceed_all_standing.py
  Do not require sibling charge files to exist to author fixtures; check playbook
  / skill paths only if your harness design needs them (prefer fixture-local traces).

Write findings/PASB-W1c-return.md with: checker path, fixture list, sample run notes.
No git. No push. Escalate to orch/O0 only.
MODEL: cursor-grok-4.5-high-fast
```
