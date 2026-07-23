# IPB-W1d — adversarial

```yaml
lens: adversarial
wave: IPB-W1d
artifact: feature-requests/20260719_ip-before-cutover.md
repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Lens verdict (this lens only)

**REVISE**

The FR names a real, expensive failure (VIB: IP strip known, cutover wired,
ACCEPT first hard FAIL, Midtown consume rollback, then cheap manifest
redact). As written, BUILD can still ship charter prose + three soft
fixtures and leave that hole open: soft produce PASS, warn-only cutover,
checklist-only probes that miss novel keys, and Acceptance with no runnable
detector.

O0 owns the lane verdict. This file does not grade sibling lenses.

## Proposed fail ids (map)

| id | Covers | Operable in FR as written? |
|---|---|---|
| `PROC-IP-AFTER-CUTOVER` | consume cutover / "pack shipped" PASS before hard public-surface remasure | Partial. Named; no detector; soft PASS / warn-only defeat it |

### Missing fail ids (needed before BUILD ACCEPT)

| id | Why |
|---|---|
| `PROC-IP-PROBE-FAIL` | Probe ran; strip/baseline parity FAILED at produce-exit |
| `PROC-IP-PROBE-MISSING` | Cutover/seam-wire started with no probe capture |
| `PROC-IP-SOFTPASS-WIRE` | `produce_bytes_only` / pending probe treated as cutover-ready |
| `PROC-IP-WARN-ONLY-WIRE` | Missing/FAIL probe logged as warning; wire proceeded (IP-CUT-1 footgun) |
| `PROC-IP-BASELINE-POISON` | Baseline exemplar itself contains strip-banned atoms |
| `PROC-IP-CHECKLIST-GAP` | Checklist-only PASS while deny-class keys present in manifest |

Keep `PROC-IP-AFTER-CUTOVER` as the umbrella ordering failure. Do not collapse
probe-fail and probe-missing.

## Blocking failure modes

### FM-1 — Soft produce PASS becomes the VIB-W2 escape hatch

**Class:** happy-path-only / loophole that recreates the bug  
**Severity:** blocking  
**Fail ids:** `PROC-IP-SOFTPASS-WIRE` (missing), `PROC-IP-AFTER-CUTOVER`

Sketch allows `produce_bytes_only` with `cutover_blocked: ip_probe_pending`.
VIB-W2 already PASSed on hours/bbox/grid with fat manifests. A BUILD that
keeps a single `PASS` token will wire from that PASS.

**Concrete BUILD footgun:** Produce writes island packs + fat manifests,
stamps PASS, notes "ip later." Cutover dispatch reads produce PASS, amends
`/beta` roots. ACCEPT A6 FAIL → rollback. Same thrash.

**Required revise:** Closed verdict enum. Cutover precondition remasures a
durable `ip_probe` capture (`PASS`) or refuses. Fixture: produce_bytes_only
artifact presented to cutover → FAIL (`PROC-IP-SOFTPASS-WIRE`).

### FM-2 — IP-CUT-1 warn-only recreates late enforcement

**Class:** unsafe default / decide fork that undoes the FR  
**Severity:** blocking  
**Fail ids:** `PROC-IP-WARN-ONLY-WIRE` (missing)

If mod-decide picks warn-only, the pattern documents the strip and still
allows wire. That is the current failure with better logging.

**Concrete BUILD footgun:** Charter says `ip_strip_checklist` present; probe
FAIL or skipped; cutover logs warning; visitor plane serves equations/coeffs.

**Required revise:** When checklist/baseline fields are set, hard-block only.
Warn-only is non-goal (or limited to lanes that explicitly set
`ip_enforcement: advisory` with operator lock, never default).

### FM-3 — Checklist-only probe misses novel leak keys

**Class:** works on happy path only  
**Severity:** blocking  
**Fail ids:** `PROC-IP-CHECKLIST-GAP` (missing); interacts with IP-CUT-2

VIB fail atoms were concrete keys (`class_defaults` numerics, AT equation
string, combination transmittance prose). A hand-maintained checklist that
lists "no equations" without schema/allowlist remasure can PASS while new
coeff fields ship.

**Concrete BUILD footgun:** Checklist checks three banned substrings. Builder
emits `method.steadman_v2.coeffs`. Probe PASS. Cutover ships. ACCEPT may or
may not catch it depending on matrix drift.

**Required revise:** Default probe = allowlist / public_contract shape vs
approved baseline **plus** deny-key/deny-pattern scan from checklist. Not
naive whole-pack byte-diff (island ids/bbox differ). Fixture: novel coeff key
absent from checklist text but outside allowlist → FAIL.

### FM-4 — Poisoned or wrong baseline rubber-stamps fat packs

**Class:** unsafe default  
**Severity:** blocking  
**Fail ids:** `PROC-IP-BASELINE-POISON` (missing)

`public_baseline_pack` pointing at a fat or wrong exemplar makes parity
PASS meaningless. Midtown `*_20260701` worked as baseline only because it
was already public_contract-shaped (illustration remasure on klosr tip).

**Concrete BUILD footgun:** Charter sets baseline = previous island fat
manifest. Probe "parity" PASS. Strip doctrine bypassed.

**Required revise:** Baseline must be an approved public-surface exemplar
(operator lock or doctrine pin). Probe FAILS if baseline itself matches
deny-class atoms. Fixture: baseline with equation string →
`PROC-IP-BASELINE-POISON`.

### FM-5 — Acceptance gates cannot actually run

**Class:** gate that can't run / process-PASS  
**Severity:** blocking  

Sketch names three eval behaviors; no harness path. Charter today has no
`ip_probe` command. Sibling pattern shows the bar:
`evals/check_proof_before_accept.py` + `proof_host_probe.py`.

**Concrete BUILD footgun:** Three markdown fixtures under `evals/fixtures/`
with expected keywords. BUILD ACCEPT greens. Live produce/cutover still
orders as VIB.

**Required revise:** Mechanical checker over synthetic manifests + synthetic
waveset/cutover stubs. Minimum emit: `PROC-IP-PROBE-FAIL`,
`PROC-IP-PROBE-MISSING`, `PROC-IP-SOFTPASS-WIRE`,
`PROC-IP-AFTER-CUTOVER`. BUILD ACCEPT requires checker PASS, not docs-only.

### FM-6 — Pattern optional by omission (absent fields = no gate)

**Class:** silent skip  
**Severity:** blocking  
**Fail ids:** `PROC-IP-PROBE-MISSING`, `PROC-IP-AFTER-CUTOVER`

Sketch: fields apply "when lane publishes public packs or amends visitor
consume roots." If BUILD makes fields optional and omission skips the gate,
pack lanes will omit them under schedule pressure (exact VIB incentives).

**Concrete BUILD footgun:** Waveset has W-produce + W-cutover, no
`ip_strip_checklist`. Orchestrator treats pattern N/A. Wire proceeds.

**Required revise:** Classifier field (e.g. `publishes_public_packs: yes|no`
or non-empty `cutover_requires`) with default for visitor consume amend =
yes. Omission on cutover-capable lanes → FAIL, not skip. Fixture: cutover
wave without checklist/baseline → `PROC-IP-PROBE-MISSING`.

### FM-7 — Re-emit after probe without re-probe

**Class:** TOCTOU / thrash twin  
**Severity:** blocking  
**Fail ids:** `PROC-IP-AFTER-CUTOVER`, `PROC-IP-PROBE-MISSING`

VIB-R1 patched builders after FAIL. A lane could ip_probe PASS, then rebuild
manifests, then cutover on stale PASS.

**Concrete BUILD footgun:** Probe PASS at T0. Produce resumes hour rebuild
rewriting manifest with coeffs. Cutover uses T0 capture. ACCEPT FAIL.

**Required revise:** Probe capture must hash the exact manifest/asset set
cutover will wire; cutover remasures hash match or re-runs probe. Stale
capture → FAIL.

## Non-blocking failure modes

### FM-8 — ACCEPT remasure removed "to avoid duplication"

**Severity:** non-blocking (Non-goals already forbid)  

Pressure to delete ACCEPT A6-class checks once pre-wire exists. Defense in
depth is the point.

**Revise ask:** Keep Non-goals bullet; Acceptance requires both pre-wire
probe fixture and an ACCEPT-still-remasures docs/fixture note.

### FM-9 — Scope creep to all public assets without cost model

**Severity:** non-blocking  

"Authority-before-wire" for every public asset (homepage, docs, graphs)
without classifier creates either ignored gates or constant false alarms.

**Revise ask:** v0 = visitor consume packs / public bake manifests (IP-CUT-3
lean visitor-plane); expand later with explicit asset classes.

### FM-10 — Foreign VIB/klosr paths hardcoded into plugin playbooks

**Severity:** non-blocking (dispatch: illustration only)  

**Revise ask:** Examples stay illustrative; fixtures synthetic under
`evals/fixtures/`.

### FM-11 — Cutover measured-transition Rule 1 confused with IP probe

**Severity:** non-blocking  

`EXECUTION_WIRING.md` Rule 1 already uses "cutover" for probe-across-deploy
liveness gaps. An implementer may bolt IP checks into transition_gap_probe
instead of a manifest strip probe.

**Revise ask:** Separate rule id (e.g. Rule 2c ip-before-cutover) distinct
from Rule 1 transition measurement.

## What would change REVISE → GO (this lens)

1. Closed produce verdict tokens; cutover binds `ip_probe` capture only.
2. Hard-block when IP fields present; warn-only non-goal (or explicit lock).
3. Probe class = allowlist/public_contract parity + deny scan; not naive
   byte-diff; checklist-gap fixture.
4. Baseline poison detector.
5. Mechanical eval harness with operable fail ids.
6. Omission on cutover-capable lanes FAILS.
7. Probe capture hash-binds artifacts cutover will wire.

## Out of scope for this lens

- Grounding of foreign path prefixes (W1a)
- Internal FR contradictions inventory (W1b)
- Completeness Acceptance section inventory (W1c)
- Implementation plan or code

## Commit file list (orchestrator only)

- `wavves/lanes/20260719_ip-before-cutover-check/findings/IPB-adversarial.md` (this file)

No git. Escalation to O0 only.
