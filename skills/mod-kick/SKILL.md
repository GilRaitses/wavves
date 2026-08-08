---
name: mod-kick
description: >-
  Cross-environment exit: publish lane allowlist to a kick-target repo, write
  a KICK receipt, emit a paste one-liner for another environment. Use for
  /mod-kick, hand to another machine, readback elsewhere. Not /mod-rotate;
  pickup playbook stays rotate-hydrate only.
disable-model-invocation: true
---

# mod-kick

Leave **this** Cursor environment and continue in another agent / machine /
modality that shares **git remotes** (or, with explicit auth, the same
machine only). Publish first. Paste only after publish PASS (or labeled
`LOCAL_ONLY` same-machine).

**Kick ≠ rotate.** `/mod-rotate` + the **pickup** playbook = same-orchestrator
family continuity (`O0.R(N+1)`, rotation file, hydrate). `/mod-kick` =
cross-environment exit for an arbitrary successor. Prefer **kick target** /
**target repo** in UX. Do not route kick cues to rotate (or reverse) without
an explicit dual-invoke ordered publish-kick-then-rotate.

## When to use

Cues: `/mod-kick`, "hand to another environment", "other machine", "readback
elsewhere", "paste for voice / phone / separate workspace".

**Not** for: fresh thread / token velocity / `O0.R(N+1)` → use `/mod-rotate`
and `pickup`.

## Locked decisions (do not reopen)

| Id | Lock |
|---|---|
| D1 | Receipt: `wavves/handoffs/KICK_<YYYYMMDD>_<HHMM>.md` + lane mirror `findings/KICK_RECEIPT.md` |
| D2 | `/mod-kick` utterance = **publish auth** for the **allowlist only** |
| D3a | Copy-in term is **leash** / `LEASH_AUTH` (ban `vendor` / `VENDOR_*` in product text) |
| D3 | Leash thin: ≤8 files AND ≤256 KiB AND no secret globs; else require `MULTI_REPO_AUTH` |
| D4 | `LOCAL_ONLY` = same-machine / shared-FS + `LOCAL_ONLY_AUTH` |
| D5 | Bare shrug / proceed accepts **single-repo default only** (never MULTI / LEASH) |

## Fail ids

| id | Meaning |
|---|---|
| `PROC-KICK-NO-PUBLISH` | Paste claims remote pull while surfaces are local-only / unpushed |
| `PROC-KICK-MULTI-SILENT` | Multi-remote hydration without recorded `MULTI_REPO_AUTH` |
| `PROC-KICK-LEASH-SILENT` | Leash without recorded `LEASH_AUTH` |
| `PROC-KICK-LOCAL-ONLY-ABUSE` | `LOCAL_ONLY` used for cross-env (other machine / no shared FS) |
| `PROC-KICK-WRONG-DEFAULT` | Proposed default ≠ lane `repos:` primary (or sole listed) |
| `PROC-KICK-UNRELATED-PUSH` | Publish outside lane-owned allowlist |
| `PROC-KICK-SECRET-LEAK` | Leash or paste includes `.env*`, credentials, or secret substrings |
| `PROC-KICK-DESKTOP-AUTHORITY` | Desktop / `desktop_staging` cited as kick authority instead of git hash |
| `PROC-KICK-ROTATE-COLLAPSE` | Kick cues routed to rotate (or reverse) without explicit dual-invoke |
| `PROC-KICK-LEASH-UNBOUNDED` | Leash over ≤8 files / ≤256 KiB thin threshold |
| `PROC-KICK-SHRUG-WIDEN` | Bare shrug / proceed accepts MULTI or LEASH without auth lines |

## Default operator UX

```text
/mod-kick

Kick target repo? [default: <lane repos: primary or sole listed>]
  A) accept default (single-repo)
  B) name another single repo
  C) multi-repo (list + MULTI_REPO_AUTH — shrug does NOT accept)
  D) single-repo + leash thin deps (LEASH_AUTH + thin threshold — shrug does NOT accept)

→ publish allowlist → paste one-liner → this environment done for that stream
```

