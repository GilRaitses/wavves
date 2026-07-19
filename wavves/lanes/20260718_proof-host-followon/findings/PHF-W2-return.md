# PHF-W2 return

lane: PHF
wave: W2
date: 2026-07-18 (America/New_York)
repo_state_verified_against: `538437cad76764fd989cd028f64927b1ae839292`
status: complete — pause before PHF-ACCEPT
INT: not required (playbook + EXECUTION_WIRING applied in W2)

## W2a — probe

Shipped `skills/charter/scripts/proof_host_probe.py`:

- stdlib `--self-check` / `--dry-run` emits `host_client_height`, `blank_canvas`
- exercises healthy / zero-height / blank-canvas gate fixtures
- live mode: `--url` + `--selector` via optional Playwright; clear error if missing

Smoke (measured):

```bash
python3 skills/charter/scripts/proof_host_probe.py --self-check \
  --out wavves/lanes/20260718_proof-host-followon/gate-captures/PHF-W2-probe-self-check.json
# EXIT:0; self_check_logic_ok: true; required fields present
```

Capture: `gate-captures/PHF-W2-probe-self-check.json`

## W2b — wiring + playbook

- `skills/charter/EXECUTION_WIRING.md` Rule 2b cites
  `skills/charter/scripts/proof_host_probe.py` (not contract-only)
- Screenshot subsection → capture-then-grade required when `visual_accept: yes`;
  DOM green ≠ done
- `skills/wavves/playbooks/proof-before-accept.md` hardened: real probe path;
  steps 5–8 require capture-then-grade on `visual_accept: yes`

## Regression (pre-ACCEPT spot)

- `python3 evals/check_proof_before_accept.py` → 4/4 PASS
- `python3 evals/check_paragraph_tunnel.py` → 6/6 PASS
- PBB-ACCEPT not reopened or rewritten

## Not done (parked / deferred)

- PHF-EVAL: no product-look fixture corpus
- PHF-ETIQUETTE: empty-return note outside this BUILD
- Live Playwright ACCEPT against a real product URL (needs visitor host)

## Pause

STOP before PHF-ACCEPT. O0 / independent evaluator owns ACCEPT gate.
