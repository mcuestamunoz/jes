# JES — Workflow

> Este documento define el ciclo de ingeniería estándar del JARVIS Engineering System.  
> Un workflow no describe qué construir. Describe cómo se trabaja.  
> Cada fase tiene un responsable definido en `04_ROLES.md` y un criterio de salida verificable.

---

## Qué es un workflow en JES

Un **workflow** responde a la pregunta: *¿cómo se lleva un problema a una solución válida?*

No es un proceso burocrático.  
No es una checklist de tareas.  
No es un diagrama de Gantt.

Un workflow es un ciclo con fases ordenadas, cada una con un responsable, una entrada, una salida y un criterio de completitud. Si una fase no se puede cerrar, el ciclo no avanza.

El workflow no garantiza que el resultado sea correcto. Garantiza que el resultado sea **verificable, trazable y revisable** *(P5 — Deterministic Engineering)*.

---

## El ciclo de ingeniería

```
┌─────────────────────────────────────────────────────────────────┐
│                     Engineering Cycle                            │
│                                                                  │
│   Intent ──► Analysis ──► Design ──► Plan ──► Implementation    │
│                                                ▼                 │
│   Completion ◄── Documentation ◄── Validation ◄──               │
└─────────────────────────────────────────────────────────────────┘
```

| Fase | Responsable | Entrada | Salida |
|---|---|---|---|
| Intent | Engineer | Problema o necesidad | Objetivo claro y acotado |
| Analysis | Engineering Agent | Objetivo + contexto JES | Análisis de impacto y alternativas |
| Design | Engineer | Análisis | Decisión de diseño aprobada |
| Plan | Engineering Agent | Decisión de diseño | Plan de implementación con tareas verificables |
| Implementation | Engineering Agent | Plan aprobado | Artefactos (código, tests, documentación técnica) |
| Validation | Engineer + Engineering Agent | Artefactos | Resultado verificado y aprobado |
| Documentation | Knowledge Manager | Resultado aprobado | Repositorio actualizado |
| Completion | Engineer | Repositorio actualizado | Ciclo cerrado |

---

## Fase 1 — Intent

**Responsable:** Engineer

**Qué ocurre:**  
El Engineer define qué problema se va a resolver o qué cambio se va a introducir. Esta definición debe ser lo suficientemente concreta para que el Engineering Agent pueda analizar su impacto.

**Criterio de salida:**  
El objetivo está formulado en términos de comportamiento observable o resultado verificable. No puede ser vago ("mejorar el sistema") ni ilimitado ("refactorizar todo").

**Qué no ocurre aquí:**  
No se decide la solución. No se estima el esfuerzo. No se asignan tareas.

---

## Fase 2 — Analysis

**Responsable:** Engineering Agent (con contexto explícito de JES)

**Qué ocurre:**  
El Engineering Agent analiza el problema dentro del contexto del sistema. Identifica qué partes del sistema están implicadas, qué riesgos existen y qué alternativas de solución son viables.

El contexto que usa el agente proviene del repositorio JES: arquitectura, reglas, decisiones previas registradas *(P7 — Context over Memory)*.

**Criterio de salida:**  
El análisis incluye: alcance del cambio, riesgos identificados, al menos dos alternativas con sus tradeoffs.

**Qué no ocurre aquí:**  
El Engineering Agent no decide qué alternativa se implementa. Propone; el Engineer decide.

---

## Fase 3 — Design

**Responsable:** Engineer

**Qué ocurre:**  
El Engineer revisa el análisis y toma la decisión de diseño: qué solución se implementará, con qué restricciones y dentro de qué límites. Esta decisión puede producir un ADR (Architecture Decision Record) si tiene implicaciones arquitectónicas.

**Criterio de salida:**  
La solución está documentada con suficiente detalle para que el Engineering Agent pueda planificar su implementación sin hacer suposiciones sobre la dirección.

**Qué no ocurre aquí:**  
El Engineering Agent no participa en la decisión de diseño. Puede responder preguntas técnicas concretas, pero la elección es del Engineer *(P1 — Human Authority, P2 — AI as Collaborator)*.

---

## Fase 4 — Plan

