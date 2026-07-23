# MDA-W1d — adversarial lens

```yaml
lens: adversarial
wave: MDA-W1d
artifact: feature-requests/20260722_mod-decide-decision-alignment.md
repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Lens verdict (this lens only)

**REVISE**

The FR names a real failure (hygiene-safe Hold leans with no exit;
option grain hides successor BUILD). The two proposed fail ids are the
right spine. As written, BUILD can still ship template prose + soft
fixtures and leave those ids open: exit_criteria can be circular,
program_tag can be theater without disk cites, grain invent can smuggle
BUILD past a check that never opened that fork, and Acceptance has no
mechanical detector.

O0 owns the lane verdict. This file does not grade sibling lenses.

## Proposed fail ids (map)

| id | Covers | Operable in FR as written? |
|---|---|---|
| `PROC-DECIDE-HOLD-NO-EXIT` | recommend/lean Hold/ban/pause without named exit criteria | Partial. Named; no detector; "named condition" unbounded |
| `PROC-DECIDE-GRAIN-MISMATCH` | option set at wrong grain vs standing intent, no callout | Partial. Named; Midtown-specific fixture sketch; no checker |

### Missing fail ids (needed before BUILD ACCEPT)

| id | Why |
|---|---|
| `PROC-DECIDE-EXIT-CIRCULAR` | exit_criteria is "until next decide" / "until operator feels ready" / "more hygiene" with no artifact/wave |
| `PROC-DECIDE-ALIGN-THEATER` | program_tag or program_intent without verbatim disk cite (waveset/decision/charter path) |
| `PROC-DECIDE-GRAIN-SMUGGLE` | coverage-BUILD option invented that conflicts with check BLOCK/REVISE or absent operator intent cite |
| `PROC-DECIDE-HYGIENE-REOPEN` | after check/wire PASS in Grounding, decide re-walks hygiene as a product fork (DA-06 breach) |
| `PROC-DECIDE-LEAN-OVERRIDE` | lean/auto-prefer aligns locks a pick without operator wait |

Keep HOLD-NO-EXIT for missing exit. EXIT-CIRCULAR covers fake exits.
Keep GRAIN-MISMATCH for omitted BUILD path. GRAIN-SMUGGLE covers illegal
invent. Do not collapse them.

## Blocking failure modes

### FM-1 — Circular or hygiene-shaped exit_criteria

**Class:** happy-path-only / loophole that recreates the bug  
**Severity:** blocking  
**Fail ids:** `PROC-DECIDE-HOLD-NO-EXIT`, `PROC-DECIDE-EXIT-CIRCULAR` (missing)

DA-01 requires an exit line. It does not require the exit to be a concrete
artifact, wave id, or remasureable PASS. An implementer can lean Hold with
`exit_criteria: more hygiene / re-check later` and claim DA-01 satisfied.
That is the indefinite-hold loop with a filled template.

**Concrete BUILD footgun:** Post-wire admit decide leans B Hold;
`unlocks_next: another decide`; `exit_criteria: until hygiene clears`.
Fixture for HOLD-NO-EXIT greens if it only checks the key is non-empty.

**Required revise:** exit_criteria must name an existing or charterable
artifact/wave/path (or `none — permanent park`). Ban exits that only point
at another decide turn or unspecified hygiene. Fixture: Hold +
"until next decide" → `PROC-DECIDE-EXIT-CIRCULAR`.

### FM-2 — Program alignment theater

**Class:** process-PASS / ungrounded tags  
**Severity:** blocking  
**Fail ids:** `PROC-DECIDE-ALIGN-THEATER` (missing)

DA-02 asks for 2–4 bullets "from waveset/charter/prior locks (verbatim
cites)" then per-option tags. No rule that cites remasure on disk this
turn. Agent can invent "standing intent: ship coverage" from chat and tag
Hold as `defers`.

**Concrete BUILD footgun:** Decide session with empty waveset Locked.
Agent writes program_intent from transcript, tags coverage BUILD
`aligns`, leans it, charters BUILD. Originating misalignment inverted:
alignment language launders chat memory.

**Required revise:** Each intent bullet cites `path` + verbatim quote
present on disk (or operator paste block with explicit "operator-supplied
intent" label). Missing cites → `program_intent: unset`; ban `aligns`
tags; lean Hold only as `defers` with exit. Fixture:
unset intent + aligns tag → `PROC-DECIDE-ALIGN-THEATER`.

### FM-3 — Grain invent smuggles BUILD past check

**Class:** unsafe default / authority bypass  
**Severity:** blocking  
**Fail ids:** `PROC-DECIDE-GRAIN-MISMATCH`, `PROC-DECIDE-GRAIN-SMUGGLE` (missing)

DA-03 forces a coverage-BUILD pick when operator intent names successor
coverage. Live mod-decide forbids inventing forks the check did not
surface. Combined with a check REVISE/BLOCK that left BUILD closed, grain
invent can present and lean a BUILD path the check never unlocked.

**Concrete BUILD footgun:** Check returns REVISE on coverage claims; open
calls are hold vs eval-only. Decide grain-adds "coverage BUILD first,"
leans it, emits Locked paste, O0 charters BUILD. Check verdict bypassed.

**Required revise:** Grain-added picks require (a) verbatim intent cite on
disk and (b) check verdict not BLOCK on that scope, or explicit operator
override this turn. Else surface grain mismatch as callout without
adding a BUILD letter. Fixture: BLOCK check + invented BUILD pick →
`PROC-DECIDE-GRAIN-SMUGGLE`.

### FM-4 — Hygiene re-open after PASS (anti-loop hollow)

**Class:** recreates originating loop  
**Severity:** blocking  
**Fail ids:** `PROC-DECIDE-HYGIENE-REOPEN` (missing), DA-06 intent

DA-06 says after check/wire PASS, admit/build-scope decide must not
re-open hygiene. No fail id, no fixture, no rule when the check return
still lists a hygiene call.

**Concrete BUILD footgun:** TRAIN-WIRE-class PASS in Grounding; check
still names "confirm freeze." Decide walks freeze again, leans Hold
pending freeze, loop continues.

**Required revise:** If Grounding cites PASS for the hygiene artifact,
hygiene open calls are parked with cite, not presented as product
options. Fixture: Grounding PASS + hygiene option presented →
`PROC-DECIDE-HYGIENE-REOPEN`.

### FM-5 — Acceptance gates cannot actually run

**Class:** gate that can't run / process-PASS  
**Severity:** blocking  

FR has no Acceptance section. DA-07 sketches two fixtures only. No named
harness:

- no `evals/check_mod_decide_alignment.py` (or equivalent)
- if cases land under `run_fixtures.py`, PASS only means keywords survive
  (`evals/README.md` known limitation)
- no check that exit_criteria is non-circular
- no check that program_intent cites exist

**Concrete BUILD footgun:** Two markdown fixtures under `evals/fixtures/`
with expected fail-id strings. BUILD ACCEPT greens. Live decide still
leans Hold with `exit_criteria: later`.

**Required revise:** Mechanical checker over synthetic decide transcripts
(or structured option blocks). Minimum emit:
`PROC-DECIDE-HOLD-NO-EXIT`,
`PROC-DECIDE-GRAIN-MISMATCH`,
`PROC-DECIDE-EXIT-CIRCULAR`,
`PROC-DECIDE-ALIGN-THEATER`. BUILD ACCEPT requires checker PASS, not
docs-only.

### FM-6 — Prefer-aligns becomes silent auto-lock

**Class:** unsafe default  
**Severity:** blocking  
**Fail ids:** `PROC-DECIDE-LEAN-OVERRIDE` (missing)

DA-04 "prefer options that aligns" plus one-at-a-time wait can be
implemented as: present only the aligns option, or record pick without
wait when lean is clear. That removes the operator gate the skill exists
to enforce.

**Concrete BUILD footgun:** Agent writes decisions/IWD-D*-style file with
Pick: B from lean, no operator utterance this turn, proceeds to AUTH sync
and recommended charter.

**Required revise:** Prefer = lean sentence only. Pick requires operator
letter this turn. Fixture: lean without operator pick → must not write
decision record (`PROC-DECIDE-LEAN-OVERRIDE`).

## Non-blocking failure modes

### FM-7 — IWD/Midtown nouns hard-coded into skill

**Severity:** non-blocking  

Risks warn against over-fit; DA-03/DA-07 still use Midtown N / island
coverage as normative examples. BUILD may paste those nouns into
`SKILL.md` as required grain labels.

**Revise ask:** Skill uses generic labels only; examples/usage may show
one synthetic coverage-vs-fixtures vignette without pax paths.

### FM-8 — Option D alignment card doubles surface without schema

**Severity:** non-blocking  

D adds an operator-facing card in Locked paste while DA-02/DA-05 already
add stanza + fields. Extra surface increases drift (card says aligns;
tags say defers).

**Revise ask:** v0 = DA-02 stanza + DA-05 fields inside one Locked paste
block; no second card format.

### FM-9 — Ban lean only; Hold-no-exit still presented

**Severity:** non-blocking (if CX-02 fixed)  

DA-01 bans lean; options may still list Hold with blank exit. Operator
picks A; loop continues without a lean.

**Revise ask:** Validate option block before present; Hold/ban/pause
without exit cannot appear.

### FM-10 — Foreign evidence as BUILD dependency

**Severity:** non-blocking (dispatch: illustration)  

If BUILD hard-codes pax IWD paths into fixtures or skill examples as
required remasure, consumer clones break.

**Revise ask:** Fixtures synthetic; Originating evidence stays FR-only.

## What would change REVISE → GO (this lens)

1. Concrete exit rule (artifact/wave or permanent park); id
   `PROC-DECIDE-EXIT-CIRCULAR`.
2. Disk-cited program_intent; id `PROC-DECIDE-ALIGN-THEATER`.
3. Grain invent bounds vs check verdict; id `PROC-DECIDE-GRAIN-SMUGGLE`.
4. Hygiene park after PASS; id `PROC-DECIDE-HYGIENE-REOPEN`.
5. Mechanical eval harness with operable fail ids.
6. Prefer = lean only; id `PROC-DECIDE-LEAN-OVERRIDE`.
7. Acceptance section that requires checker PASS.

## Out of scope for this lens

- Grounding of foreign pax pins (W1a)
- Internal FR contradictions (W1b)
- Completeness inventory (W1c)
- Implementation plan or code
- Verdict file (O0)

## Commit file list (orchestrator only)

- `wavves/lanes/20260722_mod-decide-alignment-check/findings/MDA-adversarial.md` (this file)

No git. Escalation to O0 only.
