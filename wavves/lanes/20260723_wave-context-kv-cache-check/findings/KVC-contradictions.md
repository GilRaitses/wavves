# KVC-W1b — contradictions lens

```yaml
lens: contradictions
wave_id: KVC-W1b
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260723_wave-context-kv-cache.md
tip: de75b4c4118c78dcc0164fdaa916bbc53f99225f
verdict_lean: REVISE
escalation: O0 only
git: none performed
```

## Hydrated (this lens)

- artifact FR (KV-01..06, fail ids, open calls, non-goals, locked analogy sentence)
- `waveset.md`, `dispatch-w1.md`
- WOF FR leave-acts / resume contract (`feature-requests/20260723_wave-orchestrator-fanout.md`)
- PAS FR stale/remasure (`feature-requests/20260723_proceed-all-standing.md`)
- `skills/mod-rotate/SKILL.md`; `skills/wavves-init/SKILL.md` §4–5
- RTH synthesis (illustration): `lanes/20260723_mod-rotate-theory-research/findings/RTH-SYNTHESIS.md`
- INDEX remasure: `current_rotation: none`, `current_identity: O0`

O0 owns the lane verdict. This file does not grade sibling lenses.

## Verdict lean (this lens)

**REVISE.** The three cache homes (checkpoint, standing file, rotations) are
directionally consistent with the locked analogy sentence. BUILD cannot pick
faithfully while alias fail-ids collide with WOF/PAS ids, CACHE-NAME still
allows stripping KV from visitor copy, WOF-BIND ignores WOF already SHIPPED,
and KV-03 locks "from template" while ROTATION-TEMPLATE stays open. Not BLOCK:
conflicts are decide/revise edits, not a product-scope collapse.

## Contradiction table

### CX-KVC-01 — Alias/bind fail ids vs "closed" duplicate vocabulary

| | |
|---|---|
| **Claim A** | Fail ids "closed for BUILD": `PROC-KV-YIELD-NO-CACHE` alias/bind to WOF `PROC-ORCH-NO-RESUME-CONTRACT`; `PROC-KV-STANDING-STALE` bind PAS stale (`PROC-PROCEED-STALE-QUEUE`). KV-01: missing checkpoint → FAIL id already in WOF. |
| **Claim B** | Same table + KV-05: CTX-KV evals emit/check `PROC-KV-*` fixtures; WOF/PAS keep their own fail ids and checkers. |
| **Evidence** | artifact §Fail ids; §KV-01; §KV-05; WOF fail table + leave-acts bind; PAS `PROC-PROCEED-STALE-QUEUE` |
| **Conflict** | Alias without emit precedence = two ids for one condition. Checkers may double-FAIL, disagree on which string is mechanical, or silently drop one id. "Closed for BUILD" pretends the collision is settled. |
| **Severity** | high |
| **Lean** | REVISE — lock emit rule: WOF/PAS id only (KV prose alias), or KV id supersedes with explicit bind map; no dual mechanical emit. |

### CX-KVC-02 — CACHE-NAME open call vs locked KV vocabulary

| | |
|---|---|
| **Claim A** | Open call **CACHE-NAME** includes checkpoint-only (no KV in visitor copy). |
| **Claim B** | Title "Wave/context KV cache"; locked analogy sentence (K/V vs Q); KV-04 allows **context cache** / **KV-cache analogy** and requires "analogy"; Acceptance #4 requires analogy label when visitor text names "KV cache." |
| **Evidence** | artifact title; Problem locked sentence; §KV-04; §Acceptance 4; §Open calls #1 |
| **Conflict** | checkpoint-only visitor copy is mutually exclusive with title + locked sentence + KV-04. Naming is treated as undecided while product text already commits to KV analogy language. |
| **Severity** | high |
| **Lean** | REVISE — drop checkpoint-only option, or rewrite title/locked sentence/KV-04 before decide. |

### CX-KVC-03 — WOF-BIND vs "No BUILD from this folder alone" + WOF SHIPPED

| | |
|---|---|
| **Claim A** | Open call **WOF-BIND**: land as part of WOF BUILD vs separate CTX-KV BUILD after WOF. |
| **Claim B** | Next: `/charter` BUILD after WOF/PAS land remasured; "No BUILD from this folder alone." Non-goals: does not auto-BUILD WOF/PAS. WOF FR **Status: SHIPPED**. |
| **Evidence** | artifact §Open calls #2; §Next; §Non-goals; WOF FR status line |
| **Conflict** | "Part of WOF BUILD" is a dead fork once WOF is SHIPPED unless WOF is reopened. Separate BUILD after WOF is the only live path, but the open call still presents a mutually exclusive pair. Phase leak: decide call ignores land status. |
| **Severity** | high |
| **Lean** | REVISE — close WOF-BIND to separate CTX-KV after WOF (remeasure), or explicitly reopen WOF. |

