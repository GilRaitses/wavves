# PBB W1+W2 return (pause before INT/ACCEPT)

```yaml
lane: PBB
repo_state_verified_against: 517dd85190cf93cf744434338dec4b1eb1d859c5
waves_run: [PBB-W1a, PBB-W1b, PBB-W1c, PBB-W1d, PBB-W2a, PBB-W2b, PBB-W2c, PBB-W2d]
gated_paused: [PBB-INT, PBB-ACCEPT]
git_actions: none
model: cursor-grok-4.5-high-fast
```

## Gate verdicts (W1/W2 only)

| wave | verdict | notes |
|---|---|---|
| W1 discovery | complete | four findings under `findings/PBB-*.md` |
| W2a playbook | complete | NEW playbook |
| W2b checker | PASS | `python3 evals/check_proof_before_accept.py` → pass=4 fail=0 |
| W2c/d skill drafts | complete | drafts only; SKILL.md files untouched |
| paragraph-tunnel regression | PASS | check_paragraph_tunnel.py pass=6 fail=0 |
| `/proof-gate` absent | PASS | no skill dir |

## Smoke (measured)

```text
PASS  proof-before-accept-no-visual-fail: verdict=FAIL fail_ids=['PROC-NO-VISUAL']
PASS  proof-before-accept-optout-no-rationale-fail: verdict=FAIL fail_ids=['PROC-PASS-NO-PROOF']
PASS  proof-before-accept-proc-pass-no-proof-fail: verdict=FAIL fail_ids=['PROC-PASS-NO-PROOF']
PASS  proof-before-accept-with-proof-pass: verdict=PASS fail_ids=[]
summary: pass=4 fail=0 total=4
exit: 0
```

## Escalation / pause for O0

Unlock **PBB-INT** to apply skill patches (single editor):

1. `findings/PBB-charter-SKILL-patch.md` → `skills/charter/SKILL.md`
2. `findings/PBB-EXECUTION_WIRING-patch.md` → `skills/charter/EXECUTION_WIRING.md`
3. `findings/PBB-mod-check-patch.md` → `skills/mod-check/SKILL.md`
4. `findings/PBB-mod-decide-patch.md` → `skills/mod-decide/SKILL.md`
5. `findings/PBB-wavves-router-patch.md` → `skills/wavves/SKILL.md`

Then unlock **PBB-ACCEPT** (independent evaluator preferred): re-run checker,
capture JSON under `gate-captures/PBB-ACCEPT-proof.json`, spot-check locks.

## Gaps

- Live `scripts/proof_host_probe.py` not shipped; EXECUTION_WIRING draft names
  the contract + example command for product lanes to bind.
- Review-only PROC ids remain non-mechanical (by lock).
- Registry / step-log updates deferred to O0 reconcile.
- No gate-captures JSON yet (ACCEPT wave).

## Commit file list for O0

### NEW
- `skills/wavves/playbooks/proof-before-accept.md`
- `evals/check_proof_before_accept.py`
- `evals/fixtures/proof-before-accept-proc-pass-no-proof-fail/{input.md,expected.md}`
- `evals/fixtures/proof-before-accept-with-proof-pass/{input.md,expected.md}`
- `evals/fixtures/proof-before-accept-optout-no-rationale-fail/{input.md,expected.md}`
- `evals/fixtures/proof-before-accept-no-visual-fail/{input.md,expected.md}`
- `wavves/lanes/20260718_proof-before-accept-build/` (waveset, dispatch, README, findings/*, decisions/)

### MODIFIED
- `evals/README.md` (proof-before-accept section)
- `feature-requests/README.md` (status)
- `feature-requests/20260718_proof-before-accept.md` (status)

### EXCLUDE until INT
- `skills/charter/SKILL.md`
- `skills/charter/EXECUTION_WIRING.md`
- `skills/mod-check/SKILL.md`
- `skills/mod-decide/SKILL.md`
- `skills/wavves/SKILL.md`

No git performed by runners.
