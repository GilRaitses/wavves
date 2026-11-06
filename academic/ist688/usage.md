# Published usage

These are prompt shapes from the public listing and the repository README. They are not measured runs. The README says the paths and metrics in `examples/usage.md` are fictional. That file is not in this repository.

## Listing session

The listing's example session prompt:

```text
/wavves charter a lane named docs-sweep for the public docs refresh and run a first /mod-check on the written plan
```

The listing says that session chartered the lane, wrote `waveset.md`, ran a read-only review wave and left the build step unstarted.

## README prompt shapes

```text
/wavves set up in this repo, then audit our README for drift.
/mod-check the landed spec.
/mod-decide lock the open calls.
/wavves hydrate from the rotation paste and tell me what's active.
```

## Skills

| Skill | When the sources say to use it |
|:------|:-------------------------------|
| `/wavves` | Default entry. Matches a playbook and runs it. |
| `/wavves-init` | Home setup only. |
| `/charter` | Charter a lane and dispatch waves behind gates. |
| `/mod-check` | Read-only review of a landed spec or plan. |
| `/mod-decide` | Lock open calls before a build charter. |
| `/layover` | Read-only audit of a multi-root workspace. |
| `/mod-rotate` | Hand a heavy thread to the next moderator term. |
| `/mod-kick` | Move to another machine with an allowlist and a short paste. |
| `/shrug` | Carry out recommended actions from a verdict. |
| `/remeasure` | Listing name for turning a done claim into a rerunnable gate. |

`/set-key` is in the README as a local secret helper. It is omitted here so this reading carries no key name and no setup command for a secret.

## Two orders

The README gives the spec to build order as `/mod-check`, then `/mod-decide`, then `/charter`.

The listing gives the heavy-thread order as a rotation file, then the pickup check, then a remeasure of `gate-captures`.

The charts for those orders are in the PDF. The chart of the files a fresh term reads is there too.
