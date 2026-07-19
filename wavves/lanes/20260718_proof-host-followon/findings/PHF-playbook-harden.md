# PHF-W1b — playbook harden

lane: PHF
wave: W1b
date: 2026-07-18 (America/New_York)
repo_state_verified_against: `538437cad76764fd989cd028f64927b1ae839292`
status: discovery complete

## Lock

PHF-SCOPE S2: harden playbook/docs so `visual_accept: yes` ⇒ capture-then-grade
required; DOM green ≠ done. No VPB product-look port. PBB stays shipped.

## Current playbook state (measured)

`skills/wavves/playbooks/proof-before-accept.md` already partially hardened
locally (uncommitted per LOCKED-DECISIONS):

- Named harness mentions DOM/host hard gate + notes DOM green alone is not
  done when `visual_accept: yes`
- Step 8 requires capture-then-grade and says do not treat DOM/host green as
  ACCEPT-complete

## Residual gaps to close in W2b

1. **Cite the real probe path** once shipped:
   `python3 skills/charter/scripts/proof_host_probe.py` (not the old
   contract-only `scripts/proof_host_probe.py` placeholder).
2. **Strengthen mandatory language** for `visual_accept: yes`:
   capture-then-grade is required (frozen captures + independent product-look
   review against `proof_reference`), not optional color.
3. **Keep screenshot miss ≠ blank-canvas hard gate** (DOM/host still required
   for `PROC-BLANK-CANVAS`). Do not collapse the two gates.
4. **Do not add** VPB product-look fail vocab rows (contradicting metrics,
   near-dup alts, overlay-buried paths, reference-class readability) into
   wavves closed fail table — PHF-EVAL parks that in pax VPB.

## EXECUTION_WIRING Rule 2b doc harden (same wave, single editor)

- Replace example command path with `skills/charter/scripts/proof_host_probe.py`
- Remove or rewrite the “If `scripts/proof_host_probe.py` is not yet in-repo”
  fallback once the script exists
- Screenshot subsection: when `visual_accept: yes`, capture-then-grade is
  required; DOM/host green alone is not ACCEPT-complete. Screenshot remains
  never the sole blank-canvas hard gate.

## Out of scope

- Reopening PBB-ACCEPT or rewriting it as failed
- Porting product-look fixture corpus into `evals/`
- Etiquette empty-return note (PHF-ETIQUETTE park)

## Commit file list (this finding)

- `wavves/lanes/20260718_proof-host-followon/findings/PHF-playbook-harden.md`
