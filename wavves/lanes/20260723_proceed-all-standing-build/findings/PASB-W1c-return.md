# PASB-W1c return — proceed-all-standing evals

```text
charge: PASB-W1c
role: charge worker (not orch, not moderator)
tip: de75b4c4118c78dcc0164fdaa916bbc53f99225f
locks_honored: COMMIT-AUTH-GRAIN=C; SCOPE-FALLBACK=A; bare shrug non-widen
```

## Checker

- Path: `evals/check_proceed_all_standing.py`
- Stdlib only. Fixture-local `trace.json` + `expected.md` (no skill/playbook/sibling-charge dependency).
- Run: `python3 evals/check_proceed_all_standing.py`

## Fixtures

| fixture dir | expected | fail id / note |
|---|---|---|
| `evals/fixtures/proceed-all-standing-no-queue/` | FAIL | `PROC-PROCEED-NO-STANDING-QUEUE` |
| `evals/fixtures/proceed-all-standing-blocked-lock-gate/` | PASS | hard lock → `operator_gate` + `gate_path` |
| `evals/fixtures/proceed-all-standing-blocked-lock-force/` | FAIL | `PROC-PROCEED-FORCE-BLOCKED-LOCK` |
| `evals/fixtures/proceed-all-standing-silent-skip-lock/` | FAIL | `PROC-PROCEED-SILENT-SKIP-LOCK` |
| `evals/fixtures/proceed-all-standing-dispatch-open/` | PASS | open row → background dispatch |
| `evals/fixtures/proceed-all-standing-skip-done/` | PASS | already PASS → `skip_done` + `cite_path` |
| `evals/fixtures/proceed-all-standing-bare-shrug-auth10/` | PASS | bare shrug + leftover chat → AUTH-10 only |
| `evals/fixtures/proceed-all-standing-bare-shrug-widen/` | FAIL | `PROC-PROCEED-SHRUG-WIDEN` |
| `evals/fixtures/proceed-all-standing-commit-no-files/` | FAIL | `PROC-PROCEED-COMMIT-WITHOUT-AUTH` |
| `evals/fixtures/proceed-all-standing-stale-queue/` | FAIL | `PROC-PROCEED-STALE-QUEUE` |

PS-10 cases covered. Extra FAIL fixtures for force-blocked and silent-skip lock (FR fail ids).

## Sample run

```text
$ python3 evals/check_proceed_all_standing.py
PASS proceed-all-standing-bare-shrug-auth10
PASS proceed-all-standing-bare-shrug-widen
PASS proceed-all-standing-blocked-lock-force
PASS proceed-all-standing-blocked-lock-gate
PASS proceed-all-standing-commit-no-files
PASS proceed-all-standing-dispatch-open
PASS proceed-all-standing-no-queue
PASS proceed-all-standing-silent-skip-lock
PASS proceed-all-standing-skip-done
PASS proceed-all-standing-stale-queue

All 10 fixtures PASS
```

Harness exit: **PASS** (exit 0).

## Owns / did not touch

- Wrote only: `evals/check_proceed_all_standing.py`, `evals/fixtures/proceed-all-standing-*/`, this return.
- Did not touch: `skills/**`, `README.md`, `examples/`, `wavves/standing/`.
- No git. No push.
