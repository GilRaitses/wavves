# Purpose gates

Purpose gates are pass-or-fail checks for wavves public copy (landing page,
README lead, outbound articles). They judge whether prose states the product
point, not whether mechanics lint clean. Run `prose-gates/check_gates.py` for
mechanical style; run this list for fidelity.

Surfaces in scope:

- `index.html` hero and above-the-fold copy
- `README.md` opening paragraphs
- Published aimez articles and whitepaper excerpts that describe wavves

## Hard fail

| ID | Rule | Why |
|---|---|---|
| PG1 | Lead with capture and durable alignment, not release-note mechanics | AUTH sync, `dispatch-w{N}.md`, scoped verdicts and `/wavves proceed` support the story; they do not headline it |
| PG2 | Synthesize causally; no stacked one-fact-per-sentence propositions | Each sentence must earn the next through cause, consequence or answer |
| PG3 | Do not open with adopted ontology | Do not presuppose fleet taxonomy, moderator-layer vocabulary or architecture the reader has not yet felt as a problem |
| PG4 | Do not open with inventory list buildup | Do not enumerate scope fields before the reader knows why the list matters |
| PG5 | Every sentence at least 15 words | Short leads read as fragments on marketing surfaces |
| PG6 | No Oxford commas | House style; see prose gate **OXFORD** and approved remedies (`docs/purpose-gates.md` § Remedies) |
| PG7 | No `no longer` | Banned negation-adjacent hedge; state where things are or what fails, affirmatively |
| PG8 | No `rather than` or `instead of` | Same affirmative rule as prose gate G1 on these surfaces |

## Review (human)

| ID | Rule | Why |
|---|---|---|
| PG9 | Alignment packet before runners deploy | Capture precedes dispatch |
| PG10 | Successor hydrates from `wavves/` files | Files carry the record; chat does not |
| PG11 | Runnable check evidence on disk | Acceptance is measured, not asserted in chat |

## Usage

Read the surface aloud. Hard-fail any row that triggers. For landing hero
edits, check PG1 through PG8 before push.

Automated substring check for PG7, PG8 and PG6 (OXFORD) on hero copy:

```bash
rg -n 'no longer|rather than|instead of' index.html README.md
python3 ~/prose-gates/check_gates.py index.html
```

Zero matches required on hero for PG7/PG8. OXFORD must be 0 hard-fail on hero.

## Remedies

Serial comma fixes that pass OXFORD and purpose gates:

| Violation | Fix |
|---|---|
| `, X, and Y` in a list | `, X and Y` |
| `, and` between clauses | `, while` when the second clause is subordinate |
| `, and` between clauses | Split into two sentences |

A comma before `while` is allowed. A comma before `and` between clauses is not.
