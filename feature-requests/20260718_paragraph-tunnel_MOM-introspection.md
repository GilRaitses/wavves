# Feedback memo — MoM Humanizer thread × paragraph-tunnel FR

**To:** thread mod / FR reviewer (paragraph-tunnel ACCEPT)  
**From:** O0 (operator-facing)  
**Date:** 2026-07-18 (America/New_York)  
**Artifact under review:** `feature-requests/20260715_paragraph-tunnel-gate.md`  
**External stimulus:** made-of-meat thread “Humanizer / De-Slopper / Self-Deepfaker”  
  (Matt Mireles opener + replies from Abdullah Sarwar, Peter Bell, Akshay Patel, others)  
**repo_state_verified_against:** wavves `9ae90e9` / FR status as on disk at memo time  
**landing_commit_hash:** _(completion report only)_

## What the MoM thread is arguing (compressed)

| voice | claim |
|---|---|
| Matt | Post-process AI email into “me” via SFT (AI-slop → real emails as pairs). |
| Abdullah | Don’t feed thousands of samples for taste. Golden samples + HITL edits → persistent rules. Writer ≠ reviewer. Deterministic checks beside LLM judges. Teach **judgment**, not historical phrasing. |
| Peter | Voice without structure is slop that sounds like you and says nothing. Need intermediate artifacts (strategy → outline → adversarial → draft). Blind reviewer until indistinguishable. Dreaming/memory often becomes stale cache. |
| Akshay | Framework of good writing > copying past examples; tone is tunable by context. |

Fiction (Adam) is out of scope for outbound research email; Peter’s nonfiction constraint applies.

## How that maps onto paragraph-tunnel (what we already built)

Paragraph-tunnel is **not** Matt’s humanizer. It is closer to Peter’s intermediate stage + Abdullah’s HITL→rules + deterministic panel.

| MoM idea | Tunnel FR / playbook already |
|---|---|
| Intermediate artifact before “voice” | Named `tunnel_field` after render, before prose_lint |
| Adversarial before draft ships | Gate 1 fail ids; separate re-adversarial after rewrite |
| Writer ≠ reviewer | Rewrite agent ≠ re-adversarial capture; mechanical `check_paragraph_tunnel.py` |
| Deterministic checks | Closed vocab + fixtures (STACK/COMPARE/GLOSS/FIXTURE/MULTI/STANDIN…) |
| HITL correction → persistent rule | Operator struck agent-invented BECAUSE/EXPLAIN; whitelist locked in playbook + evals |
| Freeze what is already good | Sibling paragraph freeze checksums (opener/close stay put) |
| Escalate, don’t auto-pass | Loop cap 1 → operator REVISE |

Live APPL evidence: opener/close stabilized early; P2 ate revise cycles; lint kept passing. That is Peter’s “sounds like you, says nothing” failure at **paragraph** scale, not mailbox-scale voice.

## What the thread suggests we should **not** do in ACCEPT / v1

1. **Do not expand FR into SFT/LoRA humanizer.** Different product. Tunnel can sit *under* a future humanizer; it does not replace it.
2. **Do not treat golden-email corpus as the acceptance metric.** Acceptance stays runnable fixtures + playbook order, not “blind reviewer can’t tell.”
3. **Do not add dreaming/memory compounding into tunnel.** Peter’s stale-cache warning; our durable surface is locked decisions + fail vocab, not transcript residue.
4. **Do not reintroduce agent-invented bans** (BECAUSE/EXPLAIN) without operator ask. That was the opposite of Abdullah’s “teach judgment” — it taught the agent’s guess.

## Introspection for the ACCEPT reviewer (use these as feedback comments)

1. **Scope honesty:** Confirm ACCEPT language still says mid-render structural tunnel, not voice-clone / de-slop model.
2. **Complement, don’t absorb:** Prose_lint / purpose / public-copy remain siblings. Tunnel fails what lint misses (gloss, stack, compare, fixture-only, multi). Matt’s post-process would still miss “works at night” / “come together” until a human named them.
3. **HITL path is first-class:** The NICE-BECAUSE overturn is not a footnote. ACCEPT should treat operator overturn → lock file as a required lifecycle, not an exception.
4. **Mechanical panel stays king for v0:** Keep `evals/check_paragraph_tunnel.py` as the runnable gate. Optional later: LLM reviewer panel (Abdullah-style) *after* mechanical PASS — not instead of it.
5. **Structure before tone:** If a future FR adds “voice guidelines,” require an intermediate artifact (strategy / outline / tunneled field) first — Peter’s dead-end warning.
6. **Defer slash skill:** LAND=C still correct; packaging as MCP/API humanizer (Matt) is a different FR family.

## One-line position for the mod

Matt is solving *voice transfer*; Abdullah/Peter are solving *judgment + structure*; paragraph-tunnel ships a thin, runnable slice of the second family for one outbound paragraph, with operator HITL as the rule-writing loop — which is why ACCEPT should stay narrow and why the MoM thread is corroboration, not a reason to widen the FR into SFT.
