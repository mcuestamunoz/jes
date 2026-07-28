# JES — Principios

> Este documento define los principios que gobiernan el JARVIS Engineering System.  
> Un principio no es una regla operativa ni un proceso. Es una afirmación sobre cómo debe comportarse el sistema — incluso cuando no existe una regla explícita que cubra la situación.  
> Si un principio y una regla entran en conflicto, el principio prevalece.

---

## Qué es un principio (y qué no es)

Un **principio** responde a la pregunta: *¿qué valoramos cuando tomamos decisiones?*

No es una instrucción de cómo hacer algo (eso es un workflow).  
No es una restricción específica (eso es una regla).  
No es una descripción de cómo está organizado el sistema (eso es arquitectura).

Un principio es una declaración de valor que puede aplicarse a situaciones que nadie anticipó.

---

> Engineering exists to build systems that remain understandable, maintainable and evolvable over time.  
> The principles below describe how JES pursues that objective.

---

## Los nueve principios de JES

---

### P1 — Human Authority

> La autoridad técnica nunca se delega.

El ingeniero es el único con capacidad de decisión sobre dirección, arquitectura y estrategia. Los agentes de IA pueden proponer, analizar, revisar e implementar. No pueden decidir.

**Por qué importa.**  
Cuando la autoridad es ambigua, los sistemas tienden a expandirse hacia el espacio vacío. Un agente sin límites claros toma decisiones por omisión. P1 elimina esa ambigüedad.

**Cómo se aplica.**  
Cualquier cambio que afecte dirección, arquitectura o comportamiento observable del sistema requiere aprobación explícita del ingeniero. La aprobación no puede ser implícita ni inferida.

**Qué lo viola.**  
Que un agente aplique un cambio arquitectónico porque "parece la dirección correcta". Que se asuma aprobación por silencio.

---

### P2 — AI as Collaborator

> La implementación puede delegarse. La responsabilidad del diseño, no.

Los agentes son colaboradores técnicos de alta capacidad. Pueden escribir código, ejecutar tests, analizar impacto, revisar consistencia. No pueden diseñar el sistema.

**Por qué importa.**  
Diseño e implementación son responsabilidades de naturaleza distinta. Diseño requiere comprensión del contexto, de las restricciones no escritas, de la dirección a largo plazo. La implementación puede derivarse del diseño. No al revés.

**Cómo se aplica.**  
Antes de delegar cualquier tarea, el ingeniero define qué se debe hacer y por qué. El agente decide cómo.

**Qué lo viola.**  
Pedir a un agente "que diseñe la arquitectura de X" sin haber definido previamente las restricciones y los objetivos.

---

### P3 — Repository First

> Todo conocimiento relevante vive en el repositorio.

No se acepta ninguna dependencia de conversaciones privadas, memoria de sesión o contexto externo no documentado. Si algo es importante, está escrito. Si no está escrito, no existe.

**Por qué importa.**  
Un sistema que depende de quién estuvo presente en una conversación no es reproducible. P3 garantiza que cualquier agente o ingeniero que llegue en el futuro pueda entender el sistema leyendo el repositorio.

**Cómo se aplica.**  
Cada decisión relevante queda registrada. Cada cambio de dirección queda justificado. La regla práctica: si no puedes encontrarlo en el repositorio, no puedes asumir que existe.

**Qué lo viola.**  
"Ya lo hablamos en la sesión anterior." "El agente sabe el contexto." Cualquier dependencia de memoria de conversación.

---

### P4 — Documentation as Engineering

> La documentación es un artefacto de ingeniería.

La documentación tiene el mismo rango que el código, la arquitectura y los tests. Un sistema sin documentación es un sistema incompleto.

**Por qué importa.**  
La documentación es la interfaz entre el sistema y las personas (y los agentes) que trabajan con él. Sin interfaz, el sistema no es utilizable por nadie que no lo haya construido.

**Cómo se aplica.**  
Ningún cambio está terminado hasta que su documentación está actualizada. La documentación se escribe cuando el conocimiento existe, no cuando hay tiempo libre.

**Qué lo viola.**  
"Ya lo documento después." Código implementado sin actualizar la arquitectura o el roadmap.

---

### P5 — Deterministic Engineering

> Todo cambio debe ser reproducible, observable, verificable y trazable.

Un sistema de ingeniería que no puede repetir sus resultados no es fiable. P5 exige que cada acción tenga una causa documentada y un resultado observable y verificable.

**Por qué importa.**  
La reproducibilidad es la base de la confianza. Si un resultado no puede verificarse, no puede mejorarse. Si un cambio no puede trazarse, no puede revertirse.

**Cómo se aplica.**  
Cada implementación termina con validación. Cada decisión queda justificada. Los tests son la verificación formal; la documentación es la trazabilidad.

