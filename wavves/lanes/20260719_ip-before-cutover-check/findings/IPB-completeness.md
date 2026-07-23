# IPB-W1c — completeness

- **Lens:** completeness
- **Artifact:** `feature-requests/20260719_ip-before-cutover.md`
- **Repo state (dispatch):** `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5`
- **Hydrated:** waveset.md, dispatch.md, artifact;
  `skills/charter/SKILL.md`, `skills/charter/EXECUTION_WIRING.md`,
  `skills/mod-check/SKILL.md`,
  `skills/wavves/playbooks/proof-before-accept.md`,
  `feature-requests/README.md`,
  `evals/README.md` (+ proof-before-accept / paragraph-tunnel checkers),
  foreign pax VIB chain (illustration only)
- **Lens verdict recommendation:** **REVISE**
- **Blocker count:** 7 blocking gaps; 4 non-blocking
- **statement:** read-only; no git; no code edits outside this findings file
- **Escalation:** O0 only

## Verdict (this lens only)

REVISE. Problem, fail id, and VIB narrative are enough for `/mod-decide`.
The FR is not complete enough to charter BUILD: no Acceptance section, no
named landing files, no `ip_probe` contract, no fixture homes/runner, and
open calls that still leave hard vs warn and probe class undecided.

O0 owns the lane verdict. Not BLOCK: intent and non-goals are product-shaped.
Not GO: BUILD would invent schema, wiring, and eval shape.

---

## Blocking gaps

### B1 — No Acceptance criteria section

**Evidence:** FR has Problem, Feature sketch, Why wavves, Non-goals, Options,
Suggested next. No Acceptance / Done-when checklist.

**Missing for charter:** testable bullets O0 can copy into a BUILD waveset
(charter fields present; produce-exit FAIL on fat fixture; cutover refuse;
ACCEPT still remasures; docs index).

**Why blocking:** Sibling shipped FR (proof-before-accept) and PAS-class
checks treat Acceptance as BUILD unlock. Without it, BUILD greens on prose.

**Needed edit:** Add Acceptance section with mechanical + docs bullets.

### B2 — Landing surfaces unnamed

**Evidence:** Product surface line lists "wavves skills / charter templates /
EXECUTION_WIRING / pack-produce playbooks." Sketch never names paths.

**Live seams today:**

| candidate | status |
|---|---|
| `skills/charter/SKILL.md` (waveset mandatory fields) | exists; no IP fields |
| `skills/charter/EXECUTION_WIRING.md` | exists; cutover only in Rule 1 example |
| `skills/wavves/playbooks/proof-before-accept.md` | sibling pattern; IP playbook absent |
| pack-produce playbook | **does not exist** |

**Why blocking:** BUILD cannot open a waveset without knowing which files to
patch. "Charter templates" is not a file in `skills/charter/` (same class of
gap PBA hit).

**Needed edit:** Explicit patch list (required vs optional), e.g. SKILL.md
fields + EXECUTION_WIRING rule + optional `playbooks/ip-before-cutover.md`.

### B3 — `ip_probe` contract underspecified

**Evidence:** Sketch names `ip_probe: PASS` in `cutover_requires` and
"named IP probe vs baseline / checklist." No inputs, outputs, command,
JSON fields, or fail atoms.

**Missing:**

| element | specified | missing |
|---|---|---|
| inputs | baseline + checklist paths (charter fields) | manifest/asset glob under produce out |
| remasure class | "vs baseline / checklist" | schema parity vs byte-diff vs deny-key scan |
| outputs | PASS/FAIL token | capture path shape; atom list |
| runner | — | stdlib script path / lane-local harness |
| when required | "when lane publishes public packs…" | classifier field name + default |

**Why blocking:** Cutover precondition cannot bind an undefined probe.

**Needed edit:** Freeze `ip_probe` as a named harness contract (command +
JSON + closed fail atoms), analogous to `proof_host_probe.py` / Rule 2b.

### B4 — Charter field schema incomplete

**Evidence:** Sketch lists `public_baseline_pack`, `ip_strip_checklist`,
`cutover_requires` including `ip_probe: PASS`.

**Missing for BUILD:**

- types (path vs pack id); required vs optional
- interaction when fields absent (skip pattern vs FAIL)
- where fields live (waveset Meta vs Locked vs contracts/)
- `produce_bytes_only` / `cutover_blocked` field homes
- authority_precedence / dispatch paste requirements

**Why blocking:** Unowned defaults recreate VIB (fields omitted → wire anyway).

### B5 — Eval fixture homes and runner unnamed

**Evidence:** Sketch §6: fat-manifest → produce-exit FAIL; baseline-parity →
PASS; cutover without ip_probe → FAIL. `evals/README.md` shows
lens-keyword `run_fixtures.py`, `check_paragraph_tunnel.py`,
`check_proof_before_accept.py`. No `ip-before-cutover` prefix or checker.

**Why blocking:** Same hole as PBA/PAS: Acceptance can be "documented"
without a runnable corpus. Keyword fixtures alone will not enforce ordering.

**Needed edit:** Name e.g. `evals/fixtures/ip-before-cutover-*/` +
`evals/check_ip_before_cutover.py` (or explicit defer with lane-local
fixtures). Map each sketch case to a fixture id.

