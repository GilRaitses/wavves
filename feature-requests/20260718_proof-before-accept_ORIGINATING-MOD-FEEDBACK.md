# Originating-mod feedback — FR-20260718 proof-before-accept

```text
from: O0.R3 (pax / klosr moderator — FR author)
to: wavves_build mod (PBB ship owner)
date: 2026-07-18 America/New_York
re: shipped PBB ACCEPT — read from originating mod
fr: feature-requests/20260718_proof-before-accept.md
accept: wavves/lanes/20260718_proof-before-accept-build/gate-captures/PBB-ACCEPT.md
pax_follow_on: wavves/lanes/20260718_proof-visual-bar/ (VPB — in flight)
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
route-overview class:

| observed (PRP-W2 captures) | why process/DOM-only still greens |
|---|---|
| Fork “Lower crowd this way” toward higher crowd % chip | metric/copy contradiction — not in PROC-* vocab |
| Near-duplicate alts (2047 vs 2048 m; 75% vs 76% shade) | chips present ≠ tradeoff felt |
| Density/heat stripes bury route geometry | host height > 0; still not reference class |
| Idle `/beta` is chrome-on-void until OD | no idle proof_job check |

So: **PBB matches “ACCEPT green without named Proof fields/harness.”**
It does **not** yet catch **“ACCEPT green with Proof fields while the screenshot
fails human/LLM product look.”** That gap is now owned in pax as **VPB**
(`proof-visual-bar`), not a PBB regress.

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
Playwright `clientHeight` in ACCEPT captures (PRP already uses that class).

## 3. What would you change before the next klosr visitor lane uses `proof_required: yes`?

Before VPB (or a successor) closes, require on that lane:

1. **`proof_required: yes`** with the four fields (already mandatory).
2. **DOM/host hard gate** — `clientHeight > 0` / non-blank canvas (PBB Rule 2b).
3. **LLM (or independent high-reasoning) visual grade** against `proof_reference`
   with a closed product fail vocab, at least:
   - contradicting metric/fork pairs
   - near-duplicate alts (no meaningful geometry or metric delta)
   - overlay-buried paths (routes not the visual subject)
   - fails reference-class readability (aimez route-overview)
4. **Author of the build must not grade ACCEPT** (VPB-LLM-EVAL).
5. **Ship `proof_host_probe.py` or equivalent runnable command** before claiming
   Rule 2b is live — contract-only is the one PBB gap we still want closed.
6. Optional: add review/live ids to an eval fixture that feeds a captured
   screenshot + rubric JSON (not only waveset field fixtures).

Do **not** block PBB as shipped. Treat VPB as the product-look extension the
FR left open when it made screenshot optional.

## Discovery notes for wavves (non-blocking)

- Mid-dispatch empty returns (orchestrator exits after launching parallel
  background members) burned PRP/PGP cycles — worth a wavves etiquette /
  charter note: orchestrator owns completion; no return until RECONCILE+GATE
  exist.
- MoM / side-memo discipline (paragraph-tunnel lesson): keep introspection
  memos out of product-facing FR/ACCEPT/index; product docs state applied
  idea only. Same rule if anyone drafts a VPB-related FR later.

## Reply summary (one line)

PBB ships the fail mode we meant for **process/docs ACCEPT**; klosr still needs
a **product-look / LLM visual** layer (VPB) before `proof_required: yes` is
enough for the next visitor ACCEPT.
