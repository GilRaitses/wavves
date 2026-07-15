# PTB-W1a — playbook shape for `paragraph-tunnel.md`

- **Runner:** PTB-W1a
- **Date:** 2026-07-15 (America/New_York)
- **Owned output:** this file
- **Target for W2a:** `skills/wavves/playbooks/paragraph-tunnel.md`
- **repo_state_verified_against:** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2` (from `waveset.md`)
- **Locks authority:** `decisions/LOCKED-DECISIONS.md` (PTG copy; do not reopen)

## 1. Section structure (match existing playbooks)

Existing playbooks under `skills/wavves/playbooks/` share a fixed skeleton
(see `check.md`, `decide.md`, `proceed.md`, `charter-lane.md`, `bootstrap.md`):

1. **Title** — `# <Name> playbook`
2. **Route** — one line: `Route: **<leaf or invoke path>** (\`<operator token>\`)`
3. **Optional one-line purpose** (proceed/pickup style) — only if Route alone is ambiguous
4. **STEPS** — fenced checklist:
   ```
   - [ ] 1. …
   - [ ] 2. …
   ```
5. **Lane types table** — `Lane types this playbook covers:` + `| type | operator says |`

### Recommended Route line (v0 — no slash skill)

Per PTG-LAND (C + dispatch STEPS; defer A) and PTG-INVOKE (lane runner):

```text
Route: **dispatch STEPS** (lane runner; no `/paragraph-tunnel` slash skill in v0)
```

Do **not** invent a leaf-skill row like `Route: **paragraph-tunnel** (\`/paragraph-tunnel\`)`.
That would reopen A. Mirror `proceed.md` / `pickup.md` (hydrate + execute paths)
more than `check.md` / `decide.md` (which bind a slash leaf).

### Recommended title

```text
# Paragraph tunnel playbook
```

### Recommended lane-types table (draft)

```markdown
Lane types this playbook covers:

| type | operator says |
|:-----|:--------------|
| outbound mid-render tunnel | render then tunnel then lint; CLEARED preview blocked until tunnel PASS |
| tunneled field named | waveset `tunnel_field` (default body paragraph 2) |
| rewrite-capped revise | after one rewrite still FAIL → operator REVISE |
```

## 2. Exact invoke order

Hard order from FR + PTG-INVOKE (do not reorder):

```text
render  →  tunnel  →  prose_lint  →  (preview / CLEARED)
                 │
                 ├─ adversarial (Grok) → capture
                 ├─ if FAIL → rewrite once (Grok), siblings frozen
                 └─ re-adversarial (separate capture) + freeze checksum
```

| phase | who | when | output |
|---|---|---|---|
| render | lane runner | produces draft body | rendered artifact on disk |
| tunnel:adversarial | Grok subagent | immediately after render; field = `tunnel_field` | `gate-captures/<CODE>-pN-adversarial.json` |
| tunnel:rewrite (optional) | Grok subagent | only if adversarial FAIL; loop cap **1** | `gate-captures/<CODE>-pN-rewrite.json` |
| tunnel:re-adversarial | **separate** Grok capture (PTG-JUDGE) | after rewrite; not same-agent inline PASS | second adversarial JSON (or `-pN-re-adversarial.json`) |
| freeze check | mechanical | with re-adversarial | sibling paragraph checksums match pre-tunnel |
| prose_lint | existing lint tool | **only after** tunnel PASS (or operator REVISE path) | lint capture |

**Hard-fail if skipped** on CLEARED-preview outbound lanes when `tunnel_field` is named in waveset (PTG-INVOKE implications).

Internal tunnel micro-order the playbook must spell out:

1. Resolve `tunnel_field` from waveset (default: body paragraph 2).
2. Snapshot sibling paragraphs; record freeze checksums.
3. Adversarial attack **only** the named field; emit closed-vocab fail ids (PN-* + STANDIN / RESEARCH-META / FALSEFACT; aliases to P2-* per PTG-VOCAB — vocab detail owned by W1c; playbook cites closed vocab, does not redefine).
4. On PASS → skip rewrite; proceed to prose_lint.
5. On FAIL → one rewrite of **only** that field; write rewrite capture with loop metadata.
6. Separate re-adversarial + sibling freeze verify.
7. If still FAIL after loop 1 → stop; escalate operator REVISE (no second rewrite, no auto-pass).
8. Only then run prose_lint / ASP-F-style preview.

## 3. What the playbook must say (locks → prose)

### Grok model lock (PTG-MODEL)

Playbook MUST state, in STEPS and/or a one-line non-negotiable under Route:

- Adversarial and rewrite Task/subagent launches **must** set
  `model: cursor-grok-4.5-high-fast`.
- No Claude / Composer / unspecified "high-reasoning" fallback for tunnel lenses.
- Same model may judge rewrite (Grok-on-Grok OK); **separate capture** still required (PTG-JUDGE).

### Fail-cap (PTG-FAIL-CAP)

Playbook MUST state:

- Remediation loop cap = **1** rewrite.
- After loop 1 still FAIL → **operator REVISE**; do not auto-pass; do not silent-keep; do not second rewrite.
- Rewrite JSON must record `post_cap: escalate` when escalating.
- Preview / send / CLEARED blocked until operator revise clears the tunnel.

### Judge / freeze (PTG-JUDGE)

Playbook MUST state:

- Rewrite re-check is a **separate re-adversarial step + capture**, not an inline same-agent PASS claim.
- Sibling paragraphs (opener/close / non-`tunnel_field` body) are **frozen**; checksums after tunnel must match pre-tunnel snapshot.
- Two captures minimum after a rewrite path: rewrite + re-adversarial (plus freeze evidence in capture or sibling file).

