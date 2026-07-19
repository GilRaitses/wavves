# PHF-ACCEPT — gate capture

lane: PHF (proof-host-followon)
gate: PHF-ACCEPT
date: 2026-07-18 (America/New_York)
evaluator: O0 (no authorship of W2 probe/script under review)
repo_state_verified_against: `f837244e5aa236240bc863d297cb01ed44cad7d9`

## Pass metric (stated before the run)

1. `proof_host_probe.py --self-check` EXIT 0; JSON has `host_client_height`,
   `blank_canvas`, and self-check cases for healthy / zero-height / blank
2. EXECUTION_WIRING Rule 2b cites the real script path
3. Playbook: `visual_accept: yes` ⇒ capture-then-grade; DOM green ≠ done
4. PBB checker 4/4 and paragraph-tunnel 6/6 still PASS
5. No VPB product-look port; PBB not reopened

## (1) Probe self-check — measured

```bash
python3 skills/charter/scripts/proof_host_probe.py --self-check \
  --out wavves/lanes/20260718_proof-host-followon/gate-captures/PHF-ACCEPT-probe-self-check.json
```

EXIT 0. Capture fields: `host_client_height: 711`, `blank_canvas: false`,
`self_check_logic_ok: true`; cases healthy/zero-height/blank-canvas all ok.

Live `--url/--selector` path not exercised (Playwright optional; disclosed).

## (2) Wiring spot-check

| lock | evidence | result |
|---|---|---|
| Rule 2b real path | EXECUTION_WIRING cites `skills/charter/scripts/proof_host_probe.py` | PASS |
| visual_accept harden | playbook steps 8 + named harness | PASS |
| no VPB port | no new product-look fixture corpus | PASS |

## (3) Regression

- `check_proof_before_accept.py` → pass=4 fail=0
- `check_paragraph_tunnel.py` → pass=6 fail=0

## Known gap (disclosed, non-blocking for PHF ACCEPT)

Live browser ACCEPT against a product URL not run in this capture. Self-check
proves gate logic and JSON schema. Product lanes still bind `--url` /
`--selector` at ACCEPT time.

## Verdict

**PASS.** PHF ACCEPT criteria met. Shared probe is live tooling (self-check
harness). PBB remains shipped.
