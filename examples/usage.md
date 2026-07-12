# Using wavves

Type `/wavves` at the start of a task. It routes to the right leaf skill,
like `/poteto-mode` in pstack.

## System inventory

| Piece | Where | Role |
|:------|:------|:-----|
| Moderator (O0) | operator-facing thread | charters, dispatches, reconciles |
| Home | `wavves/` | hydration contract across rotations |
| Lane | `wavves/lanes/<date>_<label>/` | one bounded workstream |
| Charter | `lanes/.../waveset.md` | scope, locks, waves, gates |
| Dispatch | `lanes/.../dispatch-w{N}.md` | per-wave paste block for background runners |
| Registry | `wavves/registry.yml` | every lane and its status (`active_dispatch`, `conflicts_with`, …) |
| Rotation | `wavves/rotations/` | handoffs with term identity |
| Gates | `lanes/.../gate-captures/` | runnable evidence (JSON + log) |

## Skills

| skill | use it when |
|:------|:------------|
| `/wavves` | default entry. routes by playbook |
| `/wavves-init` | home setup only |
| `/charter` | charter a lane only |
| `/mod-check` | adversarial sanity-check of a landed spec or plan |
| `/mod-decide` | lock open product/design calls after a check return |
| `/layover` | workspace preflight audit before cloud handoff |
| `/mod-rotate` | rotation only |

## Playbooks (`/wavves` routes here)

| playbook | leaf skill | for |
|:---------|:-----------|:----|
| bootstrap | `/wavves-init` | first time, repair home |
| charter-lane | `/charter` | bug fix, audit, refactor, flaky CI, overnight lane |
| check | `/mod-check` | adversarial review of a landed spec or plan before build |
| decide | `/mod-decide` | lock open calls before BUILD charter |
| layover | `/layover` | preflight multi-repo workspace before cloud agent |
| rotate | `/mod-rotate` | hand off to fresh thread |
| pickup | hydrate | resume, "where are we" |
| layover | `/layover` | preflight multi-repo workspace before cloud agent |
| proceed | hydrate + execute | `proceed as recommended`, `/wavves proceed` |

## Quick reference

```text
default:           /wavves set up in this repo, then audit our README for drift.
                   read-only, no commits.
spec check:        /mod-check review docs/superpowers/specs/2026-07-08-example.md
                   before we write the implementation plan. adversarial parallel
                   wave. read-only. landing_commit_hash <hash>.
decide:            /mod-decide navigate open calls from the check return.
                   one decision at a time. write decisions/*.md. no BUILD yet.
layover:           /layover audit ~/my.code-workspace. read-only.
rotate:            /wavves rotate this thread. write a handoff for active lanes.
pickup:            /wavves hydrate from the rotation paste and tell me what's active.
proceed:           /wavves proceed as recommended after mod-check or mod-decide return.
setup only:        /wavves-init set up wavves in this repo. do not commit.
charter only:      /charter migrate every callsite to the async config store.
check only:        /mod-check the landed spec. GO / REVISE / BLOCK with named gaps.
decide only:       /mod-decide lock the open calls. emit Locked decisions paste.
rotate only:       /mod-rotate token velocity is too high. give me the one-line paste.
```

## From check to BUILD

When work starts as a written spec, do not jump straight to `/charter`. Use
three skills in order. The moderator (O0) stays operator-facing the whole way.

```text
spec landed
    → /mod-check     adversarial parallel wave → GO | REVISE | BLOCK
    → /mod-decide    lock open product/design calls → decisions/*.md
    → /charter       BUILD with Locked decisions pasted into waveset.md
```

| Step | Skill | You get | Stop if |
|:-----|:------|:--------|:--------|
| 1. Check | `/mod-check` | verdict + named gaps + settled technical findings | `BLOCK` or `REVISE` until the artifact is fixed |
| 2. Decide | `/mod-decide` | one-at-a-time picks, `decisions/*.md`, Locked decisions paste | any fork a build agent would have to invent is still open |
| 3. Charter | `/charter` | BUILD lane, waves, gated acceptance | locks missing, or two disjoint features stuffed into one lane |

After mod-decide, O0 syncs locks to `waveset.md`, active `dispatch-w{N}.md`,
and `registry.yml` before W2 dispatch. Each dispatch carries an authority
precedence block (locks → waveset → findings marked STALE).

Mod-check verdicts may include scoped blockers:

