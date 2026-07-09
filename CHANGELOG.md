# Changelog

## 0.1.0 (2026-07-08)

- Add `mod-check` (`/mod-check`) and the `check` playbook: one adversarial
  parallel wave against a landed spec or plan, returning `GO` / `REVISE` /
  `BLOCK` with named gaps. Wired into `/wavves` routing and the usage grid.
- Add `mod-decide` (`/mod-decide`) and the `decide` playbook: walk open
  product/design calls after a check return, write `decisions/*.md`, emit a
  Locked decisions paste for BUILD. Document the
  `/mod-check` → `/mod-decide` → `/charter` lifecycle in `examples/usage.md`.
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
