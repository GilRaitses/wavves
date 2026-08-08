# MKK-D2 — commit-publish-protocol

- **Date:** 2026-08-08
- **Lane:** `wavves/lanes/20260808_mod-kick-check/`
- **repo_state_verified_against:** `d327b66`
- **Question:** How does `/mod-kick` get commit/push auth under house commit-when-asked?
- **Options considered:**
  - A: `/mod-kick` utterance = publish auth for allowlisted kick surfaces only
  - B: Always emit commit plan and wait; paste gated until operator lands push
  - C: Per-repo protocol matrix
- **Pick:** A
- **Rationale:** Operator: "oh yeah A". Product is publish-first; the invocable is the ask; allowlist keeps unrelated dirty trees out.
- **Implications for BUILD:** KICK-01 may commit+push allowlisted paths when `/mod-kick` is invoked. Must still FAIL `PROC-KICK-UNRELATED-PUSH` if staging escapes the allowlist. Do not implement plan-first (B) or a repo-class matrix (C) in v0.
