# JES — Arquitectura

> Este documento describe cómo está estructurado el JARVIS Engineering System.  
> La arquitectura define capas, responsabilidades y reglas de dependencia.  
> Toda decisión de este documento es trazable a un principio de `01_PRINCIPLES.md`.

---

## Qué es arquitectura en este contexto

La arquitectura de JES no es la arquitectura del software que JES ayuda a desarrollar.

Es la estructura interna del propio sistema de ingeniería:

- qué componentes existen
- qué responsabilidad tiene cada uno
- qué puede depender de qué
- dónde están los límites

Un cambio en la arquitectura de JES afecta a cómo trabajan las personas y los agentes que lo usan. No afecta directamente al código de los proyectos.

---

## El modelo de capas

JES opera en cuatro capas. Las dependencias fluyen en una única dirección: de arriba hacia abajo.

```
┌─────────────────────────────────────────────┐
│              ENGINEER                        │  Capa 1 — Autoridad
│      decisión · dirección · validación       │
└──────────────────────┬──────────────────────┘
                       │ gobierna
                       ▼
┌─────────────────────────────────────────────┐
│                  JES                         │  Capa 2 — Metodología
│   principios · arquitectura · roles          │
│   workflows · reglas · conocimiento          │
└──────────────────────┬──────────────────────┘
                       │ alimenta
                       ▼
┌─────────────────────────────────────────────┐
│           INTEGRATION LAYER                  │  Capa 3 — Adaptación
│    traduce metodología a capacidades         │
│    de herramientas concretas                 │
└──────────────────────┬──────────────────────┘
                       │ ejecuta en
                       ▼
┌─────────────────────────────────────────────┐
│               TOOLS                          │  Capa 4 — Ejecución
│    editores · LLMs · version control         │
│    CI/CD · cualquier herramienta externa     │
└─────────────────────────────────────────────┘
```

**Regla de dependencia:** ninguna capa superior depende de ninguna capa inferior. Las herramientas son reemplazables sin modificar la metodología. La metodología existe independientemente de las herramientas *(P6 — Replaceable Tools)*.

---

## Capa 1 — Engineer

El ingeniero es el origen de toda autoridad técnica dentro del sistema. No es un componente más de JES: es la capa que lo gobierna.

**Responsabilidades:**

- Tomar decisiones estratégicas de dirección
- Aprobar cambios arquitectónicos
- Validar el resultado de cada ciclo de ingeniería
- Definir y actualizar el sistema de ingeniería

**Límites:**

- Las decisiones del ingeniero no requieren justificación ante ninguna capa inferior
- Las aprobaciones son explícitas, nunca inferidas *(P1 — Human Authority)*

**Qué no hace:**

El ingeniero no ejecuta tareas operativas que puedan delegarse. Delegar ejecución es una forma de eficiencia, no de renuncia a la autoridad.

---

## Capa 2 — JES (Metodología)

Esta es la capa central del sistema. Contiene la metodología, el conocimiento y las reglas que gobiernan cómo se trabaja.

```
               JES Methodology
        ┌──────────┼──────────┐
        │          │          │
   Governance  Operations  Repository
```

Tiene tres dominios:

### Governance

Define qué es JES, qué valores guían las decisiones y cómo está organizado el sistema.

| Artefacto | Responsabilidad |
|---|---|
| `SYSTEM_DEFINITION.md` | Qué es JES, sus límites y sus responsabilidades |
| `01_PRINCIPLES.md` | Los valores que gobiernan todas las decisiones |
| `02_ARCHITECTURE.md` | Cómo está estructurado el sistema (este documento) |
| `04_ROLES.md` | Quién hace qué dentro del sistema |

Este subsistema no cambia con frecuencia. Cuando cambia, es por una decisión de ingeniería deliberada, no por adaptación a herramientas.

### Operations

Define cómo se trabaja dentro del sistema.

| Artefacto | Responsabilidad |
|---|---|
| `03_WORKFLOW.md` | El ciclo de ingeniería estándar |
| `05_RULES.md` | Restricciones concretas aplicables a decisiones específicas |
| `rules/` | Reglas por dominio: arquitectura, código, documentación |
| `templates/` | Plantillas para artefactos recurrentes |
| `prompts/` | Prompts reutilizables para agentes |

Este subsistema evoluciona con la experiencia real. Cuando un workflow no funciona, se documenta y se mejora. Esto es iteración esperada, no inestabilidad.

### Repository

El repositorio de JES es la fuente de verdad del sistema *(P3 — Repository First)*.

El conocimiento no vive en las herramientas, no vive en los agentes y no vive en las conversaciones. Vive en los artefactos escritos del repositorio.

