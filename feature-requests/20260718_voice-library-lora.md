# FR-20260718 — Voice library + optional LoRA (MoM pipeline)

- **Status:** parked-pending-apollo-proof  
  Proof lane: pax `wavves/lanes/20260718_apollo-voice-proof/` (AVP).  
  Do not `/charter` wavves BUILD until AVP-ACCEPT.
- **Date:** 2026-07-18 (America/New_York)
- **Product surface:** wavves skill/playbook family (separate from paragraph-tunnel)
- **External stimulus:** Matthew W. MoM pipeline (2026-07-18) — mailbox →
  scrub → label → hybrid index → VOICE.md → rewrite → verify → HITL →
  optional LoRA
- **Related:** `20260715_paragraph-tunnel-gate.md` (structure mid-render);
  `20260718_paragraph-tunnel_MOM-introspection.md`
- **evidence_verified_against:** _(set at mod-check)_  
- **landing_commit_hash:** _(O0 completion only)_

## Intent

Build a **local-first** pipeline that turns the operator’s real sent mail into a
searchable voice library, rewrites new drafts with retrieved examples +
VOICE.md, verifies meaning/voice stats, learns from corrections, and
**optionally** trains a LoRA that writes closer to the operator without
retrieval every time.

Composes with paragraph-tunnel: tunnel owns structural mid-render fail modes;
this FR owns voice retrieval / profile / optional weight adapt. Do not merge
scopes.

## Pipeline (locked from MoM write-up — open calls below)

1. Real sent emails as sole voice source of truth  
2. Local PII scrub → placeholders; originals never leave machine  
3. Label: intent / audience / formality (extendable: time)  
4. Hybrid index: embedding + labels  
5. Distill VOICE.md from strong examples + corpus stats  
6. Rewrite new draft via situation match + retrieved examples + VOICE.md  
7. Auto-check: meaning/facts kept; statistical “like you / not generic AI”  
8. Operator review; corrections → high-quality train pairs  
9. Expand train set (real + corrections + deliberate AI-slop contrast)  
10. Optional: LoRA on small open model (e.g. Llama 3.3 8B class)

Peter Bell addendum (capture as open call): document **strategies per
classified category** as reviewable artifacts so today’s judgment can diverge
from historical habit.

## Non-goals (v0)

- Accepting mailbox passwords / sharing Gmail credentials with any agent  
- Shipping originals or unscrubbed text to remote train hosts by default  
- Replacing paragraph-tunnel / prose_lint  
- Requiring LoRA in v0 (retrieval+VOICE.md path must stand alone)  
- Blind “sounds like me” as sole acceptance without meaning check  

## Data intake (required lock before BUILD)

| option | meaning |
|---|---|
| A | Google Takeout / MBOX export operator drops in a local path |
| B | Gmail API OAuth app operator installs; agent never sees password |
| C | Manual curated golden corpus (Abdullah-style) only — no full mailbox |

**Hard rule:** no password paste into chat, MCP, or repo. Scrub before any
index/train artifact is written outside an operator-designated private dir
(not committed to public remotes).

## Open calls for `/mod-decide`

1. **VOICE-INTAKE** — A / B / C (or A then C hybrid)  
2. **VOICE-HOST** — local-only vs private GPU host for embeddings/LoRA  
3. **VOICE-SCOPE** — email-only vs + LinkedIn/docs later  
4. **VOICE-LORA** — v0 retrieval-only / v1 optional LoRA / LoRA-required  
5. **VOICE-STRATEGY** — require per-category strategy docs (Peter) yes/no  
6. **VOICE-COMPOSE** — order vs paragraph-tunnel: draft → tunnel → voice
   rewrite vs voice then tunnel  
7. **VOICE-LAND** — wavves playbook+skill vs separate private repo for corpus  

## Acceptance sketch (after locks)

1. Scrubbed corpus + hybrid retrieve returns situation-matched examples  
2. VOICE.md regenerable from corpus  
3. Rewrite path keeps a fact checklist; fails if key facts drop  
4. Correction loop appends train pairs without storing raw PII  
5. If LoRA unlocked: adapter loads and beats baseline VOICE.md-only on a
   held-out blind set (metric named at decide time)  

## Charter readiness

**Yes, charterable** after FR mod-check + mod-decide on open calls.  
Recommended first charter shape: discovery/read-only on Takeout path + scrub
design + index prototype; LoRA gated as later wave.
