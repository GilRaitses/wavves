# PTB-W1c — vocab port (corrected: no BECAUSE/EXPLAIN)

- **Wave:** PTB-W1c (corrected per PTG-NICE-BECAUSE + outbound-copy NICE-BECAUSE-ALLOWED)
- **Date:** 2026-07-15 (America/New_York)
- **Lane:** `wavves/lanes/20260715_paragraph-tunnel-build/`
- **Lock:** PTG-VOCAB with **STRIKE BECAUSE/EXPLAIN**; nice because **ALLOWED**
- **repo_state_verified_against (wavves_build):** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2`
- **Authority:** `PTG-NICE-BECAUSE.md`; outbound copy lane NICE-BECAUSE-ALLOWED decision

**PASS rule:** one sentence; one concrete place fact the recipient would
recognize; no gloss / compare / fixture-only / stand-in / research-meta /
falsefact / multi-sentence.

**Whitelist (non-negotiable):** `"nice because"` / `"because it is"` as a
profile frame is **ALLOWED**. Never emit `PN-BECAUSE`, `P2-BECAUSE`,
`PN-EXPLAIN`, or `P2-EXPLAIN`. Do not fail solely for niceness framing.

**Emit rule:** fixtures and `check_paragraph_tunnel.py` emit **PN-*** and
extension ids only (never P2-*). P2-* appears only in alias/compat notes
when reading historical outbound copy captures (map struck ids to dropped).

---

## 1. Closed fail vocabulary (product)

| fail_id | fail condition |
|---|---|
| PN-STACK | Two or more distinct claims in one paragraph |
| PN-COMPARE | Compares subject to other types or destinations |
| PN-GLOSS | Meta gloss ("personality of…", "part of how") |
| PN-FIXTURE | Fixture inventory as sole content (glass, planters, awning) |
| PN-MULTI | More than one sentence when tunnel requires one |
| STANDIN | Generic category proxy / stand-in instead of this place's fact |
| RESEARCH-META | Research-process / sender-intent meta in the tunneled profile |
| FALSEFACT | Concrete place fact wrong vs fixture ground_truth |

### Struck (never emit; never fixture-as-fail)

| struck id | note |
|---|---|
| PN-BECAUSE / P2-BECAUSE | Agent-invented; operator overturn |
| PN-EXPLAIN / P2-EXPLAIN | Agent-invented ban on niceness framing; struck |

---

## 2. Alias map: legacy P2-* → product

| legacy (outbound copy captures) | product emit |
|---|---|
| P2-STACK | PN-STACK |
| P2-COMPARE | PN-COMPARE |
| P2-GLOSS | PN-GLOSS |
| P2-FIXTURE | PN-FIXTURE |
| P2-MULTI | PN-MULTI |
| P2-BECAUSE | **DROP** (allowed framing; not a fail) |
| P2-EXPLAIN | **DROP** (struck) |

No P2-* alias for STANDIN, RESEARCH-META, FALSEFACT.

When ingesting historical outbound copy JSON, rewrite through this map and **discard**
BECAUSE/EXPLAIN before comparing to fixture expected arrays.

---

## 3. Extension ids

### STANDIN

**Fail when:** paragraph presents the subject as a generic category proxy
rather than one owner-recognizable place fact about *this* subject.

**Mechanical cues:** `stand-in`, `stand in`, `fair stand-in`, `kind of place`,
`fair example`, `looked like a` (as category proxy).

### RESEARCH-META

**Fail when:** research-process / sender-intent meta bleeds into the profile.

**Mechanical cues:** `early research`, `research phase`, `part I care about`,
`for my research`.

### FALSEFACT

**Fail when:** fixture supplies `ground_truth` / `forbidden_claims` and the
paragraph contradicts them. Without those fields, checker must not emit
FALSEFACT.

---

## 4. Outbound copy capture remapping (post-strike)

| shop | historical fail_ids | product fail_ids after strike |
|---|---|---|
| Apollo Bagels | `[]` | `[]` |
| Ardesia Wine Bar | EXPLAIN, STACK, BECAUSE, GLOSS, MULTI | **PN-STACK, PN-GLOSS, PN-MULTI** (BECAUSE/EXPLAIN dropped) |
| Scotts Flowers NYC | COMPARE, MULTI | PN-COMPARE, PN-MULTI |

**Operator mid profile (allowed nice-because):** keep patio/sidewalk
come-together with "nice because"; do not strip for tunnel. Still FAIL if
STACK/GLOSS/MULTI remain.

**Must fixture (outbound copy never fired):** PN-FIXTURE, STANDIN.

---

## 5. Exact emit strings

```
PN-STACK
PN-COMPARE
PN-GLOSS
PN-FIXTURE
PN-MULTI
STANDIN
RESEARCH-META
FALSEFACT
```

---

## 6. Port checklist for W2

| consumer | use |
|---|---|
| playbook | closed vocab §1; whitelist nice-because; no EXPLAIN/BECAUSE |
| checker | detect STACK/COMPARE/GLOSS/FIXTURE/MULTI/STANDIN/RESEARCH-META; never BECAUSE/EXPLAIN |
| fixtures | one-fact PASS; stack/gloss FAIL; compare FAIL; FIXTURE FAIL; STANDIN FAIL; optional nice-because PASS |
