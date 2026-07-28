# JES — System Definition

> Este es el documento más importante del JARVIS Engineering System.  
> Todo lo demás (arquitectura, workflows, reglas, automatizaciones) debe derivar de él.  
> Si algo no encaja aquí, no pertenece a JES.
>
> Este documento define **qué es JES**. `01_PRINCIPLES.md` define **cómo piensa**. Ambos forman juntos la capa raíz del sistema.

---

## 1. Qué es JES

El JARVIS Engineering System (JES) es un sistema de ingeniería diseñado para organizar, coordinar y gobernar el desarrollo de proyectos complejos mediante la colaboración estructurada entre un ingeniero y múltiples agentes de inteligencia artificial.

JARVIS es el principal proyecto desarrollado bajo JES, pero no el único.

No es un conjunto de herramientas.  
No es una metodología teórica.  
No es documentación pasiva.

JES no desarrolla software.

JES desarrolla la forma en la que el software es desarrollado.

Es un sistema con responsabilidades activas que gobierna cómo se toman decisiones, cómo se coordina el trabajo entre el ingeniero y los agentes de IA, y cómo se preserva el conocimiento del proyecto a lo largo del tiempo.

JES existe porque construir sistemas complejos con IA como colaborador requiere más que buenas intenciones. Requiere estructura.

---

## 2. Qué problemas resuelve

| Problema | Cómo lo resuelve JES |
|---|---|
| Las decisiones se toman sin registro ni justificación | Documenta y versiona cada decisión arquitectónica |
| El contexto se pierde entre sesiones | Define reglas de contexto explícito para los agentes |
| La IA asume autoridad que no le corresponde | Establece límites claros entre delegación e implementación |
| El conocimiento queda en conversaciones privadas | Todo conocimiento vive en el repositorio |
| La calidad depende del estado del ingeniero | Define procesos reproducibles independientes del estado |
| Las herramientas condicionan la arquitectura | Separa metodología de implementación |

---

## 3. Responsabilidades

JES existe para:

- ✓ **Organizar la ingeniería** — dar estructura al proceso de desarrollo
- ✓ **Mantener el contexto** — garantizar que los agentes operan con información correcta y completa
- ✓ **Coordinar las IA** — definir roles, alcances y límites de cada agente
- ✓ **Preservar el conocimiento** — todo lo que importa vive en el repositorio
- ✓ **Automatizar tareas repetitivas** — eliminar fricción en el ciclo de ingeniería
- ✓ **Garantizar la calidad** — todo cambio es reproducible, verificable y trazable
- ✓ **Mantener al ingeniero como autoridad absoluta** — ninguna decisión estratégica se delega
- ✓ **Facilitar la toma de decisiones de ingeniería** — proporcionar al ingeniero la información y el contexto necesarios para tomar decisiones informadas

---

## 4. Límites

JES **nunca debe**:

- ✗ Tomar decisiones estratégicas de forma autónoma
- ✗ Modificar arquitectura sin aprobación explícita del ingeniero
- ✗ Hacer merge, deploy o cambios irreversibles automáticamente
- ✗ Ocultar decisiones o razonamientos
- ✗ Generar conocimiento que no quede documentado en el repositorio
- ✗ Condicionar la arquitectura del software a una herramienta concreta
- ✗ Crecer en complejidad sin justificación clara de valor
- ✗ Sustituir el criterio del ingeniero

---

## 5. Principios

Estos principios gobiernan todas las decisiones dentro de JES.

**P0 — Engineering First**
JES existe para mejorar la ingeniería, no para demostrar capacidades de inteligencia artificial.

Toda decisión dentro del sistema debe justificarse por el valor que aporta al proceso de ingeniería.

**P1 — Human Authority**  
La autoridad técnica nunca se delega. Los agentes proponen, implementan, analizan y revisan. La decisión final pertenece siempre al ingeniero.

**P2 — AI as Collaborator**  
La implementación puede delegarse. El diseño, no.

**P3 — Repository First**  
Todo conocimiento vive en el repositorio. No se aceptan dependencias de conversaciones, memoria personal o contexto externo.

**P4 — Documentation as Engineering**  
La documentación forma parte del sistema, no es una tarea posterior.

**P5 — Deterministic Engineering**  
Todo cambio debe ser reproducible, verificable y trazable.

**P6 — Replaceable Tools**  
Las herramientas son intercambiables. La arquitectura del sistema nunca depende de un proveedor concreto.

**P7 — Context over Memory**  
Los agentes trabajan con contexto explícito. Nunca se asume que recuerdan conversaciones anteriores.

**P8 — Continuous Validation**  
No existe implementación sin verificación. Todo cambio finaliza con validación.

**P9 — Simplicity by Default**  
Cada componente añadido incrementa la complejidad. Toda nueva herramienta, dependencia o abstracción debe justificar el valor que aporta.

---

## 6. Criterio de pertenencia

Antes de añadir cualquier cosa a JES, la pregunta es:

> **¿Cumple alguna de las responsabilidades definidas en la sección 3?**

Si sí → pertenece a JES.  
Si no → no entra en JES.

Este criterio es la única regla de incorporación que necesitamos.

---

## 7. Relación con JARVIS

JES y JARVIS son dos sistemas separados con una relación unidireccional:

```
JES (Engineering System)
        │
        │ desarrolla
        ▼
  JARVIS (Software Product)
```

JARVIS referencia JES mediante una línea en su documentación (`docs/engineering.md`).  
No existe dependencia técnica entre ambos.  
JES puede aplicarse a cualquier proyecto; no es exclusivo de JARVIS.

JES puede existir sin JARVIS. JARVIS puede desarrollarse sin JES. Sin embargo, la combinación de ambos constituye el entorno de ingeniería recomendado para proyectos complejos.

---

## 8. Flujo de trabajo bajo JES

                    JES

             (Coordina ingeniería)

                     │

      ┌──────────────┼──────────────┐

      ▼              ▼              ▼

 Knowledge      Workflows       Rules

      │              │              │

      └──────────────┼──────────────┘

                     ▼

          Context Builder

                     ▼

           Prompt Builder

                     ▼

                Cursor

                     ▼

             Implementación


*Versión: 2026.1 — Actualizado: julio 2026*
