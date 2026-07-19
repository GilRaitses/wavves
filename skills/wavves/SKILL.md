---
name: wavves
description: >-
  Main entry for durable multi-agent routing. Reads your request, checks the
  wavves home, picks a playbook and runs the leaf skill (/wavves-init, /charter,
  /mod-check, /mod-decide, /layover or /mod-rotate). Use for /wavves or any
  bounded lane work, setup, spec check, decision lock, workspace preflight,
  rotation, pickup or proceed.
disable-model-invocation: true
---

# wavves

Default entry point for the plugin. Read the operator's request, check whether
`<repo>/wavves/` exists, match a playbook below and **read the routed leaf
skill in full** before acting.

## Non-negotiables

1. **Start with a todo list.** First item: match a playbook and name the leaf
   skill you will read.
2. **Read the leaf skill in full** (`wavves-init`, `charter`, `mod-check`,
   `mod-decide`, `layover` or `mod-rotate`) before any substantive write. Do
   not improvise charter, check, decide, layover or rotation steps from memory.
3. **The moderator (O0) stays operator-facing.** Dispatched runners answer to
   O0, not the operator directly. Gates are runnable with captured evidence.
4. **No commit, push, deploy or external mutation** unless the operator
   explicitly asks or repo governance grants it.
5. **If `wavves/` is missing**, route to **bootstrap** before any charter work.

## Routing

| Playbook | Leaf skill | For |
|:---------|:-----------|:----|
| bootstrap | `wavves-init` (`/wavves-init`) | first time in repo, repair home, "set up wavves" |
| charter-lane | `charter` (`/charter`) | bounded multi-wave work: bug fix, audit, refactor, feature, flaky CI, security pass, overnight lane |
| check | `mod-check` (`/mod-check`) | adversarial sanity-check of a written spec or plan before implementation |
| decide | `mod-decide` (`/mod-decide`) | lock open product/design calls after a check return, before BUILD charter |
| layover | `layover` (`/layover`) | preflight a bespoke multi-repo workspace before a cloud agent takes over |
| paragraph-tunnel | dispatch STEPS | mid-render outbound paragraph gate (adversarial + capped rewrite; no slash skill in v0) |
| proof-before-accept | dispatch STEPS | pre-ACCEPT proof fields + mechanical/DOM harness (no `/proof-gate` slash skill in v0) |
| rotate | `mod-rotate` (`/mod-rotate`) | rotate, handoff, fresh thread, self-fork, replay, token velocity too high |
| pickup | hydrate + moderate | resume from rotation paste, "where are we", reconcile active lanes |
| proceed | hydrate + execute | `proceed as recommended`, `/wavves proceed`, execute verdict actions |

When the request is ambiguous, default to **check** if the operator points at
a landed spec/plan and asks for review before the next writing step. Default
to **decide** if a check return left open calls and the operator wants locks
before BUILD. Default to **charter-lane** if `wavves/` exists and the
operator describes build work with locks already stated (or no open forks).
Default to **bootstrap** if the home is missing.

## Playbook steps

Open the matched playbook file and copy its steps verbatim into your todo list
before adding task-specific items.

- **Bootstrap.** `playbooks/bootstrap.md`
- **Charter lane.** `playbooks/charter-lane.md`
- **Check.** `playbooks/check.md`
- **Decide.** `playbooks/decide.md`
- **Layover.** `playbooks/layover.md`
- **Paragraph tunnel.** `playbooks/paragraph-tunnel.md`
- **Proof-before-accept.** `playbooks/proof-before-accept.md`
- **Rotate.** `playbooks/rotate.md`
- **Pickup.** `playbooks/pickup.md`
- **Proceed.** `playbooks/proceed.md`

A step you skip stays in the list with `skip: <reason>`.

## Leaf skills

| skill | slash | when to reach for directly |
|:------|:------|:---------------------------|
| `wavves-init` | `/wavves-init` | you know you only need home setup |
| `charter` | `/charter` | you know you only need a new lane |
| `mod-check` | `/mod-check` | you know you only need an adversarial spec/plan check |
| `mod-decide` | `/mod-decide` | you know you only need to lock open calls before BUILD |
| `layover` | `/layover` | you only need the workspace preflight audit |
| `mod-rotate` | `/mod-rotate` | you know you only need rotation |

Most operators can type `/wavves` plus the task and let routing handle the rest.

## Lifecycle (spec → BUILD)

For work that starts as a written spec, use the skills in order:

1. **`/mod-check`** — adversarial parallel wave. Verdict `GO` / `REVISE` / `BLOCK`.
2. **`/mod-decide`** — if open product/design calls remain, lock them one at a
   time into `decisions/*.md`. Emit a Locked decisions paste.
3. **`/charter`** — BUILD lane with those locks in `waveset.md`. One feature
   per lane when scopes are disjoint.

Do not skip decide when the check return still has forks a build agent would
have to invent. Do not re-run check to "make decisions." See
`examples/usage.md` → "From check to BUILD".

## Pairing with `/loop`

`/wavves` plus Cursor's `/loop` works for long lanes: charter once, let the
background orchestrator run waves with captured gates, rotate when context fills.
