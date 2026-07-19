# PBA-W1a — grounding

```text
lens: grounding
wave: PBA-W1a
date: 2026-07-18 America/New_York
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260718_proof-before-accept.md
check_lane: wavves/lanes/20260718_proof-before-accept-check/
wavves_build_asserted_head: af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
originating_product_repo_evidence_hash_in_fr: foreign pin
git_actions: none (git ban)
```

## Lens verdict recommendation

**REVISE**

Core fail mode is grounded in originating product repo doctrine + visitor rebuild / product-look / beta visitor lane ACCEPT packets.
Named citation and measurement gaps should be fixed before BUILD treats the
FR evidence block as complete. Not BLOCK: no false landing path inside
wavves_build for the proposed surfaces, and the process-PASS story matches
captured gates.

## What grounds cleanly

Evidence cited in the FR was verified in the originating product repo at check time.
Absolute paths are redacted here for public tip hygiene.

| claim | evidence | match |
|---|---|---|
| Doctrine exists and ratifies Proof-then-consume | originating product repo multi-surface proof doctrine yaml (`status: ratified`, foreign pin) | YES |
| FR `evidence_verified_against` matches doctrine hash | FR line + doctrine `repo_state_verified_against` both foreign pin | YES |
| Visitor rebuild lane home present | originating product repo visitor rebuild lane home | YES |
| Product-look lane home present | originating product repo product-look lane home | YES |
| Visitor rebuild ACCEPT PASS on process/shell gates, not visual proof class | visitor rebuild ACCEPT capture gates: F1, F2, phone_IA, LAND_C, ComfortViewer_off, honesty; no screenshot-vs-reference | YES |
| Post-ACCEPT map-host hotfix | visitor rebuild waveset post-ACCEPT hotfix note; doctrine `blank_map_hotfix`; step-log note | YES |
| Product-look ACCEPT closes with residuals as debt notes | product-look ACCEPT capture `PASS-WITH-RESIDUALS` + residual list | YES |
| Beta visitor lane W4 shipped route alternatives + fork markers | beta visitor lane W4 reconcile finding (route alternatives + fork marker modules); files exist under visitor product beta app path | YES |
| Proposed wavves landing paths exist as directories / siblings | `skills/mod-check/SKILL.md`, `skills/mod-decide/SKILL.md`, `skills/charter/{SKILL.md,EXECUTION_WIRING.md}`, `evals/fixtures/`, `skills/wavves/playbooks/`, `docs/purpose-gates.md`, `feature-requests/README.md` | YES |
| mod-check today has four default lenses; fifth is special-cased | `skills/mod-check/SKILL.md` L72–84 | YES (Option B is a proposal to change that) |
| Non-goal boundary file exists | `docs/purpose-gates.md` (public-copy purpose gates, not ACCEPT process) | YES |

## Named gaps

### G1 — Source evidence paths omit repo root (blocking)

**Claim:** Source evidence lists doctrine yaml and visitor rebuild / product-look lane homes under an originating-product-repo label.

**Evidence:** Those paths resolve in the originating product repo. They do **not** exist under `<repo-root>/` (no matching doctrine tree; no visitor rebuild / product-look lane homes in this repo's `wavves/lanes/`).

**Gap:** Cross-repo FR in wavves_build cites originating-product-repo-relative paths without an explicit root + hash prefix. Hydration from the FR's product repo alone fails.

**Blocking:** yes — revise Source evidence to name originating product repo root + foreign pin for every cited file/lane (absolute paths redacted in public tip).

### G2 — Beta visitor lane home not cited (blocking)

**Claim:** Source evidence and Problem cite "beta visitor lane W4 intent (route alternatives + fork markers)" and chrome rebuild chain beta visitor → product-look → visitor rebuild.

**Evidence:** Beta visitor lane home is present in originating product repo. FR Source evidence names visitor rebuild + product-look only; beta visitor lane is prose-only.

**Gap:** Missing cited seam for a named actor in the failure chain.

**Blocking:** yes — add beta visitor lane path (and preferably ACCEPT capture + W4 reconcile).

### G3 — "height-0" is stronger than cited measurements (blocking)

**Claim:** Symptom 3: "height-0 map that still left chrome PASS"; Source line ties empty /beta feel to visitor product hotfix foreign pin.

**Evidence:**
- Visitor rebuild ACCEPT certifies visitor product foreign pin with no map-host height gate (visitor rebuild ACCEPT capture).
- Visitor rebuild waveset records post-ACCEPT hotfix foreign pin for **collapsed** map host height (not a measured `clientHeight: 0` in that packet).
- Later product-look lane capture at hotfix foreign pin measures healthy host (`map_host_clientHeight: 711`), and product-look fail vocabulary uses `clientHeight ≤ 0` as a class.

**Gap:** Numeric "height-0" is not transcribed from a cited pre-hotfix capture. Timeline (ACCEPT PASS, then height hotfix) is grounded; the zero measurement is not.

**Blocking:** yes — soften to "collapsed / zero-height class" and cite visitor rebuild waveset + product-look fail bar, or add a capture that measured height ≤ 0.

### G4 — Doctrine seams under-cited for route alternatives / fork markers / ACCEPT (non-blocking)

**Claim:** Route alternatives + fork markers vs process gates; visitor rebuild ACCEPT PASS while product felt empty.

**Evidence doctrine lists:** visitor rebuild ACCEPT capture, visitor product beta fork marker module, route alternatives module. FR cites lane folders only.

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

Product-look lane gate capture in originating product repo already records `process_pass_insufficient` against the same doctrine hash. FR does not cite it; adding it would tighten the "felt empty after process PASS" claim without changing the proposal.

## Blocking count

**3 blocking gaps** (G1, G2, G3). **4 non-blocking** (G4–G7). **1 O0 note** (G8).

## Recommended FR edits (grounding only)

1. Prefix every Source evidence path with originating product repo root + foreign pin (absolute paths redacted for public tip).
2. Add beta visitor lane home + W4/ACCEPT capture paths.
3. Replace bare "height-0" with "collapsed map host (post-ACCEPT hotfix foreign pin)" unless a pre-hotfix measurement path is added.
4. Optionally cite visitor rebuild ACCEPT capture, visitor product route alternatives / fork marker modules, and product-look gate for process≠proof.

## Escalation

None that stops this lens. G8 is an O0 note only (git ban). No human operator solicitation.
