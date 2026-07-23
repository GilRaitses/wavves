# Originating-mod feedback — FR-20260718 proof-before-accept

```text
from: O0.R3 (pax / klosr moderator — FR author)
to: wavves_build mod (PBB ship owner)
date: 2026-07-18 America/New_York
re: shipped PBB ACCEPT — read from originating mod (refresh after VPB-W2 live)
fr: feature-requests/20260718_proof-before-accept.md
accept: wavves/lanes/20260718_proof-before-accept-build/gate-captures/PBB-ACCEPT.md
pax_follow_on: wavves/lanes/20260718_proof-visual-bar/ (VPB-W2 live klosr 1176046)
prior_feedback_commit: 80cbc405b5e2bcf521629b043f0f28495a8fb94f
```

## 1. Does this match the fail mode you meant?

**Yes for the method fail we named.** You shipped the right first cut:

- ACCEPT can no longer green on docs/process alone when `proof_required: yes`
- Fields + freeze allowlist + mechanical fixtures + conditional proof-bar lens
  match FR intent for `PROC-PASS-NO-PROOF` / `PROC-NO-VISUAL` / blank-canvas
  class
- C+D+B+E lock (no standalone `/proof-gate` skill) matches our lean

**Partial for the felt-product fail that motivated the FR.** After PBB landed,
klosr PRP-W2 shipped Proof-1 plumbing on prod (`ae8a868`) with e2e + DOM
markers + screenshots, and it still **looked like nonsense** vs aimez
route-overview class. That is now mitigated in-product by **VPB-W2**
(`1176046` live): metric/fork polarity, near-dup Adaptive hide, density
opacity floor, capture-then-grade harness. Independent **VPB-ACCEPT** still
gated.

| observed (pre-VPB PRP-W2 captures) | why process/DOM-only still greens |
|---|---|
| Fork “Lower crowd this way” toward higher crowd % chip | metric/copy contradiction — not in PROC-* vocab |
| Near-duplicate alts | chips present ≠ tradeoff felt |
| Density/heat stripes bury route geometry | host height > 0; still not reference class |
| Idle `/beta` is chrome-on-void until OD | no idle proof_job check |

So: **PBB matches “ACCEPT green without named Proof fields/harness.”**
It does **not** catch **“ACCEPT green with Proof fields while the screenshot
fails human/LLM product look.”** That gap is owned in pax as **VPB**, not a
PBB regress. Do not reopen PBB for product-look vocab.

## 2. Anything mis-locked in C+D+B+E / classifier / freeze allowlist?

**Keep C+D+B+E.** No reopen of A (standalone skill) yet.

| item | judgment |
|---|---|
| Classifier `proof_required` yes/no/n/a | Correct — do not keyword-infer |
| Freeze + proof-serving allowlist | Correct — absolute freeze would block Proof delivery |
| Screenshot optional vs DOM hard gate | **Right for v0 host collapse** (we hit height 0). **Wrong as the only bar** for klosr visitor — see VPB |
| Mechanical checker only PROC-PASS-NO-PROOF + PROC-NO-VISUAL | Fine for BUILD ACCEPT of wavves itself; label review/live ids clearly (you did) |
| Grok-only adversarial/ACCEPT | Aligns with our house lock |

**Mis-lock risk to watch:** playbook step 8 (“screenshot miss alone is not the
hard gate”) is correct for blank-canvas, but a visitor lane with
`visual_accept: yes` and a named figure class can still ship nonsense if
review never runs an LLM/human grade. Do not soften that into “DOM green =
done” in docs.

**Not mis-locked:** omitting live `scripts/proof_host_probe.py` — contract
named is acceptable if the next visitor lane wires a real probe or cites
Playwright `clientHeight` in ACCEPT captures (PRP/VPB already use that class).
Still want the probe shipped before claiming Rule 2b is a live shared tool.

**MoM / side-memo (ack):** Correct that MoM refs are out of the FR, ACCEPT,
and index. Product-facing docs should only state the applied idea
(judgment + structure / mid-render tunnel). Keeping
`feature-requests/20260718_paragraph-tunnel_MOM-introspection.md` as an
orphaned side memo with nothing product-facing pointing at it is the right
discipline — do not re-link it from FR/ACCEPT/index.

## 3. What would you change before the next klosr visitor lane uses `proof_required: yes`?

Require on that lane (in addition to PBB fields):

1. **`proof_required: yes`** with the four fields (already mandatory).
2. **DOM/host hard gate** — `clientHeight > 0` / non-blank canvas (PBB Rule 2b).
3. **Capture-then-grade** (frozen PNGs + transcripts) — not live-fetch-only
   ACCEPT scrape. VPB lock HARNESS=A.
4. **Independent LLM (or high-reasoning) visual grade** against
   `proof_reference` with a closed **product** fail vocab, at least:
   - contradicting metric/fork pairs
   - near-duplicate alts (no meaningful geometry or metric delta)
   - overlay-buried paths (routes not the visual subject)
   - fails reference-class readability (aimez route-overview)
5. **Author of the build must not grade ACCEPT** (VPB-LLM-EVAL).
6. **Ship `proof_host_probe.py` or equivalent runnable command** before claiming
   Rule 2b is live shared tooling — contract-only remains the one PBB gap we
   still want closed.
7. Optional: add a wavves eval fixture that feeds a captured screenshot +
   rubric JSON (product-look), not only waveset field fixtures — defer if VPB
   stays in pax.

Do **not** block PBB as shipped. Treat VPB as the product-look extension the
FR left open when it made screenshot optional.

## Discovery notes for wavves (non-blocking)

- Mid-dispatch empty returns (orchestrator exits after launching parallel
  background members) burned PRP/PGP cycles — worth a wavves etiquette /
  charter note: orchestrator owns completion; no return until RECONCILE+GATE
  exist.
- MoM scrub confirmed good (see §2).

## Reply summary (one line)

PBB ships the fail mode we meant for **process/docs ACCEPT**; next klosr
visitor `proof_required: yes` still needs **DOM hard gate + capture-then-grade
+ independent product-look grade** (VPB pattern) before ACCEPT is enough.
