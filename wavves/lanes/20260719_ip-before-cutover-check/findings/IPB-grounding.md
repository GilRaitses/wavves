# IPB-W1a — grounding

```text
lens: grounding
wave_id: IPB-W1a
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260719_ip-before-cutover.md
artifact_sha256: 9dad5f5e68244fbb97c888465af2da4540697b3cbb873d8cf9959f94662643ae
artifact_bytes_lines: 100
check_repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
verdict_lean: REVISE
escalation: O0 only
git: none performed
```

## Verdict lean (this lens)

**REVISE.** The fail mode is real and remasures against foreign pax VIB
artifacts (illustration only): IP strip declared in `VIB-IP-DELTA`, W2/W3
PASS without public-surface parity remasure, ACCEPT A6 FAIL then Midtown
rollback, R1 manifest redact without PNG re-bake. Citation hygiene and
product-surface landing names need fixes before BUILD treats the evidence
block or "pack-produce playbooks" claim as closed.

Not BLOCK: no false in-repo landing path for the FR itself; wavves charter /
EXECUTION_WIRING / proof-before-accept seams exist and currently omit
pre-wire IP ordering.

## Claims vs evidence

| claim (FR / lane) | evidence_path | match |
|---|---|---|
| Artifact exists; status `draft → ready-for-mod-check` | `feature-requests/20260719_ip-before-cutover.md` | yes |
| FR indexed ready-for-mod-check | `feature-requests/README.md` (FR-20260719-ip-before-cutover) | yes |
| Check lane pin `26ad2d2a…` across README/waveset/dispatch/registry | `wavves/lanes/20260719_ip-before-cutover-check/*`; `wavves/registry.yml` (IPB) | yes |
| INDEX lists FR + IPB active lane | `wavves/INDEX.md` | yes |
| Related fail id `PROC-PASS-NO-PROOF` shipped as separate pattern | `feature-requests/20260718_proof-before-accept.md` (shipped); `skills/wavves/playbooks/proof-before-accept.md`; `skills/charter/EXECUTION_WIRING.md` Rule 2b | yes (do not collapse) |
| Charter / EXECUTION_WIRING emphasize ACCEPT / proof more than pre-wire IP | `skills/charter/SKILL.md` (proof_required + Wave 4 acceptance); `EXECUTION_WIRING.md` (cutover named only as measured-transition example) | yes (gap is real) |
| Product surface includes "pack-produce playbooks" | `skills/wavves/playbooks/` (no pack-produce / cutover / IP playbook) | **no** (proposed surface absent; name invents a seam) |
| VIB lane home + IP delta declared strip early | foreign pax `…/20260719_visitor-island-bake/contracts/VIB-IP-DELTA.md` (equations/coeffs/canopy defaults private) | yes (illustration) |
| W2 PASS = bake hours/bbox/grid, not manifest≤baseline | foreign `findings/VIB-W2.md` (PASS on hours/grid/bbox; no IP remasure) | yes (illustration) |
| W3 cutover pointed `/beta` at island packs | foreign `findings/VIB-W3.md` (PASS; pack bases `*_20260719`) | yes (illustration) |
| VIB-ACCEPT A6 first FAIL → Midtown rollback | foreign `gate-captures/VIB-ROLLBACK.json` (`vib_a_fail_ids: [VIB-A6]`, restore `*_20260701`); `findings/VIB-ROLLBACK.md` | yes (illustration) |
| A6 fail atoms = equations/coeffs/canopy numerics | foreign `findings/VIB-R1.md` before/after table; `VIB-ACCEPT-A6.json` `prior_fail_atoms_reversed` | yes (illustration) |
| Cited `gate-captures/VIB-ACCEPT-A6.json` as "fail atoms" | same file now `result: PASS`, `fail_atoms: []`; prior FAIL preserved via `prior_fail_*` + ROLLBACK | **partial** (path exists; current JSON is post-R1 PASS) |
| VIB-R1 redact + re-cutover; no full re-bake | foreign `findings/VIB-R1.md` ("PNG ground bytes untouched") | yes (illustration) |
| Post-R1 island manifests Midtown `public_contract` parity | klosr local tip manifests `*_20260701` vs `*_20260719` (method/`class_keys` parity; illustration) | yes (illustration) |
| Final ACCEPT PASS after R1 | foreign `gate-captures/VIB-ACCEPT.json` (`status: PASS`, `vib_a6: PASS`, prior fail superseded) | yes (illustration) |
| `evidence_verified_against` pax `e6f78d39…` (LCZ-W1 blocked tip) | foreign pax `…/20260719_lcz-workbench/decisions/LCZ-RES-D1-resolution-and-source.md` cites same hash | yes (illustration; pin is LCZ tip, not VIB land tip) |
| Proposed charter fields / fail id land in wavves | fields/fail id proposed only; not in charter SKILL today | n/a (proposal) |

