# NTV — mod-decide pre-auth

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_n8n-template-fit/`
- **repo_state_verified_against:** `de75b4c4118c78dcc0164fdaa916bbc53f99225f`

## Pre-auth checklist

| # | check | result |
|---|---|---|
| 1 | `wavves/` home exists | PASS |
| 2 | W1 adversarial pack complete + GATE PASS | PASS — `gate-captures/NTV-W1.md` |
| 3 | Named open calls queued (not invented ad hoc) | PASS — `NTV-DECIDE-QUEUE.md` (5 calls) |
| 4 | SYNTHESIS available for job framing | PASS — O0 remediation (`NTV-INTa` never wrote; orch yield only) |
| 5 | No BUILD while forks open | PASS — enforced |
| 6 | AUTH-01 sync | **blocked** until operator completes picks |
| 7 | proof fields for later BUILD | pre-noted: expect `proof_required: yes` on execution charter |

## INT remediation note

[NTV-INT orch](83e7c2cf-fbba-43e2-bb92-12104187cd93) yielded; charge
`NTV-INTa` left no transcript or files. O0 wrote SYNTHESIS + DECIDE-QUEUE so
mod-decide can walk. NTV-ACCEPT still GATED after locks if operator wants an
independent grade; not required to start decide.

## Grounding paste (for Locked decisions later)

```text
Grounding (already verified — do not rediscover):
- Repo has zero n8n workflow JSON at tip de75b4c; template is greenfield.
- W1 KEEP musts: sticky notes, credentials, Set Fields, originality, SEO title form, personal-ID strip, Free first submit.
- REMOVE/Cursor-only: /wavves and mod-* slash skills, wavves/ standing home, plugin install.
- Library gap name: governed wave accept (not another CEO/orchestrator demo). Cites: n8n.io/workflows/7504, 7158, 8578; blog.n8n.io/multi-agent-systems/
- Example 4817 is description shape only; do not copy its graph.
```
