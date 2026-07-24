# KVC-W1d — adversarial (failure modes / unsafe defaults)

```yaml
lens: adversarial
wave_id: KVC-W1d
role: charge_worker
tip: de75b4c4118c78dcc0164fdaa916bbc53f99225f
artifact: feature-requests/20260723_wave-context-kv-cache.md
verdict_lean: REVISE
git: none
build: none
skill_edits: none
model: cursor-grok-4.5-high-fast
```

## Remasure (live disk at write)

| fact | measured |
|---|---|
| `wavves/rotations/` | empty (0 files) |
| INDEX `current_rotation` | `none` |
| INDEX `current_identity` | `O0` (bare; no `.R1`) |
| `evals/check_wave_context_kv_cache.py` | absent |
| HF blog | external analogy only (not a product requirement) |

RTH-SYNTHESIS honesty constraint (illustration): disk + INDEX win over
continuity prose; do not claim live multi-term hydration while rotations are
empty. Same constraint applies to this FR's KV-03 / hydrate path.

## Verdict lean

**REVISE** — wire scope and named fail ids are usable for `/mod-decide`, but
alias bind semantics, three open calls, and eval runnability gaps make a
GO-to-BUILD path unsafe if left unlocked. Not BLOCK: problem seams match
WOF/PAS/mod-rotate evidence; bans and non-goals are stated.

## Failure modes

### FM-KVC-01 — resume without checkpoint (chat as K/V)
- **Severity:** high
- **Evidence:** Artifact problem §1; WOF `PROC-ORCH-NO-RESUME-CONTRACT` +
  `yield_awaiting_children` requires `findings/<wave>-orch-checkpoint.md`;
  WOF resume contract Mechanism B. Artifact also names
  `PROC-KV-RESUME-NO-CACHE` for integrate without readable checkpoint/rollup.
- **Mode:** Orch yields or host ends the Task; O0 or a resumed orch rebuilds
  charge table / next integrate step from chat memory and labels that rebuild
  "context cache." That is standard inference without cache (artifact locked
  sentence), not a durable K/V load.
- **Happy-path gap:** KV-01 mandates schema fields but does not name a
  resume gate that refuses work when checkpoint path is missing or unreadable
  (only FAIL ids). BUILD that documents schema without a hard stop still
  allows chat resume.

### FM-KVC-02 — proceed invents inventory from chat, labeled as cache
- **Severity:** high
- **Evidence:** PAS `PROC-PROCEED-CHAT-INVENTORY` and
  `PROC-PROCEED-STALE-QUEUE`; artifact KV-02 / `PROC-KV-STANDING-STALE` binds
  stale only.
- **Mode:** Operator says all-standing; agent invents rows from transcript,
  writes a standing file after the fact, and cites KV-02 "standing file is
  the program cache" as if invent-then-persist were remasure.
- **Gap:** Artifact binds KV standing FAIL to PAS **stale**, not to
  **chat-inventory**. A pass that invents then immediately writes a fresh
  file can dodge `PROC-KV-STANDING-STALE` while still violating PAS chat
  inventory. Unsafe default if CTX-KV evals only cover stale.

### FM-KVC-03 — hydrate / continuity claim with empty rotations
- **Severity:** high (live today)
- **Evidence:** Remasure above; RTH-SYNTHESIS fact row; artifact
  `PROC-KV-ROTATION-EMPTY-CLAIM`; mod-rotate: "Follow the section shape of
  the newest existing file in `rotations/`" with no empty-dir branch in the
  installed skill.
- **Mode:** Successor paste or hydrate prose claims continuity from rotation
  cache while INDEX says `current_rotation: none` and `rotations/` is empty.
  Same honesty fail RTH-W1e already flagged for DS/continuity language.
- **BUILD footgun if GO wrongly:** KV-03 / ROTATION-TEMPLATE stay open;
  BUILD lands visitor "context cache" wording without a first-write fence;
  installed mod-rotate still points at "newest existing file" with zero
  files → shape invented from chat.

### FM-KVC-04 — isomorphism / RotatE vocabulary leak
- **Severity:** medium-high
- **Evidence:** Artifact inspiration + non-goals + `PROC-KV-ISOMORPHISM-CLAIM`
  + KV-04; waveset ban; RTH-SYNTHESIS "not RotatE / not transformer KV
  isomorphism"; HF blog is analogy-only.
- **Mode:** Visitor README or skill text drops the word **analogy**, claims
  "we implement KV cache," Raft isomorphism for checkpoint, or RotatE for
  `/mod-rotate`. CACHE-NAME open call unlocked → product term may ship as
  bare "KV cache" without the analogy fence.
- **Unsafe default:** Treating the HF blog as a product requirement (tensor
  shapes, `use_cache`, attention math). Artifact non-goals forbid that; BUILD
  copy writers can still import blog vocabulary.

### FM-KVC-05 — fail-id alias / bind loopholes
- **Severity:** medium-high
- **Evidence:** Artifact fail table: `PROC-KV-YIELD-NO-CACHE` "alias/bind to
  WOF `PROC-ORCH-NO-RESUME-CONTRACT`"; standing "bind PAS stale"; no
  dual-emit, precedence, or eval-binding rule.
- **Modes:**
  1. Eval emits only WOF id → CTX-KV fixture marked PASS though
     `PROC-KV-*` never appears.
  2. Eval emits only `PROC-KV-*` → WOF mechanical suite does not see the
     yield-without-checkpoint case (split-brain).
  3. Alias treated as "either id satisfies" without requiring the checkpoint
     path remasure → string swap without behavior.
