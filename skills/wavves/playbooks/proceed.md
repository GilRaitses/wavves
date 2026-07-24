# Proceed playbook

Route: **wavves** (`/wavves proceed`)

## Mode fork (run first)

Pick **exactly one** mode from the triggering utterance. Do not mix paths.

| mode | when |
|:-----|:-----|
| **AUTH-10 proceed** | Bare `/wavves proceed`, `proceed as recommended`, `ship it`, bare `¯\_(ツ)_/¯`, or bare `/shrug` after a verdict / reconcile with `recommended_actions`. |
| **proceed-all-standing** | Same utterance contains an explicit all-standing phrase (closed list below). May combine with shrug / `/shrug` / `/wavves proceed`. |

**Widen lock:** Bare shrug and bare `/shrug` never widen to all-standing
(`PROC-PROCEED-SHRUG-WIDEN`). Fuzzy phrases such as "the rest" do not widen.

### Closed all-standing triggers (PS-06)

Widen **only** when the same utterance contains one of:

- `all still standing`
- `queue all standing and move`
- `proceed all standing`
- `/wavves proceed all standing`
- `/shrug` + one of the phrases above
- emoji shrug (`¯\_(ツ)_/¯`) + one of the phrases above

---

## AUTH-10 proceed (recommended_actions)

Execute the ordered **recommended_actions** block from a mod-check verdict,
mod-decide completion, or lane reconcile return (AUTH-10).

```
- [ ] 1. Locate the source verdict or reconcile file. Read `recommended_actions`
        in order. If absent, infer from verdict prose and stop if ambiguous.
- [ ] 2. For each `commit` action: stage listed files only (`files:` required).
        Commit and push only when the operator explicitly asked or said
        "proceed as recommended" / "ship it" in this turn
        (`PROC-PROCEED-COMMIT-WITHOUT-AUTH` if land without authorize + files:).
- [ ] 3. For each `dispatch` action: read the named `dispatch_file`, verify
        AUTH-05 gate (waveset synced after mod-decide). Dispatch wave
        orchestrator to background; then O0_release_window. Do not poll or
        foreground-hold BUILD.
- [ ] 4. For each `operator_gate` action: surface the gate to the operator and
        pause until they respond. Do not skip approval gates.
- [ ] 5. Report what ran, what is blocked on operator input, and landing
        commit hash when commits occurred.
```

Trigger language (AUTH-10 only): `proceed as recommended`, `/wavves proceed`,
`ship it`, bare `¯\_(ツ)_/¯`, or bare `/shrug` after a verdict with
`recommended_actions`.

---

## proceed-all-standing

Inventory standing work from disk, classify the full queue, move what can,
surface every hard gate together. Never invent the queue from chat or
transcript search (`PROC-PROCEED-CHAT-INVENTORY`).

### Fail ids (closed)

| id | fail condition |
|:---|:---|
| `PROC-PROCEED-NO-STANDING-QUEUE` | all-standing runs without a remasured, persisted standing inventory + class per item |
| `PROC-PROCEED-FORCE-BLOCKED-LOCK` | pass reopens/invents past a hard lock instead of an operator_gate artifact |
| `PROC-PROCEED-SHRUG-WIDEN` | bare shrug / bare `/shrug` (or fuzzy widen) executed as all-standing |
| `PROC-PROCEED-COMMIT-WITHOUT-AUTH` | `commit` land without this-turn authorize + `files:` list (AUTH-10) |
| `PROC-PROCEED-DISPATCH-STORM` | multiple background dispatches ignoring `active_dispatch` / `conflicts_with` / AUTH-05 |
| `PROC-PROCEED-CHAT-INVENTORY` | queue rows from chat/transcript without disk remasure of `source_path` |
| `PROC-PROCEED-STALE-QUEUE` | moves from a persisted standing file without remasure against live registry/dispatch/gates |
| `PROC-PROCEED-SILENT-SKIP-LOCK` | hard lock classified `skip_done` / `out_of_scope` with no gate artifact path |

### Step 0 — Standing queue (persist before any move)