Todo agente que necesite contexto del sistema lo obtiene de aquí. No puede obtenerlo de otro lugar *(P7 — Context over Memory)*.

---

## Capa 3 — Integration Layer

Las integraciones son adaptadores. Traducen la metodología de JES a las capacidades de una herramienta específica.

**Responsabilidad única:** exponer JES al entorno de ejecución de la herramienta.

**Lo que una integración puede hacer:**

- Configurar reglas de comportamiento del agente en la herramienta
- Definir comandos que activen workflows de JES
- Proporcionar context files que alimenten al agente con metodología JES
- Automatizar tareas operativas que JES haya definido

**Lo que una integración no puede hacer:**

- Redefinir principios o reglas de JES
- Ser la fuente de verdad de ningún conocimiento
- Alterar el flujo de autoridad (engineer → JES → integration → tool)
- Sobrevivir independientemente de JES

La integración con Cursor, por ejemplo, no es "Cursor Rules". Es la traducción de las reglas de JES al formato que Cursor entiende. Si Cursor desaparece, las reglas de JES permanecen. Solo se pierde el adaptador *(P6 — Replaceable Tools)*.

---

## Capa 4 — Tools

Los editores, los modelos de lenguaje, el control de versiones, el CI/CD — son entornos de ejecución. No pertenecen a JES.

JES no asume ninguna herramienta específica. No puede depender de que una herramienta concreta exista. Si una herramienta desaparece, el sistema sigue siendo operable con una herramienta diferente.

> **Las herramientas son las únicas entidades del sistema que JES no controla.**

Por eso se sitúan en la capa más baja y por eso la capa de integración existe: para que ese contacto entre metodología y herramienta esté mediado, no sea directo.

---

## Flujo de información

El conocimiento fluye en dos direcciones:

**Hacia abajo (contexto):**

```
JES repository
    │
    ▼  proporciona contexto explícito
Agent (via integration)
    │
    ▼  ejecuta en
Tool
```

El agente recibe el contexto de JES antes de actuar. Siempre. No lo deduce, no lo recuerda: lo recibe *(P7 — Context over Memory)*.

**Hacia arriba (artefactos):**

```
Tool
    │
    ▼  produce
Agent output (código, análisis, propuestas)
    │
    ▼  validado por
Engineer
    │
    ▼  si aprobado, integrado en
JES repository
```

Los artefactos producidos por los agentes no se integran automáticamente en el repositorio. Pasan por revisión del ingeniero. Esa aprobación es el punto de control que mantiene la integridad del sistema *(P1 — Human Authority, P8 — Continuous Validation)*.

---

## Reglas de dependencia

Estas reglas se derivan directamente de los principios y no pueden romperse sin violarlos.

| Regla | Principio de origen |
|---|---|
| Ninguna capa inferior puede modificar una capa superior | P1 — Human Authority |
| Las herramientas no definen la metodología | P6 — Replaceable Tools |
| Los agentes no toman decisiones sin contexto explícito | P7 — Context over Memory |
| Ningún conocimiento relevante existe fuera del repositorio | P3 — Repository First |
| Ningún cambio de arquitectura se hace sin aprobación del ingeniero | P1 — Human Authority |
| La complejidad de una capa no puede crecer sin justificación | P9 — Justified Complexity |

---

## Límites del sistema

JES termina donde empieza la herramienta.

El código de JARVIS, los proyectos en `Projects/`, el contenido de `Knowledge/` — son outputs del sistema de ingeniería, no parte de la arquitectura de JES.

JES no es un proyecto. Es la infraestructura que permite desarrollar proyectos.

```
Workspace
│
├── Systems/JES/        ← JES vive aquí
│
├── Projects/           ← Proyectos que JES ayuda a desarrollar
│   ├── Jarvis/
│   └── ...
│
└── Knowledge/          ← Base de conocimiento del ingeniero
```

La arquitectura de JARVIS está en `Projects/Jarvis/docs/ARCHITECTURE.md`.  
La arquitectura de JES está en este documento.  
Son arquitecturas de sistemas distintos.

---

## Evolución de la arquitectura

La arquitectura de JES puede evolucionar. No es un documento estático.

Pero toda modificación de este documento debe:

1. Trazarse a un principio en `01_PRINCIPLES.md`
2. Ser aprobada explícitamente por el ingeniero
3. No romper ningún principio establecido

Si una propuesta de cambio arquitectónico contradice un principio, no se cambia el principio: se cambia la propuesta.

---

*Versión: 2026.1 — Actualizado: julio 2026*
