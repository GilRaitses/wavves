# wavves index

current_identity: O0.R1
current_rotation: none (bootstrap term, no rotation file yet)

active_lanes:
  - code: SELF
    home: lanes/20260709_wavves-self-improvement/
    status: completed
    next_read: lanes/20260709_wavves-self-improvement/gate-captures/SELF-ACCEPT.md
  - code: LAYOVER
    home: lanes/20260709_layover-preflight/
    status: completed
    next_read: wavves/layovers/curl-20260709.md

blocked_decisions:
  - parked: mod-decide skill patch (broaden "when to use" beyond the
    check->decide->charter gate, add safely-decidable auto-progression
    criteria, sync the "Invoke once per queue" drift between repo source
    and installed plugin copy). Operator held this on 2026-07-09 to finish
    the active decision queue first. Drafted, not applied. Re-raise at the
    start of a future /mod-decide invocation.

project_skills:
  proposed: skills/proposed/
  accepted: skills/accepted/

feature_requests:
  home: ../feature-requests/
  open:
    - id: FR-20260715-paragraph-tunnel
      path: ../feature-requests/20260715_paragraph-tunnel-gate.md
      status: draft

model_policy:
  default: record recommendation before dispatch
  high_reasoning: architecture, integration, adversarial review, acceptance
  balanced: bounded implementation with local validation
  fast: inventory, search, formatting, link checks, mechanical scans
  note: this repo has no confirmed model-slug mapping yet. tier names only
    until an operator confirms concrete slugs available in this environment.
