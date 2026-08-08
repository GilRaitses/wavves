# MKK-W1b — contradictions

- **Lens:** contradictions
- **Artifact:** `feature-requests/20260808_mod-kick.md` (working-tree; uncommitted at check)
- **Repo verified against:** `b7ce95f075e89183a49e0486b6764ec299aeecac` (`wavves_build` `main`)
- **Hydrated:** waveset.md, dispatch.md, full FR, `skills/mod-rotate/SKILL.md`, `skills/wavves/SKILL.md` + proceed/rotate/pickup playbooks, FR open calls, `feature-requests/20260723_proceed-all-standing.md` (shrug/proceed widen lock)
- **Lens lean:** **REVISE**

## Verdict in one line

Product split kick≠rotate is stated and alias rejected, but several internal forks (LOCAL_ONLY vs NO-PUBLISH, shrug-as-default-accept, publish-first vs commit-when-asked, plural “remotes”, vendor↔multi exclusion) must be locked or the BUILD agent invents policy.

---

## C1 — Kick vs rotate: no hard collapse; soft seams remain

**Evidence**

- FR Problem + Explicit non-goals + Where-it-lands option C **reject** `/mod-rotate --kick` (FR L34–37, L87–90, L102).
- KICK-07: document rotate = same O0 family continuity; kick = cross-environment exit (FR L58).
- waveset Locked: “distinguish kick vs mod-rotate; do not collapse products.”
- `mod-rotate`: successor term `O0.R(N+1)`, rotation file / five-file handoff, paste leads with `/wavves hydrate…` (`skills/mod-rotate/SKILL.md`).
- FR kick paste: pull repo @ hash + read-order; **no** term assignment (non-goals).

**Finding**

Not a product collapse. Soft risks that can still confuse routing/BUILD:

1. **Shared “one-liner paste + leave thread” shape** without a router leave-act row yet — ambiguous requests (“hand this off to another agent”) may still route to **rotate** (`skills/wavves/SKILL.md` rotate row / pickup playbook step 8 “If they asked to rotate”).
2. FR non-goal hedges “no rotation file shape **unless operator also rotates**” (FR L89–90) — invites a combined kick+rotate path without a defined order (publish? term? paste?).
3. Vocabulary clash: existing **pickup** playbook = resume from **rotation**; FR **pickup repo** = remote successor hydration target. Same word, different products.

**Gap:** `GAP-KICK-ROTATE-ROUTE` — name kick triggers vs rotate triggers; forbid silent combined path or define sequenced dual-invoke; rename or qualify “pickup repo” vs rotation pickup.

**Severity:** medium (clarify, not rewrite product).

---

## C2 — Single-repo default vs multi-repo-by-default wording

**Evidence**

- Originating mod feedback: “ask only for pickup repo (default single); multi-repo allowed only with clear auth” (FR L19–22).
- KICK-02 / Default UX: single question; options A/B single, C multi with auth (FR L53–54, L61–70).
- KICK-03 / PROC-KICK-MULTI-SILENT: multi only after explicit auth (FR L42–43, L54–55).
- **Leak:** KICK-01 “**push** pickup **remotes**” (plural) + “verify `origin` sync” without scoping to the chosen single pickup (FR L52).
- UX example default hardcodes `applications-for-jobs` (FR L66) — foreign-repo illustration baked into default UX copy (dispatch warned not to hard-depend on apps paths).

**Finding**

Intent is single-default / multi-opt-in. Draft text still reads multi-capable by default at publish time (“remotes”) and seeds a foreign default identity. That fights KICK-02 and the originating single-question UX.

**Gap:** `GAP-KICK-SINGLE-DEFAULT-WORDING` — rephrase KICK-01 to “push the **chosen** pickup remote (singular) unless MULTI_REPO_AUTH”; default proposal rule without baking a foreign repo name into the product contract.

**Severity:** medium.

---

## C3 — Publish-first vs “commit only when asked” (open call #2 unresolved while KICK-01 asserts both)

**Evidence**

- KICK-01: **publish first**; commit if protocol allows **or** emit commit plan + wait; refuse paste until publish PASS (FR L52).
- Acceptance: paste refuses (or LOCAL_ONLY) when not on remote (FR L109).
- Open call #2: auto-commit under apps-style push-to-main **vs** always emit plan when protocol is “commit only when asked”? (FR L116).
- House router non-negotiable #4: no commit/push unless operator asks or governance grants (`skills/wavves/SKILL.md` L28–29).
- `mod-rotate` / rotate playbook: return commit plan; commit only when asked or governance grants (`skills/mod-rotate/SKILL.md` L57–60, L83–86; `playbooks/rotate.md` L12–13).
- Kick is **more aggressive** than rotate: publish is the product, not optional continuity.

