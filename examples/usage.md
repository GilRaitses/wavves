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
| Dispatch | `lanes/.../dispatch.md` | paste block for background runners |
| Registry | `wavves/registry.yml` | every lane and its status |
| Rotation | `wavves/rotations/` | handoffs with term identity |
| Gates | `lanes/.../gate-captures/` | runnable evidence (JSON + log) |

## Skills

| skill | use it when |
|:------|:------------|
| `/wavves` | default entry. routes by playbook |
| `/wavve` | home setup only |
| `/charter` | charter a lane only |
| `/mod-rotate` | rotation only |

## Playbooks (`/wavves` routes here)

| playbook | leaf skill | for |
|:---------|:-----------|:----|
| bootstrap | `/wavve` | first time, repair home |
| charter-lane | `/charter` | bug fix, audit, refactor, flaky CI, overnight lane |
| rotate | `/mod-rotate` | hand off to fresh thread |
| pickup | hydrate | resume, "where are we" |

## Examples

```text
default:           /wavves set up in this repo, then audit our README for drift.
                   read-only, no commits.
bug fix:           /wavves our checkout webhook sometimes creates duplicate
                   invoices. reproduce, fix and verify with gate captures.
flaky ci:          /wavves three integration tests flake on main. fix root causes
                   and prove stability.
overnight:         /wavves i'm stepping away. land the auth hardening lane with
                   captured gates. no deploy without my approval.
rotate:            /wavves rotate this thread. write a handoff for active lanes.
pickup:            /wavves hydrate from the rotation paste and tell me what's active.
setup only:        /wavve set up wavves in this repo. do not commit.
charter only:      /charter migrate every callsite to the async config store.
rotate only:       /mod-rotate token velocity is too high. give me the one-line paste.
```

## End-to-end session

```text
/wavves set up in this repo, then fix the cart 500 when line items exceed 50.
reproduce, fix and verify. no deploy.

# ... lane runs in background ...

/wavves rotate. I want a fresh thread for the next lane.
```

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
    YYYYMMDD_checkout-webhook-dedup/
      README.md
      waveset.md
      dispatch.md
      findings/
      gate-captures/
      decisions/
```

Inspect a gate by opening the JSON under `gate-captures/`, reading the paired
log and checking the verdict in `findings/`.
