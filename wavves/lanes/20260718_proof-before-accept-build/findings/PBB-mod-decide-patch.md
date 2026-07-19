# PBB-W2d draft — mod-decide AUTH sync for proof_job (APPLY IN INT ONLY)

```yaml
wave: PBB-W2d
target: skills/mod-decide/SKILL.md
apply_in: PBB-INT
git_actions: none
status: DRAFT — do not apply until O0 unlocks INT
```

## Placement

In workflow **Step 5b. Authority sync (AUTH-01)**, after the existing
bullets that patch waveset / dispatch / registry, append proof sync
requirements.

## Patch text (append under step 5b)

```markdown
        - **Proof fields (PBA-LAND E).** When the feature or check lane will
          charter an execution lane with visitor/product surface, ensure
          Locked decisions and the synced `waveset.md` carry
          `proof_required: yes|no|n/a`. If `proof_required: yes`, AUTH sync
          FAILS (block BUILD unlock / W2 dispatch) until `proof_job` appears
          in the Locked decisions paste and in `waveset.md` Meta, along with
          `proof_reference`, `chrome_freeze` (freeze list + proof-serving
          allowlist), and `visual_accept` (with rationale if `no` or if
          `proof_reference: none`). Dropping `proof_job` from the paste after
          decide is a sync failure, not a soft warning.
```

## Also patch "Recommended next charter shape"

Add bullet:

```markdown
- `proof_required` and, when `yes`, `proof_job` (+ three companion fields)
  present in Locked decisions and waveset Meta before BUILD dispatch
```

## Do not

- Re-open PBA locks
- Charter BUILD inside mod-decide
- Apply until INT

## Commit file list (after INT applies)

- `skills/mod-decide/SKILL.md` (INT only)
