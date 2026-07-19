# proof_reference none without rationale

proof_required: yes
proof_job: primary product host clientHeight > 0
proof_reference: none
chrome_freeze: yes
visual_accept: yes
proof_harness: evals/check_proof_before_accept.py

accept_criteria: |
  - proof_job recorded
  - host_height check named in ACCEPT