```yaml
verdict: REVISE
blocks_w2: false
blocks_w4: true
recommended_actions:
  - action: commit
    files: [wavves/lanes/...]
  - action: dispatch
    wave: w2
  - action: operator_gate
    id: approve-quarantine-manifest
```

Use `/wavves proceed` to execute `recommended_actions` in order.

**What belongs in decide vs what is already locked grounding**

- **Decide (product / design forks):** gesture choice, which data source is
  authoritative, v1 share scope, whether to replace a shipped behavior.
- **Grounding (already verified — do not rediscover):** measured facts from
  the check (e.g. point-in-polygon renders nothing; Vercel body cap rules out
  a naive server route). Confirm them into the Locked / Grounding paste; do
  not re-debate them unless new evidence appears.

**Practical paste after a check return**

```text
/mod-decide You are O0. Do not charter BUILD yet.

Check landed at <hash>. Navigate the open product decisions listed in the
return. One decision at a time: options in one line each, wait for my pick,
write decisions/<CODE>-<slug>.md, append to a Locked decisions draft.

Do not reopen settled technical findings. When I say locks are complete,
emit the Locked decisions paste and the /charter invocation(s). One feature
per BUILD lane when scopes are disjoint.
```

**Practical paste once locks exist**

```text
/charter BUILD lane for <feature>.

repo_state_verified_against: <check landing hash>
type: execution

Locked decisions (do NOT reopen):
<paste from /mod-decide>

Grounding (already verified — do not rediscover):
<paste from /mod-decide>

Wave shape: discovery → build → gated integration → gated acceptance.
No commits/deploy without my ask. Escalate any lock conflict to O0.
```

**Anti-patterns**

| Temptation | Why not |
|:-----------|:--------|
| `/charter` while forks are still open | build agents pick for you and fight the check |
| `/mod-check` again to "make the decisions" | check reviews; decide locks |
| One mega-charter for two disjoint features | file ownership and risk diverge; split lanes |
| Asking Mod to "just start building" mid-decide | O0's job is lock first, dispatch second |

The walkthroughs below go deeper on other mechanics. For the check → decide →
BUILD path, the section above is the guide.

