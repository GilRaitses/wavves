# PASB-W1a — proceed playbook mode fork

```text
ROLE: charge worker PASB-W1a. One charge only. Not orch. Not moderator.
HOME: /Users/gilraitses/wavves_build/wavves/lanes/20260723_proceed-all-standing-build/
REPO: /Users/gilraitses/wavves_build
TIP: de75b4c4118c78dcc0164fdaa916bbc53f99225f
OWNS (only): skills/wavves/playbooks/proceed.md
DO NOT TOUCH: skills/shrug/, skills/wavves/SKILL.md, evals/, README.md, examples/

AUTHORITY (do not reopen):
  - LOCKS: wavves/lanes/20260723_proceed-all-standing-check/decisions/LOCKED-DECISIONS.md
  - FR: feature-requests/20260723_proceed-all-standing.md (PS-01..PS-06, PS-09; fail ids)
  - COMMIT-AUTH-GRAIN = C (same-repo one authorize; cross-repo per-land gate)
  - SCOPE-FALLBACK = A (empty standing file + stop)
  - Bare shrug / bare /shrug never widen to all-standing

MISSION:
  Edit skills/wavves/playbooks/proceed.md to ship proceed-all-standing mode fork:
  1. Mode fork at top: AUTH-10 proceed (existing recommended_actions path) vs
     proceed-all-standing.
  2. All-standing Step 0: build Standing queue from disk only; never transcript.
     Persist only at wavves/standing/<YYYYMMDD>_<label>.md (create dir if needed).
     Schema rows per FR PS-02. Empty inventory → write empty queue + stop (SCOPE-FALLBACK A).
  3. Scope-then-remasure (PS-03), move rules (PS-04), gate-continue (PS-05).
  4. Triggers closed (PS-06): widen only on explicit all-standing phrases;
     bare shrug and bare /shrug stay AUTH-10 only (PROC-PROCEED-SHRUG-WIDEN).
  5. COMMIT-AUTH-GRAIN C in commit-class rules; AUTH-10 files: still required.
  6. Return card from standing file (PS-09).
  Keep AUTH-10 path intact for bare proceed / bare shrug.

Write findings/PASB-W1a-return.md with: paths touched, locks honored, residual risks.
No git. No push. Escalate to orch/O0 only.
MODEL: cursor-grok-4.5-high-fast
```
