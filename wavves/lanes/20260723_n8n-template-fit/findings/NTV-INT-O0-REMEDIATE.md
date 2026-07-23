# NTV-INT — O0 fail remediation

| field | value |
|---|---|
| prior_orch | 83e7c2cf-fbba-43e2-bb92-12104187cd93 |
| leave_act_seen | yield_awaiting_children |
| worker_NTV-INTa | a29b3df9-9312-4007-804a-3742d27293ea — no files, no local transcript |
| remediation | O0 wrote `findings/NTV-SYNTHESIS.md` + `decisions/NTV-DECIDE-QUEUE.md` |
| INT rollup/GATE | skipped; mod-decide pre-auth unblocked from W1 PASS + remediation |
| git_actions | none |

Operator asked pre-auth for `/mod-decide`. Do not re-dispatch INT unless
operator wants a second synthesis author.