- [A. Feature build with real parallelism](#a-feature-build-with-real-parallelism)
- [B. Flaky test stabilization with proof](#b-flaky-test-stabilization-with-proof)
- [C. Performance sprint with before/after numbers](#c-performance-sprint-with-beforeafter-numbers)
- [D. A migration that outlives one chat session](#d-a-migration-that-outlives-one-chat-session)

## A. Feature build with real parallelism

Shows: file-ownership discipline, why two waves can run in parallel safely and
why a third wave (integration) has to be serialized.

```text
/wavves add a CSV export button to the reports page. build the endpoint and the
button in parallel, keep them disjoint. gate on a real downloaded file that
matches the table.
```

`/wavves` reads `wavves/` (exists already), matches charter-lane, reads
`/charter` in full, then charters lane `EXP` at
`wavves/lanes/20260708_reports-csv-export/`.

**Wave 1, discovery (fast model, read-only).** Two subagents in parallel:

- `EXP-W1a` reads the reports page, the table's data source and any existing
  export patterns elsewhere in the codebase. Writes
  `findings/EXP-reports-page.md`.
- `EXP-W1b` (the adversarial member) hunts for gotchas: the table only renders
  page 1 while the export needs every row, the API route needs the same auth
  check as the page, a CSV library is already a dependency so nothing new to
  install. Writes `findings/EXP-risks.md`.

**Wave 2, build (balanced model, disjoint new files, parallel).**

- `EXP-W2a` owns a new file, the export API route, streaming CSV from the same
  query the table already uses (so the export can't drift from what the user
  sees).
- `EXP-W2b` owns a new file, the export button component, plus a short wiring
  note on how it mounts.

Neither subagent touches the reports page file itself. That's the whole point
of the split: two new files with zero overlap can run in parallel with no
collision risk. If both agents needed to edit the *same* file (say, both
patching the reports page directly), that would not be a safe parallel wave.
It would be one serialized editor instead, which is exactly what wave 3 is for.

**Wave 3, integration (single serialized editor, GATED on O0 approval).** One
agent, no parallelism, mounts the new button into the reports page and wires
the new route into the router config. This is the only wave allowed to touch
that shared file.

**Wave 4, acceptance (GATED, high-reasoning, no authorship of the build).**
Downloads the CSV from the real running app, not a mock, and diffs it
row-by-row against the table's live data. Capture:

```json
{
  "gate": "EXP-ACCEPT",
  "pass_metric": "csv_row_count == table_row_count AND mismatched_rows == 0",
  "measured": {
    "table_row_count": 248,
    "csv_row_count": 248,
    "mismatched_rows": 0,
    "download_latency_ms": 812
  },
  "verdict": "PASS",
  "command": "node scripts/verify-csv-export.js --url http://localhost:3000/reports"
}
```

Registry entry after reconciliation:

```yaml
EXP:
  label: reports-csv-export
  home: wavves/lanes/20260708_reports-csv-export/
  waves: [EXP-W1a, EXP-W1b, EXP-W2a, EXP-W2b, EXP-INT, EXP-ACCEPT]
  status: completed
  note: >
    CSV export on reports page. Backend route and button built as disjoint
    new files in parallel. Integration wired the single mount point.
    Acceptance verified a real download against 248 live rows, 0 mismatches.
```

## B. Flaky test stabilization with proof

Shows: gates measure before and after with the same harness, so "looks stable
now" is never the verdict. A failed gate is reported as failed, not softened.

```text
/wavves three tests in checkout.spec.ts flake on main, maybe 1 in 5 runs.
charter a lane to characterize them, fix root causes and prove stability,
not just "looks fixed".
```

Lane `FLK` at `wavves/lanes/20260708_checkout-flakes/`.

**Wave 1, discovery (fast model).** Before touching anything, rerun each named
test 20 times in isolation to get a real baseline, not an impression:

```text
test                          runs   failures   rate
checkout > applies discount   20     4          20%
checkout > handles retry      20     6          30%
checkout > final total        20     1          5%
```

Root cause traced in `findings/FLK-baseline.md`: a shared test helper races a
debounced UI update on a `setTimeout`, and the retry test additionally leaks
mock state left over from the discount test.

**Wave 2, build (balanced model, disjoint files, parallel).** One subagent
fixes the timing race in the shared helper. A second isolates the mock leak
inside the retry test's own file. Different files, so they run in parallel.
If the fix for both bugs lived in the same helper file, this would collapse
to one subagent, not two racing to edit the same file.

**Wave 3, acceptance (GATED, high-reasoning, no authorship of the fix).**
Reruns the exact same 20x-per-test harness used for the baseline, so the
before/after comparison is apples-to-apples:

```json
{
  "gate": "FLK-ACCEPT",
  "pass_metric": "failure_rate == 0 across 20 runs per test",
  "baseline": {"applies_discount": "4/20", "handles_retry": "6/20", "final_total": "1/20"},
  "measured": {"applies_discount": "0/20", "handles_retry": "0/20", "final_total": "0/20"},
  "verdict": "PASS",
  "command": "npx jest checkout.spec.ts --testNamePattern='applies discount|handles retry|final total' --repeat 20"
}
```

If the rerun had come back 2/20 instead of 0/20, the verdict is FAIL with the
named test, and the wave repeats once against the charter's remediation-loop
cap (default 2) before escalating to the operator instead of quietly calling
it "mostly fixed."

## C. Performance sprint with before/after numbers

Shows: model routing with a real cost rationale, and a trace harness reused
unchanged for baseline and acceptance so the improvement number is trustworthy.

```text
/wavves the /dashboard route takes about 4 seconds to load. charter a lane to
find the real bottlenecks and fix them, with before/after numbers.
```

Lane `PERF` at `wavves/lanes/20260708_dashboard-load/`.

**Wave 1, discovery (fast model, profiling).** One subagent captures a
cold-load trace and finds three independent bottlenecks in
`findings/PERF-trace.md`:

1. `getWidgetsForUser()` issues 47 sequential queries (N+1).
2. The hero image is a 2.1MB PNG with no responsive sizes.
3. The full charting library ships in the main bundle even though only 2 of
   its 12 chart types are used.

Baseline captured once, as measured numbers, not three separate impressions:

```json
{"p95_load_ms": 4180, "main_bundle_kb": 1840, "db_query_count": 52}
```

**Wave 2, build (balanced model, three disjoint fixes, parallel).** Each
subagent owns one unrelated file: the query batching fix, the image pipeline,
the chart bundle split. Independent files, so all three run at once.

**Wave 3, acceptance (GATED, high-reasoning).** Reruns the identical trace
tool used for the baseline, not a different one:

```json
{
  "gate": "PERF-ACCEPT",
  "pass_metric": "p95_load_ms < 2000",
  "baseline": {"p95_load_ms": 4180, "main_bundle_kb": 1840, "db_query_count": 52},
  "measured": {"p95_load_ms": 1340, "main_bundle_kb": 620, "db_query_count": 3},
  "verdict": "PASS",
  "command": "node scripts/trace-dashboard.js --runs 10 --url http://localhost:3000/dashboard"
}
```

Model routing for this lane, from `waveset.md`:

```text
role                model tier       reason
discovery (trace)   fast             read one trace, categorize bottlenecks
build (3x)          balanced         bounded, disjoint fixes, local validation
acceptance gate     high-reasoning   judges whether 3 fixes together clear the bar
```

The discovery and build roles don't need an expensive model to read a trace or
apply a scoped fix. Judging whether the combined result actually clears the
bar, on the other hand, is exactly the kind of call reserved for the
high-reasoning tier.

## D. A migration that outlives one chat session

Shows: the standing home and rotation file are the real state-transfer
mechanism, not a chat summary, and a successor verifies claims before trusting
them.

```text
/wavves migrate every caller from the sync ConfigStore to the async
ConfigStoreAsync. behavior must stay identical. this will take a while.
```

Lane `MIG` at `wavves/lanes/20260708_config-async/`.

**Wave 1, discovery (fast model).** Finds all 34 call sites across 12 files,
listed with file:line in `findings/MIG-callsites.md`.

**Wave 2, build (balanced model, four disjoint file groups, parallel).** The
34 callsites split into 4 non-overlapping file groups, one subagent per group,
each migrating its group and ending typecheck-clean.

Partway through wave 2, the operator's thread has been running long enough
that context is heavy:

```text
/wavves rotate this thread. write a handoff for active lanes.
```

`/mod-rotate` writes `rotations/rotation-r01-20260708-1940.md`. Section 0
assigns the successor identity first, `O0.R2`, never self-chosen. The file
records:

- Positions landed so far (none yet committed, per the runner git ban and
  no operator commit ask).
- Active dispatches: `MIG-W2a` and `MIG-W2b` returned (two file groups
  migrated, typecheck clean); `MIG-W2c` and `MIG-W2d` still running, with the
  pickup action "check status; if dead, re-dispatch against the same file
  group, do not reassign to a sibling."
- Uncommitted local state: two migrated files sitting in the working tree.
- The one-line paste:

```text
/wavves hydrate as O0.R2 from <repo>/wavves/INDEX.md (current rotation:
rotations/rotation-r01-20260708-1940.md) and ack per the rotation contract,
stating your assigned identity, before acting.
```

The operator pastes that into a fresh chat. The new thread:

1. Reads `wavves/INDEX.md`, finds the newest rotation file, acks: "I am
   O0.R2, hydrated from rotation-r01-20260708-1940.md."
2. Verifies the claimed positions before trusting them: opens the two
   "migrated" files and confirms they actually match what the rotation file
   claimed. A discrepancy here becomes a recorded gap, not a silently
   executed pickup.
3. Checks on `MIG-W2c` and `MIG-W2d`. One finished while the rotation file was
   being written, a normal race; O0.R2 reconciles that return and keeps
   waiting on the other rather than double-dispatching it.
4. Once wave 2 fully lands, O0.R2 runs wave 3 (integration, gated) and wave 4
   (acceptance: the full test suite, same command as the pre-migration run,
   same pass/fail count expected).

Nothing about picking up this lane required re-reading the original chat.
Every fact the successor needed to act correctly was already on disk.

## What lands on disk

```text
wavves/
  INDEX.md
  AGENTS.md
  registry.yml
  step-log.md
  rotations/
    rotation-r01-YYYYMMDD-HHMM.md
  lanes/
    20260708_reports-csv-export/
      README.md
      waveset.md
      dispatch.md
      findings/
      gate-captures/
      decisions/
    20260708_checkout-flakes/
      ...
    20260708_dashboard-load/
      ...
    20260708_config-async/
      ...
```

Inspect a gate by opening the JSON under `gate-captures/`, reading the paired
log and checking the verdict in `findings/`. A chat summary is not a gate
capture; if the JSON is missing or hand-authored, the gate is not accepted.