**Responsable:** Engineering Agent

**Qué ocurre:**  
El Engineering Agent descompone la decisión de diseño en tareas concretas y verificables. El plan debe ser lo suficientemente específico para que cada tarea tenga un resultado observable al completarse.

**Criterio de salida:**  
El plan es aprobado por el Engineer. Cada tarea tiene: qué se hace, cómo se verifica, qué artefacto produce.

**Qué no ocurre aquí:**  
El plan no modifica la decisión de diseño. Si durante la planificación aparecen problemas que cuestionan la decisión, se vuelve a Fase 3.

---

## Fase 5 — Implementation

**Responsable:** Engineering Agent

**Qué ocurre:**  
El Engineering Agent ejecuta el plan. Produce los artefactos definidos: código, tests, documentación técnica, configuración, scripts.

El Engineering Agent opera dentro del alcance definido en el plan. Si durante la implementación detecta que el alcance necesita ampliarse, lo comunica al Engineer antes de proceder *(P1 — Human Authority)*.

**Criterio de salida:**  
Los artefactos existen y son verificables. Los tests pasan. No hay cambios fuera del alcance del plan.

**Qué no ocurre aquí:**  
El Engineering Agent no integra nada en el repositorio principal sin validación. Los artefactos existen en un estado pendiente de revisión *(P8 — Continuous Validation)*.

---

## Fase 6 — Validation

**Responsable:** Engineer + Engineering Agent

**Qué ocurre:**  
Dos validaciones ocurren en esta fase:

- **Validación técnica** (Engineering Agent): los artefactos cumplen los criterios de aceptación. Los tests pasan. El comportamiento es el esperado.
- **Validación humana** (Engineer): la solución implementada resuelve el problema original y es coherente con la arquitectura y los principios del sistema.

Ambas validaciones son necesarias. Una no sustituye a la otra *(P8 — Continuous Validation)*.

**Criterio de salida:**  
El Engineer aprueba explícitamente. La aprobación no puede ser implícita *(P1 — Human Authority)*.

**Qué ocurre si la validación falla:**  
Se vuelve a Fase 5 (si el problema es de implementación) o a Fase 3 (si el problema es de diseño). El ciclo no avanza.

---

## Fase 7 — Documentation

**Responsable:** Knowledge Manager

**Qué ocurre:**  
El Knowledge Manager actualiza el repositorio para reflejar el estado actual del sistema tras el cambio:

- Si hay decisiones arquitectónicas nuevas: se registran (ADR u equivalente)
- Si hay cambios en la arquitectura del sistema: se actualiza el documento correspondiente
- Si hay cambios en el comportamiento de los agentes o en las reglas: se actualizan las reglas o prompts afectados

La documentación refleja decisiones ya tomadas. No anticipa decisiones futuras *(P4 — Documentation as Engineering)*.

**Criterio de salida:**  
El repositorio refleja el estado real del sistema. No quedan cambios sin documentar.

**Qué no ocurre aquí:**  
La documentación no es una tarea opcional ni postergable. Un cambio sin documentar es un cambio incompleto *(P4 — Documentation as Engineering)*.

---

## Fase 8 — Completion

**Responsable:** Engineer

**Qué ocurre:**  
El Engineer revisa que el ciclo está cerrado: el problema original está resuelto, los artefactos están integrados, la documentación está actualizada. El ciclo se da por completado.

**Criterio de salida:**  
El ciclo está cerrado. El sistema puede iniciar un nuevo ciclo.

---

## Reglas del ciclo

**R1 — El ciclo no puede saltarse fases.**  
Cada fase tiene un propósito. Si una fase parece innecesaria, es señal de que el ciclo está mal definido o el problema es demasiado pequeño para un ciclo formal.

**R2 — El ciclo puede volver hacia atrás.**  
Si en cualquier fase se descubre que la fase anterior fue incompleta, se vuelve a esa fase. Retroceder es esperado y correcto.

**R3 — El Engineer es el único que puede completar el ciclo.**  
Las fases 1, 3, 6 y 8 requieren participación humana. El ciclo no puede completarse sin el Engineer.

