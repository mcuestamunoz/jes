# Field Notes — JES in practice

Evidence from real engineering sessions.  
Source of truth for Phase 3. Interface features must cite notes here (**P9**).

## How to write an entry

Keep it short. One friction → one consequence → one optional idea.

```text
## YYYY-MM-DD

Proyecto:
Jarvis

Problema observado:


Consecuencia:


Idea:

```

## Entries

## 2026-09-08

Proyecto:
Jarvis + multiagent_problem_solving / JES

Problema observado:
Claude Code en terminal agota el límite de uso por sesión; hace falta otro implementador sin mezclar roles arquitectónicos.

Consecuencia:
Sin frontera, Codex podría usarse “por cuota” sobre Jarvis y diluir el contrato; con split por proyecto, se mantiene un agente por repo.

Idea:
Usar Codex en `multiagent_problem_solving` con `AGENTS.md` (no `CODEX.md`). Jarvis sigue con Claude/`CLAUDE.md`. Misma forma de Implementation Contract. Plantillas en `integrations/codex/`.

## 2026-08-08

Proyecto:
Jarvis / JES

Problema observado:
Para refactors y comprensión de alto nivel del repo hace falta un agente de implementación (Claude Code), pero cargarle todo JES invita a que razone como arquitecto.

Consecuencia:
Sin frontera explícita, el agente tendería a reinterpretar dirección de producto.

Idea:
Frontera JES → Implementation Contract → `CLAUDE.md` / Claude Code (PR sibling). No validar P6 aún.
