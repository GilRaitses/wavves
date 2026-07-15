# wavves index

current_identity: O0
current_rotation: none

active_lanes:
  - code: PTB
    home: lanes/20260715_paragraph-tunnel-build/
    status: chartered-dispatched-w1w2
    next_read: lanes/20260715_paragraph-tunnel-build/dispatch-w1.md
  - code: PTG
    home: lanes/20260715_paragraph-tunnel-gate-check/
    status: mod-decide-complete-awaiting-build
    next_read: lanes/20260715_paragraph-tunnel-gate-check/decisions/LOCKED-DECISIONS.md
  - code: SELF
    home: lanes/20260709_wavves-self-improvement/
    status: completed
    next_read: lanes/20260709_wavves-self-improvement/gate-captures/SELF-ACCEPT.md
  - code: LAYOVER
    home: lanes/20260709_layover-preflight/
    status: completed
    next_read: wavves/layovers/curl-20260709.md

project_skills:
  proposed: skills/proposed/
  accepted: skills/accepted/

feature_requests:
  home: ../feature-requests/
  open:
    - id: FR-20260715-paragraph-tunnel
      path: ../feature-requests/20260715_paragraph-tunnel-gate.md
      status: locks-complete-ptb-building

model_policy:
  default: record recommendation before dispatch
  subagent_model_lock: cursor-grok-4.5-high-fast
  high_reasoning: architecture, integration, adversarial review, acceptance
  note: PTB/PTG require Grok for every subagent. No Claude/Composer fallback.
