# PBA — OPTOUT

- **Date:** 2026-07-18
- **Lane:** wavves/lanes/20260718_proof-before-accept-check/
- **repo_state_verified_against:** af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
- **Question:** When may `proof_reference: none` or `visual_accept: no`?
- **Options considered:**
  - A: Freely allowed
  - B: On `proof_required: yes`, each requires a written rationale; missing rationale → FAIL
  - C: Forbidden entirely on proof_required: yes
- **Pick:** B
- **Rationale:** Operator `¯\_(ツ)_/¯` / proceed as recommended.
- **Implications for BUILD:** Schema requires rationale strings; mechanical fixtures cover missing-rationale FAIL. Does not waive `proof_job` itself on `proof_required: yes`.
