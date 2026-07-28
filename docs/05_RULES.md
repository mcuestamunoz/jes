# JES — Rules

> Este documento define qué es una regla dentro del JARVIS Engineering System y establece las reglas fundacionales del sistema.  
> Las reglas específicas de dominio (arquitectura, código, documentación) viven en `rules/` y evolucionan con la experiencia.  
> Ninguna regla puede contradecir un principio de `01_PRINCIPLES.md`. Si existe conflicto, el principio prevalece.

---

## Qué es una regla en JES

Una **regla** responde a la pregunta: *¿qué restricción concreta aplica en esta situación?*

No es un principio — los principios son valores. Las reglas son restricciones operativas derivadas de esos valores.  
No es un workflow — los workflows describen cómo se trabaja. Las reglas acotan qué está permitido dentro de ese trabajo.  
No es un patrón — los patrones capturan soluciones reutilizables. Las reglas definen límites no negociables.

Una regla tiene tres propiedades:

1. **Es específica.** Describe una situación concreta y una restricción concreta. Una regla vaga no es una regla.
2. **Es trazable.** Puede conectarse a un principio que la justifica. Una regla sin origen puede ser arbitraria.
3. **Es verificable.** Se puede comprobar si se cumple o no. Una regla que no puede verificarse no puede aplicarse.

---

## Estructura de una regla

```
ID:        Identificador único (ej: R-GOV-1)
Regla:     Enunciado de la restricción
Origen:    Principio del que deriva
Aplica a:  Qué contexto o rol activa esta regla
Viola si:  Ejemplo de comportamiento que la incumple
```

---

## Tipos de reglas

JES organiza las reglas en categorías según el dominio que gobiernan:

| Categoría | Prefijo | Qué gobierna |
|---|---|---|
| Governance | R-GOV | Autoridad, aprobaciones, decisiones |
| Collaboration | R-COL | Relación Engineer–Agent |
| Knowledge | R-KNW | Repositorio, documentación, contexto |
| Engineering | R-ENG | Ciclo de ingeniería, implementación |
| Agent | R-AGT | Comportamiento de los agentes |
| Integration | R-INT | Herramientas e integraciones |
| Growth | R-GRW | Evolución del sistema |

---

## Reglas fundacionales de JES

Estas reglas derivan directamente de los principios y son obligatorias en todo contexto bajo JES.

---

### R-GOV-1
**Toda decisión arquitectónica requiere aprobación explícita del Engineer.**

| Campo | Valor |
|---|---|
| Origen | P1 — Human Authority |
| Aplica a | Engineer, Engineering Agent |
| Viola si | Un agente aplica un cambio arquitectónico sin que el Engineer lo haya aprobado explícitamente. La aprobación no puede inferirse del silencio. |

---

### R-GOV-2
**El alcance de una tarea no puede expandirse sin confirmación del Engineer.**

| Campo | Valor |
|---|---|
| Origen | P1 — Human Authority |
| Aplica a | Engineering Agent |
| Viola si | El Engineering Agent detecta que necesita cambiar más de lo previsto y procede sin comunicarlo al Engineer. |

---

### R-GOV-3
**Ningún agente puede integrar cambios en el repositorio sin validación humana.**

| Campo | Valor |
|---|---|
| Origen | P1 — Human Authority, P8 — Continuous Validation |
| Aplica a | Engineering Agent, Integration Adapter |
| Viola si | Código, documentación o configuración se añade al repositorio principal sin haber pasado por revisión del Engineer. |

---

### R-COL-1
**El Engineering Agent propone alternativas. El Engineer decide.**

| Campo | Valor |
|---|---|
| Origen | P2 — AI as Collaborator |
| Aplica a | Engineer, Engineering Agent |
| Viola si | El Engineering Agent elige entre alternativas de diseño sin consultar al Engineer. O el Engineer delega esa elección al agente. |

---

### R-COL-2
**Toda tarea delegada a un agente debe tener contexto, alcance y criterio de salida definidos antes de comenzar.**

| Campo | Valor |
|---|---|
| Origen | P2 — AI as Collaborator, P7 — Context over Memory |
| Aplica a | Engineer |
| Viola si | El Engineer asigna una tarea al agente sin especificar qué se espera como resultado o sin proporcionar el contexto del sistema. |

---

### R-KNW-1
**Ninguna decisión relevante puede existir solo en una conversación.**

| Campo | Valor |
|---|---|
| Origen | P3 — Repository First |
| Aplica a | Engineer, Knowledge Manager |
| Viola si | Una decisión de diseño o dirección tomada en conversación no queda registrada en el repositorio antes de cerrar el ciclo. |

---

### R-KNW-2
**Los agentes reciben contexto del repositorio. No se asume conocimiento previo.**

| Campo | Valor |
|---|---|
| Origen | P7 — Context over Memory |
| Aplica a | Engineer, Integration Adapter |
| Viola si | Un agente recibe una instrucción sin el contexto del sistema, o se asume que "ya sabe" algo de sesiones anteriores. |

