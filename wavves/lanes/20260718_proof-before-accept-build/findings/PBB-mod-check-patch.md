# PBB-W2d draft — mod-check SKILL.md proof-bar (APPLY IN INT ONLY)

```yaml
wave: PBB-W2d
target: skills/mod-check/SKILL.md
apply_in: PBB-INT
git_actions: none
status: DRAFT — do not apply until O0 unlocks INT
```

## Placement

1. After the **Default parallel lenses** table (four lenses), replace the
   paragraph "Add a fifth lens only when the operator names a domain..."
   with the conditional proof-bar text below.
2. Optionally add a row to a new subsection table for the conditional lens.

## Patch text (replace fifth-lens paragraph)

```markdown
### Conditional fifth lens: proof-bar (PBA-LENS)

Dispatch `<CODE>-W1e` **proof-bar** as a default fifth parallel lens when the
artifact or its waveset Meta sets `proof_required: yes`, or when the
artifact is a product/visitor feature request that will charter an execution
lane. Otherwise keep the four-lens default; operators may still name
proof-bar as an optional fifth domain lens.

| Wave id | Lens | Owns | Hunts for |
|:--------|:-----|:-----|:----------|
| `<CODE>-W1e` | proof-bar | `findings/<CODE>-proof-bar.md` | ACCEPT criteria that can PASS without measuring `proof_job`; chrome-only waves with no frozen proof_job; `proof_reference: none` / `visual_accept: no` without rationale on proof_required:yes; debt-close treated as product done; missing named DOM/host or mechanical proof harness |

proof-bar owns its findings file alone. It does not replace grounding,
contradictions, completeness, or adversarial. Playbook
`skills/wavves/playbooks/proof-before-accept.md` teaches the same hunt for
BUILD lanes.

For research-only, mod-check-of-check, plugin-meta, or outbound-copy-only
artifacts with `proof_required: no` or `n/a`, do not force proof-bar unless
the operator asks.

Other domain fifth lenses (security, perf, migration blast radius) remain
operator-named and stay disjoint from proof-bar ownership.
```

## Also patch Workflow step 6

Where it says "default 4 lenses", change to:

```markdown
- [ ] 6. Dispatch ONE wave of parallel high-reasoning reviewers (default 4
        lenses below; add proof-bar when proof_required: yes or
        product/visitor FR). Background preferred. Do not poll.
```

## Do not

- Make proof-bar silent fifth on every check (PBA-LENS pick B)
- Defer entirely to "or playbook check" (PBA-adversarial FM-4)
- Apply until INT

## Commit file list (after INT applies)

- `skills/mod-check/SKILL.md` (INT only)
