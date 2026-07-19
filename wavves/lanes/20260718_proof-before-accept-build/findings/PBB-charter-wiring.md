# PBB-W1c — charter-wiring-seams

```yaml
lens: charter-wiring-seams
wave: PBB-W1c
repo_state_verified_against: 517dd85190cf93cf744434338dec4b1eb1d859c5
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Verdict (this lens)

Land C patches are **draft-only in findings** until PBB-INT. Do not edit
`skills/charter/SKILL.md` or `EXECUTION_WIRING.md` in W2.

## Seam map (where INT will patch)

### 1. `skills/charter/SKILL.md` — waveset Meta / authority sections

**Insert after** the waveset section list that names lane code, owner, type,
`repo_state_verified_against` (approx. lines 117–122 today):

- Required Meta field: `proof_required: yes|no|n/a`
- When `yes`, require four fields with homes:
  - `proof_job` — waveset Intent or Meta table
  - `proof_reference` — waveset Meta / Grounding
  - `chrome_freeze` — waveset Locked decisions or Meta (path list +
    proof-serving allowlist)
  - `visual_accept` — waveset Meta (`yes`/`no` + rationale if `no`)
- Acceptance criteria must name a runnable proof gate (mechanical and/or
  DOM/host), not process-only LAND-C / honesty / e2e shell.
- Defaults (guidance, not keyword inference): visitor/product execution →
  `yes`; research/check/plugin-meta/outbound-copy → `no`/`n/a` + rationale.

### 2. `skills/charter/EXECUTION_WIRING.md` — new Rule after Rule 2 or as Rule 2b

**Named harness rule (hard):**

- On `proof_required: yes`, ACCEPT FAILS if:
  - `proof_job` unset, or
  - no capture under `gate-captures/` from a named proof command, or
  - primary product host height ≤ 0 / blank-canvas class while chrome PASS
- Mechanical tripwire for method fixtures:
  `python3 evals/check_proof_before_accept.py`
- Screenshot-vs-reference: optional operator step when `visual_accept: yes`
- Freeze: non-proof-serving chrome frozen; proof-serving allowlist may edit
  (PBA-FREEZE)
- Implements house visual-verification rule for ACCEPT (cite, one sentence)

### 3. mod-decide AUTH (E) — noted for W2d draft

AUTH-01 sync must include `proof_required` / `proof_job` on waveset locks
before BUILD unlock when `proof_required: yes`. Seam is
`skills/mod-decide/SKILL.md` step 5b, not charter alone.

## Anti-patterns (from PBA-adversarial)

- Docs-only BUILD ACCEPT (FM-1)
- Assertion-only visual gate (FM-2)
- Lens-keyword tripwire via `run_fixtures.py` as sole eval (FM-3)
- Agent opt-out without rationale (FM-4)
- Marker-only honesty without host geometry (FM-5)

## W2c ownership

`findings/PBB-charter-SKILL-patch.md` +
`findings/PBB-EXECUTION_WIRING-patch.md` (draft text ready to apply in INT).

## Commit file list

- `wavves/lanes/20260718_proof-before-accept-build/findings/PBB-charter-wiring.md`

No git. Escalation to O0 only.
