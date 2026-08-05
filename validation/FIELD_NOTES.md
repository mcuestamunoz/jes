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

## 2026-08-05 — stub hygiene

Proyecto:
JES

Problema observado:
Carpetas y `.md` vacíos (`prompts/`, `rules/`, `templates/`, `workflows/`, skeleton Cursor) daban falsa sensación de madurez.

Consecuencia:
Parecía que faltaba “rellenar” artefactos; en realidad no había contrato ni evidencia que los exigiera.

Idea:
Solo existe lo que el contrato o Field Notes exigen (P9). Stubs vacíos eliminados; `commands/`/`prompts` Cursor se reintroducen solo con necesidad demostrada.
