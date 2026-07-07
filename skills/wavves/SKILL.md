---
name: wavves
description: >-
  Main entry for durable multi-agent routing. Reads your request, checks the
  wavves home, picks a playbook and runs the leaf skill (/wavve, /charter or
  /mod-rotate). Use for /wavves or any bounded lane work, setup, rotation or
  pickup.
disable-model-invocation: true
---

# wavves

Default entry point for the plugin. Read the operator's request, check whether
`<repo>/wavves/` exists, match a playbook below and **read the routed leaf
skill in full** before acting.

## Non-negotiables

1. **Start with a todo list.** First item: match a playbook and name the leaf
   skill you will read.
2. **Read the leaf skill in full** (`wavve`, `charter` or `mod-rotate`) before
   any substantive write. Do not improvise charter or rotation steps from
   memory.
3. **The moderator (O0) stays operator-facing.** Dispatched runners answer to
   O0, not the operator directly. Gates are runnable with captured evidence.
4. **No commit, push, deploy or external mutation** unless the operator
   explicitly asks or repo governance grants it.
5. **If `wavves/` is missing**, route to **bootstrap** before any charter work.

## Routing

| Playbook | Leaf skill | For |
|:---------|:-----------|:----|
| bootstrap | `wavve` (`/wavve`) | first time in repo, repair home, "set up wavves" |
| charter-lane | `charter` (`/charter`) | bounded multi-wave work: bug fix, audit, refactor, feature, flaky CI, security pass, overnight lane |
| rotate | `mod-rotate` (`/mod-rotate`) | rotate, handoff, fresh thread, self-fork, replay, token velocity too high |
| pickup | hydrate + moderate | resume from rotation paste, "where are we", reconcile active lanes |

When the request is ambiguous, default to **charter-lane** if `wavves/` exists
and the operator describes work to do. Default to **bootstrap** if the home is
missing.

## Playbook steps

Open the matched playbook file and copy its steps verbatim into your todo list
before adding task-specific items.

- **Bootstrap.** `playbooks/bootstrap.md`
- **Charter lane.** `playbooks/charter-lane.md`
- **Rotate.** `playbooks/rotate.md`
- **Pickup.** `playbooks/pickup.md`

A step you skip stays in the list with `skip: <reason>`.

## Leaf skills

| skill | slash | when to reach for directly |
|:------|:------|:---------------------------|
| `wavve` | `/wavve` | you know you only need home setup |
| `charter` | `/charter` | you know you only need a new lane |
| `mod-rotate` | `/mod-rotate` | you know you only need rotation |

Most operators can type `/wavves` plus the task and let routing handle the rest.

## Pairing with `/loop`

`/wavves` plus Cursor's `/loop` works for long lanes: charter once, let the
background orchestrator run waves with captured gates, rotate when context fills.
