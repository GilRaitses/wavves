# PAS-W1d — adversarial lens

```yaml
lens: adversarial
wave: PAS-W1d
artifact: feature-requests/20260723_proceed-all-standing.md
repo_state_verified_against: 73b09bad223ed004a2e8f10443f48196cbbbf396
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Lens verdict (this lens only)

**REVISE**

The FR names a real failure (O0 invents a standing stack from chat, then
moves or skips without a durable queue). The two proposed fail ids are the
right spine. As written, BUILD can still ship playbook prose + three soft
fixtures and leave those ids open: inventory sources re-admit chat memory,
commit_land auth is weaker than today's proceed step 2, dispatch has no
storm brake, and Acceptance does not name a mechanical detector.

O0 owns the lane verdict. This file does not grade sibling lenses.

## Proposed fail ids (map)

| id | Covers | Operable in FR as written? |
|---|---|---|
| `PROC-PROCEED-NO-STANDING-QUEUE` | all-standing runs without remasured, persisted standing inventory + class per item | Partial. Named; no detector; PS-03 chat clauses defeat it |
| `PROC-PROCEED-FORCE-BLOCKED-LOCK` | reopen/invent past hard lock instead of operator_gate artifact | Partial. Named + one fixture sketch; silent skip / out_of_scope not covered |

### Missing fail ids (needed before BUILD ACCEPT)

| id | Why |
|---|---|
| `PROC-PROCEED-SHRUG-WIDEN` | Bare shrug (or shrug + fuzzy "the rest" without explicit all-standing scope) executed as proceed-all-standing |
| `PROC-PROCEED-COMMIT-WITHOUT-AUTH` | `commit_land` runs without this-turn operator authorize for that land (or explicit AUTH-10 commit row) |
| `PROC-PROCEED-DISPATCH-STORM` | Multiple background dispatches in one pass ignoring `active_dispatch`, `conflicts_with`, or AUTH-05 |
| `PROC-PROCEED-CHAT-INVENTORY` | Standing items taken from chat/transcript without disk remasure of `source_path` |
| `PROC-PROCEED-STALE-QUEUE` | Moves executed from a persisted standing file without remasure against live registry/dispatch/gates |
| `PROC-PROCEED-SILENT-SKIP-LOCK` | Hard lock classified `skip_done` / `out_of_scope` with no gate artifact path |

`PROC-PROCEED-FORCE-BLOCKED-LOCK` should stay for active force/unlock.
`PROC-PROCEED-SILENT-SKIP-LOCK` covers the quieter twin (drop the lock from
the queue). Do not collapse them.

## Blocking failure modes

### FM-1 — Chat-memory inventory sneaks back through PS-03

**Class:** happy-path-only / loophole that recreates the bug  
**Severity:** blocking  
**Fail ids:** `PROC-PROCEED-NO-STANDING-QUEUE`, `PROC-PROCEED-CHAT-INVENTORY`

PS-01 says invent from live surfaces, not chat. PS-03 then allows:

- "open product FRs/handoffs the operator just named"
- optional pasted "what still stands" list "this turn"

Those are chat-scoped. An implementer can build the queue from the
operator's last paragraph, write a pretty `standing/*.md`, and claim Step 0
done. That is the originating failure mode with a file attached.

Non-goal "default scope = current conversation's program / named lanes"
reinforces conversation as scope without requiring named lane codes or
paths on disk.

**Concrete BUILD footgun:** Agent sees "queue all standing and move" after
a long IWD chat, invents four items from memory, writes
`wavves/standing/20260723_iwd.md`, dispatches W27, commits set-key docs.
No remasure of `registry.yml` / gate files. Fixture for
`PROC-PROCEED-NO-STANDING-QUEUE` greens if it only checks "standing file
exists."

**Required revise:** Every queue row must cite a remasured `source_path`
that exists on disk at inventory time. Operator-named items are candidates
only; unverified names become `operator_gate` ("unverified standing claim"),
never `dispatch` / `commit_land`. Lock scope to named lane codes /
`registry.yml` keys / explicit paths in the triggering turn. Ban transcript
search as an inventory source.

### FM-2 — Bare-shrug widen via fuzzy trigger "the rest"

**Class:** shrug-widen footgun / unsafe trigger default  
**Severity:** blocking  
**Fail ids:** `PROC-PROCEED-SHRUG-WIDEN` (missing), PS-05 intent

Triggers table maps `¯\_(ツ)_/¯` + "all still standing" / "the rest" to
proceed-all-standing. "the rest" is anaphoric. In a turn that also has an
AUTH-10 `recommended_actions` block, an agent can treat bare shrug plus
any residual chat topic as all-standing and widen beyond AUTH-10.

Today `proceed.md` binds shrug to recommended_actions only. FR correctly
says do not widen bare shrug, then softens the boundary with "the rest."

**Concrete BUILD footgun:** Operator: `¯\_(ツ)_/¯` after a verdict that
lists two commits. Agent also "remembers" train-busy and densify from
earlier in the thread, widens to all-standing, lands commits plus a
dispatch. Bare shrug contract broken; pax `shrug-means-proceed.mdc` and
plugin proceed diverge.

**Required revise:** Closed trigger list. Allow widen only on explicit
phrases: `all still standing`, `queue all standing and move`,
`proceed all standing`, `/wavves proceed all standing`. Drop "the rest"
or require it adjacent to "standing" / "still open" in the same utterance.
Eval fixture: bare shrug with leftover chat topics → AUTH-10 only
(`PROC-PROCEED-SHRUG-WIDEN` FAIL if widened).

### FM-3 — commit_land without per-land auth

**Class:** unsafe default / auth downgrade  
**Severity:** blocking  
**Fail ids:** `PROC-PROCEED-COMMIT-WITHOUT-AUTH` (missing)

PS-04: `commit_land` → "only when shrug/proceed authorizes." All-standing
is itself often shrug-scoped. One authorize utterance then lands every
`commit_land` row in the queue (product commits, docs bumps, multi-repo
lands) without the file-list discipline in current proceed step 2
("stage listed files only"; commit/push only when operator explicitly
asked or said proceed/ship this turn).

Originating evidence table treats `/set-key` FR → skill as `commit_land`
inside the same shrug+standing pass. That is the footgun pattern the
product would encode.

**Concrete BUILD footgun:** Standing queue has three `commit_land` rows
across wavves_build + foreign handoff notes. Operator says
`queue all standing and move`. Agent commits all three, pushes main
(homepage publish surface per `wavves/AGENTS.md`), no per-row file list
and no second confirm. Gated surface mutated under a queue expand.

**Required revise:** `commit_land` requires either (a) an AUTH-10-style
row with explicit file list already operator-approved this turn, or
(b) surface as `operator_gate` until the operator says ship/proceed for
that id. All-standing authorize ≠ blanket git write. Return card must
show `auth: explicit|blocked` per commit row. Fixture:
all-standing with commit candidates → gates, not silent land
(`PROC-PROCEED-COMMIT-WITHOUT-AUTH`).

### FM-4 — Dispatch storm / concurrent lane smash

**Class:** works on happy path only (single open wave)  
**Severity:** blocking  
**Fail ids:** `PROC-PROCEED-DISPATCH-STORM` (missing)

PS-04: every `dispatch` → background only; do not poll. No rule for:

- registry `active_dispatch` already non-null
- `conflicts_with` between lanes
- git concurrency ("Never land commits on a branch a dispatched agent is
  actively editing" — `wavves/AGENTS.md`)
- AUTH-05 waveset sync (present in bare proceed, absent from FR move rules)
- N dispatches in one pass without order / batch cap

**Concrete BUILD footgun:** Inventory marks five open waves `dispatch`.
Agent fires five background orchestrators. Two share a findings tree or
repo branch. Returns poison each other; O0 reconciles fiction.

**Required revise:** Before each dispatch: remasure `active_dispatch`,
conflicts, AUTH-05 if mod-decide lane. Cap or serialize when >1 movable
dispatch; extras stay queued with reason. Fixture: lane with
`active_dispatch: dispatch.md` already set → must not re-dispatch
(`PROC-PROCEED-DISPATCH-STORM`).

### FM-5 — Silent skip of hard locks (twin of FORCE-BLOCKED-LOCK)

**Class:** silent skip / invent past gate  
**Severity:** blocking  
**Fail ids:** `PROC-PROCEED-FORCE-BLOCKED-LOCK`,
`PROC-PROCEED-SILENT-SKIP-LOCK` (missing)

FR Acceptance: "blocked lock → operator_gate, not dispatch." Good for the
force path. Missing:

- classify lock as `skip_done` because "we'll get ridership later"
- classify as `out_of_scope` to clear the return card
- "named `*_OPERATOR_GATE.md` / lock ABSENT honesty" — ABSENT is ambiguous:
  absent file can mean "no gate, movable" or "gate not written yet, must
  create gate." BUILD will pick the movable reading.
- no requirement that `operator_gate` rows write a durable gate path before
  the pass reports complete

**Concrete BUILD footgun:** IWD-V3-class lock present in charter prose but
gate file missing. Agent sets `out_of_scope` or invents a densify dispatch
"because key is set." Return card looks clean. Ridership lock never
surfaces.

**Required revise:** Closed rule: known hard-lock classes (spend, ToS,
ridership/train-busy, API key absent when wave needs it) →
`operator_gate` with written artifact path, or FAIL the pass. ABSENT gate
file for a named lock id → create/surface gate, never treat as movable.
Fixtures: force-unlock attempt →
`PROC-PROCEED-FORCE-BLOCKED-LOCK`; drop/skip without gate path →
`PROC-PROCEED-SILENT-SKIP-LOCK`.

### FM-6 — Acceptance gates cannot actually run

**Class:** gate that can't run / process-PASS  
**Severity:** blocking  

Acceptance asks for playbook docs + standing file written + three
eval/fixture behaviors + README row + mod-check GO. No named harness:

- no `evals/check_proceed_standing.py` (or equivalent) analogous to
  `check_paragraph_tunnel.py` / `check_proof_before_accept.py`
- if fixtures land under `evals/run_fixtures.py`, PASS only means lens
  keywords survive (evals/README known limitation)
- no schema check that standing queue rows have remasured `source_path`
- no check that bare-shrug path still binds to AUTH-10 only

**Concrete BUILD footgun:** Three markdown fixtures under
`evals/fixtures/` with expected keywords in mod-check lens table. BUILD
ACCEPT greens. Live agent still invents inventory from chat.

**Required revise:** Mechanical checker over fixture standing queues +
synthetic proceed traces. Minimum emit:
`PROC-PROCEED-NO-STANDING-QUEUE`,
`PROC-PROCEED-FORCE-BLOCKED-LOCK`,
`PROC-PROCEED-SHRUG-WIDEN`,
`PROC-PROCEED-CHAT-INVENTORY`. Review-only ids labeled as such. BUILD
ACCEPT requires checker PASS, not docs-only.

### FM-7 — Standing-queue poison / stale file as authority

**Class:** unsafe persistence default  
**Severity:** blocking  
**Fail ids:** `PROC-PROCEED-STALE-QUEUE` (missing),
`PROC-PROCEED-NO-STANDING-QUEUE`

PS-02: persist under `wavves/standing/<date>_<label>.md` or lane
`standing.md`. No rule for:

- freshness (written when? remasured when?)
- which file wins if both paths exist
- moves using yesterday's standing file after registry changed
- agent editing the standing file to reclassify a lock as `skip_done`
  mid-pass

Today `wavves/standing/` does not exist (glob zero). Persistence is greenfield;
wrong defaults become doctrine.

**Concrete BUILD footgun:** Morning pass writes standing queue. Afternoon
operator says proceed all standing. Agent reuses morning file; a completed
wave is re-dispatched; a new gate is missing from the file; lock row was
hand-edited to `out_of_scope`.

**Required revise:** Standing file is a snapshot with
`remasured_at` + `repo_state_verified_against`. Move phase must remasure
each row against live sources or refuse with
`PROC-PROCEED-STALE-QUEUE`. Single canonical path (pick one in mod-decide;
drop the or-clause). Standing file is append/audit evidence, not a writable
authority that overrides disk.

## Non-blocking failure modes

### FM-8 — Return card without hard stop on mixed results

**Severity:** non-blocking  

PS-06 return card is a table. No rule that any `operator_gate` row fails
the pass or blocks later `commit_land` in the same turn. Agent can dispatch
movable work and bury gates below the fold.

**Revise ask:** Ordered execution: surface all gates before any
`commit_land`; optional dispatch of clearly unlocked waves may proceed,
but the pass status is `partial` when any gate remains.

### FM-9 — `skip_done` cite can be fake PASS

**Severity:** non-blocking  

PS-04: `skip_done` → one-line cite of PASS artifact. No remasure that the
cited file exists and contains PASS. Agent can cite a planned filename.

**Revise ask:** `skip_done` requires existing path + verbatim PASS/status
line, else reclassify.

### FM-10 — Cross-repo / foreign evidence as BUILD dependency

**Severity:** non-blocking (dispatch says foreign pins are illustration)  

Originating table cites pax/klosr paths and IWD gate filenames. If BUILD
hard-codes those paths into playbook examples as required inventory
sources, consumer repos without pax break or invent.

**Revise ask:** Examples stay illustrative; inventory source list is
repo-local (`registry.yml`, lane homes, `feature-requests/`, handoffs under
`wavves/handoffs/`).

### FM-11 — Router / SKILL.md / pickup seam unspecified

**Severity:** non-blocking  

`skills/wavves/SKILL.md` route row for proceed is still
"execute verdict actions." pickup.md inventories active lanes but is not
named as a subroutine. BUILD may only patch `proceed.md` and leave
routing/trigger ambiguity.

**Revise ask:** Explicit patch list: `proceed.md` mode section,
`SKILL.md` route triggers, optional pointer from pickup ("report standing;
do not move unless proceed-all-standing").

### FM-12 — Optional leaf skill doubles surface without auth clarity

**Severity:** non-blocking  

FR allows "optional leaf skill or proceed mode." A slash leaf that
defaults to move-all increases discoverability of the storm/commit
footguns.

**Revise ask:** v0 = proceed playbook mode only (same pattern as
paragraph-tunnel / proof-before-accept). Slash leaf deferred.

## What would change REVISE → GO (this lens)

1. Close PS-03 chat loopholes; every row remasured `source_path` or gate.
2. Closed triggers; fixture for `PROC-PROCEED-SHRUG-WIDEN`.
3. `commit_land` auth equal or stricter than proceed step 2; missing id
   `PROC-PROCEED-COMMIT-WITHOUT-AUTH`.
4. Dispatch preflight: active_dispatch, conflicts, AUTH-05; missing id
   `PROC-PROCEED-DISPATCH-STORM`.
5. Lock handling: force and silent-skip both covered; ABSENT means write
   gate, not movable.
6. Mechanical eval harness with operable fail ids (not lens-keyword
   tripwire alone).
7. Single standing persistence path + stale remasure rule
   (`PROC-PROCEED-STALE-QUEUE`).

## Out of scope for this lens

- Grounding of foreign pax/klosr pins (W1a)
- Internal FR contradictions (W1b)
- Completeness inventory (W1c)
- Implementation plan or code

## Commit file list (orchestrator only)

- `wavves/lanes/20260723_proceed-all-standing-check/findings/PAS-adversarial.md` (this file)

No git. Escalation to O0 only.
