# MKK-D3a — copy-in-term

- **Date:** 2026-08-08
- **Lane:** `wavves/lanes/20260808_mod-kick-check/`
- **repo_state_verified_against:** `d327b66`
- **Question:** What surf-native term replaces packaging jargon “vendor” for thin cross-repo file copy into the kick-target?
- **Options considered:**
  - leash / `LEASH_AUTH`
  - daybag / `DAYBAG_AUTH`
  - quiver-in / `QUIVER_AUTH`
- **Pick:** leash / `LEASH_AUTH`
- **Rationale:** Operator chose leash. Kick = leave this break; leash = thin tether of must-have files so the board (kick-target) does not drift without them. Ban “vendor” / `VENDOR_*` in skill, playbook, fail ids, and UX.
- **Implications for BUILD:** Rename throughout FR and implementation: `VENDOR_INTO_*` → `LEASH_INTO_TARGET` (or `leash`), `VENDOR_AUTH` → `LEASH_AUTH`, `PROC-KICK-VENDOR-SILENT` → `PROC-KICK-LEASH-SILENT`, `PROC-KICK-THIN-UNBOUNDED` stays or becomes `PROC-KICK-LEASH-UNBOUNDED`. UX option D uses “leash thin deps.” Docs one-liner: leash ≠ person; means authorized thin copy-in.
