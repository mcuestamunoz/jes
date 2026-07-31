# AGENTS.md

## Cursor Cloud specific instructions

This repository is the **JARVIS Engineering System (JES)** — a tool-independent
engineering *methodology*, not a software application. It contains only Markdown
documents (`README.md`, `SYSTEM_DEFINITION.md`, `CHANGELOG.md`, and the `docs/`,
`integrations/`, `prompts/`, `rules/`, `templates/`, and `workflows/` trees) plus
one PDF under `docs/`.

Key implications for agents working here:

- There is **no application to build or run**, and **no dependencies to install**.
  There is no `package.json`, lockfile, `Makefile`, `Dockerfile`, CI config, or
  build script anywhere in the repo. The startup/update script is intentionally a
  no-op.
- There are **no automated tests** and **no linter** configured. "Validation" for
  this repo means reviewing the Markdown/PDF content for correctness and internal
  consistency (see the principles in `SYSTEM_DEFINITION.md` and `docs/01_PRINCIPLES.md`).
- Several `.md` files are intentionally **empty placeholders** (e.g. files under
  `prompts/`, `rules/`, `templates/`, `workflows/`, and `docs/00_INTRODUCTION.md`).
  Empty files are expected — they are skeleton content, not a bug.
- The "product" is the readable documentation. To **preview docs as HTML** locally,
  render the Markdown and serve it, for example:
  ```bash
  pip3 install --break-system-packages markdown pymdown-extensions
  # render *.md -> HTML however you prefer, then:
  python3 -m http.server 8787   # from the directory containing the rendered HTML
  ```
  The `markdown` package is only a preview aid; it is **not** a repo dependency and
  must not be added to any manifest or the update script.
- Standard git authoring (branch / commit / push) is the primary workflow here.
