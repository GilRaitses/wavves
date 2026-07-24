# NTVB-W1 rollup

| field | value |
|---|---|
| wave | NTVB-W1 |
| orch | NTVB-W1 wave orchestrator |
| answers_to | O0 |
| tip_base | de75b4c4118c78dcc0164fdaa916bbc53f99225f |
| git_actions_by_runner | none |
| gate | see `findings/NTVB-W1-GATE.md` / `gate-captures/NTVB-W1.md` |

## Charge → worker_agent_id

| charge | worker_agent_id | status |
|---|---|---|
| NTVB-W1a | 80c936b1-ea7e-4ef2-8391-dc521ef7e4a9 | done |
| NTVB-W1b | 18e11502-252d-404c-ab08-54045a3e6e5b | done |
| NTVB-W1c | b97d2165-b427-4db7-bc8a-101a95be0490 | done |
| NTVB-W1d | 44869569-d7a2-43aa-87e9-3010c6f4824e | done |

## Landed pack (W1)

| path | owner | notes |
|---|---|---|
| `pack/01-charge-research-a.json` | W1a | trigger → Set → Agent A + chat model + parser → emit |
| `pack/02-charge-research-b.json` | W1b | adversarial lens sibling; same shape, distinct role |
| `pack/DESCRIPTION.md` | W1c | SEO title + ~215w Free listing sections |
| `pack/STICKIES.md` | W1c | yellow + six step stickies (canonical) |
| `pack/GATE-TABLE-SCHEMA.md` | W1d | 8 columns; no term_id |
| `pack/README.md` | W1d | import order draft; INT TBD slots |

## Role split (charges)

- A: cite-map supportive evidence
- B: adversarial gaps / counter-claims / accept-blocking risks

## Mechanical checks (orch)

- `python3 -m json.tool` on both charge JSON → EXIT 0
- Secret/path scan on pack JSON + DESCRIPTION + STICKIES → clean (no `sk-…`, no `/Users/gil…`)
- Docs mention of forbidden patterns in README/schema are instructional only

## Still owned by INT

- `pack/03-parent-orchestrator.json`
- finalize `pack/README.md` (Execute Workflow IDs / parent name)

## commit_file_list (W1 only; INT adds more)

```text
pack/01-charge-research-a.json
pack/02-charge-research-b.json
pack/DESCRIPTION.md
pack/STICKIES.md
pack/GATE-TABLE-SCHEMA.md
pack/README.md
findings/NTVB-W1a-return.md
findings/NTVB-W1b-return.md
findings/NTVB-W1c-return.md
findings/NTVB-W1d-return.md
findings/NTVB-W1-pending.md
findings/NTVB-W1-orch-checkpoint.md
findings/NTVB-W1-rollup.md
findings/NTVB-W1-GATE.md
gate-captures/NTVB-W1.md
```
