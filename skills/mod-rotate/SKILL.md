---
name: mod-rotate
description: >-
  Rotate the moderator to a fresh thread with full hydration and provenance.
  Use for /mod-rotate, handoff, self-fork, replay or when token velocity and
  context usage are too high. Produces a rotation file under wavves/rotations/
  or a five-file lane handoff packet and emits a one-line paste for the new
  thread.
disable-model-invocation: true
---

# mod-rotate

Build a complete handoff so a NEW thread of this orchestrator resumes the
current lane without replaying the overloaded chat. The receiving thread
hydrates from files, never from the transcript linearly.

## When to use

The operator says any of "rotate you", "charter a handoff / your replacement",
"fresh thread / self-replay / self-fork", "token velocity is too high" or
"hand this branch off to a new orchestrator". An overloaded orchestrator may
also PROPOSE rotation itself. it surfaces the proposal to the operator and
rotates only on operator confirmation and the successor identity still comes
from the handoff file, never self-chosen.

## Two variants, pick the right one

**A. Whole-orchestrator rotation (the common case).** The orchestrator home
(see the sibling skill `wavve`) holds a standing hydration
contract at `<repo>/wavves/AGENTS.md` that is reused across rotations.
per-rotation state goes in
`<repo>/wavves/rotations/rotation-r<NN>-<YYYYMMDD>-<HHMM>.md`
(operator's timezone. NN = the OUTGOING term, zero-padded so lexical sort
equals term order). Do NOT create a new dated handoff home for a
whole-orchestrator rotation and do NOT restate the standing etiquette locks
per rotation, because the home AGENTS.md carries them. The rotation file
covers exactly, in order:

- **Successor identity first** (section 0). The incoming term `O0.R<N+1>`,
  assigned by the handoff, never self-chosen (see `wavve`, "Identity and
  rotation terms"). The successor stamps `O0.R<N+1>:` on
  commits, step-log entries and authored charters and suffixes dispatched
  wave ids with `.R<N+1>`.
- Positions (landed work with commit hashes).
- Active background dispatches (purpose, lane home, findings file, PICKUP
  actions when it returns, recommended model tier and whether the runtime
  accepted an explicit model setting).
- Blocked items plus what unblocks them.
- Uncommitted local state per repo.
- Operator-pending decisions.
- Active model policy and any deviations from the charter's recommended model
  tiers.
- Provenance pointer (transcript path, keyword search only).

Follow the section shape of the newest existing file in `rotations/`. Write
the rotation file and return a commit plan. Commit and push the orchestrator
home only when the repo protocol already grants that authority or the
operator explicitly asks. A separate-sandbox successor can hydrate only from
published state. if the handoff stays local, say so plainly in the paste and
scope it to the same machine. One-line paste form:

```
/wavves hydrate as O0.R<N+1> from <repo>/wavves/INDEX.md (current rotation: rotations/rotation-r<NN>-<...>.md) and ack per the rotation contract, stating your assigned identity, before acting.
```

The leading `/wavves` is required, not decorative. Every skill in this
plugin sets `disable-model-invocation: true`, so nothing auto-fires from
description matching, only from an explicit slash command. A paste without
it risks landing in a fresh thread that never invokes the plugin at all.

**B. Single-lane handoff (a lane leaves an overloaded thread. the main
orchestrator continues).** Use the five-file handoff home below.

## Output (variant B)

1. A handoff home, for example
   `<repo>/wavves/handoffs/<YYYYMMDD>_<lane>/`, containing five
   files (templates below).
2. A one-line paste emitted in chat for the operator to drop into the new
   thread.

Variant B does NOT commit or push unless the operator explicitly asks (note
any uncommitted local state in the charter section G instead). Variant A
also defaults to a commit plan unless repo governance grants the write or the
operator explicitly asks for publication. When a rotation commit is made, the
final report carries the branch verified, the final commit hash, push
confirmation, the synced state and the changed-file list. All rotation git
actions are performed by the orchestrator itself. dispatched runners never
run git.

## Concurrent terms and git safety

Rotation is the mechanism that creates concurrent terms, so its git actions
carry their own etiquette.

- **The rotation commit touches only the home's continuity files** (AGENTS.md
  and the rotation file). If a dispatched agent is actively editing the same
  branch, coordinate the commit explicitly or note the conflict in the
  rotation file. never land commits silently under an active editor.
