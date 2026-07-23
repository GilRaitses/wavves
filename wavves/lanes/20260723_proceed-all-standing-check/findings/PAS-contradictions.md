# PAS-W1b — contradictions lens

- **Artifact:** `feature-requests/20260723_proceed-all-standing.md`
- **Repo pin:** `73b09bad223ed004a2e8f10443f48196cbbbf396`
- **Hydrated:** artifact; `skills/wavves/playbooks/proceed.md`;
  `skills/wavves/SKILL.md` (proceed / pickup rows); `playbooks/pickup.md`;
  waveset Locked; sibling seams in `examples/usage.md` AUTH-10 shape
- **Lens:** internal conflicts, phase-boundary leaks, mutually exclusive
  requirements
- **Git:** none. Commits: none.

## CX-* conflicts

### CX-01 — Bare shrug locked non-widen vs Next open decide call

| | |
|---|---|
| **Claim A** | PS-05 + Triggers + Acceptance: bare `¯\_(ツ)_/¯` alone stays AUTH-10 `recommended_actions` only; do not widen bare shrug. Waveset Locked repeats this. |
| **Claim B path** | `feature-requests/20260723_proceed-all-standing.md` §Next: `/mod-decide` open calls include **bare-shrug non-widen**. |
| **Conflict** | Same requirement is both a written product lock and an undecided fork. BUILD or decide agents may reopen a non-widen the FR already states. |
| **Severity** | medium (phase-boundary leak) |
| **Lean** | REVISE — drop bare-shrug from open calls, or mark PS-05 as proposal-only until decide locks it. |

### CX-02 — Dual persistence paths (home standing file vs lane standing.md)

| | |
|---|---|
| **Claim A** | PS-02: persist Standing queue at `wavves/standing/<YYYYMMDD>_<label>.md`. |
| **Claim B path** | PS-02 same cell: "(or lane `standing.md`)". §Next lists **persistence path** as open. |
| **Conflict** | Mutually exclusive write homes with no pick, authority, or hydrate rule. Pickup / AGENTS hydrate stack has no `wavves/standing/` surface today; lane `standing.md` collides with "standing" as home-contract language. |
| **Severity** | medium (must decide before BUILD) |
| **Lean** | REVISE — one persistence authority; other path deleted or demoted to alias. |

### CX-03 — Conversation-scoped default vs mandatory disk remasure / registry breadth

| | |
|---|---|
| **Claim A** | Non-goals: default scope = **current conversation's program / named lanes**; forbid cross-lane "do everything in the registry" without operator-named scope. PS-01: queue from live surfaces, **not chat memory**. |
| **Claim B path** | Fail id `PROC-PROCEED-NO-STANDING-QUEUE` + PS-03: remasure `registry.yml` + `active_dispatch` + gates + open FRs/handoffs; optional pasted list only after disk verify. |
| **Conflict** | Scope selection is chat/program-named, inventory is disk-wide. FR never states the split ("scope from operator utterance; members only from disk inside that scope"). A literal PS-03/fail-id read can inventory all registry actives and violate the non-goal. "Current conversation's program" is itself chat memory for scope. |
| **Severity** | high |
| **Lean** | REVISE — lock scope formula (named lanes / INDEX active / explicit paste) before remasure; ban registry-wide crawl unless operator names it. |

### CX-04 — `commit_land` invent vs proceed AUTH-10 `commit` file lists

| | |
|---|---|
| **Claim A** | `playbooks/proceed.md` step 2 + `examples/usage.md`: AUTH-10 actions use `action: commit` with **listed files only**; commit/push only when this turn authorizes proceed/ship. |
| **Claim B path** | PS-02/PS-04 class `commit_land`; Evidence row ships `/set-key` as commit_land from FR/handoff inventory, not from a verdict `recommended_actions` file list. |
| **Conflict** | All-standing invents land targets from standing inventory. Existing proceed only executes commits already listed in AUTH-10. New class name (`commit_land` vs `commit`) and widened authority are unspecified relative to AGENTS gated surfaces (no commit unless operator asks). Shrug+all-standing may be read as blanket commit authorization without a file list. |
| **Severity** | high |
| **Lean** | REVISE — map `commit_land` → AUTH-10 `commit` with required `files:`; or require an operator-gated commit plan artifact before any land. |

