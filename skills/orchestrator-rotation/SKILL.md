---
name: orchestrator-rotation
description: >-
  Charter a self-replacement handoff so a fresh thread of an orchestrator can
  take over with full hydration and provenance. Use when the operator asks to
  rotate the agent, hand off to a new orchestrator, replay or self-fork into a
  fresh thread, or says token velocity or context usage is too high and the
  thread must be rotated. Produces either a rotation file under the standing
  orchestrator home (whole-orchestrator handoff) or a five-file handoff packet
  (single-lane handoff), and emits a one-line paste for the new thread.
---

# Orchestrator Rotation

Build a complete handoff so a NEW thread of this orchestrator resumes the
current lane without replaying the overloaded chat. The receiving thread
hydrates from files, never from the transcript linearly.

## When to use

The operator says any of "rotate you", "charter a handoff / your replacement",
"fresh thread / self-replay / self-fork", "token velocity is too high", or
"hand this branch off to a new orchestrator".

## Two variants, pick the right one

**A. Whole-orchestrator rotation (the common case).** The orchestrator home
(see the sibling skill `orchestrator-home`) holds a STANDING hydration
contract at `<repo>/.cca/catalogue/O0/AGENTS.md` that is REUSED across
rotations; per-rotation state goes in
`<repo>/.cca/catalogue/O0/rotations/ROTATION_R<NN>_<YYYYMMDD>_<HHMM>.md`
(operator's timezone; NN = the OUTGOING term, zero-padded so lexical sort
equals term order). Do NOT create a new dated handoff home for a
whole-orchestrator rotation and do NOT restate the standing etiquette locks
per rotation, because the home AGENTS.md carries them. The rotation file
covers exactly, in order:

- **Successor identity first** (section 0). The incoming term `O0.R<N+1>`,
  assigned by the handoff, never self-chosen (see `orchestrator-home`,
  "Identity and rotation terms"). The successor stamps `O0.R<N+1>:` on
  commits, step-log entries, and authored charters, and suffixes dispatched
  wave ids with `.R<N+1>`.
- Positions (landed work with commit hashes).
- Active background dispatches (purpose, lane home, findings file, PICKUP
  actions on completion).
- Blocked items plus what unblocks them.
- Uncommitted local state per repo.
- Operator-pending decisions.
- Provenance pointer (transcript path, keyword search only).

Follow the section shape of the newest existing file in `rotations/`. Commit
and push the orchestrator home (AGENTS.md plus the rotation file) if the repo
protocol allows it, so the successor can hydrate from a clean checkout.
One-line paste form:

```
Hydrate as O0.R<N+1> from <repo>/.cca/catalogue/O0/AGENTS.md (current rotation: rotations/ROTATION_R<NN>_<...>.md) and ack per the rotation contract, stating your assigned identity, before acting.
```

**B. Single-lane handoff (a lane leaves an overloaded thread; the main
orchestrator continues).** Use the five-file handoff home below.

## Output (variant B)

1. A handoff home, for example
   `<repo>/.cca/catalogue/O0/<YYYYMMDD>_<lane>-handoff/`, containing five
   files (templates below).
2. A one-line paste emitted in chat for the operator to drop into the new
   thread.

Variant B does NOT commit or push unless the operator explicitly asks (note
any uncommitted local state in the charter section G instead). Variant A
commits and pushes when the repo's protocol mandates it.

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

**HANDOFF_CHARTER.md** is the authority doc. Sections, in order:

- A. Purpose (one paragraph, what the new thread resumes)
- B. Decisions that are LOCKED, do not reopen (numbered; the highest-value
  section; capture every fact an unprimed agent would get wrong)
- C. Registry snapshot (table of slice | what shipped | status)
- D. PRIMER, meaning open items, using the operator's **verbatim** framing
  when given
- E. Dispatch table (lane | owner | inputs | exit bar | status)
- F. Open gate/metric state (why anything is still blocked, with numbers)
- G. Pending uncommitted local state (flag files not yet committed; note
  whether the successor shares the same machine or must rehydrate from the
  remote)
- H. Return contract (the exact ack the new thread must produce)
- I. Transcript / provenance pointer (path plus "search by keyword, not
  linear")

**HYDRATION_PACKET.md** is an ordered read list, grouped. Governance/canon
first, then this lane's charter and trace, then evidence, then code, then
assets, then a repo map and environments. Every entry is an absolute or
repo-relative path.

**STEP_LOG.md** is the synthesis trace, newest last (S01, S02, ...). Each
step runs 2-4 lines, names the files touched and any commit hash. Point to
the transcript for detail; do not transcribe it.

**ORCHESTRATOR_DISPATCH_PROMPT.md** is a fenced paste block that

- declares the role and lane
- lists 3-4 hydration files in order
- restates the locked decisions inline (1 sentence)
- names active lanes and which need operator approval
- forbids commit/push without an operator ask
- forbids linear transcript reads
- demands the section H return contract

plus a "more context" table (need, then file), files not transcript.

**README.md** is 8-15 lines. What this home is, the file list, how to start
the fresh thread, current lane status.

### Step 5, the one-line paste

Emit exactly one line in chat the operator can paste. Form:

```
Hydrate as O0 (<LANE> lane) from <repo>/.cca/catalogue/O0/<DATE>_<lane>-handoff/ORCHESTRATOR_DISPATCH_PROMPT.md and ack per HANDOFF_CHARTER section H before acting.
```

## Quality bar

- The charter's section B (locked decisions) must let an unprimed agent avoid
  every known footgun for this lane. This is the point of the skill.
- Use the operator's verbatim wording for primer/open items when provided.
- No time-bombs ("before Monday do X"); state conditions, not deadlines,
  unless a real external deadline exists.
- Paths must be real. Verify with a file search before citing.
