# JES — Engineering Operations

> Este documento define las operaciones de ingeniería reconocidas por JES.  
> Una operación no es un comando de herramienta. Es una unidad metodológica de trabajo que cualquier integración debe poder ejecutar.  
> Si una operación debe existir igual en Cursor, Claude Code o ChatGPT, pertenece a JES.

---

## Qué es una operación de ingeniería

Una **Engineering Operation** responde a la pregunta:

> *¿Qué tipo de trabajo de ingeniería se está realizando en este ciclo?*

No define sintaxis de prompts, ni comandos concretos, ni detalles de una herramienta.

Define una interfaz estable entre:

- la metodología JES (`03_WORKFLOW.md`, `05_RULES.md`),
- los modelos operativos de integración,
- y la implementación concreta en cada herramienta.

---

## Posición arquitectónica

Las operaciones pertenecen al núcleo metodológico de JES, no a una integración.

```text
JES Core
    │
    ├── Principles
    ├── Rules
    ├── Workflow
    └── Engineering Operations
            │
            ▼
      Integration Layer
            │
            ▼
       Tool Runtime
```

Las integraciones implementan operaciones. No las inventan.

---

## Conjunto de operaciones (v1)

- Research
- Analyze
- Plan
- Implement
- Review
- Validate
- Document
- Explain
- Refactor

---

## Definición de operaciones

### Research

**Objetivo:** recopilar y organizar contexto relevante antes de decidir implementación.

**Salidas típicas:**
- resumen de hallazgos
- referencias a módulos/archivos afectados
- incógnitas y riesgos identificados

### Analyze

**Objetivo:** evaluar impacto, restricciones y alternativas para un intent definido.

**Salidas típicas:**
- análisis de alcance
- análisis de tradeoffs
- opciones recomendadas para decisión del Engineer

### Plan

**Objetivo:** convertir una dirección aprobada en tareas verificables.

**Salidas típicas:**
- lista ordenada de tareas
- criterios de aceptación/verificación
- artefactos esperados por tarea

### Implement

**Objetivo:** ejecutar el plan aprobado dentro del alcance definido.

**Salidas típicas:**
- cambios de código/configuración
- tests/checks asociados
- notas de implementación

### Review

**Objetivo:** evaluar corrección, calidad y alineación con arquitectura/reglas.

**Salidas típicas:**
- hallazgos priorizados por severidad
- notas de riesgo/regresión
- propuestas de corrección

### Validate

**Objetivo:** verificar que la implementación cumple criterios técnicos y de workflow.

**Salidas típicas:**
- evidencia de validación (tests/checks/resultados)
- estado pass/fail con justificación
- brechas de validación pendientes

### Document

**Objetivo:** actualizar el conocimiento del repositorio para reflejar el estado aprobado.

**Salidas típicas:**
- documentación/especificaciones actualizadas
- nota explícita de artefactos impactados
- verificación de completitud documental

### Explain

**Objetivo:** comunicar razonamiento, comportamiento e impacto de un cambio.

**Salidas típicas:**
- explicación concisa de qué cambió y por qué
- resumen de impacto
- consideraciones de seguimiento

### Refactor

**Objetivo:** mejorar estructura interna sin alterar comportamiento externo esperado.

**Salidas típicas:**
- mejoras estructurales del código
- evidencia de preservación de comportamiento
- cambios sobre deuda técnica identificada

---

## Selección de operación (Operation Selection)

Entre el Intent y la ejecución existe una traducción obligatoria:

```text
Intent
  ↓
Operation Selection
  ↓
Engineering Operation
  ↓
Execution
```

La selección de operación forma parte del modelo operativo de cada integración, pero el conjunto de operaciones seleccionado pertenece a JES.

---

## Relación con workflow y artefactos

Las operaciones no reemplazan el workflow.

- El **workflow** define fases, responsables y cierre del ciclo.
- La **operación** define el tipo de trabajo ejecutado.

Los artefactos finales se determinan por:

> **workflow + operation**

No por preferencia de herramienta.

---

## Reglas de implementación para integraciones

Cada integración debe especificar:

1. cómo se activa cada operación (comando o equivalente),
2. qué prompt(s) implementan esa operación,
3. qué bundle de artefactos debe entregar.

El mapeo operación → prompt puede ser 1:1 o 1:N según restricciones de la herramienta.

---

## Gobierno y evolución

- Ninguna operación puede contradecir `01_PRINCIPLES.md`.
- Toda operación debe respetar gates de autoridad del Engineer.
- Cambios al conjunto de operaciones requieren aprobación explícita del Engineer.
- Nuevas operaciones solo se incorporan con valor transversal demostrado en más de una integración o contexto.

---

*Versión: 2026.1 — Actualizado: julio 2026*
