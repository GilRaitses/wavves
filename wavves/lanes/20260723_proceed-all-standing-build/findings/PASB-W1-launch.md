# PASB-W1 launch board

```yaml
wave: PASB-W1
role: wave_orchestrator
moderator: O0
tip_expected: de75b4c4118c78dcc0164fdaa916bbc53f99225f
git: none
leave_act_now: yield_awaiting_children
```

## Role (locked)

| role | who | does |
|---|---|---|
| moderator | O0 | charter orch; reconcile rollup+ACCEPT; git land |
| wave orchestrator | PASB-W1 (this Task) | fan-out charges; INT; ACCEPT; return_to_O0 |
| charge worker | PASB-W1a…d | one disjoint BUILD each |

## Charge ownership / dispatch state

| id | owns | prompt | return path | orch action |
|---|---|---|---|---|
| PASB-W1a | `skills/wavves/playbooks/proceed.md` | `charges/PASB-W1a-proceed.md` | `findings/PASB-W1a-return.md` | deploy background |
| PASB-W1b | `skills/shrug/SKILL.md` (new) | `charges/PASB-W1b-shrug.md` | `findings/PASB-W1b-return.md` | deploy background |
| PASB-W1c | `evals/check_proceed_all_standing.py` + fixtures | `charges/PASB-W1c-evals.md` | `findings/PASB-W1c-return.md` | deploy background |
| PASB-W1d | `skills/wavves/SKILL.md`, README, `examples/usage.md` | `charges/PASB-W1d-router-docs.md` | `findings/PASB-W1d-return.md` | deploy background |

Locks honored at dispatch: COMMIT-AUTH-GRAIN=C, SCOPE-FALLBACK=A, bare shrug non-widen.

## Next after returns

1. PASB-INT (single editor) if router/playbook/leaf drift
2. Run `python3 evals/check_proceed_all_standing.py`
3. Write `gate-captures/PASB-ACCEPT.md` (+ JSON if harness emits)
4. `findings/PASB-W1-rollup.md` then `return_to_O0`