**Finding**

Open call #2 is load-bearing, but KICK-01 already commits to “publish first” as a non-negotiable. That is an internal fork: either kick **is** authorized mutation (and must say how `/mod-kick` itself counts as ask / governance), or kick must **stop at commit plan** and cannot refuse paste on unpushed state without waiting — which collapses the fail model.

**Gap:** `GAP-KICK-COMMIT-PROTOCOL` — lock before BUILD: (a) `/mod-kick` utterance = publish auth for listed surfaces, or (b) plan-first always when commit-when-asked, paste gated until operator lands, or (c) protocol matrix per repo class. Do not leave “commit if protocol allows” as agent judgment.

**Severity:** **high** (blocks coherent KICK-01 / evals).

---

## C4 — LOCAL_ONLY vs `PROC-KICK-NO-PUBLISH`

**Evidence**

- Fail id: paste emitted while pickup paths are local-only / unpushed → `PROC-KICK-NO-PUBLISH` (FR L39–40).
- KICK-01: refuse paste until publish PASS **or operator overrides with `LOCAL_ONLY` labeled paste** (FR L52).
- Acceptance: “Paste refuses **(or LOCAL_ONLY-labels)** when pickup not on remote” (FR L109).
- KICK-08 fixture: “paste without push → FAIL `PROC-KICK-NO-PUBLISH`” — **no LOCAL_ONLY carve-out** (FR L59).
- Explicit non-goal: “kick authority is **git-published** pickup” (FR L91–92).

**Finding**

Three incompatible readings:

1. LOCAL_ONLY paste is a **PASS override** (labeled); fail id does not fire.
2. LOCAL_ONLY paste is still a **FAIL** of the fail id (label only warns) — then “override” wording is false.
3. LOCAL_ONLY is allowed but **non-authoritative** / same-machine only (rotate’s local-handoff pattern) — FR never states machine-scope or successor-visibility rule.

Non-goal “authority is git-published” contradicts an allowed unlabeled-success LOCAL_ONLY path unless LOCAL_ONLY is explicitly **non-authority** and out of kick’s success criteria.

**Gap:** `GAP-KICK-LOCAL-ONLY-FAIL-MODEL` — define: when LOCAL_ONLY may be emitted; whether it trips `PROC-KICK-NO-PUBLISH`; whether ACCEPT/shipped kick may end in LOCAL_ONLY; eval fixture must match. Prefer: unlabeled unpushed paste = FAIL; LOCAL_ONLY = operator-gated exception that is **not** “publish PASS” and is scoped same-machine / non-cross-env.

**Severity:** **high**.

---

## C5 — Vendor vs multi-repo: auth named, mutual exclusion incomplete

**Evidence**

- UX options C (multi-repo) and D (vendor thin deps) listed as alternatives (FR L67–70).
- KICK-03 MULTI_REPO_AUTH; KICK-04 VENDOR_INTO_PICKUP + VENDOR_AUTH; fail ids MULTI-SILENT / VENDOR-SILENT (FR L54–56, L42–46).
- Non-goal: not silent vendoring of **large** trees; thin only else multi-repo auth (FR L94).
- Open call #3: max size / file-count for “thin deps” — **unset** while KICK-04 is a non-negotiable (FR L117, L57).
- Paste optional second line if MULTI_REPO_AUTH **or** VENDOR_AUTH (FR L85) — allows both tokens, does not forbid both.

**Finding**

Auth lines exist; **exclusion and order do not**:

1. Can operator take C and D in one kick? (vendor some paths + still list another remote?)
2. After successful vendor, is secondary remote **forbidden** in the paste (should be single-repo) — not stated as hard rule.
3. KICK-04 “**offer** VENDOR_INTO_PICKUP” when thin deps detected — may auto-steer into D without the single question staying single (widens UX beyond “Pickup repo?”).
4. Vendor copies into pickup lane then still requires publish of those copies — interaction with C3/C4 unstated (vendor then LOCAL_ONLY?).
5. “Thin” is undefined → PROC-KICK-VENDOR-SILENT cannot be evaluated mechanically until open call #3 locks.

