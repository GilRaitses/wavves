# PBA — CLASSIFIER

- **Date:** 2026-07-18
- **Lane:** wavves/lanes/20260718_proof-before-accept-check/
- **repo_state_verified_against:** af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
- **Question:** How is a lane classified as needing Proof fields?
- **Options considered:**
  - A: Infer from prose keywords (product/UX/visitor)
  - B: Explicit waveset field `proof_required: yes|no|n/a`
  - C: All execution lanes require proof
- **Pick:** B — `proof_required: yes|no|n/a` on waveset
- **Rationale:** Operator `¯\_(ツ)_/¯` / proceed as recommended (closes RFU-shaped research+visitor leak).
- **Implications for BUILD:** Charter template requires the field. Defaults: visitor/product execution → `yes`; mod-check / research-discovery / plugin-meta / outbound-copy-only → `no` or `n/a` with one-line rationale. Missing field on new product/visitor lanes fails mod-decide unlock (PBA-LAND E).
