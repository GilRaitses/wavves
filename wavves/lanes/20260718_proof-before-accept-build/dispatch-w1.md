# PBB-W1+W2 dispatch — UNLOCKED

```yaml
authority_precedence:
  order:
    - path: ../20260718_proof-before-accept-check/decisions/LOCKED-DECISIONS.md
      role: primary_locks
    - path: decisions/LOCKED-DECISIONS.md
      role: local_locks_copy
    - path: waveset.md
      role: wave_plan
    - path: ../../feature-requests/20260718_proof-before-accept.md
      role: fr_under_build
```

```text
ROLE: You are the PBB lane orchestrator. Run W1 then W2. Pause before INT/ACCEPT.
HOME: /Users/gilraitses/wavves_build/wavves/lanes/20260718_proof-before-accept-build/
REPO: /Users/gilraitses/wavves_build (branch main, HEAD 517dd85190cf93cf744434338dec4b1eb1d859c5)
LOCKS: ../20260718_proof-before-accept-check/decisions/LOCKED-DECISIONS.md

HYDRATE:
  1. waveset.md
  2. LOCKED-DECISIONS (check lane)
  3. feature-requests/20260718_proof-before-accept.md
  4. skills/wavves/playbooks/paragraph-tunnel.md (shape)
  5. evals/check_paragraph_tunnel.py + evals/README.md
  6. skills/charter/SKILL.md + EXECUTION_WIRING.md
  7. skills/mod-check/SKILL.md + skills/mod-decide/SKILL.md
  8. findings/PBA-adversarial.md (footguns to avoid)

MISSION:
  Run PBB-W1 then PBB-W2 per waveset. Write findings incrementally.
  W2: prefer NEW files for playbook + checker + fixtures.
  Skill-file patches (charter, mod-check, mod-decide, wavves router) as
  findings drafts only — do NOT edit those SKILL.md files until O0 unlocks INT.
  Update evals/README.md tunnel-style section for proof fixtures (disjoint).
  Patch FR status / feature-requests index toward chartered-build.
  STOP before PBB-INT / PBB-ACCEPT. Return commit file list.

LOCKS INLINE:
  LAND=C+D+B+E; defer A
  CLASSIFIER=proof_required yes|no|n/a
  HARNESS=DOM/host hard + check_proof_before_accept.py; screenshot optional
  FREEZE=non-proof-serving + proof-serving allowlist
  OPTOUT=rationale required on proof_required:yes
  LENS=proof-bar conditional default

MODEL: every subagent model: cursor-grok-4.5-high-fast. No Claude/Composer.

GIT BAN: no git.

ESCALATION: to O0 only. Never solicit the human operator.

RETURN CONTRACT:
  - waves run + gate verdicts + capture paths
  - commit file list for O0
  - escalations / pause for INT+ACCEPT
  - gaps for anything promised but not delivered
```
