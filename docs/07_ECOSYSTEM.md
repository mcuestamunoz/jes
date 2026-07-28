# JES — Ecosystem

> Este documento define el ecosistema de ejecución del JARVIS Engineering System.  
> Un ecosistema no es una lista de herramientas. Es un conjunto de capacidades y la forma en que colaboran para llevar la metodología JES a la práctica.  
> Las herramientas cambiarán. El ecosistema debe seguir siendo válido cuando eso ocurra.

---

## Qué es el ecosistema de ejecución

La metodología de JES define principios, roles, workflows y reglas. El ecosistema define **dónde y cómo se ejecutan**.

Un ecosistema responde a tres preguntas:

1. ¿Qué capacidades necesita JES para funcionar?
2. ¿Qué tipos de herramientas pueden proporcionar esas capacidades?
3. ¿Cómo colaboran esas herramientas dentro de un ciclo de ingeniería?

El ecosistema no pertenece a JES — las herramientas son externas y reemplazables *(P6 — Replaceable Tools)*. Lo que pertenece a JES es la especificación de las capacidades que el ecosistema debe cubrir.

---

## Las capacidades de JES

JES requiere seis capacidades para ejecutar su ciclo de ingeniería completo:

| Capacidad | Descripción | Fase del ciclo |
|---|---|---|
| **Governance** | Diseño metodológico, planificación, toma de decisiones de alto nivel, revisión conceptual | Intent, Analysis, Design |
| **Development** | Implementación de código, ejecución de tareas técnicas, desarrollo interactivo | Plan, Implementation |
| **Review** | Análisis de calidad, revisión arquitectónica, refactorización profunda, detección de riesgos | Validation |
| **Automation** | Ejecución de workflows repetitivos, CI/CD, validación automática | Validation, Completion |
| **Knowledge** | Consulta de contexto, documentación técnica del ingeniero, base de conocimiento del proyecto | Analysis, Documentation |
| **Execution** | IDE, control de versiones, compilación, tests — el entorno base de ejecución | Todo el ciclo |

Ninguna herramienta cubre todas las capacidades de forma óptima. El ecosistema distribuye las capacidades entre herramientas según sus fortalezas.

---

## Criterios de integración

Antes de incorporar una herramienta al ecosistema JES, debe cumplir al menos uno de estos criterios:

1. **Cubre una capacidad no cubierta o mal cubierta** por las herramientas existentes.
2. **Ofrece una ventaja significativa** en calidad, velocidad o fiabilidad para una capacidad existente.
3. **No duplica** lo que ya hace otra herramienta del ecosistema.
4. **Puede integrarse sin modificar la metodología** — la herramienta se adapta a JES, no al revés.
5. **Puede reemplazarse** — su ausencia no rompe el ecosistema, solo obliga a usar otra herramienta para esa capacidad.

La popularidad o la novedad no son criterios válidos *(P9 — Justified Complexity)*.

---

## Arquitectura del ecosistema

```
                          JES
                           │
         ┌─────────────────┼──────────────────┐
         │                 │                  │
    Governance         Development         Knowledge
         │                 │                  │
         ▼                 ▼                  ▼
  ChatGPT / Claude      Cursor            Workspace
                         Claude Code      Projects/
                         GitHub Actions
```

---

## Mapa de capacidades actual

Esta es la distribución de responsabilidades en el ecosistema activo de JES.

| Capacidad | Implementación actual | Justificación |
|---|---|---|
| Governance | ChatGPT / Claude | Diseño metodológico, planificación, revisión conceptual y arquitectónica de alto nivel |
| Development | Cursor | Desarrollo asistido sobre el repositorio, implementación interactiva diaria |
| Review | Claude Code | Refactorizaciones grandes, revisión de repositorios completos, análisis de impacto transversal |
| Automation | GitHub Actions | Validación automática, CI/CD, ejecución determinista de workflows |
| Knowledge | Workspace Knowledge Base | Base de conocimiento técnica del Engineer — matemáticas, física, dominio de ingeniería |
| Execution | Git + IDE | Control de versiones, ejecución y compilación |

Cada herramienta tiene una responsabilidad principal. No se espera que ninguna cubra todo el ciclo.

---

## El pipeline de ingeniería

Las herramientas colaboran de forma ordenada dentro del ciclo. Este es el pipeline estándar:

```
Engineer
    │
    │  Intent + contexto
    ▼
ChatGPT / Claude
    │  Governance
    │  Analysis, Design
    ▼
ADR / Feature Spec / Plan
    │  (artefacto de JES)
    ▼
Cursor
    │  Development
    │  Implementation
    ▼
Claude Code
    │  Review
    │  Validation técnica y arquitectónica
    ▼
GitHub Actions
    │  Automation
    │  Validación automática (tests, lint, CI)
    ▼
Engineer
    │  Aprobación final
    ▼
Knowledge Manager
    │  Documentation
    │  Repositorio actualizado
```

Este no es el único pipeline posible. Para ciclos mínimos, algunas fases se comprimen. Pero el orden de responsabilidades se mantiene.

---

## Principios del ecosistema

### La metodología no depende de ninguna herramienta

Si Cursor desaparece mañana, JES sigue siendo válido. El Development se haría con otro IDE o asistente. El ecosistema se adapta; la metodología permanece.

### Cada herramienta tiene una responsabilidad principal

Una herramienta puede participar en varias capacidades, pero solo debe tener una responsabilidad principal dentro del ecosistema.

No se optimiza el ecosistema intentando que una herramienta haga todo. Se optimiza eligiendo la herramienta más adecuada para cada capacidad y manteniendo los límites claros.

### Las integraciones traducen, no redefinen

Una integración de Cursor no es "la metodología de desarrollo de JES". Es la traducción de esa metodología al formato que Cursor entiende. Si la integración desaparece, la metodología no cambia.

### El contexto fluye del repositorio hacia las herramientas

El repositorio JES es siempre la fuente de verdad. Cada herramienta recibe contexto del repositorio antes de actuar. Ninguna herramienta genera conocimiento que no vuelva al repositorio *(P3 — Repository First, P7 — Context over Memory)*.

---

## Evolución del ecosistema

El ecosistema evolucionará a medida que aparezcan nuevas herramientas y cambie el panorama tecnológico. La evolución se gestiona mediante el proceso de Knowledge Evolution descrito en `03_WORKFLOW.md`:

- Una herramienta nueva entra cuando cubre una capacidad real no cubierta
- Una herramienta existente se reemplaza cuando una alternativa la supera claramente
- Una capacidad nueva se añade cuando el ciclo de ingeniería la requiere y no existe forma de cubrirla con las actuales

El ecosistema no crece por anticipación. Crece por necesidad demostrada *(R-GRW-1)*.

---

## Relación con las integraciones

`06_INTEGRATIONS.md` describe la arquitectura de la Integration Layer: cómo se diseñan los adaptadores, qué pueden y no pueden hacer, y cómo se relacionan con JES.

`07_ECOSYSTEM.md` (este documento) responde a una pregunta anterior: qué capacidades necesita JES y qué herramientas las cubren.

```
07_ECOSYSTEM.md   ← qué capacidades y qué herramientas
        │
        ▼
06_INTEGRATIONS.md ← cómo se construyen los adaptadores
        │
        ▼
integrations/     ← los adaptadores concretos
```

---

*Versión: 2026.1 — Actualizado: julio 2026*