**Qué lo viola.**  
"Funcionó en mi máquina." Cambios sin tests. Decisiones sin registro.

---

### P6 — Replaceable Tools

> Las herramientas son intercambiables. La arquitectura del sistema no depende de ninguna de ellas.

Cursor, Copilot, Ollama, Git, Docker — son herramientas. El sistema de ingeniería existe independientemente de ellas. Si una herramienta desaparece o cambia, la metodología no cambia.

**Por qué importa.**  
Los ecosistemas de herramientas evolucionan rápidamente. Un sistema atado a una herramienta concreta tiene una vida útil limitada por esa herramienta.

**Cómo se aplica.**  
La metodología se define en términos de responsabilidades y resultados, no de herramientas. Las herramientas implementan la metodología; no la definen.

**Qué lo viola.**  
"Este workflow solo funciona con Cursor." Documentación que asume una herramienta específica como requisito de la metodología.

---

### P7 — Context over Memory

> Los agentes operan con contexto explícito. Nunca se asume que recuerdan conversaciones anteriores.

Cada interacción con un agente empieza desde el contexto documentado, no desde la memoria de la sesión anterior.

**Por qué importa.**  
Los modelos de lenguaje no tienen memoria persistente real. Asumir que la tienen lleva a inconsistencias que son difíciles de detectar y costosas de corregir.

**Cómo se aplica.**  
Los archivos de reglas (`rules/`), definiciones del sistema (`SYSTEM_DEFINITION.md`) y arquitectura del proyecto (`ARCHITECTURE.md`) son el contexto que se proporciona explícitamente a los agentes. No se asume conocimiento previo.

**Qué lo viola.**  
"El agente ya sabe esto." Instruir a un agente sin proporcionar el contexto del sistema.

---

### P8 — Continuous Validation

> No existe implementación sin verificación. Todo cambio finaliza con validación.

La validación no es la última fase de un proyecto. Es el cierre de cada cambio individual.

**Por qué importa.**  
Los errores detectados tarde son exponencialmente más caros de corregir. P8 garantiza que cada cambio está validado en el momento en que se produce, no cuando ya ha propagado sus efectos.

**Cómo se aplica.**  
Cada ciclo de ingeniería termina con una fase de validación explícita. En JARVIS: los tests son la validación técnica; la revisión humana es la validación de diseño.

**Qué lo viola.**  
Implementar sin tests. Fusionar sin revisión. Declarar un cambio "hecho" antes de verificar que funciona correctamente.

---

### P9 — Justified Complexity

> Cada componente añadido incrementa la complejidad del sistema. La incorporación requiere justificación explícita de valor.

La complejidad accidental — la que no resuelve ningún problema real — es el enemigo de la sostenibilidad. El sistema debe activamente resistir la tendencia a crecer.

**Por qué importa.**  
Los sistemas complejos son más difíciles de entender, mantener y delegar. La complejidad no gestionada acaba superando la capacidad del equipo.

**Cómo se aplica.**  
Antes de añadir cualquier herramienta, abstracción, proceso o documento: ¿qué problema concreto resuelve? ¿Podría resolverse con lo que ya existe? Si la respuesta no es clara, no se añade.

**Qué lo viola.**  
Añadir una herramienta porque es popular. Crear una abstracción "por si acaso". Documentar algo que nadie va a leer.

---

## Relación entre principios

Los nueve principios no son independientes. Forman una jerarquía implícita:

```
P1 — Human Authority       ← base de todo lo demás
P2 — AI as Collaborator    ← define el rol de los agentes
P3 — Repository First      ← define dónde vive el conocimiento
P4 — Documentation         ← define cuándo está terminado algo
P5 — Determinism           ← define cómo se verifica
P6 — Replaceable Tools     ← define la independencia tecnológica
P7 — Context over Memory   ← define cómo interactúan los agentes
P8 — Validation            ← cierra cada ciclo de trabajo
P9 — Justified Complexity ← gobierno continuo del sistema
```

P1 es el principio raíz. Si P1 no se cumple, el resto pierde su base.  
P9 es el principio de mantenimiento. Si P9 no se cumple, el sistema crece sin control.

---

Los principios definidos en este documento constituyen el nivel más alto del modelo de gobierno de JES.

La arquitectura, los workflows, las reglas y las integraciones derivan de estos principios.

Ningún artefacto de ingeniería puede contradecirlos.

Si existe un conflicto, los principios prevalecen.

---

## Resolución de conflictos

Los principios están diseñados para ser complementarios.

Cuando parezcan entrar en conflicto, el ingeniero debe interpretar cuál preserva mejor el propósito de JES definido en SYSTEM_DEFINITION.md.

Los principios no deben aplicarse de forma aislada, sino como un sistema coherente.

---

*Versión: 2026.1 — Actualizado: julio 2026*
