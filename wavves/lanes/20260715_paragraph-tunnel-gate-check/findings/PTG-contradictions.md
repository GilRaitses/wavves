# PTG-W1b — contradictions

- **Lens:** contradictions
- **Artifact:** `feature-requests/20260715_paragraph-tunnel-gate.md`
- **repo_state_verified_against:** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2`
- **Lens lean:** **REVISE**

Named internal / phase-boundary conflicts only. No grounding or completeness inventory.

---

## C1 — Option B collapses mid-render outbound gate into mod-check (phase leak)

**Conflict:** Landing option B treats the paragraph tunnel as an extension of the **mod-check adversarial lens**, while the same FR states the gate is **mid-render** and that mod-check is the wrong phase.

| Claim | Quote / path |
|---|---|
| B = mod-check extension | FR §Where it lands: `B \| Extension to mod-check adversarial lens + charter Step "tunneled field"` |
| Self-rejection of B | FR: `B alone is too late (mod-check is pre-build, this gate is mid-render)` |
| Tunnel order | FR §Feature sketch: `Order — after render, before prose_lint / ASP-F-style preview` |
| mod-check purpose | `skills/mod-check/SKILL.md`: adversarial check of a **written artifact** **before** implementation planning or build; check playbook (`skills/wavves/playbooks/check.md`) same |

**Why it matters:** mod-check lenses review specs/plans; they do not sit in a render → lint → preview outbound pipeline. Naming option B as a landing site re-imports the phase leak the FR already diagnoses. Half of B (“charter Step tunneled field”) also collides with charter adversarial timing (C2).

**Severity:** blocking for any plan that picks B as-stated; non-blocking if mod-decide **strikes B** or redefines it as “document the pattern in check docs only (not runtime).”

---

## C2 — “Charter gate / tunneled field” ≠ mid-render copy tunnel (charter purpose conflict)

**Conflict:** Product surface and option B pull **charter** gate templates into scope; charter adversarial/acceptance gates judge **build artifacts after they exist**, not a single outbound paragraph mid-render.

| Claim | Quote / path |
|---|---|
| Product surface includes charter | FR header: `Product surface: wavves skills / charter gate templates / optional playbook` |
| B includes charter step | FR: `charter Step "tunneled field"` |
| Charter adversarial timing | `skills/charter/SKILL.md` model table: `adversarial gate … run after build artifacts exist` |
| Charter gate semantics | `skills/charter/EXECUTION_WIRING.md` + charter workflow step 11: runnable adversarial/**acceptance** harnesses → `gate-captures/` for wave evidence |

**Why it matters:** Reusing the word “adversarial” and `gate-captures/` from outbound copy lane evidence does not make the tunnel a charter wave gate. Extending charter templates for mid-render outbound rewrite would mutate charter purpose (build/accept evidence) into copy remediation.

**Severity:** REVISE — drop “charter gate templates” from product surface unless the FR means “future chartered **build** of the skill installs templates,” not “runtime = charter adversarial step.”

---

## C3 — A / B / C are not a clean exclusive set; acceptance pulls A and C at once

**Conflict:** Options are presented as alternate landings; narrative favors **A or C** and rejects **B alone**; acceptance sketch simultaneously requires dispatch-order docs (A-shaped) and an eval fixture (C-shaped).

| Claim | Quote / path |
|---|---|
| Three options table | FR §Where it lands: A skill / B mod-check+charter / C playbook+eval |
| Prefer A or C | FR: `Evidence so far favors A or C as a reusable outbound-copy gate` |
| Acceptance #1 (C) | `Eval fixture: stacked / gloss / compare inputs FAIL…` |
| Acceptance #3 (A) | `Dispatch template documents order: render → tunnel → lint → preview` |

**Why it matters:** “A or C” leaves open whether (i) exclusive pick, (ii) A+C hybrid, or (iii) C-only playbook without `/paragraph-tunnel`. A plan cannot satisfy “choose landing” while acceptance assumes both dispatch wiring and eval fixtures unless hybrid is an explicit allowed outcome.

**Severity:** REVISE — mod-decide must lock A-only / C-only / A+C; B out (per C1).

---

## C4 — “Reusable for any paragraph” vs copy-adjacent closed vocab + storefront PASS rule

**Conflict:** Pattern claims general paragraph/field reuse; default fail ids and PASS criteria are outbound storefront-copy semantics (outbound copy lane P2 lifted to `PN-*`).

| General claim | Copy-bound claim |
|---|---|
| FR: `Add a reusable **paragraph tunnel** pattern` | FR vocab header: `Default fail vocabulary (copy-adjacent; lane may extend)` |
| FR: `attack only a named paragraph / field` | `PN-EXPLAIN` … `nice / interesting / a fit`; `PN-COMPARE` … `other types or destinations`; `PN-FIXTURE` … `Fixture inventory` |
| Default field: `body paragraph 2` | PASS: `one concrete fact the recipient would recognize` |
| Worked example + problem = outbound copy lane storefront P2 | Evidence `outbound copy lane-P2-TUNNEL.md`: shop/owner/cold-email PASS rule |

**Why it matters:** A lane that “extends” vocab cannot clear a default PASS rule that assumes a human recipient recognizing a place fact. Either the feature is **outbound-copy-scoped** (vocabulary + PASS are domain-bound) or the defaults must be **mechanism-only** (scoped field, freeze siblings, loop cap, capture names) with domain vocab supplied per lane. As written, both claims stand.

**Severity:** REVISE (would become BLOCK if charter shipped universal defaults without a domain lock).

---

## C5 — Dual meaning of “adversarial” (mod-check lens vs outbound tunnel gate)

**Conflict:** FR and evidence reuse “adversarial gate” language that mod-check already owns for **spec review lenses**; the tunnel is a **runtime rewrite gate** with fail ids and a remediation loop.

| Surface | Meaning of “adversarial” |
|---|---|
| `skills/mod-check/SKILL.md` W1d | Read-only findings lens on a written artifact; no rewrite of production copy |
| FR §Feature sketch + outbound copy lane-P2-TUNNEL | Attack named paragraph; on FAIL, rewrite that paragraph; capture JSON; loop cap 1 |
| Option B | Literally extends “mod-check adversarial lens” |

**Why it matters:** Without distinct naming (`paragraph-tunnel` / `copy-tunnel` vs `mod-check` adversarial), implementers can wire the tunnel into check lanes or treat check lenses as rewrite authorities.

**Severity:** non-blocking naming debt if B is struck; blocking if B remains.

---

## C6 — Soft internal tension: remediates copy vs non-goal “broad tone rewriting”

**Conflict (weak):** Rewrite gate must clear every fail id (may restyle the paragraph) while non-goals ban broad tone rewriting of whole emails.

| Claim | Quote |
|---|---|
| Rewrite | `rewrite **only** that paragraph to clear every fail id` |
| Non-goal | `Broad tone rewriting of whole emails` |

**Resolution if locked:** Scoped single-paragraph remediation is allowed; whole-email tone passes remain forbidden. Not a hard contradiction unless rewrite agents interpret “clear every fail id” as license to restyle siblings (frozen) or the full body.

**Severity:** non-blocking if freeze rule is kept hard.

---

## Lens lean

**REVISE**

Not **BLOCK**: the FR correctly states mid-render order and that **B alone is too late**, so the worst phase leak is partially self-flagged. Salvageable before plan if mod-decide:

1. Strike or redefine **B** (no mod-check runtime; no charter adversarial-step identity).
2. Lock scope: **outbound-copy tunnel** (domain vocab OK) **or** mechanism-only reusable core + per-lane vocab (not both as defaults).
3. Lock landing: **A**, **C**, or explicit **A+C**; align acceptance to that lock.
4. Narrow product surface away from “charter gate templates” unless meaning is install-via-chartered-build only.

Not **GO**: C1–C4 remain live contradictions in the draft text.
