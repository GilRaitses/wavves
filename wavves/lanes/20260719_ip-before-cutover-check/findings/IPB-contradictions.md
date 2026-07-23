# IPB-W1b — contradictions

- **Artifact:** `feature-requests/20260719_ip-before-cutover.md`
- **Repo pin:** `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5`
- **Hydrated:** artifact; `skills/charter/SKILL.md`;
  `skills/charter/EXECUTION_WIRING.md`;
  `skills/wavves/playbooks/proof-before-accept.md`;
  sibling FR `feature-requests/20260718_proof-before-accept.md`;
  foreign pax VIB IP delta / W2 / W3 / ROLLBACK / R1 (illustration)
- **Lens:** internal conflicts, phase-boundary leaks, mutually exclusive
  requirements
- **Git:** none. Commits: none.

## CX-* conflicts

### CX-01 — Hard produce/cutover block vs IP-CUT-1 warn-only fork

| | |
|---|---|
| **Claim A** | Feature sketch §§2–3: produce exit hard (cannot PASS cutover-ready without `ip_probe`); cutover refuse/auto-FAIL if missing or FAIL. |
| **Claim B path** | Options IP-CUT-1: "Hard-block cutover vs warn-only on missing ip_probe" |
| **Conflict** | Warn-only recreates the VIB hole (declare early, wire anyway, ACCEPT first hard fail). Sketch already picks hard-block; table reopens it as undecided. |
| **Severity** | high |
| **Lean** | REVISE — lock hard-block as product invariant (or demote sketch language to proposal until decide). Drop warn-only or quarantine it as explicit non-goal. |

### CX-02 — Soft `produce_bytes_only` PASS vs hard produce exit

| | |
|---|---|
| **Claim A** | "Produce wave cannot PASS as cutover-ready without [ip_probe]." |
| **Claim B path** | Same bullet: optional softer PASS `produce_bytes_only` with `cutover_blocked: ip_probe_pending`. |
| **Conflict** | Without a closed vocabulary for which PASS token cutover reads, agents can treat any produce PASS as wire-ready (VIB-W2 pattern: hours/grid PASS). Soft PASS and hard exit need a phase split. |
| **Severity** | high |
| **Lean** | REVISE — two explicit verdict tokens (`produce_bytes_only` vs `cutover_ready`); cutover precondition binds only the latter. |

### CX-03 — General "authority-before-wire" vs IP-CUT-3 visitor-only

| | |
|---|---|
| **Claim A** | Title/sketch: reusable IP-before-cutover "**or more generally** authority-before-wire"; Why-wavves: repeatable across pack lanes (bake, graph, covariates). |
| **Claim B path** | IP-CUT-3: apply only to visitor-plane packs vs all public assets. |
| **Conflict** | Scope is both plugin-wide authority ordering and optionally visitor-only. BUILD acceptance cannot be both universal charter fields and visitor-scoped without a classifier. |
| **Severity** | medium |
| **Lean** | REVISE — lock classifier (e.g. when `public_baseline_pack` / `ip_strip_checklist` set, or `publishes_public_packs: yes`) before claiming "all public assets." |

### CX-04 — ACCEPT defense-in-depth vs "must not be first hard gate"

| | |
|---|---|
| **Claim A** | Non-goals: do not weaken ACCEPT IP remasure. Sketch §4: ACCEPT still remasures. |
| **Claim B path** | Sketch §4: ACCEPT must not be the **first** hard gate after wire. |
| **Conflict** | Not mutually exclusive if pre-wire gate is mandatory. Becomes a conflict if IP-CUT-1 warn-only or missing checklist makes ACCEPT the first real FAIL again. |
| **Severity** | medium (depends on CX-01) |
| **Lean** | REVISE — state ordering invariant: `ip_probe` before cutover start; ACCEPT remeasure after; warn-only forbidden when checklist present. |

### CX-05 — Byte-diff vs checklist-only (IP-CUT-2) vs VIB evidence class

| | |
|---|---|
| **Claim A** | Observed fix class: Midtown `public_contract` parity (shape/keys), not full pack byte identity (PNGs untouched in R1). |
| **Claim B path** | IP-CUT-2: "Require byte-diff vs baseline vs checklist-only"; evals sketch "baseline-parity manifest → PASS." |
| **Conflict** | Full byte-diff of packs would FAIL honest island expands (bbox/hours/ids differ). Checklist-only can miss novel leak keys. FR never picks the remasure class that VIB actually used (schema/allowlist parity). |
| **Severity** | high |
| **Lean** | REVISE — lock probe class: public_contract / strip-checklist schema remasure (allow differing coverage ids); forbid naive whole-pack byte-diff as default. |

### CX-06 — VIB-IP-DELTA "expose after ACCEPT" vs lane W3-before-ACCEPT sequence

| | |
|---|---|
| **Claim A** | Foreign `VIB-IP-DELTA.md`: pack root replace is "**replace** live expose after ACCEPT." |
| **Claim B path** | Foreign W3 PASS cutover before ACCEPT; FR Problem narrates that hole; waveset default Wave 3 integrate / Wave 4 accept (`skills/charter/SKILL.md`) invites the same order. |
| **Conflict** | Originating contract already said after-ACCEPT; execution ignored it. FR treats missing wavves enforcement as the bug (correct) but does not say whether BUILD hardens charter wave order, cutover precondition, or both. Phase leak: "cutover_requires" without forbidding W-cutover before ACCEPT. |
| **Severity** | medium |
| **Lean** | REVISE — name both: produce-exit `ip_probe` **and** cutover wave may not start without it; ACCEPT remains later remasure. |

### CX-07 — Builder emit rule vs produce-exit ownership

| | |
|---|---|
| **Claim A** | Sketch §5: builders default to baseline public_contract; science blocks private. |
| **Claim B path** | Sketch §2: produce-exit IP probe is the hard gate. |
| **Conflict** | Two enforcement loci (emit-time vs probe-time) with no primacy. VIB needed both builder patch (R1) and ACCEPT remasure. Unclear whether emit rule is advisory docs or a BUILD acceptance surface. |
| **Severity** | low–medium |
| **Lean** | REVISE — probe is hard gate; builder emit is recommended default / anti-re-emit note, not a substitute PASS. |

### CX-08 — Sibling Proof-before-accept timing vs IP-before-cutover

| | |
|---|---|
| **Claim A** | Related: do not collapse with `PROC-PASS-NO-PROOF`; Non-goals: do not replace Proof-before-accept. |
| **Claim B path** | Both reorder authority relative to ACCEPT/wire; charter already has `proof_required` pre-ACCEPT fields; IP pattern adds pre-cutover fields. |
| **Conflict** | No joint order when a lane has both Proof and public packs: Proof before ACCEPT, IP before cutover, cutover before ACCEPT. Silent assumption that they compose. A lane could cutover for Proof photography with fat manifests still live. |
| **Severity** | medium |
| **Lean** | REVISE — one composition sentence: for public-pack lanes, `ip_probe` before cutover; Proof harness may run on wired surface only after `ip_probe` PASS (or on unwired fixture host with explicit note). |

## Lens verdict

**REVISE** (not BLOCK, not GO).

Core story is consistent: IP declared early, enforced late, cutover in the
hole. Blocking for BUILD if unaddressed: CX-01, CX-02, CX-05 (probe class and
PASS tokens). Must-clear in `/mod-decide`: CX-03 scope, CX-06 wave order,
CX-08 composition with Proof-before-accept.

## Commit file list (findings only; no git)

- `wavves/lanes/20260719_ip-before-cutover-check/findings/IPB-contradictions.md`

## Escalation

O0 only. No operator solicit.
