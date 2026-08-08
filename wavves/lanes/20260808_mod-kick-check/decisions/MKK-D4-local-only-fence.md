# MKK-D4 — local-only-fence

- **Date:** 2026-08-08
- **Lane:** `wavves/lanes/20260808_mod-kick-check/`
- **repo_state_verified_against:** `d327b66`
- **Question:** When publish cannot complete, may kick emit a LOCAL_ONLY paste?
- **Options considered:**
  - A: Yes — same-machine / shared-FS only; `LOCAL_ONLY_AUTH`; paste must not claim cross-env pull
  - B: No LOCAL_ONLY — refuse paste until remote publish succeeds
- **Pick:** A
- **Rationale:** Operator chose A. Same-box thread hops stay possible; cross-env abuse is a named fail.
- **Implications for BUILD:** Implement KICK-01b. Fixture `PROC-KICK-LOCAL-ONLY-ABUSE`. Cross-env wording in a LOCAL_ONLY paste = FAIL.
