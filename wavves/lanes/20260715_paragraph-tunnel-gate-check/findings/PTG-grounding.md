# PTG-W1a — grounding findings

- **lens:** grounding
- **model:** Grok (Cursor Grok 4.5; model lock honored)
- **artifact:** `<repo-root>/feature-requests/20260715_paragraph-tunnel-gate.md`
- **wavves_build HEAD (must cite):** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2` on `main` (verified live)
- **repo_state_verified_against:** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2` (wavves_build main at check)
- **originating product repo tip at check (informational):** foreign pin
- **lens lean (grounding only):** **REVISE**

## Paths checked

Evidence cited in the FR was verified in the originating product repo at check time.
Absolute paths are redacted here for public tip hygiene.

| surface | exists | notes |
|---|---|---|
| `feature-requests/20260715_paragraph-tunnel-gate.md` | yes | artifact under review (wavves_build) |
| `feature-requests/README.md` | yes | indexes FR-20260715-paragraph-tunnel as draft |
| `skills/mod-check/` (`SKILL.md`) | yes | landing option B parent; has design-review adversarial lens W1d |
| `skills/charter/` (`SKILL.md`, `EXECUTION_WIRING.md`) | yes | landing option B parent; no "tunneled field" step today |
| `skills/wavves/playbooks/` | yes | landing option C parent (bootstrap, check, decide, proceed, …) |
| `evals/` (`README.md`, `fixtures/`, runners) | yes | landing option C / acceptance-sketch parent; current fixtures are mod-check design defects, not outbound tunnel |
| `skills/paragraph-tunnel/` | **no** | option A proposed skill; FR does not claim it already exists |
| outbound copy lane P2-TUNNEL decision | yes (originating product repo) | cited source decision |
| outbound copy lane p2-adversarial capture | yes (originating product repo) | cited |
| outbound copy lane p2-rewrite capture | yes (originating product repo) | cited |
| outbound copy lane sample drafts (high/mid/low) | yes (originating product repo) | post-rewrite one-sentence P2s match rewrite capture |
| outbound copy lane prose capture | yes (originating product repo) | supports "lint kept passing" / mechanical PASS history |
| outbound copy lane ASP-F preview capture | yes (originating product repo) | ASP-F order sibling |
| external prose gate tools | yes (consumer repos) | external tools named by outbound copy dispatch / FR |
| `docs/purpose-gates.md`, `docs/public-copy-gates.md` | yes | FR non-goal names match real wavves_build docs |

## Claims that ground (no gap)

1. **Source decision path** resolves in originating product repo; Pick A P2 adversarial + rewrite + order before ASP-F matches FR sketch.
2. **Worked example tiers** match captures: Apollo PASS/keep; Ardesia FAIL EXPLAIN/STACK/BECAUSE/GLOSS/MULTI → one-sentence patio rewrite; Scotts FAIL COMPARE/MULTI → drop food-shop comparison.
3. **Post-rewrite drafts** match p2-rewrite capture `after` strings.
4. **Landing parents** for options A/B/C (`mod-check`, `charter`, `playbooks/`, `evals/`) all exist at wavves_build HEAD `f2fb8ce…`. Missing `/paragraph-tunnel` skill is consistent with "proposed, not decided."
5. **Outbound copy evidence foreign pin exists** and is the landing commit that added P2-TUNNEL + gate-captures (ancestor of current originating product repo tip).

## Grounding gaps

### G1 — stale / mislabeled `repo_state_verified_against` on evidence (REVISE)

- **FR claims:** `repo_state_verified_against (evidence):` outbound copy foreign pin
- **Evidence artifacts actually record:** a different foreign pin in:
  - outbound copy P2-TUNNEL decision
  - p2-adversarial capture
  - p2-rewrite capture
- **Why wrong:** the FR evidence pin is the **landing** commit that *introduced* those files, not the pre-landing state the artifacts certify. Doctrine: `repo_state_verified_against` must not be the commit that contains the artifact.

### G2 — fail-id vocabulary renamed without mapping (REVISE soft)

- **FR vocabulary:** `PN-EXPLAIN`, `PN-STACK`, … (paragraph-N generic)
- **Live evidence vocabulary:** `P2-EXPLAIN`, `P2-STACK`, … (scoped to paragraph 2)
- **Worked example** drops the `P2-` / `PN-` prefix entirely (`EXPLAIN/STACK/…`) while matching the same conditions.
- FR says "copy-adjacent; lane may extend" but never states that `PN-*` = generalized `P2-*` from outbound copy lane.
- **evidence path:** FR fail table vs outbound copy P2-TUNNEL fail table / p2-adversarial capture `fail_ids`.

### G3 — source gate-capture paths incomplete on FR header (REVISE soft)

- **FR header:** "plus gate-captures p2-adversarial.json, p2-rewrite.json" (filenames only).
- **Actual paths:** under outbound copy lane home in originating product repo (full paths redacted).
- Resolvable by convention under the cited lane, but not a full cited path in the FR.

### G4 — "dispatch STEPS" seam not present in charter docs (REVISE soft / naming)

- **FR option A:** "New skill `/paragraph-tunnel` invoked from dispatch STEPS"
- **Checked:** no `STEPS` token in `skills/charter/SKILL.md`, `EXECUTION_WIRING.md`, or `docs/`.
- Not a false claim of an existing skill, but the invocation seam name is ungrounded in current charter vocabulary (dispatch / waveset / runnable gates exist; "STEPS" does not).

### G5 — not a gap (recorded for O0)

- Option B "charter Step tunneled field" and option A skill are **proposed**; absence is expected.
- `evals/` exists; FR acceptance sketch would add *new* fixtures — parent surface is real.
- External `prose_lint` / `check_gates` exist in consumer repos and are wired in outbound copy dispatch; FR does not falsely locate them inside wavves_build.

## Lens lean

**REVISE** (grounding only).

No BLOCK: cited evidence files open in originating product repo, worked example matches captures/drafts, and proposed landing parents exist at required wavves_build HEAD.

Must fix before grounding GO: **G1** (correct evidence `repo_state_verified_against` to artifact certification pin, or relabel landing pin as evidence landing commit). Strongly preferred: **G2** explicit PN↔P2 mapping; **G3** full gate-capture paths in FR (with redaction policy for public tip).
