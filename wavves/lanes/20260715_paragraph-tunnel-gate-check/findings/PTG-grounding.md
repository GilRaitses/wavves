# PTG-W1a — grounding findings

- **lens:** grounding
- **model:** Grok (Cursor Grok 4.5; model lock honored)
- **artifact:** `/Users/gilraitses/wavves_build/feature-requests/20260715_paragraph-tunnel-gate.md`
- **wavves_build HEAD (must cite):** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2` on `main` (verified live)
- **repo_state_verified_against:** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2` (wavves_build main at check)
- **pax tip at check (informational):** `55282a544cb55e6e7be3539fea86675605dbf143`
- **lens lean (grounding only):** **REVISE**

## Paths checked

| path | exists | notes |
|---|---|---|
| `feature-requests/20260715_paragraph-tunnel-gate.md` | yes | artifact under review |
| `feature-requests/README.md` | yes | indexes FR-20260715-paragraph-tunnel as draft |
| `skills/mod-check/` (`SKILL.md`) | yes | landing option B parent; has design-review adversarial lens W1d |
| `skills/charter/` (`SKILL.md`, `EXECUTION_WIRING.md`) | yes | landing option B parent; no "tunneled field" step today |
| `skills/wavves/playbooks/` | yes | landing option C parent (bootstrap, check, decide, proceed, …) |
| `evals/` (`README.md`, `fixtures/`, runners) | yes | landing option C / acceptance-sketch parent; current fixtures are mod-check design defects, not outbound tunnel |
| `skills/paragraph-tunnel/` | **no** | option A proposed skill; FR does not claim it already exists |
| pax `wavves/lanes/20260715_apply-case-crack-asp-send/decisions/APPL-P2-TUNNEL.md` | yes | cited source decision |
| pax `…/gate-captures/APPL-p2-adversarial.json` | yes | cited |
| pax `…/gate-captures/APPL-p2-rewrite.json` | yes | cited |
| pax `…/drafts/APPL-sample-{high,mid,low}.txt` | yes | post-rewrite one-sentence P2s match rewrite capture |
| pax `…/gate-captures/APPL-prose.json` | yes | supports "lint kept passing" / mechanical PASS history |
| pax `…/gate-captures/APPL-asp-f-previews.json` | yes | ASP-F order sibling |
| `/Users/gilraitses/prose-gates/check_gates.py` | yes | external tool named by APPL dispatch / FR |
| `/Users/gilraitses/applications-for-jobs/cursor/prose_lint.py` | yes | external tool named by APPL dispatch / FR |
| `docs/purpose-gates.md`, `docs/public-copy-gates.md` | yes | FR non-goal names match real wavves_build docs |

## Claims that ground (no gap)

1. **Source decision path** resolves; Pick A P2 adversarial + rewrite + order before ASP-F matches FR sketch.
2. **Worked example tiers** match captures: Apollo PASS/keep; Ardesia FAIL EXPLAIN/STACK/BECAUSE/GLOSS/MULTI → one-sentence patio rewrite; Scotts FAIL COMPARE/MULTI → drop food-shop comparison.
3. **Post-rewrite drafts** match `APPL-p2-rewrite.json` `after` strings.
4. **Landing parents** for options A/B/C (`mod-check`, `charter`, `playbooks/`, `evals/`) all exist at wavves_build HEAD `f2fb8ce…`. Missing `/paragraph-tunnel` skill is consistent with "proposed, not decided."
5. **pax commit `21b1d7cf…` exists** and is the landing commit that added APPL-P2-TUNNEL + gate-captures (ancestor of current pax tip).

## Grounding gaps

### G1 — stale / mislabeled `repo_state_verified_against` on evidence (REVISE)

- **FR claims:** `repo_state_verified_against (evidence): pax 21b1d7cf06557a19ee042d6fde00d60a7ed8e759`
- **Evidence artifacts actually record:** `079f4c4cacb961996b23e66bd7749b4e243708f8` in:
  - `decisions/APPL-P2-TUNNEL.md`
  - `gate-captures/APPL-p2-adversarial.json`
  - `gate-captures/APPL-p2-rewrite.json`
- **Why wrong:** `21b1d7cf…` is the **landing** commit that *introduced* those files (`git show --stat`), not the pre-landing state the artifacts certify. Doctrine: `repo_state_verified_against` must not be the commit that contains the artifact.
- **evidence path:** FR lines 8–9 vs APPL-P2-TUNNEL.md L5 and both p2 JSON `repo_state_verified_against` fields.

### G2 — fail-id vocabulary renamed without mapping (REVISE soft)

- **FR vocabulary:** `PN-EXPLAIN`, `PN-STACK`, … (paragraph-N generic)
- **Live evidence vocabulary:** `P2-EXPLAIN`, `P2-STACK`, … (scoped to paragraph 2)
- **Worked example** drops the `P2-` / `PN-` prefix entirely (`EXPLAIN/STACK/…`) while matching the same conditions.
- FR says "copy-adjacent; lane may extend" but never states that `PN-*` = generalized `P2-*` from APPL.
- **evidence path:** FR fail table vs `APPL-P2-TUNNEL.md` fail table / `APPL-p2-adversarial.json` `fail_ids`.

### G3 — source gate-capture paths incomplete on FR header (REVISE soft)

- **FR header:** "plus gate-captures `APPL-p2-adversarial.json`, `APPL-p2-rewrite.json`" (filenames only).
- **Actual paths:** `wavves/lanes/20260715_apply-case-crack-asp-send/gate-captures/APPL-p2-adversarial.json` (and sibling rewrite).
- Resolvable by convention under the cited lane, but not a full cited path.
- **evidence path:** FR L7–8 vs real `gate-captures/` directory listing.

### G4 — "dispatch STEPS" seam not present in charter docs (REVISE soft / naming)

- **FR option A:** "New skill `/paragraph-tunnel` invoked from dispatch STEPS"
- **Checked:** no `STEPS` token in `skills/charter/SKILL.md`, `EXECUTION_WIRING.md`, or `docs/`.
- Not a false claim of an existing skill, but the invocation seam name is ungounded in current charter vocabulary (dispatch / waveset / runnable gates exist; "STEPS" does not).
- **evidence path:** FR landing table option A vs charter skill surfaces at HEAD `f2fb8ce…`.

### G5 — not a gap (recorded for O0)

- Option B "charter Step tunneled field" and option A skill are **proposed**; absence is expected.
- `evals/` exists; FR acceptance sketch would add *new* fixtures — parent surface is real.
- External `prose_lint` / `check_gates` exist on disk and are wired in APPL `dispatch-w1.md`; FR does not falsely locate them inside wavves_build.

## Lens lean

**REVISE** (grounding only).

No BLOCK: cited evidence files open, worked example matches captures/drafts, and proposed landing parents exist at required wavves_build HEAD.

Must fix before grounding GO: **G1** (correct evidence `repo_state_verified_against` to `079f4c4c…`, or relabel `21b1d7cf…` as evidence landing commit). Strongly preferred: **G2** explicit PN↔P2 mapping; **G3** full gate-capture paths.
