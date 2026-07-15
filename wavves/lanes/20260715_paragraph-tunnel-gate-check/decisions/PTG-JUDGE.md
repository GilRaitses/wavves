# PTG — JUDGE

- **Date:** 2026-07-15
- **Lane:** wavves/lanes/20260715_paragraph-tunnel-gate-check/
- **repo_state_verified_against:** f2fb8ce144b68d820b0992f5075a2cbbf44673d2
- **Question:** How is rewrite re-checked without self-grade gaming?
- **Options considered:**
  - A: Separate re-adversarial step + capture; freeze checksum on sibling paragraphs
  - B: Same agent inline PASS claim sufficient
  - C: Human-only re-check
- **Pick:** A
- **Rationale:** Proceed-as-recommended. Same model (Grok) allowed; separate capture required.
- **Implications for BUILD:** Two captures after rewrite; opener/close hash must match pre-tunnel.
