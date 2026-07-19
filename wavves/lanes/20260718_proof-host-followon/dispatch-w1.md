# PHF-W1+W2 dispatch — UNLOCKED

```yaml
authority_precedence:
  order:
    - path: decisions/LOCKED-DECISIONS.md
      role: primary_locks
    - path: waveset.md
      role: wave_plan
    - path: ../../feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md
      role: originating_mod_source
```

```text
ROLE: You are the PHF lane orchestrator. Run W1 then W2. Pause before INT/ACCEPT if needed.
HOME: wavves/lanes/20260718_proof-host-followon/
REPO: <repo-root> (branch main, HEAD 538437cad76764fd989cd028f64927b1ae839292)

HYDRATE:
  1. waveset.md + decisions/LOCKED-DECISIONS.md
  2. ORIGINATING-MOD-FEEDBACK.md
  3. skills/charter/EXECUTION_WIRING.md Rule 2b
  4. skills/charter/scripts/transition_gap_probe.py (shape)
  5. skills/wavves/playbooks/proof-before-accept.md
  6. PBB-ACCEPT.md (known gap)

MISSION:
  W1: probe-shape, playbook-harden, adversarial findings.
  W2: NEW skills/charter/scripts/proof_host_probe.py (stdlib; JSON fields
      host_client_height, blank_canvas); wire EXECUTION_WIRING Rule 2b to
      that path; harden playbook visual_accept:yes (DOM green ≠ done;
      capture-then-grade required). No product-look lane port. No PBB reopen.
  Prefer applying playbook + EXECUTION_WIRING in W2 if single-editor safe;
  otherwise draft INT patches under findings/.
  STOP before PHF-ACCEPT (and INT if still gated). Return commit file list.

LOCKS: SCOPE=S2; PROBE=charter/scripts/proof_host_probe.py; EVAL=defer; ETIQUETTE=park

MODEL: cursor-grok-4.5-high-fast every subagent. No Claude/Composer.
GIT BAN: no git.
ESCALATION: O0 only.
```
