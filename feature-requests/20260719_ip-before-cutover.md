# FR-20260719 — IP-before-cutover (authority timing vs terminal remasure)

- **Status:** draft → ready-for-mod-check
- **Date:** 2026-07-19 (America/New_York)
- **Product surface:** wavves skills / charter templates / EXECUTION_WIRING /
  pack-produce playbooks
- **Source evidence (pax):**
  - `wavves/lanes/20260719_visitor-island-bake/` (VIB)
  - `gate-captures/VIB-ACCEPT.json` (first FAIL on VIB-A6; PASS after R1)
  - `gate-captures/VIB-ACCEPT-A6.json` (fail atoms)
  - `contracts/VIB-IP-DELTA.md`
  - `findings/VIB-R1.md` (manifest redact + re-cutover; no full re-bake)
  - Midtown baseline packs `shade_field_20260701` / `felt_heat_20260701`
    (public_contract shape) vs island `*_20260719` pre-R1 fat manifests
- **evidence_verified_against:** pax `e6f78d39399747b1d29cb93c70c6dfa9f29b63dc`
  (LCZ-W1 blocked tip; VIB-ACCEPT PASS already landed earlier same day)
- **Originating mod feedback:** O0.R3 after VIB Midtown consume rollback

## Problem

wavves lanes can sequence:

```text
design → produce public packs → cutover consume → ACCEPT remasure
```

When **IP / public-surface strip** is only enforced at **terminal ACCEPT**,
produce+cutover can ship forbidden bytes (equations, coeffs, transmissivity
defaults) that doctrine already named in an IP delta. ACCEPT then correctly
FAILs and triggers **fail-closed rollback of consume** — expensive thrash for
a defect that was cheap to catch before wire.

**Observed fail mode (VIB):**

1. `VIB-IP-DELTA` declared strip early (equations/coeffs/canopy defaults private).
2. W2 PASS meant bake hours + bbox + grid — **not** “manifest ≤ approved
   public baseline.”
3. W3 cutover pointed `/beta` at island packs with fat manifests.
4. VIB-ACCEPT A6 FAIL → rollback to Midtown `*_20260701` consume.
5. VIB-R1 redacted manifests to Midtown public_contract parity, re-cutover,
   re-ACCEPT PASS — **no PNG re-bake required**.

So IP was **declared early, enforced late**. Cutover sat in the hole.

**Fail id (proposed):** `PROC-IP-AFTER-CUTOVER` — lane allows consume cutover
(or “pack shipped” PASS) before a hard remasure that public artifacts match
the approved public-surface baseline / IP strip checklist.

Related (do not collapse): `PROC-PASS-NO-PROOF` (FR-20260718) is about
process-PASS without product Proof. This FR is about **authority timing** for
public IP / strip relative to cutover.

## Feature sketch

Add reusable **IP-before-cutover** (or more generally **authority-before-wire**)
pattern to wavves:

1. **Charter fields** (when lane publishes public packs or amends visitor
   consume roots):
   - `public_baseline_pack` (path/id of approved public-surface exemplar)
   - `ip_strip_checklist` (path to delta / inventory)
   - `cutover_requires` list including `ip_probe: PASS`
2. **Produce exit (hard):** after writing public manifests/assets, run named
   IP probe vs baseline / checklist. Produce wave cannot PASS as
   cutover-ready without it. Optional softer PASS: `produce_bytes_only` with
   explicit `cutover_blocked: ip_probe_pending`.
3. **Cutover precondition:** W-cutover / seam-wire dispatch must refuse to
   start (or auto-FAIL) if `ip_probe` missing or FAIL.
4. **ACCEPT still remasures IP** (defense in depth) but must not be the
   **first** hard gate after wire.
5. **Builder emit rule:** pack builders default to baseline public_contract
   shape; science blocks stay private / omitted.
6. **Evals / fixtures:** fat-manifest fixture → produce-exit FAIL;
   baseline-parity manifest → PASS; cutover without ip_probe → FAIL.

## Why this belongs in wavves (not only pax lane docs)

- Repeatable across pack lanes (bake, graph, covariates).
- Skills/`/charter` templates currently emphasize ACCEPT matrices more than
  **pre-wire** authority ordering.
- Prevents rollback-class incidents when strip is already known.

## Non-goals

- Weakening ACCEPT IP remasure
- Auto-approving Midtown-as-island or other coverage lies
- Replacing Proof-before-accept

## Options for mod-decide (later)

| id | question |
|---|---|
| IP-CUT-1 | Hard-block cutover vs warn-only on missing ip_probe |
| IP-CUT-2 | Require byte-diff vs baseline vs checklist-only |
| IP-CUT-3 | Apply only to visitor-plane packs vs all public assets |

## Suggested next

`/mod-check` on this FR → `/mod-decide` forks → charter skill/template BUILD
if GO.