### CX-KVC-04 — KV-01 tip-hash schema vs WOF locked resume contract

| | |
|---|---|
| **Claim A** | KV-01 checkpoint schema: charge table, pending worker ids, next integrate step, **tip hash**. |
| **Claim B** | WOF Resume contract (v0 lock) + leave-acts: same three fields, **no tip hash**. WOF SHIPPED; Problem §1 still frames WOF yield-without-checkpoint as an open recompute surface. |
| **Evidence** | artifact §KV-01, §Problem #1; WOF §Resume contract, §Leave-acts, Status SHIPPED |
| **Conflict** | Alias to WOF fail id while expanding schema past WOF lock. Problem text understates WOF land; BUILD may patch charter twice or invent tip-hash without WOF reopen. |
| **Severity** | medium |
| **Lean** | REVISE — mark tip hash as additive WOF patch (reopen/bind) or drop it from KV-01; remasure Problem #1 against SHIPPED WOF. |

### CX-KVC-05 — KV-02 / PROC-KV-STANDING-STALE vs PAS not landed

| | |
|---|---|
| **Claim A** | KV-02: standing file is program cache; remasure = invalidate+rewrite; stale → `PROC-PROCEED-STALE-QUEUE` / `PROC-KV-STANDING-STALE` bind. Fail ids closed for BUILD. |
| **Claim B** | PAS FR Status: revised-after-PAS, awaiting `/charter` BUILD. Next on KV FR: BUILD only after PAS land remasured. |
| **Evidence** | artifact §KV-02, §Fail ids, §Next; PAS FR status + `PROC-PROCEED-STALE-QUEUE` |
| **Conflict** | Closing a bind id before the bound surface ships. Separate CTX-KV BUILD cannot honestly claim PAS-stale coverage until PAS lands, yet fail table reads as ready. |
| **Severity** | medium |
| **Lean** | REVISE — keep bind as decide note; do not call PAS-bound ids "closed for BUILD" until PAS land remasured. |

### CX-KVC-06 — KV-03 "from template" vs ROTATION-TEMPLATE open + mod-rotate newest-file

| | |
|---|---|
| **Claim A** | KV-03: if `rotations/` empty, rotation skill writes r01 **from template** (not chat). Acceptance #3: bootstrap/first-rotation fence named. |
| **Claim B** | Open call **ROTATION-TEMPLATE**: ship `wavves/rotations/_template.md` vs **only skill prose** for first write. mod-rotate: "Follow the section shape of the newest existing file in `rotations/`" (no empty-dir branch). |
| **Evidence** | artifact §KV-03, §Acceptance 3, §Open calls #3; `skills/mod-rotate/SKILL.md`; RTH-SYNTHESIS FIRST-ROTATION open call |
| **Conflict** | Template file vs skill-only prose are mutually exclusive. KV-03 prose already picks "from template" while the open call leaves it undecided. Live mod-rotate has no empty-`rotations/` write path. |
| **Severity** | high |
| **Lean** | REVISE — decide ROTATION-TEMPLATE first; demote KV-03 template wording to proposal until locked. |

### CX-KVC-07 — Empty-rotations fact vs KV-03 bootstrap match rule

| | |
|---|---|
| **Claim A** | KV-03: INDEX `current_rotation` + `current_identity` must match newest rotation **or explicit bootstrap**. `PROC-KV-ROTATION-EMPTY-CLAIM` fails hydrate/continuity claim while `current_rotation: none` and `rotations/` empty. |
| **Claim B** | RTH-SYNTHESIS remasure (illustration) + live INDEX: `rotations/` empty, `current_rotation: none`, `current_identity: O0` (bare) vs AGENTS/step-log `O0.R1` bootstrap with no rotation file. wavves-init §4: bootstrap assigns `O0.R1` via setup act + step-log, not via rotation file. |
| **Evidence** | artifact §KV-03, §Fail ids; RTH-SYNTHESIS facts table; `wavves/INDEX.md`; wavves-init §4–5 |
| **Conflict** | "Explicit bootstrap" is unnamed relative to step-log-only `O0.R1` and INDEX bare `O0`. Same empty-dir state is both the motivating bug and a FAIL under the new id, without a legal bootstrap exception text. |
| **Severity** | medium |
| **Lean** | REVISE — define bootstrap exception (INDEX/AGENTS/step-log) vs require first rotation write; align identity string. |

