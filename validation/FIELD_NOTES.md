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

## 2026-08-08

Proyecto:
Jarvis / JES

Problema observado:
Para refactors y comprensión de alto nivel del repo hace falta un agente de implementación (Claude Code), pero cargarle todo JES (historia, field notes, roadmap, filosofía) invita a que razone como arquitecto y mezcle responsabilidades.

Consecuencia:
Sin frontera explícita, Claude Code tendería a reinterpretar dirección de producto; con frontera, puede ejecutar cambios locales con tests bajo contrato.

Idea:
Definir en JES la infraestructura `integrations/claude-code/` (Foundation + Operating Model + templates `CLAUDE.md` / `IMPLEMENTATION_CONTRACT.md`). Materializar `CLAUDE.md` en Jarvis. No validar P6 aún. Primer experimento: un solo refactor quirúrgico con contrato estricto tras revisar la frontera.
