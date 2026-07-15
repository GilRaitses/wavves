# PTG — MODEL

- **Date:** 2026-07-15
- **Lane:** wavves/lanes/20260715_paragraph-tunnel-gate-check/
- **repo_state_verified_against:** f2fb8ce144b68d820b0992f5075a2cbbf44673d2
- **Question:** Model tier for adversarial + rewrite gates?
- **Options considered:**
  - A: cursor-grok-4.5-high-fast for both (house subagent lock)
  - B: Mixed (Grok adversarial / other rewrite)
  - C: Unspecified high-reasoning
- **Pick:** A
- **Rationale:** Operator lock — all must be Grok. Same for BUILD subagents.
- **Implications for BUILD:** Dispatch prompts hard-code Grok; no Claude/Composer fallback for tunnel lenses.