**R4 — Un artefacto no aprobado no existe.**  
Los artefactos producidos en implementación no son parte del sistema hasta que el Engineer los aprueba en Validación.

**R5 — Un cambio no documentado no está terminado.**  
La documentación es parte del ciclo, no un apéndice.

---

## El ciclo mínimo

Para cambios pequeños y de bajo riesgo, el ciclo puede reducirse. El ciclo mínimo válido requiere al menos:

- Intent (Engineer define el objetivo)
- Implementation (Engineering Agent ejecuta)
- Validation (Engineer aprueba)
- Documentation (Knowledge Manager registra)

Las fases de Analysis, Design y Plan pueden comprimirse en una sola conversación si el cambio es suficientemente claro y su impacto está acotado.

El criterio para usar el ciclo mínimo: el cambio no afecta arquitectura, no introduce nueva deuda técnica y puede revertirse fácilmente.

---

## Workflow y principios

| Fase | Principios que aplican |
|---|---|
| Intent | P1 — Human Authority |
| Analysis | P7 — Context over Memory, P5 — Deterministic Engineering |
| Design | P1 — Human Authority, P2 — AI as Collaborator |
| Plan | P5 — Deterministic Engineering |
| Implementation | P2 — AI as Collaborator, P8 — Continuous Validation |
| Validation | P1 — Human Authority, P8 — Continuous Validation |
| Documentation | P3 — Repository First, P4 — Documentation as Engineering |
| Completion | P1 — Human Authority |

---

## Knowledge Evolution

El ciclo de ingeniería produce resultados. Algunos de esos resultados contienen experiencia reutilizable. La política de Knowledge Evolution define cuándo y cómo esa experiencia se incorpora a JES.

**Regla fundamental:** JES no crece acumulando documentos. Crece destilando experiencia demostrada.

Una experiencia puede permanecer en el proyecto o incorporarse a JES. Se incorpora a JES únicamente cuando demuestra ser reutilizable más allá del proyecto donde surgió.

### Árbol de decisión

```
Ciclo completado
      │
      ▼
¿El resultado es reutilizable más allá de este proyecto?
      │
      ├── No ──► permanece en el proyecto
      │
      └── Sí
              │
              ├── Es un formato o estructura repetitiva
              │         └──► Template
              │
              ├── Es una forma de resolver un problema recurrente
              │         └──► Pattern
              │
              └── Cambia la forma de trabajar de JES
                        │
                        ├── Es una restricción obligatoria  ──► Rule
                        └── Es un cambio de proceso         ──► Workflow / Principles
```

### Evolución natural del conocimiento

El conocimiento no salta directamente a Rule o Workflow. Suele seguir una progresión:

```
Primera vez que ocurre
      │ (experiencia local)
      ▼
Se resuelve en el proyecto

Tercera vez que ocurre
      │ (patrón emergente)
      ▼
Se crea un Pattern  [Status: Experimental]

Se usa en dos o tres proyectos más
      │ (evidencia de reutilización)
      ▼
Pattern  [Status: Validated]

Décima vez que ocurre
      │ (práctica consolidada)
      ▼
El patrón validado se convierte en Rule

Se aplica en múltiples proyectos
      │ (cambio de metodología)
      ▼
La regla modifica el Workflow o los Principles
```

Un patrón `Experimental` es una hipótesis: sugiere que algo puede ser reutilizable, pero aún no lo ha demostrado. Solo un patrón `Validated` — uno que ha funcionado en más de un contexto independiente — puede convertirse en Rule.

Un patrón que nunca alcanza el estado Validated sigue siendo válido como referencia. No toda experiencia reutilizable debe escalar a restricción obligatoria.

### Criterio de incorporación

Antes de incorporar cualquier cosa a JES, la pregunta es:

> **¿Ha demostrado aportar valor en más de un contexto?**

Si la respuesta es sí, se incorpora en el nivel adecuado.  
Si la respuesta es no, permanece en el proyecto hasta que tenga más evidencia.

Este criterio evita que JES se llene de abstracciones prematuras *(P9 — Justified Complexity)*.

---

*Versión: 2026.1 — Actualizado: julio 2026*
