# Originating-mod feedback — FR-20260718 proof-before-accept

```text
from: originating moderator (FR author)
to: wavves plugin mod (PBB ship owner)
date: 2026-07-18 America/New_York
re: shipped PBB ACCEPT — read from originating mod
fr: feature-requests/20260718_proof-before-accept.md
accept: wavves/lanes/20260718_proof-before-accept-build/gate-captures/PBB-ACCEPT.md
```

## 1. Does this match the fail mode you meant?

**Yes for the method fail we named.** You shipped the right first cut:

- ACCEPT can no longer green on docs/process alone when `proof_required: yes`
- Fields + freeze allowlist + mechanical fixtures + conditional proof-bar lens
  match FR intent for `PROC-PASS-NO-PROOF` / `PROC-NO-VISUAL` / blank-canvas
  class
- C+D+B+E lock (no standalone `/proof-gate` skill) matches our lean

**Partial for the felt-product fail that motivated the FR.** Process and DOM
plumbing can still PASS while a human product-look grade against
`proof_reference` would fail. That gap is owned by a **visitor product-look
lane**, not a PBB regress. Do not reopen PBB for product-look vocab.

Generic observation class (method only; no product-surface specifics):

| observation class | why process/DOM-only still greens |
|---|---|
| Copy contradicts measured fork/metric polarity | not in PROC-* vocab |
| Near-duplicate alternatives | chips present ≠ tradeoff felt |
| Overlay buries the subject geometry | host height > 0; still not reference class |
| Idle surface is chrome-on-void | no idle proof_job check |

So: **PBB matches “ACCEPT green without named Proof fields/harness.”**
It does **not** catch **“ACCEPT green with Proof fields while the capture
fails human/LLM product look.”**

## 2. Anything mis-locked in C+D+B+E / classifier / freeze allowlist?

**Keep C+D+B+E.** No reopen of A (standalone skill) yet.

| item | judgment |
|---|---|
| Classifier `proof_required` yes/no/n/a | Correct — do not keyword-infer |
| Freeze + proof-serving allowlist | Correct — absolute freeze would block Proof delivery |
| Screenshot optional vs DOM hard gate | Right for v0 host collapse. Incomplete as the only bar for visitor product — see product-look lane |
| Mechanical checker only PROC-PASS-NO-PROOF + PROC-NO-VISUAL | Fine for BUILD ACCEPT of wavves itself; label review/live ids clearly |
| High-reasoning adversarial/ACCEPT | Aligns with house lock |

**Mis-lock risk to watch:** playbook step 8 (“screenshot miss alone is not the
hard gate”) is correct for blank-canvas, but a visitor lane with
`visual_accept: yes` and a named figure class can still ship nonsense if
review never runs an LLM/human grade. Do not soften that into “DOM green =
done” in docs.

**Not mis-locked:** omitting live `scripts/proof_host_probe.py` at first ship —
contract named is acceptable if the next visitor lane wires a real probe or
cites a host-height capture in ACCEPT. Still want the probe shipped before
claiming Rule 2b is a live shared tool.

**Side-memo discipline (ack):** Product-facing docs should only state the
applied idea (judgment + structure / mid-render tunnel). Keep introspection
memos as orphaned side files with nothing product-facing pointing at them.

## 3. What would you change before the next visitor lane uses `proof_required: yes`?

Require on that lane (in addition to PBB fields):

1. **`proof_required: yes`** with the four fields (already mandatory).
2. **DOM/host hard gate** — host height > 0 / non-blank canvas (PBB Rule 2b).
3. **Capture-then-grade** (frozen captures + transcripts) — not live-fetch-only
   ACCEPT scrape.
4. **Independent visual grade** against `proof_reference` with a closed
   **product** fail vocab (contradicting pairs, near-duplicates, buried
   subject, fails reference-class readability).
5. **Author of the build must not grade ACCEPT.**
6. **Ship `proof_host_probe.py` or equivalent runnable command** before claiming
   Rule 2b is live shared tooling.
7. Optional: add a wavves eval fixture that feeds a captured screenshot +
   rubric JSON (product-look) — defer while product-look stays in the visitor
   lane.

Do **not** block PBB as shipped. Treat the product-look lane as the extension
the FR left open when it made screenshot optional.

## Discovery notes for wavves (non-blocking)

- Mid-dispatch empty returns (orchestrator exits after launching parallel
  background members) burned cycles — worth a wavves etiquette / charter note:
  orchestrator owns completion; no return until RECONCILE+GATE exist.

## Reply summary (one line)

PBB ships the fail mode we meant for **process/docs ACCEPT**; next visitor
`proof_required: yes` still needs **DOM hard gate + capture-then-grade +
independent product-look grade** before ACCEPT is enough.
