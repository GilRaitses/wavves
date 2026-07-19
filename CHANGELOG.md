# Changelog

## 0.3.0 (2026-07-18)

Disk-gate framing. Proof-before-accept. Paragraph tunnel. Honest layover scope.

- **proof-before-accept:** charter `proof_required` fields; process-only
  ACCEPT cannot clear product lanes; host probe
  `skills/charter/scripts/proof_host_probe.py` (self-check); playbook +
  `evals/check_proof_before_accept.py`.
- **paragraph-tunnel:** mid-render structural gate for one outbound field;
  playbook + `evals/check_paragraph_tunnel.py` (no slash skill in v0).
- **layover:** keep the audit; document the known cloud boundary (single-repo
  cloud agents; no autoconfig / multi-root migration). Soften marketplace
  keyword; public copy frames layover as an audit with a stated cloud boundary.
- **Public surfaces:** README, `index.html`, `examples/usage.md`, plugin
  version bump to `0.3.0`. Preferred framing: advances only after a disk
  gate capture.

## 0.2.0 (2026-07-12)

Lane authority sync (AUTH-01–AUTH-10), from KLR mod-decide → mod-check run:

- **mod-decide:** authority sync hook (waveset + dispatch-w{N} + registry);
  recommended_actions on complete.
- **mod-check:** scoped verdict schema (`blocks_w2`…`blocks_w5`); mandatory
  gate before W2 when waveset stale; batch reconcile; recommended_actions.
- **charter:** `dispatch-w{N}.md` convention; authority precedence block;
  multi-repo lane profile; evidence ledger delta; batch reconciliation.
- **wavves:** `proceed` playbook for `/wavves proceed` and "proceed as
  recommended".
- Registry optional fields: `active_dispatch`, `depends_on`, `conflicts_with`,
  `mod_decide_complete_at`, `waveset_synced_at`.
- **Usage grid** (`index.html`), README, and `examples/usage.md` updated for
  proceed, authority sync, and existing `/layover` playbook.
- **Public copy gates:** `evals/check_public_copy.py` and
  `docs/public-copy-gates.md` (universal prose); `docs/purpose-gates.md`
  (wavves story fidelity).

Evidence: `lane-authority-sync-v1` (KLR thread 2026-07-11/12).

## 0.1.0 (2026-07-08)

- Add `mod-check` (`/mod-check`) and the `check` playbook: one adversarial
  parallel wave against a landed spec or plan, returning `GO` / `REVISE` /
  `BLOCK` with named gaps. Wired into `/wavves` routing and the usage grid.
- Add `mod-decide` (`/mod-decide`) and the `decide` playbook: walk open
  product/design calls after a check return, write `decisions/*.md`, emit a
  Locked decisions paste for BUILD. Document the
  `/mod-check` → `/mod-decide` → `/charter` lifecycle in `examples/usage.md`.
- Add `layover` (`/layover`) and the `layover` playbook: read-only preflight
  audit of a bespoke multi-repo `.code-workspace` before a cloud agent takes
  over. `evals/run_fixtures.py` regression gate for skill edits.
- Document mid-queue decide picks: invoke `/mod-decide` once to start the
  queue; answer `Pick: …` in the same thread without re-slashing.
- Fix the `/mod-rotate` one-line paste to lead with an explicit `/wavves`
  invocation, since every skill disables description-based auto-invocation
  and the paste previously carried no literal slash command.
- Rename `/wavve` to `/wavves-init` to remove the one-letter collision with
  `/wavves`. Bumped to 0.1.0 (new feature plus a renamed public command).

## 0.0.0 (2026-07-06)

- Initial package. Four skills (`wavves`, `wavves-init`, `charter`, `mod-rotate`),
  playbooks, execution wiring doc, transition-gap probe script and usage
  examples.
