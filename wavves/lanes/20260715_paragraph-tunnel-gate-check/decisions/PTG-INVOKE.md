# PTG — INVOKE

- **Date:** 2026-07-15
- **Lane:** wavves/lanes/20260715_paragraph-tunnel-gate-check/
- **repo_state_verified_against:** f2fb8ce144b68d820b0992f5075a2cbbf44673d2
- **Question:** Who invokes the tunnel, when, on which field?
- **Options considered:**
  - A: Lane runner in dispatch STEPS; after render; before prose_lint; field named in waveset
  - B: O0 only, opt-in
  - C: Inside mod-check wave
- **Pick:** A
- **Rationale:** Operator proceed-as-recommended. Matches APPL live order. Strike C (wrong phase).
- **Implications for BUILD:** Playbook + dispatch template must name `tunnel_field` (default body paragraph 2) and hard-fail if skipped on CLEARED-preview outbound lanes.