### CX-05 — Optional leaf skill vs playbook-only proceed mode

| | |
|---|---|
| **Claim A** | Product surface + §Next: optional thin leaf / slash surface if wanted. |
| **Claim B path** | Same FR: proceed mode (`proceed-all` / standing queue); SKILL.md proceed row is already **hydrate + execute** (no leaf), matching pickup and paragraph-tunnel "no slash skill in v0" pattern. |
| **Conflict** | Two wiring shapes (router-only playbook mode vs new leaf skill) with no v0 pick. Name drift: `proceed-all` vs `proceed-all-standing`. |
| **Severity** | low–medium (acknowledged open call; still mutually exclusive INT paths) |
| **Lean** | REVISE — lock v0 playbook-only (sibling pattern) unless slash leaf is required for a named invoke. |

### CX-06 — `skip_done` / no-invent vs "queue everything open and move"

| | |
|---|---|
| **Claim A** | PS-04: `skip_done` cites PASS; never invent work for non-gating already-PASS research; fail id blocks invent past locks. |
| **Claim B path** | Problem phrasing + Originating mod feedback: inventory everything still standing and **move**; PS-03 pulls open product FRs/handoffs into the queue. Class enum has no `check` / `decide` / `handoff` class. |
| **Conflict** | Open FR/handoff items have no honest class. Agents may invent `dispatch` (premature BUILD), `commit_land` (land un-checked product), or silent skip. "Move everything open" rhetoric fights skip_done and out_of_scope restraint. |
| **Severity** | medium |
| **Lean** | REVISE — add classes or force `out_of_scope` / `operator_gate` for non-executable intake (open FR, docs handoff) unless operator expands. |

### CX-07 — `operator_gate` pause-all vs continue-movable pass

| | |
|---|---|
| **Claim A** | `playbooks/proceed.md` step 4: on `operator_gate`, surface and **pause until they respond**; ordered AUTH-10 execution. |
| **Claim B path** | Originating feedback + Problem: one pass that moves what can **and** gates what cannot (IWD-V3 surfaced while other items moved). PS-04/PS-06 allow mixed classes in one return card. |
| **Conflict** | Ordered pause-on-gate vs drain-movable-then-surface-gates. Without an explicit continue rule, BUILD can either halt the whole all-standing pass at the first gate (losing the originating behavior) or keep dispatching after a gate (violating proceed pause). |
| **Severity** | high |
| **Lean** | REVISE — lock semantics: classify full queue first, execute all non-gate moves, then surface gates without inventing unlock (or halt-on-first-gate if that is the pick). |

### CX-08 — Mode dual-bind on same playbook without phase split

| | |
|---|---|
| **Claim A** | Today proceed = execute ordered `recommended_actions` only (SKILL.md proceed row; proceed.md body). |
| **Claim B path** | FR adds mode `proceed-all-standing` into the same playbook with inventory/classify/move rules that do not require a verdict file. |
| **Conflict** | Not fatal, but step 0 "build Standing queue" and step 1 "locate source verdict" are mutually exclusive entry paths unless the playbook forks before step 1. Trigger table implies fork; playbook sketch does not spell the branch. Phase leak: acceptance asks for fixtures before decide locks CX-02/CX-03/CX-07. |
| **Severity** | medium |
| **Lean** | REVISE — explicit mode branch at playbook top; decide locks before fixture/BUILD charter. |

## Lens verdict

**REVISE** (not BLOCK, not GO).

Bare-shrug non-widen is directionally consistent across PS-05 / Triggers /
Acceptance / waveset Locked; the defect is treating it as still open (CX-01)
and several high-severity execution conflicts (CX-03, CX-04, CX-07) that would
make a faithful BUILD violate existing AUTH-10 proceed rules or the FR's own
non-goals. Persistence and leaf-skill forks (CX-02, CX-05) are named open
calls and must be decided, not left as dual requirements in the sketch.

Blocking for BUILD if unaddressed: CX-03, CX-04, CX-07.
Must-clear before or in `/mod-decide`: CX-01, CX-02, CX-05, CX-06, CX-08.

## Commit file list (findings only; no git)

- `wavves/lanes/20260723_proceed-all-standing-check/findings/PAS-contradictions.md`

## Escalation

O0 only. No operator solicit.