## Named gaps

### GAP-IPB-G1 — Source evidence paths omit foreign repo root

- **severity:** REVISE (citation honesty)
- **claim:** Source evidence lists `wavves/lanes/20260719_visitor-island-bake/`,
  `gate-captures/VIB-ACCEPT.json`, etc. as bare relative paths
- **evidence_path:** FR Source evidence block; those paths **absent** under
  `wavves_build/wavves/lanes/` (glob: no VIB lane here)
- **note:** Paths resolve under foreign pax lane home
  `/Users/gilraitses/pax/wavves/lanes/20260719_visitor-island-bake/`.
  Dispatch marks them illustration-only. Revise FR to prefix `pax@<hash>:`
  (or absolute redacted form) so hydration from wavves_build alone cannot
  treat them as local.

### GAP-IPB-G2 — Cited A6 capture is now PASS, not FAIL

- **severity:** REVISE (precision)
- **claim:** `gate-captures/VIB-ACCEPT-A6.json` (fail atoms)
- **evidence_path:** foreign `VIB-ACCEPT-A6.json` (`result: PASS`,
  `fail_atoms: []`, `prior_fail_atoms_reversed` populated);
  `VIB-ROLLBACK.json` / `findings/VIB-ROLLBACK.md` for the FAIL→rollback event
- **note:** First FAIL atoms are transcribed in R1 + `prior_fail_*`, not as
  live `fail_atoms`. Cite ROLLBACK + R1 (or a preserved FAIL snapshot if one
  is re-emitted) alongside A6.

### GAP-IPB-G3 — "pack-produce playbooks" product surface invents a seam

- **severity:** REVISE (landing grounding)
- **claim:** Product surface includes "pack-produce playbooks"
- **evidence_path:** `skills/wavves/playbooks/` (bootstrap, charter-lane,
  check, decide, layover, pickup, paragraph-tunnel, proceed,
  proof-before-accept, rotate, set-key only)
- **note:** BUILD must name real targets (e.g. charter waveset fields +
  `EXECUTION_WIRING.md` rule + optional new playbook path). Do not imply an
  existing pack-produce playbook.

### GAP-IPB-G4 — Midtown / island pack bytes are foreign product (note)

- **severity:** note
- **claim:** Midtown baseline packs `*_20260701` vs island `*_20260719`
- **evidence_path:** klosr `public/assets/engine/…` (illustration); not under
  wavves_build
- **note:** Acceptance fixtures for BUILD must be repo-local synthetics, not
  hard-deps on klosr pack trees.

### GAP-IPB-G5 — evidence pin is LCZ tip, not VIB ACCEPT land (note)

- **severity:** note
- **claim:** `evidence_verified_against` pax `e6f78d39…` (LCZ-W1 blocked tip;
  VIB-ACCEPT PASS earlier same day)
- **evidence_path:** FR lines 15–16; LCZ decision cites hash; VIB-ACCEPT.json
  pins different hashes (`dae87d59…` / klosr `0d96890d…`)
- **note:** Honest as "same-day program tip," but not a remasure of VIB
  ACCEPT land. Prefer citing VIB-ACCEPT / ROLLBACK hashes for the fail chain.

## Hydration opened (must-cite list)

| path | opened |
|---|---|
| `feature-requests/20260719_ip-before-cutover.md` | yes |
| `feature-requests/README.md` | yes |
| `wavves/lanes/20260719_ip-before-cutover-check/{README,waveset,dispatch}.md` | yes |
| `skills/charter/SKILL.md` | yes |
| `skills/charter/EXECUTION_WIRING.md` | yes |
| `skills/mod-check/SKILL.md` | yes |
| `skills/wavves/playbooks/proof-before-accept.md` | yes |
| foreign pax VIB IP delta / W2 / W3 / R1 / ROLLBACK / ACCEPT(+A6) | yes (illustration) |
| klosr Midtown + island manifests (post-R1 parity) | yes (illustration) |

## Commit file list

- This findings file only:
  `wavves/lanes/20260719_ip-before-cutover-check/findings/IPB-grounding.md`
- No git performed (status / add / commit / push none).
