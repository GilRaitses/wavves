# PBA-W1a — grounding

```text
lens: grounding
wave: PBA-W1a
date: 2026-07-18 America/New_York
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260718_proof-before-accept.md
check_lane: wavves/lanes/20260718_proof-before-accept-check/
wavves_build_asserted_head: af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
pax_evidence_hash_in_fr: b083b5a76e580265ab3ebabaeb1df1053dc8a565
git_actions: none (git ban)
```

## Lens verdict recommendation

**REVISE**

Core fail mode is grounded in pax doctrine + RFU/CRE/BETA ACCEPT packets.
Named citation and measurement gaps should be fixed before BUILD treats the
FR evidence block as complete. Not BLOCK: no false landing path inside
wavves_build for the proposed surfaces, and the process-PASS story matches
captured gates.

## What grounds cleanly

| claim | evidence | match |
|---|---|---|
| Doctrine exists and ratifies Proof-then-consume | `/Users/gilraitses/pax/.ddb/decisions/pax_multi_surface_proof_then_consume_doctrine_v1_20260718.yaml` (`status: ratified`, `repo_state_verified_against: b083b5a…`) | YES |
| FR `evidence_verified_against` matches doctrine hash | FR line + doctrine `repo_state_verified_against` both `b083b5a76e580265ab3ebabaeb1df1053dc8a565` | YES |
| RFU lane home present | `/Users/gilraitses/pax/wavves/lanes/20260718_route-first-ux/` | YES |
| CRE lane home present | `/Users/gilraitses/pax/wavves/lanes/20260715_comfort-route-explorer/` | YES |
| RFU ACCEPT PASS on process/shell gates, not visual proof class | `…/RFU/gate-captures/RFU-ACCEPT.json` gates: F1, F2, phone_IA, LAND_C, ComfortViewer_off, honesty; no screenshot-vs-reference | YES |
| Post-ACCEPT map-height hotfix `c76e19b` | RFU `waveset.md` L84–86; RFU `README.md` L18–19; doctrine `blank_map_hotfix`; step-log note | YES |
| CRE ACCEPT closes with residuals as debt notes | `…/CRE/gate-captures/CRE-ACCEPT.json` `PASS-WITH-RESIDUALS` + residual list | YES |
| BETA W4 shipped alts + shade forks | `…/beta-visitor-interact/findings/BETA-W4-BUILD-RECONCILE.md` (W4e: `routeAlternates.ts` + `shadeForkMarkers.ts`); files exist under klosr `app/beta/` | YES |
| Proposed wavves landing paths exist as directories / siblings | `skills/mod-check/SKILL.md`, `skills/mod-decide/SKILL.md`, `skills/charter/{SKILL.md,EXECUTION_WIRING.md}`, `evals/fixtures/`, `skills/wavves/playbooks/`, `docs/purpose-gates.md`, `feature-requests/README.md` | YES |
| mod-check today has four default lenses; fifth is special-cased | `skills/mod-check/SKILL.md` L72–84 | YES (Option B is a proposal to change that) |
| Non-goal boundary file exists | `docs/purpose-gates.md` (public-copy purpose gates, not ACCEPT process) | YES |

## Named gaps

### G1 — Source evidence paths omit absolute repo root (blocking)

**Claim:** Source evidence lists `.ddb/decisions/…` and `wavves/lanes/20260718_route-first-ux/` / `20260715_comfort-route-explorer/` under a `(pax)` label.