**Gap:** `GAP-KICK-VENDOR-MULTI-EXCLUSION` — lock: C XOR D; post-vendor paste must be single-repo; offer vs ask; thin threshold numbers; vendor implies publish of vendored paths in pickup remote before paste (unless LOCAL_ONLY rule from C4).

**Severity:** **high** for thin threshold + XOR; medium for offer-vs-ask.

---

## C6 — Shrug / proceed widening

**Evidence**

- KICK-02: “Operator may accept default with **shrug / proceed**” (FR L53–54).
- Dispatch HYDRATE note: `20260723_proceed-all-standing.md` — “**do not widen kick into shrug**” (`dispatch.md`).
- Standing house rule: bare `¯\_(ツ)_/¯` / bare `/shrug` → AUTH-10 **recommended_actions only**; widen to all-standing only on closed phrases (`playbooks/proceed.md`; FR-20260723 PS-06; `PROC-PROCEED-SHRUG-WIDEN`).
- Router proceed row: bare shrug stays AUTH-10 (`skills/wavves/SKILL.md` L46).

**Finding**

Binding shrug/proceed to “accept kick pickup-repo default” **widens** shrug semantics inside `/mod-kick` beyond AUTH-10 proceed. Conflicts with dispatch instruction and with shipped proceed-all-standing locks. Ambiguity if a verdict’s `recommended_actions` are also live: shrug might mean accept kick default **and/or** run AUTH-10 lands (including unrelated commits).

**Gap:** `GAP-KICK-SHRUG-SEMANTICS` — do **not** overload shrug. Accept default via explicit A / “yes” / “default” / empty-accept inside kick prompt; leave shrug = AUTH-10 proceed only. If kick wants one-key accept, invent a kick-local token, not shrug.

**Severity:** **high** (cross-product regression risk).

---

## C7 — Other internal tensions (named, secondary)

| id | tension | evidence |
|---|---|---|
| `GAP-KICK-RECEIPT-HOME` | Open call #1 (lane vs `wavves/kicks/`) vs KICK-06 already allowing both | FR L115 vs L57 |
| `GAP-KICK-PASTE-SLASH` | Rotate paste **requires** leading `/wavves` because skills are `disable-model-invocation`; kick paste is free-form successor instruction with no slash contract | `mod-rotate` L67–70 vs FR paste contract L75–83 |
| `GAP-KICK-DONE-STREAM` | “this environment done for that stream” vs no fence rules (rotate has outgoing-term fence); kick does not say whether O0 may keep committing after paste | FR L72 vs `mod-rotate` Concurrent terms |
| `GAP-KICK-OPEN-VS-NN` | Open calls #1–3 still open while Acceptance requires KICK-01…08 non-negotiables shipped | FR L104–111 vs L113–117 |

Secondary gaps are decide-time; they reinforce REVISE, not alone BLOCK.

---

## What is *not* contradictory

- Rejecting option C alias (`/mod-rotate --kick`) is consistent with the Problem statement.
- Multi-repo **opt-in with auth** is consistent with single-default **if** C2 wording leak is fixed.
- Preferring vendor-to-collapse thin deps under auth is consistent with originating feedback **once** thin threshold + XOR with multi are locked.

---

## Lens lean

**REVISE** — not BLOCK: kick≠rotate is intentional and documented; salvageable with decide locks.

**Must lock / fix before BUILD (blocking for this lens):**

1. `GAP-KICK-COMMIT-PROTOCOL` (C3)
2. `GAP-KICK-LOCAL-ONLY-FAIL-MODEL` (C4)
3. `GAP-KICK-VENDOR-MULTI-EXCLUSION` + thin threshold (C5)
4. `GAP-KICK-SHRUG-SEMANTICS` (C6)

**Should fix in FR revise (non-blocking alone):**

5. `GAP-KICK-SINGLE-DEFAULT-WORDING` (C2)
6. `GAP-KICK-ROTATE-ROUTE` / pickup vocabulary (C1)
7. Receipt-home open call alignment (C7)

**Not GO:** open forks would force BUILD invention on publish auth, fail-id semantics, and shrug.

---

## Cite honesty

Artifact under review is **working-tree / uncommitted** per waveset (`landing_commit_hash: n/a`). Seams cited from published HEAD `b7ce95f…`. No code edits outside this findings file; no commits by this lens.