Ask **only** for the kick-target repo by default. Default = lane `repos:`
primary, else sole dirty listed repo, else ask with **no foreign hardcode**.
Bare shrug / proceed may accept **that default only**.

## Workflow

```
- [ ] 1. Resolve kick-target default from the active lane (repos primary / sole).
- [ ] 2. Ask: Kick target repo? Record A/B/C/D. Enforce D5 on shrug.
- [ ] 3. Build publish allowlist: lane-owned paths for this kick stream only.
- [ ] 4. If MULTI: list each remote + hash + why; require MULTI_REPO_AUTH.
- [ ] 5. If LEASH: require LEASH_AUTH; enforce ≤8 files / ≤256 KiB / no secret
        globs; record source hash + paths. Over threshold → refuse leash;
        require MULTI_REPO_AUTH.
- [ ] 6. Publish: stage allowlist only; commit+push under D2 publish auth;
        verify origin sync for the kick-target. Refuse paste until PASS.
        LOCAL_ONLY path: require LOCAL_ONLY_AUTH; paste MUST say same-machine
        and MUST NOT instruct a different-environment pull.
- [ ] 7. Write receipt (D1) + optional lane mirror. Include auth lines,
        allowlist, paste body.
- [ ] 8. Emit paste (≤12 lines / ≤2000 chars). Max contract fields below.
```

### Publish allowlist (KICK-01 / D2)

`/mod-kick` = publish auth **only** for the closed allowlist of lane-owned
paths for this stream. Refuse paths outside that allowlist
(`PROC-KICK-UNRELATED-PUSH`). Do not publish the whole dirty tree.

### LOCAL_ONLY (KICK-01b / D4)

Same-machine / shared filesystem only. Requires `LOCAL_ONLY_AUTH` in the
receipt. Paste must say same-machine and must not tell another environment to
`git pull`. Cross-env claim under LOCAL_ONLY → `PROC-KICK-LOCAL-ONLY-ABUSE`.

### Leash (KICK-04 / D3)

Thin copy-in into the kick-target under `LEASH_AUTH` and the thin threshold.
Deny `.env*`, keys, credentials (`PROC-KICK-SECRET-LEAK`). Product text uses
**leash** / `LEASH_AUTH` only — never `vendor` / `VENDOR_*`.

### Paste contract (KICK-05)

Minimum fields:

1. Kick-target repo identity + full commit hash  
2. Ordered read list **derived from the lane** (artifact types the lane owns;
   not hard-coded foreign names)  
3. Standing locks as applicable  
4. Operator next move  
5. Readback / discuss modality OK  

If `MULTI_REPO_AUTH` or `LEASH_AUTH`: second line cites the receipt path.

Paste body caps: **12 lines** / **2000 chars**.

### Receipt (KICK-06 / D1)

Write `wavves/handoffs/KICK_<YYYYMMDD>_<HHMM>.md` (operator timezone). If an
active lane exists, also mirror `lanes/<lane>/findings/KICK_RECEIPT.md`.

### Desktop authority ban

Git hash on the kick-target remote is authority. Never cite Desktop /
`desktop_staging` as the kick authority (`PROC-KICK-DESKTOP-AUTHORITY`).

### Dual-invoke with rotate

If the operator asks for kick **and** rotate in one breath: publish kick
first, then rotate, or refuse. Silent collapse either way →
`PROC-KICK-ROTATE-COLLAPSE`.

## Rollback

Bad kick → do **not** submit outbound work from the paste. Re-kick after fix.
Optional revert commit is **operator-gated** (ask first).

## Out of scope

- Substitute for `/mod-rotate` / pickup hydrate  
- Auto-submit / outbound send  
- Silent large-tree leash  
- Marketplace / Substack announce packs (O0 owns those)
