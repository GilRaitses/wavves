# PBA — FREEZE

- **Date:** 2026-07-18
- **Lane:** wavves/lanes/20260718_proof-before-accept-check/
- **repo_state_verified_against:** af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
- **Question:** How does `chrome_freeze` interact with delivering `proof_job`?
- **Options considered:**
  - A: Absolute freeze of all chrome until Proof ACCEPT
  - B: Freeze non-proof-serving chrome; allowlist seams that may change to unblock proof_job
- **Pick:** B
- **Rationale:** Operator `¯\_(ツ)_/¯` / proceed as recommended (matches originating product repo doctrine selective freeze).
- **Implications for BUILD:** `chrome_freeze` is a path/surface list plus explicit allowlist for proof-serving edits. `PROC-CHROME-THRASH` fires on new IA/chrome outside the allowlist without a frozen proof_job.
