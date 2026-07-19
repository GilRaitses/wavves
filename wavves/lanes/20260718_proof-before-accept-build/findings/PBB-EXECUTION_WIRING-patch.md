# PBB-W2c draft — EXECUTION_WIRING.md patch (APPLY IN INT ONLY)

```yaml
wave: PBB-W2c
target: skills/charter/EXECUTION_WIRING.md
apply_in: PBB-INT
git_actions: none
status: DRAFT — do not apply until O0 unlocks INT
```

## Placement

Insert as **Rule 2b, proof-before-accept (DOM/host hard gate)** immediately
after Rule 2 ("gates are runnable. evidence is captured") and before Rule 3.

## Patch text (insert)

```markdown
## Rule 2b, proof-before-accept (DOM/host hard gate)

When a lane sets `proof_required: yes`, ACCEPT is a product Proof gate, not
a process green. This rule implements the house visual-verification
requirement for ACCEPT. Purpose-gates and public-copy-gates stay
copy-scoped and are not replaced.

### Classifier and fields

Waveset Meta must carry `proof_required: yes|no|n/a`. On `yes`, require
`proof_job`, `proof_reference`, `chrome_freeze` (non-proof-serving freeze +
proof-serving allowlist), and `visual_accept`. On `proof_required: yes`,
`proof_reference: none` or `visual_accept: no` without a written rationale
FAIL. Missing `proof_job` FAIL.

### Mechanical method checker (fixtures)

```bash
python3 evals/check_proof_before_accept.py
```

Stdlib only. Discovers `evals/fixtures/proof-before-accept-*/`. Emits
mechanical fail ids (`PROC-PASS-NO-PROOF`, `PROC-NO-VISUAL`). Does not
replace a live product ACCEPT.

### Live DOM / primary product host harness (hard)

Define pass metric before the run. Prefer dependency-free host geometry:

```bash
# Bind URL + CSS selector for the primary product host (lane-specific).
# Fail if clientHeight <= 0 or blank-canvas class while chrome may PASS.
python3 scripts/proof_host_probe.py \
  --url "$PROOF_URL" \
  --selector "$PROOF_HOST_SELECTOR" \
  --out gate-captures/<CODE>-ACCEPT-proof-host.json
```

If `scripts/proof_host_probe.py` is not yet in-repo, the lane MUST still
name an equivalent runnable command that writes JSON with at least
`host_client_height` and `blank_canvas` (bool) and FAIL when
`host_client_height <= 0` or `blank_canvas: true` while chrome gates PASS.

Pass metric examples:

- `host_client_height > 0` AND `blank_canvas == false`
- named proof markers alone without geometry are insufficient for
  visitor/product Proof (honesty/shell PASS is not Proof)

Capture path under lane `gate-captures/`. Verdict cites measured numbers
and the command that produced the capture. Hand-authored summaries FAIL.

### Screenshot (optional)

When `visual_accept: yes` and the environment supports it, capture
screenshot-vs-reference under `gate-captures/` as an operator/visual step.
Screenshot is never the sole hard gate; DOM/host metrics remain required.

### Chrome freeze

Until Proof ACCEPT, do not edit paths listed in `chrome_freeze` except
those on the proof-serving allowlist. New IA/chrome outside the allowlist
without a frozen `proof_job` is `PROC-CHROME-THRASH` (review gate).

### Closed fail vocabulary (method)

| id | class | notes |
|---|---|---|
| PROC-PASS-NO-PROOF | mechanical + ACCEPT | process/shell green without measured proof_job |
| PROC-NO-VISUAL | mechanical | visual_accept required but no named harness |
| PROC-BLANK-CANVAS | live harness | primary host height ≤ 0 or blank class |
| PROC-CHROME-THRASH | review | chrome outside allowlist, no frozen proof_job |
| PROC-DEBT-AS-DONE | review | residual debt close treated as product PASS |
```

## Checklist addendum

Append to "Checklist for a gate-running wave":

```markdown
- [ ] If proof_required: yes — proof_job measured; DOM/host JSON capture present; process-only gates not treated as sufficient
```

## Do not

- Make screenshot the only hard gate
- Claim live DOM without a named command + JSON fields
- Apply until INT

## Commit file list (after INT applies)

- `skills/charter/EXECUTION_WIRING.md` (INT only)
