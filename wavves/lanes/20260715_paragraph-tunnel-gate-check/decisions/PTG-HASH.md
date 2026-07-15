# PTG — HASH

- **Date:** 2026-07-15
- **Lane:** wavves/lanes/20260715_paragraph-tunnel-gate-check/
- **repo_state_verified_against:** f2fb8ce144b68d820b0992f5075a2cbbf44673d2
- **Question:** How should the FR cite evidence commits?
- **Options considered:**
  - A: Split `evidence_verified_against` (pre-landing) vs `landing_commit_hash`; never equate
  - B: Keep single field as today
- **Pick:** A
- **Rationale:** Proceed-as-recommended. Grounding G1: FR labeled landing `21b1d7cf` as verified-against; artifacts record `079f4c4c`.
- **Implications for BUILD:** Patch FR before charter; follow house self-referential hash rule.
