# JES — Roles

> Este documento define quién es responsable de qué dentro del JARVIS Engineering System.  
> Un rol no es una persona ni una herramienta. Es una responsabilidad con un alcance definido.  
> Los componentes estructurales del sistema (Integration Layer, Execution Environment) pertenecen a `02_ARCHITECTURE.md`.

---

## Qué es un rol en JES

Un **rol** responde a la pregunta: *¿quién es responsable de qué?*

No es un título.  
No es una persona específica.  
No es una herramienta concreta.

Un rol es un conjunto de responsabilidades que puede ser desempeñado por un humano, un agente de IA o una combinación de ambos — dependiendo de la tarea y del contexto.

La misma persona puede desempeñar múltiples roles. Un agente de IA puede desempeñar un rol, pero nunca puede asumir la autoridad que corresponde a un rol humano.

---

## Los tres roles de JES

| Rol | Responsable | Objetivo |
|---|---|---|
| **Engineer** | Humano | Gobernar el sistema |
| **Engineering Agent** | IA | Ejecutar tareas técnicas |
| **Knowledge Manager** | Humano / IA | Mantener el conocimiento |

```
┌───────────────────────────────────────┐
│               Engineer                │  Rol 1
│    decisión · dirección · validación  │
└──────────────────┬────────────────────┘
                   │ delega en
         ┌─────────┴─────────┐
         ▼                   ▼
┌────────────────┐  ┌────────────────────┐
│   Engineering  │  │    Knowledge       │  Roles 2–3
│   Agent        │  │    Manager         │
└────────────────┘  └────────────────────┘
```

---

## Rol 1 — Engineer

**Quién lo desempeña:** el ingeniero humano. Siempre.

**Responsabilidades:**

- Definir la visión y dirección del sistema
- Tomar decisiones arquitectónicas y estratégicas
- Aprobar cambios en la metodología JES y en los proyectos
- Validar el resultado de cada ciclo de ingeniería
- Mantener la coherencia del sistema a lo largo del tiempo

**Autoridad:**

El Engineer tiene autoridad sobre todos los demás roles. Sus decisiones no pueden ser contradichas ni ignoradas por ningún agente *(P1 — Human Authority)*.

**Qué no hace:**

El Engineer no ejecuta tareas operativas que puedan delegarse. No escribe código que puede generar un agente. No busca información que puede obtener un agente. Concentra su energía en las decisiones que requieren juicio humano.

**Transferencia de rol:**

Este rol no se transfiere. No puede ser delegado a un agente de IA ni parcial ni totalmente. Si en algún momento parece que un agente está tomando decisiones estratégicas, es una violación de este rol *(P1 — Human Authority)*.

**Nota sobre el nombre:**

El rol se llama Engineer porque describe responsabilidad de ingeniería, no un título jerárquico. En una organización puede llamarse Lead Engineer, Tech Lead o Principal Engineer. Lo que no cambia es la responsabilidad: quien desempeña este rol es el responsable último del sistema.

---

## Rol 2 — Engineering Agent

**Quién lo desempeña:** un agente de IA con capacidades de implementación.

**Responsabilidades:**

- Implementar funcionalidades definidas por el Engineer
- Generar código, tests y documentación técnica
- Analizar impacto de cambios propuestos
- Identificar problemas técnicos y proponer soluciones
- Ejecutar ciclos de validación técnica

**Alcance:**

El Engineering Agent opera dentro de los límites definidos por la tarea que le ha asignado el Engineer. No puede ampliar ese alcance por iniciativa propia.

**Límites:**

- No puede tomar decisiones de diseño sin aprobación previa
- No puede modificar arquitectura sin instrucción explícita
- No puede integrar cambios en el repositorio sin validación
- Opera siempre con contexto explícito proporcionado por JES *(P7 — Context over Memory)*

**Qué produce:**

Artefactos verificables: código, tests, análisis, propuestas documentadas. Todo lo que produce es revisable y reversible antes de aprobarse *(P5 — Deterministic Engineering)*.

**Nota sobre evolución:**

El Engineering Agent es un tipo de actor que puede especializarse. A medida que el sistema madure, pueden existir agentes especializados en revisión, investigación, testing o documentación. Todos son variantes del Engineering Agent: ejecutan dentro de los límites que define el Engineer.

---

## Rol 3 — Knowledge Manager

**Quién lo desempeña:** el Engineer en su función de mantenimiento documental, asistido opcionalmente por agentes especializados.

**Responsabilidades:**

- Mantener el repositorio de JES actualizado
- Asegurar que las decisiones relevantes quedan registradas
- Actualizar documentación cuando cambia el sistema
- Verificar la coherencia entre documentos

**Por qué es un rol separado:**

Mantener el conocimiento del sistema no es una tarea residual. Es una responsabilidad activa. Un sistema cuya documentación no se actualiza tiene un sistema de conocimiento degradado.

Si el Engineer es la autoridad técnica, el Knowledge Manager es la memoria del sistema.

**Límites:**

- No puede modificar principios o arquitectura sin pasar por el Engineer
- Sus actualizaciones deben reflejar decisiones ya tomadas, no anticipar decisiones futuras *(P4 — Documentation as Engineering)*

---

## Interacciones entre roles

**Flujo de asignación:**

```
Engineer
    │
    │  asigna tarea con contexto
    ▼
Engineering Agent
    │
    │  produce artefacto
    ▼
Engineer
    │
    │  valida y aprueba
    ▼
Knowledge Manager (actualiza repositorio)
```

**Flujo de contexto:**

```
Knowledge Manager (repositorio)
    │
    │  proporciona contexto
    ▼
Engineering Agent
    │
    │  ejecuta dentro de los límites definidos
```

**Regla de interacción:** ningún artefacto se integra en el repositorio sin aprobación del Engineer. El Engineering Agent nunca actúa sin contexto explícito. El Knowledge Manager registra decisiones; no las toma.

---

## Qué no es un rol en JES

**Un modelo de lenguaje no es un rol.**  
Es el entorno de ejecución donde opera el Engineering Agent.

**Una herramienta no es un rol.**  
Las herramientas y las capas de integración son componentes de la arquitectura, no roles. Ver `02_ARCHITECTURE.md`.

**Una tarea no es un rol.**  
Los roles son permanentes; las tareas son temporales.

**Un prompt no es un rol.**  
Es un mecanismo de instrucción del Engineering Agent, no una entidad con responsabilidades propias.

---

## Roles y principios

| Rol | Principios que refleja |
|---|---|
| Engineer | P1 — Human Authority |
| Engineering Agent | P2 — AI as Collaborator, P5 — Deterministic Engineering, P7 — Context over Memory |
| Knowledge Manager | P3 — Repository First, P4 — Documentation as Engineering |

---

*Versión: 2026.2 — Actualizado: julio 2026*
