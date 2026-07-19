# process-only ACCEPT without proof_job

proof_required: yes
chrome_freeze: yes
visual_accept: no
visual_accept_rationale: chrome-only gate; no product host under review

accept_criteria: |
  - LAND-C merge checklist complete
  - honesty gate recorded
  - e2e shell green
  - HEAD match on origin/main