### CX-KVC-08 — Analogy fences vs visitor-copy / Raft isomorphism scope

| | |
|---|---|
| **Claim A** | Non-goals + KV-04 + `PROC-KV-ISOMORPHISM-CLAIM`: analogy only; ban transformer KV **or Raft** isomorphism for this seam. Acceptance #4: analogy label on visitor "KV cache" sentences. |
| **Claim B** | Locked analogy sentence speaks in K/V and Q. Title and product surface name KV cache. KV-03 targets mod-rotate/init; wavves-init §4 names Raft/StatefulSet/Erlang borrows without "analogy" on the Raft bullet. |
| **Evidence** | artifact Inspiration, locked sentence, §KV-04, §Fail ids, §Acceptance 4, §KV-03; wavves-init §4; RTH-SYNTHESIS analogy/ban notes |
| **Conflict** | Visitor copy can read the locked sentence or title as implementation. Raft ban on "this seam" collides with init §4 language KV-03 would touch, without saying whether CTX-KV BUILD must fence Raft or leave that to a separate propose path. |
| **Severity** | medium |
| **Lean** | REVISE — require "analogy" in the locked sentence itself; scope isomorphism fail to KV/transformer only, or name init §4 fence as in-scope patch. |

### CX-KVC-09 — Status / closed-for-BUILD language vs open calls + Next

| | |
|---|---|
| **Claim A** | Status `ready-for-mod-check`. Fail ids "closed for BUILD." Acceptance sketch treats checkpoint, remasure, bootstrap fence, analogy label as named. |
| **Claim B** | Open calls CACHE-NAME, WOF-BIND, ROTATION-TEMPLATE still undecided. Next: mod-check → mod-decide → charter BUILD; no BUILD from this folder alone. |
| **Evidence** | artifact Status, §Fail ids, §Acceptance, §Open calls, §Next |
| **Conflict** | Phase-boundary leak: "closed for BUILD" and Acceptance-ready wording run ahead of decide locks. Status for mod-check is fine; closed-fail-id language is not. |
| **Severity** | medium |
| **Lean** | REVISE — mark fail ids / Acceptance items that depend on open calls as sketch-until-decide. |

### CX-KVC-10 — `PROC-KV-RESUME-NO-CACHE` vs WOF NO-RESUME scope

| | |
|---|---|
| **Claim A** | New id `PROC-KV-RESUME-NO-CACHE`: resume integrate without readable checkpoint or rollup. |
| **Claim B** | WOF `PROC-ORCH-NO-RESUME-CONTRACT`: yield or session end with no durable checkpoint and no rollup; resume binds to checkpoint path (fail remediation). |
| **Evidence** | artifact §Fail ids; WOF §Fail ids, §Resume contract, O0 resume etiquette |
| **Conflict** | Overlap without bind/alias note (unlike YIELD-NO-CACHE). BUILD may invent a second resume fail or leave emit undefined. |
| **Severity** | low–medium |
| **Lean** | REVISE — alias to WOF with distinct trigger note, or keep as KV-only with non-overlap predicate. |

## Named gaps requiring revise

1. **Emit precedence** for aliased fail ids (CX-KVC-01, CX-KVC-10).
2. **CACHE-NAME** closed against title + locked sentence + KV-04 (CX-KVC-02).
3. **WOF-BIND** closed given WOF SHIPPED (CX-KVC-03).
4. **Tip hash** additive vs drop relative to WOF resume lock (CX-KVC-04).
5. **ROTATION-TEMPLATE** before KV-03 "from template" lock (CX-KVC-06).
6. **Explicit bootstrap** definition for empty `rotations/` + INDEX identity (CX-KVC-07).
7. Downgrade "Fail ids closed for BUILD" until binds and open calls settle (CX-KVC-05, CX-KVC-09).

## Lens verdict

**REVISE** (not BLOCK, not GO).

Blocking for BUILD if unaddressed: CX-KVC-01, CX-KVC-02, CX-KVC-03, CX-KVC-06.
Must-clear in `/mod-decide` or FR revise: CX-KVC-04, CX-KVC-05, CX-KVC-07,
CX-KVC-08, CX-KVC-09, CX-KVC-10.

## Git

No git. No commits. No skill edits. No BUILD.
Commit file list for O0 only (if later asked):

- `wavves/lanes/20260723_wave-context-kv-cache-check/findings/KVC-contradictions.md`
- `wavves/lanes/20260723_wave-context-kv-cache-check/findings/KVC-W1b-return.md`
