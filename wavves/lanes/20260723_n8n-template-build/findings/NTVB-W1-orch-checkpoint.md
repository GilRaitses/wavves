# NTVB-W1 orch checkpoint

```yaml
leave_act: return_to_O0
wave: NTVB-W1
orch_status: W1_PASS_INT_done
answers_to: O0
git_actions_by_runner: none
accept_status: GATED_for_O0
recommended_next: O0_unlock_ACCEPT
int_status: done
int_worker_agent_id: 8a7c27c5-0a22-44ed-b85c-f9a31cd3c470
```

## Hydration done

- dispatch-w1.md, waveset.md
- NTV LOCKED-DECISIONS (JOB=A PACK=B GATE-STORE=B LLM=C V0-SCOPE=A Free)
- NTV-SYNTHESIS, guidelines-excerpt
- pack/ dirs ready; tip_base de75b4c

## Fan-out map

| charge | worker_agent_id |
|---|---|
| NTVB-W1a | 80c936b1-ea7e-4ef2-8391-dc521ef7e4a9 |
| NTVB-W1b | 18e11502-252d-404c-ab08-54045a3e6e5b |
| NTVB-W1c | b97d2165-b427-4db7-bc8a-101a95be0490 |
| NTVB-W1d | 44869569-d7a2-43aa-87e9-3010c6f4824e |

## Resume recipe (on notify)

1. Read `findings/NTVB-W1a-return.md` … `NTVB-W1d-return.md`
2. Verify pack files exist; `python3 -m json.tool` on charge JSON
3. Write `findings/NTVB-W1-rollup.md` + `findings/NTVB-W1-GATE.md` + `gate-captures/NTVB-W1.md`
4. If GATE PASS: background INT worker → `pack/03-parent-orchestrator.json` + finalize README; INT rollup
5. `return_to_O0` with recommended_next: O0 unlock ACCEPT (do not run ACCEPT)

## Illegal

- return_to_O0 after only launching (this checkpoint is yield, not return)
- git by runner
- n8n.io submit
- ACCEPT without O0 unlock
