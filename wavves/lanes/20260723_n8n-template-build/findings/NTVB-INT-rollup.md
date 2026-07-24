# NTVB-INT rollup

| field | value |
|---|---|
| wave | NTVB-INT |
| worker_agent_id | 8a7c27c5-0a22-44ed-b85c-f9a31cd3c470 |
| status | done |
| parent | Parent Orchestrator — Proof-Gated Wave Accept |
| git_actions_by_runner | none |
| prior_gate | NTVB-W1 PASS |

## proof_job path (verified in JSON)

Manual Trigger → Set Wave Packet Fields → Execute Charge A ‖ Execute Charge B → Merge Charge Returns → **Proof Merge Complete** → **IF Outcome Pass** → **Append Proof Gate Row** → Emit Pass Rollup  

Block: Append Block Gate Row → Emit Block Rollup

## Artifacts

- `pack/03-parent-orchestrator.json` — `python3 -m json.tool` EXIT 0; stickies embedded; Execute Workflow placeholders for Charge A/B names
- `pack/README.md` — INT finalize filled
- `findings/NTVB-INT-return.md`

## Leave-act for orch

`return_to_O0` — recommended_next: **O0 unlock ACCEPT** (do not start ACCEPT from INT/W1 orch).