Suggested capture names (align FR; W2a may keep exact FR names):

- `gate-captures/<CODE>-pN-adversarial.json`
- `gate-captures/<CODE>-pN-rewrite.json`
- re-adversarial: either a second adversarial file or `<CODE>-pN-re-adversarial.json` — pick one naming rule in W2a and stick to it; FR named the first two.

## 4. What NOT to include

| do not | why | lock |
|---|---|---|
| `/paragraph-tunnel` slash skill directory or Route binding | deferred until C proves out | PTG-LAND (strike A for v0) |
| Extension of `mod-check` / mid-render inside check waves | phase leak (mod-check is pre-build) | PTG-LAND strike B; PTG-INVOKE strike C |
| Replacing prose_lint / purpose-gates | non-goal | FR Non-goals |
| Auto-send outbound mail | non-goal | FR |
| Broad whole-email tone rewrite | tunnel is field-scoped only | FR |
| Unbounded rewrite loops / charter default cap 2 | outbound fail-cap is stricter | PTG-FAIL-CAP |
| Editing `skills/wavves/SKILL.md` in W2a | INT-only shared file | `waveset.md` PTB-INT gate |
| Overloading `evals/run_fixtures.py` | disjoint harness | waveset Intent / W2 |

## 5. WIRING note for later INT (do not edit SKILL.md now)

W2a ships **only** `skills/wavves/playbooks/paragraph-tunnel.md` (+ this finding's pasteable STEPS).

**PTB-INT** (O0-gated, single editor) must later patch `skills/wavves/SKILL.md`:

1. **Routing table** — add a row, e.g.:

   | Playbook | Leaf skill | For |
   |:---------|:-----------|:----|
   | paragraph-tunnel | dispatch STEPS (no slash v0) | mid-render outbound paragraph gate; after render, before prose_lint |

2. **Playbook steps list** — add:

   - **Paragraph tunnel.** `playbooks/paragraph-tunnel.md`

3. Do **not** add a Leaf skills slash row for `/paragraph-tunnel` in v0.

4. Optional: under ambiguous defaults, one sentence that CLEARED-preview outbound lanes with `tunnel_field` set route through this playbook before lint/preview.

W2a should leave a short `## WIRING (INT only)` comment **inside the playbook file** or a one-liner at the bottom pointing at this section — content only; no SKILL.md edit until INT.

## 6. Concrete STEPS checklist draft (paste-nearly-as-is for W2a)

Recommended full playbook body for W2a:

````markdown
# Paragraph tunnel playbook

Route: **dispatch STEPS** (lane runner; no `/paragraph-tunnel` slash skill in v0)

Mid-render gate for a named outbound paragraph. Order is fixed:
**render → tunnel (adversarial → optional rewrite) → prose_lint**.
Does not replace prose_lint. Does not run inside mod-check.

Model lock: adversarial and rewrite subagents MUST use
`model: cursor-grok-4.5-high-fast` (no Claude/Composer fallback).

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
        vocab (PN-* plus STANDIN / RESEARCH-META / FALSEFACT; P2-* aliases
        allowed). Write `gate-captures/<CODE>-pN-adversarial.json`.
- [ ] 5. If adversarial PASS: skip rewrite. Proceed to step 9 (prose_lint).
- [ ] 6. If adversarial FAIL: rewrite **only** `tunnel_field` once (loop cap 1)
        with `model: cursor-grok-4.5-high-fast` to clear every fail id.
        Do not touch frozen siblings. Write `gate-captures/<CODE>-pN-rewrite.json`.
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
````

## 7. Shape deltas vs sibling playbooks (for W2a awareness)

| sibling | bind | this playbook |
|---|---|---|
| `check.md` / `decide.md` | slash leaf skill | **no** slash leaf (dispatch STEPS) |
| `proceed.md` | executes `recommended_actions` | executes mid-render tunnel STEPS inside a BUILD/outbound lane |
| `charter-lane.md` | creates lanes | tunnel is a **STEPS fragment** charter/dispatch templates reference |

W2a should keep the file short like `check.md` (~25–40 lines of STEPS + table), not a mini-skill. Long vocab tables belong in evals / FR / W1c port, not duplicated in the playbook beyond a one-line closed-vocab pointer.

## 8. Acceptance spot-check map (for later PTB-ACCEPT)

From `waveset.md` ACCEPT item 2 — playbook must visibly document:

- [x] order render → tunnel → lint (section 2 + STEPS 2/9)
- [x] fail-cap escalate (STEPS 8)
- [x] Grok model lock (header + STEPS 4/6)
- [x] judge/freeze rules (STEPS 3/7)
- [x] no `/paragraph-tunnel` skill (Route + WIRING)
- [x] mod-check untouched / not mid-render (purpose line + NOT table)

## Sources (hydrated, not invented)

- `wavves/lanes/20260715_paragraph-tunnel-build/waveset.md`
- `wavves/lanes/20260715_paragraph-tunnel-build/decisions/LOCKED-DECISIONS.md`
- `skills/wavves/playbooks/{check,decide,proceed,charter-lane,bootstrap,pickup}.md`
- `skills/wavves/SKILL.md` (router shape; INT target only)
- `feature-requests/20260715_paragraph-tunnel-gate.md`
- `wavves/lanes/20260715_paragraph-tunnel-gate-check/decisions/PTG-{LAND,INVOKE,MODEL,FAIL-CAP,JUDGE}.md`
