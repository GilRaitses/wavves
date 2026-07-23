# PAS — mod-decide queue (residual after FR revise)

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_proceed-all-standing-check/`
- **Artifact:** `feature-requests/20260723_proceed-all-standing.md` (revised-after-PAS)
- **repo_state_verified_against:** `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5`
- **Status:** awaiting operator pick on call 1

## Locked already (not open)

Bare-shrug/`/shrug` non-widen; `wavves/standing/` persist; scope-then-remasure;
gate-continue; `/shrug` leaf; SKILL wiring; closed triggers; fail-id set.

## Queue

1. **COMMIT-AUTH-GRAIN** — (current)
2. **SCOPE-FALLBACK** — after (1)

## Call 1 — COMMIT-AUTH-GRAIN

**Question:** When proceed-all-standing classifies multiple `commit` rows with
explicit `files:` lists, does one all-standing authorize utterance cover every
land, or does each land need its own this-turn authorize / `operator_gate`?

| option | meaning |
|---|---|
| A | One all-standing authorize covers every `commit` row that already has `files:` |
| B | Each `commit` row needs its own “ship it” / per-land `operator_gate` when multi-repo or >1 land |
| C | Hybrid: single-repo lands covered by one authorize; cross-repo lands always per-land gate |

**Lean:** **C** (keeps AUTH-10 file-list discipline; avoids blanket multi-repo push).

Awaiting operator `Pick: A|B|C`.