**Evidence:** Those paths resolve under `/Users/gilraitses/pax/`. They do **not** exist under `/Users/gilraitses/wavves_build/` (no `.ddb/`; no RFU/CRE lane homes in this repo's `wavves/lanes/`).

**Gap:** Cross-repo FR in wavves_build cites pax-relative paths without an absolute or `pax@b083b5a:` prefix. Hydration from the FR's product repo alone fails.

**Blocking:** yes — revise Source evidence to absolute paths (or explicit `pax` root + hash) for every cited file/lane.

### G2 — BETA lane home not cited (blocking)

**Claim:** Source evidence and Problem cite "BETA W4 intent (alts + shade forks)" and chrome rebuild chain BETA → CRE → RFU.

**Evidence:** BETA home is `/Users/gilraitses/pax/wavves/lanes/20260715_beta-visitor-interact/` (present). FR Source evidence names RFU + CRE only; BETA is prose-only.

**Gap:** Missing cited seam for a named actor in the failure chain.

**Blocking:** yes — add BETA lane path (and preferably `gate-captures/BETA-ACCEPT.json` + W4 reconcile).

### G3 — "height-0" is stronger than cited measurements (blocking)

**Claim:** Symptom 3: "height-0 map that still left chrome PASS"; Source line ties empty /beta feel to hotfix `c76e19b`.

**Evidence:**
- RFU ACCEPT certifies klosr `651f25d` with no map-host height gate (`RFU-ACCEPT.json`).
- RFU `waveset.md` records post-ACCEPT hotfix `c76e19b` for **collapsed** MapLibre host height (not a measured `clientHeight: 0` in that packet).
- Later PRP capture at `c76e19b` measures healthy host (`PRP-W1-GATE.json` `map_host_clientHeight: 711`), and PRP fail vocabulary uses `clientHeight ≤ 0` as a class (`PRP-W1c-accept-bar.md`).

**Gap:** Numeric "height-0" is not transcribed from a cited pre-hotfix capture. Timeline (ACCEPT PASS, then height hotfix) is grounded; the zero measurement is not.

**Blocking:** yes — soften to "collapsed / zero-height class" and cite RFU waveset + PRP fail bar, or add a capture that measured height ≤ 0.

### G4 — Doctrine seams under-cited for alts/shade/ACCEPT (non-blocking)

**Claim:** Alts + shade forks vs process gates; RFU ACCEPT PASS while product felt empty.

**Evidence doctrine lists:** `RFU-ACCEPT.json`, `klosr/app/beta/shadeForkMarkers.ts`, `klosr/app/beta/routeAlternates.ts`. FR cites lane folders only.

**Gap:** Missing cited seams that already exist and directly support the claim.

**Blocking:** no — strengthen Source evidence; does not invalidate the claim.

### G5 — "Charter ACCEPT template" landing is underspecified (non-blocking)

**Claim:** Option C / Acceptance #1 land on "Charter template" / "charter ACCEPT templates".

**Evidence:** `skills/charter/` contains `SKILL.md`, `EXECUTION_WIRING.md`, `scripts/transition_gap_probe.py` only. No separate ACCEPT template file. Waveset/ACCEPT shape lives as prose inside `SKILL.md`.

**Gap:** Proposed landing name does not map 1:1 to an existing file; BUILD needs an explicit target (waveset mandatory fields section vs new template file).

**Blocking:** no for this lens (product fork for mod-decide); note only.

### G6 — Proposed playbook path absent today (non-blocking)

**Claim:** Option D `skills/wavves/playbooks/proof-before-accept.md`.

**Evidence:** Path does not exist; siblings under `skills/wavves/playbooks/` do (`check.md`, `charter-lane.md`, etc.).

**Gap:** None for an FR proposal. Expected absent until BUILD.

**Blocking:** no.

### G7 — Feature-request lifecycle vocabulary drift (non-blocking)

**Claim:** FR status `in-mod-check`; README index matches.

**Evidence:** `feature-requests/README.md` Lifecycle lists `draft` → `ready-for-mod-check` → `chartered` → `shipped`/`wontfix` and does not list `in-mod-check`.

**Gap:** Status token used in Index/FR is outside the Lifecycle enum.

**Blocking:** no.

### G8 — wavves_build HEAD not re-verified here (note for O0)

**Claim:** waveset/dispatch assert repo HEAD `af0c0788cb2dbb865cbce6721fcdcbf6642b11d4`.

**Evidence:** Asserted in lane artifacts. This lens is under a git ban and did not re-read `git rev-parse`.

**Gap:** Stale-HEAD check incomplete for this lens.

**Blocking:** no for FR text; escalate to O0 if branch tip may have moved since dispatch.

## Related surfaces check (touch targets)

| surface | present | FR claim about today |
|---|---|---|
| `skills/mod-check/SKILL.md` | yes | extend with proof lens — proposal OK |
| `skills/mod-decide/SKILL.md` | yes | AUTH sync exists (AUTH-01); proof_job lock is proposal |
| `skills/charter/SKILL.md` | yes | no proof_* fields today |
| `skills/charter/EXECUTION_WIRING.md` | yes | runnable gates/captures; no visual/screenshot/map-height rule today |
| `evals/fixtures/` | yes | no PROC-PASS-NO-PROOF fixture yet |
| `skills/wavves/playbooks/` | yes | no `proof-before-accept.md` yet |
| `docs/purpose-gates.md` | yes | correct non-goal boundary |
| `feature-requests/README.md` | yes | FR indexed as in-mod-check |

## Optional stronger citation (not required to pass grounding)

`/Users/gilraitses/pax/wavves/lanes/20260718_visitor-route-proof/` (`PRP-W1-GATE.json`) already records `process_pass_insufficient` / `G7_rfu_process_not_proof1` against the same doctrine hash. FR does not cite it; adding it would tighten the "felt empty after process PASS" claim without changing the proposal.

## Blocking count

**3 blocking gaps** (G1, G2, G3). **4 non-blocking** (G4–G7). **1 O0 note** (G8).

## Recommended FR edits (grounding only)

1. Prefix every Source evidence path with `/Users/gilraitses/pax/` (or `pax@b083b5a:`).
2. Add BETA lane home + W4/ACCEPT capture paths.
3. Replace bare "height-0" with "collapsed map host (post-ACCEPT hotfix `c76e19b`)" unless a pre-hotfix measurement path is added.
4. Optionally cite `RFU-ACCEPT.json`, klosr `routeAlternates.ts` / `shadeForkMarkers.ts`, and PRP gate for process≠proof.

## Escalation

None that stops this lens. G8 is an O0 note only (git ban). No human operator solicitation.
