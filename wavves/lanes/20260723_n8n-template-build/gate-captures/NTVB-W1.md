# gate-captures/NTVB-W1

```yaml
wave: NTVB-W1
verdict: PASS
captured_at: 2026-07-23T13:56:30-04:00
tip_base: de75b4c4118c78dcc0164fdaa916bbc53f99225f
git_actions_by_runner: none
```

## Evidence

### Charge map

| charge | worker_agent_id | return |
|---|---|---|
| NTVB-W1a | 80c936b1-ea7e-4ef2-8391-dc521ef7e4a9 | findings/NTVB-W1a-return.md |
| NTVB-W1b | 18e11502-252d-404c-ab08-54045a3e6e5b | findings/NTVB-W1b-return.md |
| NTVB-W1c | b97d2165-b427-4db7-bc8a-101a95be0490 | findings/NTVB-W1c-return.md |
| NTVB-W1d | 44869569-d7a2-43aa-87e9-3010c6f4824e | findings/NTVB-W1d-return.md |

### Mechanical

```text
python3 -m json.tool pack/01-charge-research-a.json → EXIT 0
python3 -m json.tool pack/02-charge-research-b.json → EXIT 0
rg sk-/Users on pack/*.json DESCRIPTION STICKIES → clean
```

### Pack inventory (pre-INT)

```text
pack/01-charge-research-a.json
pack/02-charge-research-b.json
pack/DESCRIPTION.md
pack/STICKIES.md
pack/GATE-TABLE-SCHEMA.md
pack/README.md
```

### Gate verdict quote

From `findings/NTVB-W1-GATE.md`: verdict **PASS** → proceed NTVB-INT; ACCEPT GATED for O0.
