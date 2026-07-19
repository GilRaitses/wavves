# PHF-W1a — probe shape

lane: PHF
wave: W1a
date: 2026-07-18 (America/New_York)
repo_state_verified_against: `538437cad76764fd989cd028f64927b1ae839292`
status: discovery complete

## Lock

PHF-PROBE: ship `skills/charter/scripts/proof_host_probe.py` (stdlib preferred;
JSON at least `host_client_height`, `blank_canvas`). Wire Rule 2b to that path.

## Shape reference

`skills/charter/scripts/transition_gap_probe.py`:

- `#!/usr/bin/env python3`, argparse, JSON summary to stdout + optional `--out`
- stdlib only (`argparse`, `json`, `urllib`, `time`, `datetime`)
- exit 0 after writing capture; pass metric documented in module docstring
- long-blocking friendly; prints progress + `=== SUMMARY ===`

## Contract already named (Rule 2b, contract-only today)

```bash
python3 scripts/proof_host_probe.py \
  --url "$PROOF_URL" \
  --selector "$PROOF_HOST_SELECTOR" \
  --out gate-captures/<CODE>-ACCEPT-proof-host.json
```

Required JSON fields: `host_client_height` (number), `blank_canvas` (bool).
FAIL when `host_client_height <= 0` or `blank_canvas: true` while chrome may PASS.

Path gap: EXECUTION_WIRING cites `scripts/proof_host_probe.py`; lock places the
file beside the charter harness at `skills/charter/scripts/proof_host_probe.py`.

## Proposed CLI

| flag | role |
|---|---|
| `--url` | page URL (live mode) |
| `--selector` | CSS selector for primary product host |
| `--out` | write JSON capture path |
| `--self-check` | no browser/network; run built-in fixture cases; emit required fields |
| `--dry-run` | alias intent: document that live browser is unavailable; same as self-check for CI |

## Live vs self-check

DOM `clientHeight` needs a browser. Stdlib cannot open a real page.

- **Preferred path:** stdlib always; optional Playwright if installed for live.
- **When Playwright missing:** `--self-check` / documented dry-run must still
  emit valid JSON with required fields and exercise pass/fail logic so ACCEPT
  can prove the tool ships without a live host.
- Live mode exit non-zero with clear stderr if browser backend unavailable
  and self-check not requested.

## Blank-canvas detection (live)

- `blank_canvas: true` if host missing, `clientHeight <= 0`, or host/canvas
  carries an explicit blank-canvas class / data marker the lane documents.
- Geometry alone (`host_client_height > 0` and `blank_canvas == false`) is
  the hard gate; product-look remains out of scope (PHF-EVAL defer).

## W2a deliverable

1. Create `skills/charter/scripts/proof_host_probe.py`
2. Self-check emits JSON including `host_client_height`, `blank_canvas`,
   `mode`, `pass`, `finished`
3. Document smoke: `python3 skills/charter/scripts/proof_host_probe.py --self-check`

## Commit file list (this finding)

- `wavves/lanes/20260718_proof-host-followon/findings/PHF-probe-shape.md`