---

### R-ENG-1
**Un cambio no está terminado hasta que su documentación está actualizada.**

| Campo | Valor |
|---|---|
| Origen | P4 — Documentation as Engineering |
| Aplica a | Knowledge Manager, Engineer |
| Viola si | Se considera un ciclo completo cuando el código está integrado pero los documentos afectados no han sido actualizados. |

---

### R-ENG-2
**Toda implementación debe terminar con validación antes de integrarse.**

| Campo | Valor |
|---|---|
| Origen | P8 — Continuous Validation |
| Aplica a | Engineering Agent, Engineer |
| Viola si | Se integran artefactos sin pasar por la fase de Validation del ciclo de ingeniería. |

---

### R-INT-1
**Ninguna regla puede referenciar una herramienta concreta como requisito de la metodología.**

| Campo | Valor |
|---|---|
| Origen | P6 — Replaceable Tools |
| Aplica a | Knowledge Manager, Engineer |
| Viola si | Una regla dice "se debe usar Cursor" o "se requiere GitHub" como parte de la metodología JES. Las herramientas implementan JES; no lo definen. |

---

### R-GRW-1
**Ningún nuevo componente entra en JES sin un problema demostrado que lo justifique.**

| Campo | Valor |
|---|---|
| Origen | P9 — Justified Complexity |
| Aplica a | Engineer, Knowledge Manager |
| Viola si | Se añade una carpeta, documento, regla o prompt a JES sin haber identificado primero el problema concreto que resuelve. |

---

### R-GRW-2
**Un patrón solo puede convertirse en regla cuando ha demostrado valor en más de un contexto.**

| Campo | Valor |
|---|---|
| Origen | P9 — Justified Complexity, Knowledge Evolution (03_WORKFLOW.md) |
| Aplica a | Engineer, Knowledge Manager |
| Viola si | Un patrón con estado Experimental se eleva a Rule sin haber sido validado en múltiples proyectos o contextos independientes. |

---

## Reglas de dominio

Las reglas de dominio son específicas a arquitectura, código y documentación. Viven en `rules/` y evolucionan con la experiencia del proyecto.

| Archivo | Dominio | Estado |
|---|---|---|
| `rules/architecture_rules.md` | Decisiones arquitectónicas | Pendiente de contenido |
| `rules/coding_rules.md` | Estándares de código | Pendiente de contenido |
| `rules/documentation_rules.md` | Documentación de artefactos | Pendiente de contenido |

Estas reglas emergen de la experiencia real. Siguiendo el proceso de Knowledge Evolution descrito en `03_WORKFLOW.md`, se añadirán cuando existan patrones validados que las justifiquen.

---

## Cómo se crean nuevas reglas

Una nueva regla puede incorporarse a JES siguiendo este proceso:

1. **Identificar la restricción:** ¿qué comportamiento se quiere obligar o prohibir?
2. **Trazar al principio:** ¿qué principio de `01_PRINCIPLES.md` la justifica?
3. **Definir la violación:** ¿qué ejemplo concreto la incumple?
4. **Revisar conflictos:** ¿contradice alguna regla o principio existente?
5. **Aprobación del Engineer:** la regla entra en vigor con aprobación explícita.

Una regla propuesta que no puede trazarse a un principio no puede incorporarse a JES.

---

## Jerarquía normativa y evolución del conocimiento

Existen dos jerarquías distintas en JES que no deben confundirse.

### Jerarquía normativa

Define qué nivel de autoridad prevalece cuando hay conflicto. El nivel superior siempre gana:

```
Principles       ← nivel más alto — valores que gobiernan el sistema
      │
      ▼
Rules            ← restricciones derivadas de principios
      │
      ▼
Workflows        ← procesos que operan dentro de esas restricciones
      │
      ▼
Templates        ← artefactos que materializan el trabajo
```

Un workflow no puede requerir algo que una regla prohíbe.  
Una regla no puede requerir algo que un principio prohíbe.

### Evolución del conocimiento

Define cómo la experiencia asciende en el sistema. Es el camino opuesto: de abajo hacia arriba.

```
Experience           ← experiencia concreta de un proyecto
      │
      ▼
Pattern [Experimental]
      │
      ▼
Pattern [Validated]
      │
      ▼
Rule                 ← el patrón validado se formaliza como restricción
      │
      ▼
Workflow             ← si cambia la forma de trabajar
      │
      ▼
Principle            ← muy excepcional: solo cuando la experiencia
                        acumulada demuestra que un valor debe evolucionar
```

Los patrones no son una capa de autoridad — son un mecanismo de crecimiento. Por eso no aparecen en la jerarquía normativa: su rol es nutrir a las reglas, no gobernarlas.

La posibilidad de que un principio evolucione existe, pero debe ser extraordinaria. Los principios son el fundamento del sistema; modificarlos requiere evidencia muy sólida y aprobación explícita del Engineer.

---

*Versión: 2026.1 — Actualizado: julio 2026*