```
- [ ] 0a. Resolve scope (PS-03). Union of:
          (a) lane codes / registry keys / explicit paths named in the
              triggering utterance, else
          (b) active lanes in wavves/INDEX.md for this repo only.
          Forbidden: registry-wide crawl of every lane without named scope;
          transcript search as inventory source.
- [ ] 0b. Remasure inside scope only against live disk:
          wavves/registry.yml status + active_dispatch; lane dispatch*.md /
          waveset open rows; named *_OPERATOR_GATE.md / lock ABSENT honesty;
          open FRs/handoffs named in the trigger (candidates only until
          source_path remasures on disk). Operator paste list = candidates;
          unverified names → class operator_gate
          ("unverified standing claim"), never dispatch or commit.
- [ ] 0c. Persist the queue ONLY at
          wavves/standing/<YYYYMMDD>_<label>.md
          (create wavves/standing/ if missing). One file per pass.
          Overwrite, do not append. Every source_path must exist on disk at
          inventory time.
- [ ] 0d. Empty inventory (no named lanes and zero INDEX active lanes, or
          remasure yields zero rows) → write empty standing file and STOP.
          No moves. (SCOPE-FALLBACK = A)
```

**Row schema** (one row per standing item):

`{id, source_path, class, proposed_action, result, land_hash, gate_path, blocked_reason}`

`class` ∈ `dispatch` | `commit` | `operator_gate` | `skip_done` | `out_of_scope`

**Order:** operator-named lane/FR keys first (when present), then registry
order inside scope.

Running without this persisted file → `PROC-PROCEED-NO-STANDING-QUEUE`.
Moving from a prior standing file without remasure → `PROC-PROCEED-STALE-QUEUE`.

### Step 1 — Classify full queue first (PS-04)

Classify every row before executing any move.

| class | rule |
|:------|:-----|
| `dispatch` | Executable background dispatch exists; honor `active_dispatch` / `conflicts_with` / AUTH-05. |
| `commit` | Land-ready with explicit `files:` list (AUTH-10 shape). All-standing alone is not blanket multi-land auth. |
| `operator_gate` | Hard lock, unverified claim, or needs operator. Write/surface gate artifact; do **not** invent unlock. |
| `skip_done` | Already PASS / non-gating done work; one-line cite of PASS artifact. |
| `out_of_scope` | Outside scope boundary; cite boundary; no dispatch/commit; include on return card as not-moved. |

Additional class rules:

- Never invent work for non-gating already-PASS research unless the operator
  expands the charter.
- Open FR / docs handoff without executable class → `out_of_scope` or
  `operator_gate`, not premature BUILD.
- Hard lock classified `skip_done` / `out_of_scope` with no gate artifact path
  → `PROC-PROCEED-SILENT-SKIP-LOCK`. Reclassify as `operator_gate` with
  `gate_path`.

### Step 2 — Commit-class authorize (COMMIT-AUTH-GRAIN = C)

For every `commit` row:

1. `files:` list is **required** (AUTH-10). Missing `files:` → fail
   `PROC-PROCEED-COMMIT-WITHOUT-AUTH` (reclassify to `operator_gate` or stop
   that land; do not commit).
2. **Same-repo:** one this-turn authorize (all-standing proceed / ship for that
   authorize utterance) may cover every same-repo `commit` row that already
   has `files:`.
3. **Cross-repo:** any land whose paths span another repo id / foreign tree →
   `operator_gate` until per-land authorize this turn. Never treat
   all-standing alone as blanket multi-repo push auth.

### Step 3 — Gate-continue execute (PS-05)

```
- [ ] 3a. Execute ALL non-gate moves first, in queue order:
          dispatch → background only (no storm: honor active_dispatch /
          conflicts_with / AUTH-05; PROC-PROCEED-DISPATCH-STORM if violated);
          commit → AUTH-10 + COMMIT-AUTH-GRAIN C only;
          skip_done → cite PASS artifact on the standing row;
          out_of_scope → cite scope boundary on the standing row / return card.
- [ ] 3b. Then surface EVERY operator_gate together (gate_path +
          blocked_reason). Do not halt the whole pass at the first gate.
- [ ] 3c. Do not dispatch or commit after inventing past a gate
          (PROC-PROCEED-FORCE-BLOCKED-LOCK).
- [ ] 3d. Update each standing-file row: result, land_hash, gate_path,
          blocked_reason as applicable. Persist overwrite of the same
          standing file.
```

### Step 4 — Return card (PS-09)

Emit from the standing file after the pass (one line per row):

`id | class | result | land_hash or gate_path | blocked_reason`

Include `out_of_scope` and `skip_done` rows as not-moved / already-done cites.
Include every `operator_gate` with `gate_path` and `blocked_reason`.
