# wavves index

current_identity: O0
current_rotation: none

active_lanes:
  - code: RTH
    home: lanes/20260723_mod-rotate-theory-research/
    status: chartered-dispatch
    next_read: lanes/20260723_mod-rotate-theory-research/dispatch-w1.md
    note: research into mod-rotate theory; W1 orch dispatched; INT gated
  - code: WOF
    home: lanes/20260723_wave-orchestrator-fanout-check/
    status: completed
    next_read: lanes/20260723_wave-orchestrator-fanout-check/findings/WOF-verdict.md
    note: blocks_w2 cleared by WOFB
  - code: WOFB
    home: lanes/20260723_wave-orchestrator-fanout-build/
    status: completed
    next_read: lanes/20260723_wave-orchestrator-fanout-build/findings/WOFB-GATE.md
    note: orch fan-out + mod etiquette SHIPPED; eval 11/11
  - code: PUO
    home: lanes/20260723_pre-unlock-options-check/
    status: check-revise
    next_read: lanes/20260723_pre-unlock-options-check/findings/PUO-verdict.md
  - code: IPB
    home: lanes/20260719_ip-before-cutover-check/
    status: check-revise
    next_read: lanes/20260719_ip-before-cutover-check/findings/IPB-verdict.md
  - code: MDA
    home: lanes/20260722_mod-decide-alignment-check/
    status: check-revise
    next_read: lanes/20260722_mod-decide-alignment-check/findings/MDA-verdict.md
  - code: PAS
    home: lanes/20260723_proceed-all-standing-check/
    status: check-revise-awaiting-decide
    next_read: lanes/20260723_proceed-all-standing-check/decisions/PAS-DECIDE-QUEUE.md
    note: FR revised-after-PAS; mod-decide residual COMMIT-AUTH-GRAIN
  - code: PTB
    home: lanes/20260715_paragraph-tunnel-build/
    status: completed
    next_read: lanes/20260715_paragraph-tunnel-build/gate-captures/PTB-ACCEPT.md
  - code: PTG
    home: lanes/20260715_paragraph-tunnel-gate-check/
    status: completed
    next_read: lanes/20260715_paragraph-tunnel-gate-check/decisions/LOCKED-DECISIONS.md
  - code: PBA
    home: lanes/20260718_proof-before-accept-check/
    status: mod-decide-complete
    next_read: lanes/20260718_proof-before-accept-check/decisions/LOCKED-DECISIONS.md
  - code: PBB
    home: lanes/20260718_proof-before-accept-build/
    status: completed
    next_read: lanes/20260718_proof-before-accept-build/gate-captures/PBB-ACCEPT.md
  - code: PHF
    home: lanes/20260718_proof-host-followon/
    status: completed
    next_read: lanes/20260718_proof-host-followon/gate-captures/PHF-ACCEPT.md
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
    - id: FR-20260723-wave-orchestrator-fanout
      path: ../feature-requests/20260723_wave-orchestrator-fanout.md
      status: shipped
      check_lane: lanes/20260723_wave-orchestrator-fanout-check/
      build_lane: lanes/20260723_wave-orchestrator-fanout-build/
    - id: FR-20260723-proceed-all-standing
      path: ../feature-requests/20260723_proceed-all-standing.md
      status: revised-after-PAS
      check_lane: lanes/20260723_proceed-all-standing-check/
    - id: FR-20260720-pre-unlock-options-mod-check
      path: ../feature-requests/20260720_pre-unlock-options-mod-check.md
      status: ready-for-mod-check
    - id: FR-20260719-ip-before-cutover
      path: ../feature-requests/20260719_ip-before-cutover.md
      status: ready-for-mod-check
  shipped:
    - id: FR-20260715-paragraph-tunnel
      path: ../feature-requests/20260715_paragraph-tunnel-gate.md
      status: shipped
    - id: FR-20260718-proof-before-accept
      path: ../feature-requests/20260718_proof-before-accept.md
      status: shipped

model_policy:
  default: record recommendation before dispatch
  subagent_model_lock: cursor-grok-4.5-high-fast
  high_reasoning: architecture, integration, adversarial review, acceptance
  note: PTB/PTG require Grok for every subagent. No Claude/Composer fallback.
