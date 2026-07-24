# PAS — mod-decide queue

- **Date:** 2026-07-23
- **Status:** **complete** — both residual calls locked
- **Locks:** `decisions/LOCKED-DECISIONS.md`

## Queue

| # | call | pick | record |
|---|---|---|---|
| 1 | COMMIT-AUTH-GRAIN | **C** | `PAS-B-COMMIT-AUTH-GRAIN.md` |
| 2 | SCOPE-FALLBACK | **A** | `PAS-B-SCOPE-FALLBACK.md` |

Next: AUTH-01 sync into BUILD waveset when `/charter` PAS BUILD, or
re-`/mod-check` if operator wants second pass on revise. No BUILD this turn
unless operator asks.
