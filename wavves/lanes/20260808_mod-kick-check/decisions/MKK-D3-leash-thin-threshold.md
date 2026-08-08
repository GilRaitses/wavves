# MKK-D3 — leash-thin-threshold

- **Date:** 2026-08-08
- **Lane:** `wavves/lanes/20260808_mod-kick-check/`
- **repo_state_verified_against:** `d327b66`
- **Question:** How large may an authorized leash (thin copy-in into kick-target) be in v0?
- **Options considered:**
  - A: ≤8 files AND ≤256 KiB AND no secret globs; else require multi-repo
  - B: No leash in v0
  - C: ≤3 files / 64 KiB
- **Pick:** A
- **Rationale:** Operator accepted lean. Leash ships in v0 with a measurable bar; over threshold refuses leash and requires MULTI_REPO_AUTH.
- **Implications for BUILD:** KICK-04 implements leash with those caps. Fail `PROC-KICK-LEASH-UNBOUNDED` (ex-THIN-UNBOUNDED) when auth present but over cap. Fail `PROC-KICK-LEASH-SILENT` (ex-VENDOR-SILENT) when copy-in without `LEASH_AUTH`. Secret globs still `PROC-KICK-SECRET-LEAK`.
