# PHF — PROBE

- **Date:** 2026-07-18
- **Lane:** wavves/lanes/20260718_proof-host-followon/
- **repo_state_verified_against:** 538437cad76764fd989cd028f64927b1ae839292
- **Question:** How does Rule 2b become live shared tooling?
- **Options considered:**
  - A: Ship stdlib `scripts/proof_host_probe.py` emitting JSON (`host_client_height`, `blank_canvas`)
  - B: Cite Playwright `clientHeight` only; no shared script
  - C: Defer probe entirely
- **Pick:** A
- **Rationale:** Operator `¯\_(ツ)_/¯` / proceed as recommended (closes named PBB gap).
- **Implications for BUILD:** Implement
  `skills/charter/scripts/proof_host_probe.py` (house harness home beside
  `transition_gap_probe.py`); EXECUTION_WIRING Rule 2b points at that path;
  ACCEPT runs a documented self-check / dry-run emitting required JSON fields.
