# PTG — EVAL

- **Date:** 2026-07-15
- **Lane:** wavves/lanes/20260715_paragraph-tunnel-gate-check/
- **repo_state_verified_against:** f2fb8ce144b68d820b0992f5075a2cbbf44673d2
- **Question:** How must acceptance be runnable?
- **Options considered:**
  - A: evals/fixtures/paragraph-tunnel-*/ with input.md + expected.md (fail ids / PASS) + runner
  - B: Lane-local captures only (APPL-style JSON) as acceptance
  - C: Prose acceptance sketch only
- **Pick:** A
- **Rationale:** Proceed-as-recommended. FM-1: sketch is unrunnable. Must include at least one PN-FIXTURE / stand-in case, not only the three happy-path shops.
- **Implications for BUILD:** Fixture corpus + pass metric before ACCEPT; independent of LLM self-grade where possible (expected fail_ids).