### B6 — Fail vocabulary incomplete for operable BUILD ACCEPT

**Evidence:** One proposed id `PROC-IP-AFTER-CUTOVER`. Sketch behaviors also
need produce-exit FAIL and missing-probe cutover FAIL.

**Missing ids (minimum):**

| id | covers |
|---|---|
| `PROC-IP-PROBE-FAIL` | produce-exit / probe saw strip violation |
| `PROC-IP-PROBE-MISSING` | cutover started without probe record |
| `PROC-IP-SOFTPASS-WIRE` | `produce_bytes_only` treated as cutover-ready |

**Why blocking:** Single id collapses distinct detectors; ACCEPT/docs can
claim the pattern while soft-PASS wire still works.

### B7 — Open calls listed but BUILD-critical locks not marked as gates

**Evidence:** Options IP-CUT-1/2/3; Suggested next: mod-check → mod-decide →
BUILD. No statement that BUILD is blocked until those locks land.

**Why blocking:** A proceed agent can charter BUILD from sketch prose while
hard vs warn and probe class remain forked (see contradictions CX-01/CX-05).

**Needed edit:** "BUILD blocked until IP-CUT-1/2/3 locked" (or freeze
defaults in FR now: hard-block; schema-parity probe; classifier for when
required).

---

## Non-blocking gaps

### N1 — Rollback / disable for the pattern itself absent

**Evidence:** Non-goals cover weakening ACCEPT and coverage lies. No note for
bad baseline pin, poisoned checklist, or how to disable `ip_probe` when a
lane has no public packs.

**Call:** Soft: absent fields → pattern N/A (with classifier); poisoned
baseline → operator_gate, not silent skip.

### N2 — Builder emit rule has no acceptance surface

**Evidence:** Sketch §5. Completeness hunt: unowned edge.

**Call:** Document as recommended default under produce playbook/charter
note; mechanical gate remains `ip_probe`. Optional later builder unit fixture.

### N3 — Foreign VIB/klosr pins as BUILD hard-deps

**Evidence:** Source evidence + Midtown pack ids. Dispatch: illustration only.

**Call:** State under Non-goals or Acceptance: fixtures are repo-local
synthetics; pax/klosr paths are originating illustration.

### N4 — Registry / failure_log emission unstated

**Evidence:** `wavves/failure_log.yml` exists (house surface). FR proposes
fail id but does not say whether BUILD appends it.

**Call:** Non-blocking if docs name the id; preferred: append on ship.

---

## Silent assumptions (call out)

1. "Cutover" means visitor consume-root amend (VIB-W3 class), not every
   deploy or Pages publish.
2. Baseline pack is already APPROVED public surface (not auto-trusted because
   it is old).
3. Produce wave has a single clear output directory to scan.
4. Pattern composes with `proof_required` without a written order.
5. Soft PASS is rare and always stamped `cutover_blocked` in durable
   findings/registry (unstated write home).

---

## Non-goals coverage

**Present and useful:** no weakening ACCEPT IP remasure; no Midtown-as-island
auto-approve; no replacing Proof-before-accept.

**Still thin:**

- no explicit non-goal for whole-pack byte-diff as default probe
- no illustration-only statement for foreign pins
- no v0 scope freeze (visitor packs only vs all public assets)

---

## Hunt checklist (dispatch-specific)

| hunt | result |
|---|---|
| Acceptance sufficient for BUILD charter? | **No** (B1) |
| Landing files named? | **No** (B2) |
| `ip_probe` runnable contract? | **No** (B3) |
| Charter field schema complete? | **No** (B4) |
| Eval fixture homes named? | **No** (B5) |
| Fail ids operable set? | **Partial** (B6) |
| Open calls gate BUILD? | **No** (B7) |
| Rollback / non-goals gaps? | Thin (N1) |

---

## Covered adequately (for this lens)

- Fail mode sequencing (declare → produce → cutover → late ACCEPT)
- Distinction from `PROC-PASS-NO-PROOF`
- Proposed fail id with plain-language definition
- Charter field sketch (three names)
- Defense-in-depth ACCEPT remasure kept
- Evals behaviors sketched at narrative level
- Three mod-decide forks named
- Next path: mod-check → mod-decide → BUILD
- FR indexed ready-for-mod-check

---

## Recommended FR edits (for O0 / mod-decide; not applied)

1. Add Acceptance section (mechanical + docs).
2. Name landing files; drop or redefine "pack-produce playbooks."
3. Freeze `ip_probe` harness contract + capture schema.
4. Complete charter field schema + absent-field behavior.
5. Name eval fixture prefix + checker; map three cases.
6. Expand fail vocabulary (`PROBE-FAIL` / `PROBE-MISSING` / `SOFTPASS-WIRE`).
7. Lock or gate IP-CUT-1/2/3 before BUILD.
8. (Non-blocking) Foreign pins illustration-only; baseline approval rule;
   Proof composition sentence.

---

## Commit file list (for O0; no git performed)

- Write: `wavves/lanes/20260719_ip-before-cutover-check/findings/IPB-completeness.md`
- Exclude: none
- **No git actions performed.**
