# PASB — proceed-all-standing-build

| Meta | |
|---|---|
| lane code | PASB |
| type | execution |
| `repo_state_verified_against` | `de75b4c4118c78dcc0164fdaa916bbc53f99225f` |
| `proof_required` | n/a — playbook/skill leaf; no visitor Proof surface |
| depends_on | PAS mod-decide complete |

## Intent

Ship proceed-all-standing mode + `/shrug` leaf + evals per
`feature-requests/20260723_proceed-all-standing.md` and locked decisions.

## Locked decisions (do NOT reopen)

```text
- COMMIT-AUTH-GRAIN = C — same-repo one authorize; cross-repo per-land gate
- SCOPE-FALLBACK = A — empty standing file + stop
- Bare shrug / bare /shrug never widen to all-standing
- Standing persist only under wavves/standing/; scope-then-remasure;
  gate-continue; closed triggers; fail-id set in FR
```

## Grounding

- FR: `feature-requests/20260723_proceed-all-standing.md`
- Locks: `wavves/lanes/20260723_proceed-all-standing-check/decisions/LOCKED-DECISIONS.md`
- Existing: `skills/wavves/playbooks/proceed.md`, `skills/wavves/SKILL.md`

## Wave structure

### PASB-W1 — discovery (optional thin) + build fan-out

Prefer single build wave with disjoint file ownership:

| id | owns |
|---|---|
| PASB-W1a | `skills/wavves/playbooks/proceed.md` mode fork + standing steps |
| PASB-W1b | `skills/shrug/SKILL.md` (new thin leaf) |
| PASB-W1c | `evals/check_proceed_all_standing.py` + `evals/fixtures/proceed-all-standing-*/` |
| PASB-W1d | router/docs: `skills/wavves/SKILL.md`, README/usage rows for `/shrug` |

### PASB-INT — single editor

Wire any shared convergence (router table consistency). No git.

### PASB-ACCEPT — mechanical

Run `python3 evals/check_proceed_all_standing.py`; capture
`gate-captures/PASB-ACCEPT.md` + JSON. GATED on O0 after orch rollup if INT
needed; orch may run ACCEPT if W1+INT clean and report.

## Acceptance

- Playbook AUTH-10 vs proceed-all-standing fork; bare shrug non-widen
- `/shrug` leaf ships
- Standing path + empty-queue SCOPE-FALLBACK A
- COMMIT-AUTH-GRAIN C in commit-class rules
- Eval fixtures PASS
- No git by runners

## Model

`cursor-grok-4.5-high-fast` for orch + judgment; balanced ok for fixture writing.

## Escalation

To O0 only. No operator solicitation.