- **Need before BUILD:** one sentence lock: dual-bind (both ids) vs rename
  (single canonical) vs CTX-KV eval asserts WOF id only.

### FM-KVC-06 — open calls left unlocked make BUILD unsafe
- **Severity:** high for BUILD sequencing; medium for check→decide
- **Evidence:** Artifact open calls CACHE-NAME, WOF-BIND, ROTATION-TEMPLATE;
  INDEX: WOF / WOFB **completed/shipped**; PAS revised-after-PAS, PASB
  chartered; artifact Next: BUILD after WOF/PAS land status remasured.
- **Modes:**
  - **WOF-BIND** defaulted to "land inside WOF BUILD" after WOF already
    shipped → silent reopen or no-op land that claims seam closed.
  - **CACHE-NAME** unlocked → FM-KVC-04 visitor leak.
  - **ROTATION-TEMPLATE** unlocked → FM-KVC-03 empty-dir invent.
- **Rule:** GO for check may still require `/mod-decide` on all three before
  any CTX-KV BUILD charter. Unlocking none of them is a BUILD footgun.

### FM-KVC-07 — proposed evals not runnable yet / soft gates
- **Severity:** medium
- **Evidence:** KV-05 names `evals/check_wave_context_kv_cache.py` + fixture
  cases; file absent under `evals/`. WOF already has mechanical
  `wave-orch-fanout-no-resume` / launch-and-exit fixtures; PAS evals named
  but not this seam's suite.
- **Gate runnability notes:**

| proposed fixture | runnable today? | note |
|---|---|---|
| yield-without-checkpoint FAIL | pattern exists in WOF | CTX-KV suite must exist or explicitly reuse WOF fixture + bind rule (FM-KVC-05) |
| resume-with-checkpoint PASS | blocked until schema lock | KV-01 lists fields; no fixture schema file / required keys table |
| standing stale FAIL | pattern named in PAS | must remasure live registry/dispatch; chat-inventory case not listed in KV-05 |
| empty rotations + hydrate-claim FAIL | mechanical | path: INDEX `current_rotation: none` + empty dir + claim string |
| RotatE / isomorphism phrasing FAIL | string/review | easy to soft-pass if only one banned phrase listed; need closed phrase list + analogy-required positive case |

- **Happy-path-only risk:** Suite ships only PASS resume + PASS remasure;
  omits chat-inventory, alias dual-bind, and empty-rotation claim.

### FM-KVC-08 — tip / checkpoint stale at resume (secondary)
- **Severity:** medium
- **Evidence:** KV-01 wants tip hash in checkpoint; WOF resume is
  notify-driven; AGENTS/cross-actor: live repo state governs.
- **Mode:** Resume loads checkpoint tip from yield time; HEAD moved; charge
  returns applied against wrong tip without remasure → false "cache hit."
- **Gap:** Artifact does not say tip mismatch → remasure or FAIL before
  integrate.

### FM-KVC-09 — BUILD expands into PUO/IPB/MDA or auto-BUILD WOF/PAS
- **Severity:** medium (scope poison)
- **Evidence:** Artifact non-goals; waveset bans; Next line mentions WOF/PAS
  land remasure (dependency check, not this folder BUILD).
- **Mode:** Charter author treats CTX-KV as umbrella and edits PUO/IPB/MDA
  or reopens shipped WOF skill text beyond checkpoint bind. Out of scope for
  this lens to grade those FRs; flag only as BUILD footgun if GO wrongly
  authorizes a wide charter.

## Unsafe defaults / happy-path gaps (rollup)

1. Standing file treated as always-valid cache without invalidate+rewrite
   remasure (PAS stale).
2. Chat transcript treated as K/V when checkpoint / standing / rotation
   artifacts missing.
3. "Newest rotation file" hydration with empty `rotations/` (installed
   mod-rotate).
4. HF blog patterns copied into product acceptance.
5. Alias "bind" satisfied by renaming fail strings without checkpoint or
   remasure behavior.
6. WOF-BIND assumed closed because WOF shipped, without a separate CTX-KV
   land or explicit bind patch list.

## Gates that cannot run (until decide/BUILD)

- Full `check_wave_context_kv_cache.py` (absent).
- Resume PASS fixture without locked checkpoint schema keys.
- Closed isomorphism gate without CACHE-NAME + banned-phrase list.
- Honest "seam shipped" claim while WOF-BIND and ROTATION-TEMPLATE open.

## Open calls that must lock before BUILD

| call | unsafe if left open |
|---|---|
| CACHE-NAME | visitor isomorphism / bare "KV cache" |
| WOF-BIND | land against already-shipped WOF or claim closed with no patch |
| ROTATION-TEMPLATE | empty-dir hydrate invent; skill vs `_template.md` drift |

## Scope obedience

- Did not treat FR as transformer KV isomorphism or RotatE.
- Did not expand PUO / IPB / MDA.
- Did not grade other KVC lenses or write verdict.
- HF blog used as external analogy pointer only.

## no-git

Charge worker KVC-W1d: no git. no commit. no push. Commit file list for
orchestrator only:

```text
wavves/lanes/20260723_wave-context-kv-cache-check/findings/KVC-adversarial.md
wavves/lanes/20260723_wave-context-kv-cache-check/findings/KVC-W1d-return.md
```
