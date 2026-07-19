# product ACCEPT with proof bar filled

proof_required: yes
proof_job: primary product host clientHeight > 0
proof_reference: gate-captures/DEMO-ACCEPT-proof-host.json
chrome_freeze: yes
visual_accept: yes
proof_harness: evals/check_proof_before_accept.py

accept_criteria: |
  - proof_job recorded and met
  - host_height of primary product host is greater than zero
  - chrome freeze held through ACCEPT
