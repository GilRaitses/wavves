# Changelog

## 0.0.1 (2026-07-08)

- Add `mod-check` (`/mod-check`) and the `check` playbook: one adversarial
  parallel wave against a landed spec or plan, returning `GO` / `REVISE` /
  `BLOCK` with named gaps. Wired into `/wavves` routing and the usage grid.
- Fix the `/mod-rotate` one-line paste to lead with an explicit `/wavves`
  invocation, since every skill disables description-based auto-invocation
  and the paste previously carried no literal slash command.

## 0.0.0 (2026-07-06)

- Initial package. Four skills (`wavves`, `wavve`, `charter`, `mod-rotate`),
  playbooks, execution wiring doc, transition-gap probe script and usage
  examples.
