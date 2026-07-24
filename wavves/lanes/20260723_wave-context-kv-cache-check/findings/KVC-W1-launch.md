# KVC-W1 launch board

```yaml
wave: KVC-W1
role: wave_orchestrator
moderator: O0
tip_expected: de75b4c4118c78dcc0164fdaa916bbc53f99225f
tip_remeasured: de75b4c4118c78dcc0164fdaa916bbc53f99225f
git: none
build: none
skill_edits: none
artifact: feature-requests/20260723_wave-context-kv-cache.md
leave_act_now: yield_awaiting_children
verdict_path: findings/KVC-verdict.md
```

## Role (locked)

| role | who | does |
|---|---|---|
| moderator | O0 | chartered this orch; reconciles verdict; git land if asked |
| wave orchestrator | KVC-W1 (this Task) | fan out four lenses; checkpoint on yield; integrate; write verdict; return_to_O0 |
| charge worker | KVC-W1a…d | one lens each; write only own findings file + return |

## Charge ownership / dispatch state

| id | lens | owns | return | orch action |
|---|---|---|---|---|
| KVC-W1a | grounding | `findings/KVC-grounding.md` | `findings/KVC-W1a-return.md` | deploy background |
| KVC-W1b | contradictions | `findings/KVC-contradictions.md` | `findings/KVC-W1b-return.md` | deploy background |
| KVC-W1c | completeness | `findings/KVC-completeness.md` | `findings/KVC-W1c-return.md` | deploy background |
| KVC-W1d | adversarial | `findings/KVC-adversarial.md` | `findings/KVC-W1d-return.md` | deploy background |

## Hydration (orch)

- `waveset.md`, `dispatch-w1.md`, artifact FR
- WOF FR leave-acts / checkpoint (`feature-requests/20260723_wave-orchestrator-fanout.md`)
- PAS FR stale-queue / standing (`feature-requests/20260723_proceed-all-standing.md`)
- `skills/mod-rotate/SKILL.md`; `skills/wavves-init/SKILL.md` §4–5
- RTH synthesis pointer (illustration): `lanes/20260723_mod-rotate-theory-research/findings/RTH-SYNTHESIS.md`

## Disk remasure (pre-launch)

| fact | measured |
|---|---|
| HEAD | `de75b4c4118c78dcc0164fdaa916bbc53f99225f` |
| `wavves/rotations/` | empty (0 files) |
| INDEX `current_rotation` | `none` |
| INDEX `current_identity` | `O0` |
| FR status (README) | `ready-for-mod-check` |

## Bans (all charges)

- No git. No BUILD. No skill edits.
- Ban treating FR as transformer KV isomorphism or RotatE.
- Ban expanding scope to PUO / IPB / MDA.
- Wire scope only: WOF checkpoint + PAS remasure + mod-rotate hydration.
- Escalate to O0 only (via orch). Model: `cursor-grok-4.5-high-fast`.

## Leave-acts

| act | when |
|---|---|
| `yield_awaiting_children` | four lenses launched; returns incomplete; checkpoint written |
| `return_to_O0` | only with `findings/KVC-verdict.md` (GO \| REVISE \| BLOCK) or hard FAIL |

Illegal: `return_to_O0` after launch only (`PROC-ORCH-LAUNCH-AND-EXIT`).
