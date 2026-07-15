# PTG — FAIL-CAP

- **Date:** 2026-07-15
- **Lane:** wavves/lanes/20260715_paragraph-tunnel-gate-check/
- **repo_state_verified_against:** f2fb8ce144b68d820b0992f5075a2cbbf44673d2
- **Question:** What happens after rewrite loop cap 1 still FAILs?
- **Options considered:**
  - A: Escalate to operator REVISE; do not auto-pass; do not second rewrite
  - B: Silent keep original paragraph
  - C: Raise loop cap to 2 (charter default)
- **Pick:** A
- **Rationale:** Proceed-as-recommended. Safer than silent pass; stricter than charter default is OK for outbound copy.
- **Implications for BUILD:** Capture `post_cap: escalate` in rewrite JSON; preview/send blocked until operator revise.
