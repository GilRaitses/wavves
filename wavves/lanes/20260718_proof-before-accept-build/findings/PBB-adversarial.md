# PBB-W1d — adversarial (build footguns)

```yaml
lens: adversarial
wave: PBB-W1d
repo_state_verified_against: 517dd85190cf93cf744434338dec4b1eb1d859c5
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Verdict (this lens)

**REVISE until W2 ships runnables.** Carry PBA-adversarial FM-1..FM-5 into
build: process-PASS ACCEPT of the *pattern* is still possible if W2 only
writes prose. Block BUILD-lane self-ACCEPT on docs; require mechanical
checker PASS with PROC-PASS-NO-PROOF FAIL fixture.

## Footguns for W2 (do not ship)

| id | Footgun | Mitigation in W2 |
|---|---|---|
| BF-1 | Docs-only ACCEPT of proof-before-accept | Checker + FAIL fixture required before claiming W2 done; ACCEPT gated |
| BF-2 | Put fixtures under `run_fixtures.py` lens-keyword path | Disjoint `check_proof_before_accept.py` only |
| BF-3 | Edit charter/mod-check/mod-decide/wavves SKILL.md in W2 | Drafts under `findings/` only; INT gated |
| BF-4 | Create `/proof-gate` skill | Forbidden (PBA-LAND defer A) |
| BF-5 | Touch `paragraph-tunnel-*` or overload tunnel checker | Prefix `proof-before-accept-*` only |
| BF-6 | Emit review-only PROC ids from mechanical script | Only PROC-PASS-NO-PROOF + PROC-NO-VISUAL (+ opt-out as PASS-NO-PROOF) |
| BF-7 | Allow `visual_accept: no` / `proof_reference: none` without rationale | Fixture + detector |
| BF-8 | Absolute chrome freeze blocking proof delivery | Freeze allowlist (PBA-FREEZE) |
| BF-9 | Router row early | Defer to INT |
| BF-10 | Claim screenshot hard gate | DOM/host hard; screenshot optional (PBA-HARNESS) |

## Process-PASS ACCEPT ban (lane self-discipline)

PBB-ACCEPT must not green on:

- playbook file exists
- patch drafts exist
- FR status updated

without:

1. `python3 evals/check_proof_before_accept.py` → PASS all fixtures
2. JSON capture under `gate-captures/PBB-ACCEPT-proof.json`
3. Spot-check playbook + EXECUTION_WIRING draft names harness, classifier,
   freeze allowlist, opt-out rationale
4. Confirm no `/proof-gate` directory
5. Confirm paragraph-tunnel surfaces untouched

(W2 stops before that gate; this finding locks the ACCEPT bar for O0.)

## Residual risks after W2 (for INT/ACCEPT)

- Live DOM probe script may be example-only in EXECUTION_WIRING draft until
  a consuming product lane binds selectors.
- PROC-CHROME-THRASH / PROC-DEBT-AS-DONE remain review-only in wavves_build.
- Router + real skill patches await INT.

## Commit file list

- `wavves/lanes/20260718_proof-before-accept-build/findings/PBB-adversarial.md`

No git. Escalation to O0 only.