- **Remote-rejected push** (a concurrent term landed first). Fetch, then
  rebase with autostash, then push. Never force-push over the concurrent
  commit. Before rebasing, confirm no other active agent owns unstaged files
  in the working tree. if one does, coordinate before any git action.
- **The outgoing term fences itself.** After the rotation file is committed
  and pushed, the outgoing thread makes no further commits and writes no
  further rotation files. The one-line paste goes to exactly one successor
  thread. if two threads ever claim the same term, the newest rotation file
  governs and the conflict gets logged.
- **A surviving predecessor thread conforms before landing.** An older thread
  that stays active with uncommitted work conforms that work to any newer
  term's rulings before landing it, per the stale-term rule.
- **Unverified work never rides the handoff silently.** Before the term ends,
  changes on shared branches that could not be verified or qualified are
  reverted from the working tree, preserved at a stated location and
  recorded in the rotation file's uncommitted-state section with the
  rationale.
- **The successor verifies before proceeding.** The ack includes checking
  that the rotation file's claimed positions and commit hashes are reachable
  from HEAD. discrepancies become recorded gaps, never silently executed
  pickups. If a divergent untracked local copy blocks the successor's pull,
  resolve in favor of the tracked origin artifact, delete the local
  divergence and record the deletion in the step log.

## Workflow

```
- [ ] 1. Name the lane (short kebab label) + date (operator's timezone)
- [ ] 2. Capture repo state: branch + last commit hash (git rev-parse / git log -1)
- [ ] 3. Locate this session's transcript file if the environment exposes one
- [ ] 4. Write the rotation file (variant A) or the 5 files (variant B)
- [ ] 5. Emit the one-line paste
```

### Steps 1-3 notes

- Reuse the house convention. Study one existing handoff or charter in the
  repo for tone before writing.
- If the environment exposes a transcript path, record it as provenance with
  the instruction "search by keyword, never read linearly". If not, skip it.

### Step 4, the five files (variant B)

**handoff.md** is the authority doc. Sections, in order:

- A. Purpose (one paragraph, what the new thread resumes)
- B. Decisions that are LOCKED, do not reopen (numbered. the highest-value
  section. capture every fact an unprimed agent would get wrong)
- C. Registry snapshot (table of slice | what shipped | status)
- D. PRIMER, meaning open items, using the operator's **verbatim** framing
  when given
- E. Dispatch table (lane | owner | inputs | exit bar | status)
- F. Open gate/metric state (why anything is still blocked, with numbers)
- G. Pending uncommitted local state (flag files not yet committed. note
  whether the successor shares the same machine or must rehydrate from the
  remote)
- H. Model routing state (recommended tier, actual model if known and any
  enforcement gap)
- I. Return contract (the exact ack the new thread must produce)
- J. Transcript / provenance pointer (path plus "search by keyword, not
  linear")

**hydration.md** is an ordered read list, grouped. Governance/canon
first, then this lane's charter and trace, then evidence, then code, then
assets, then a repo map and environments. Every entry is an absolute or
repo-relative path.

**step-log.md** is the synthesis trace, newest last (S01, S02, ...). Each
step runs 2-4 lines, names the files touched and any commit hash. Append
entries, never rewrite prior ones. Point to the transcript for detail. do
not transcribe it.

**dispatch.md** is a fenced paste block that

- declares the role and lane
- lists 3-4 hydration files in order
- restates the locked decisions inline (1 sentence)
- names active lanes and which need operator approval
- names recommended model tiers for the lane and active waves
- forbids commit/push without an operator ask
- forbids linear transcript reads
- demands the section H return contract

plus a "more context" table (need, then file), files not transcript.

**README.md** is 8-15 lines. What this home is, the file list, how to start
the fresh thread, current lane status.

### Step 5, the one-line paste

Emit exactly one line in chat the operator can paste. Form:

```
/wavves hydrate as O0 (<LANE> lane) from <repo>/wavves/handoffs/<DATE>_<lane>/dispatch.md and ack per handoff charter section H before acting.
```

## Quality bar

- The charter's section B (locked decisions) must let an unprimed agent avoid
  every known footgun for this lane. The locked-decision section is the point
  of the skill.
- Use the operator's verbatim wording for primer/open items when provided.
- No time-bombs ("before Monday do X"). state conditions, not deadlines,
  unless a real external deadline exists.
- Paths must be real. Verify with a file search before citing.
- An artifact the handoff cannot resolve gets an explicit gap entry with the
  reason, never a silent omission and the positions and numbers the handoff
  carries trace to step-log entries or findings files.
