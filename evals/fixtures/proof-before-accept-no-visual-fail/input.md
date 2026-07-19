# visual_accept yes without harness

proof_required: yes
proof_job: primary product host clientHeight > 0
proof_reference: gate-captures/DEMO-ACCEPT-proof-host.json
chrome_freeze: yes
visual_accept: yes

accept_criteria: |
  - proof_job recorded
  - host_height of primary product host is greater than zero
