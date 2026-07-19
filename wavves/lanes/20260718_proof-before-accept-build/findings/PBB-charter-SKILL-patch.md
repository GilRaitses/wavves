# PBB-W2c draft — charter SKILL.md patch (APPLY IN INT ONLY)

```yaml
wave: PBB-W2c
target: skills/charter/SKILL.md
apply_in: PBB-INT
git_actions: none
status: DRAFT — do not apply until O0 unlocks INT
```

## Placement

In **waveset.md is the authority doc. Sections, in order.** after the bullet
that lists lane code, owner, type, `repo_state_verified_against`, insert a
new bullet (and keep surrounding prose style).

## Patch text (insert)

```markdown
- **`proof_required: yes|no|n/a`** (required Meta field). Explicit classifier;
  never infer from prose keywords. Defaults guidance: visitor/product
  execution lanes → `yes`; mod-check / research-discovery / plugin-meta /
  outbound-copy-only → `no` or `n/a` with one-line rationale. When
  `proof_required: yes`, the waveset MUST also declare:
  - `proof_job` — one operator-facing sentence naming the Proof to measure
  - `proof_reference` — path, URL, or figure class; `none` only with written
    rationale
  - `chrome_freeze` — non-proof-serving path/surface list plus an explicit
    proof-serving allowlist (edits outside the allowlist before Proof ACCEPT
    are thrash)
  - `visual_accept` — `yes` or `no`; `no` requires written rationale
  Acceptance criteria on such lanes MUST name a runnable proof gate
  (mechanical fixture checker and/or DOM/host harness with JSON capture).
  Process-only gates (LAND-C, honesty labels, e2e shell, HEAD match) are
  insufficient alone. See playbook
  `skills/wavves/playbooks/proof-before-accept.md` and
  `EXECUTION_WIRING.md` proof-host rule.
```

## Also patch Acceptance criteria bullet (same file)

Where acceptance criteria are described as "hard, checkable, no reassurance
bias", append one sentence:

```markdown
On `proof_required: yes` lanes, acceptance is incomplete unless the named
`proof_job` is measured (capture under `gate-captures/`); docs-only or
process-only green is a FAIL (`PROC-PASS-NO-PROOF`).
```

## Do not

- Create `/proof-gate` skill
- Edit this target until INT
- Soften with "or playbook check" escape for mod-check (lens lands in mod-check patch)

## Commit file list (after INT applies)

- `skills/charter/SKILL.md` (INT only)
- this draft remains historical
