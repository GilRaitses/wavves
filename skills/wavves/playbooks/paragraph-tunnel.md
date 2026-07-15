# Paragraph tunnel playbook

Route: **dispatch STEPS** (lane runner; no `/paragraph-tunnel` slash skill in v0)

Mid-render gate for a named outbound paragraph. Order is fixed:
**render → tunnel (adversarial → optional rewrite) → prose_lint**.
Does not replace prose_lint. Does not run inside mod-check.

Model lock: adversarial and rewrite subagents MUST use
`model: cursor-grok-4.5-high-fast` (no Claude/Composer fallback).

**Whitelist:** `"nice because"` / `"because it is"` is **allowed**. Never emit
`PN-BECAUSE`, `P2-BECAUSE`, `PN-EXPLAIN`, or `P2-EXPLAIN`.

Closed fail vocab: `PN-STACK`, `PN-COMPARE`, `PN-GLOSS`, `PN-FIXTURE`,
`PN-MULTI`, plus `STANDIN`, `RESEARCH-META`, `FALSEFACT`.

```
- [ ] 1. Confirm waveset names `tunnel_field` (default: body paragraph 2).
        On CLEARED-preview outbound lanes, hard-fail if the field is missing
        or this playbook is skipped.
- [ ] 2. Confirm render is complete. Do not start tunnel before the draft
        artifact exists on disk.
- [ ] 3. Snapshot sibling paragraphs (everything outside `tunnel_field`).
        Record freeze checksums before any rewrite.
- [ ] 4. Run adversarial attack on **only** `tunnel_field` with
        `model: cursor-grok-4.5-high-fast`. Emit fail ids from the closed
        vocab above. Do not fail for nice-because framing. Write
        `gate-captures/<CODE>-pN-adversarial.json`.
- [ ] 5. If adversarial PASS: skip rewrite. Proceed to step 9 (prose_lint).
- [ ] 6. If adversarial FAIL: rewrite **only** `tunnel_field` once (loop cap 1)
        with `model: cursor-grok-4.5-high-fast` to clear every fail id.
        Keep nice-because if the operator line uses it. Do not touch frozen
        siblings. Write `gate-captures/<CODE>-pN-rewrite.json`.
- [ ] 7. Re-check with a **separate** re-adversarial capture (same Grok model
        OK; no inline same-agent PASS). Verify sibling freeze checksums match
        the pre-tunnel snapshot. Persist the re-adversarial capture.
- [ ] 8. If still FAIL after loop 1: set `post_cap: escalate`, stop rewrite,
        escalate **operator REVISE**. Do not auto-pass. Do not second rewrite.
        Block preview/send until revise clears the tunnel.
- [ ] 9. Only after tunnel PASS (or operator revise path cleared): run
        prose_lint / ASP-F-style preview. Never lint-before-tunnel on
        tunneled outbound lanes.
- [ ] 10. Report: tunnel verdict, fail ids cleared or escalated, capture paths,
        freeze checksum OK/FAIL, and that prose_lint has not been skipped ahead.
```

Lane types this playbook covers:

| type | operator says |
|:-----|:--------------|
| outbound mid-render tunnel | render then tunnel then lint; CLEARED preview gated |
| tunneled field named | waveset `tunnel_field` (default body paragraph 2) |
| rewrite-capped revise | one rewrite then still FAIL → operator REVISE |

## WIRING (INT only — do not edit SKILL.md in W2a)

Add router row + playbook list entry in `skills/wavves/SKILL.md` during PTB-INT:
playbook `paragraph-tunnel` → `playbooks/paragraph-tunnel.md`; leaf = dispatch STEPS;
no `/paragraph-tunnel` slash skill in v0.
