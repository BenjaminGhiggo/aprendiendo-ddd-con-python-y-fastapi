# Capítulo 11 — Event-Driven Architecture: Microservicios

> Fase 1 · el libro (Parte II). Capítulo autocontenido (clase + `proyecto/` + `ejercicios/`).
> **Nota:** el libro usa **Redis** real; aquí se **simula** el canal pub/sub con un broker
> en memoria (`cola_externa.py`), porque este entorno no tiene servidor Redis. El concepto
> (eventos internos vs externos, Redis como adaptador fino) es idéntico.

---

## Micro-paso 1 — Eventos internos vs externos

### 0. 🧭 La pregunta
> *"Me piden integrar con otros servicios sin llamarlos directamente (para no acoplarnos).
> ¿Cómo aviso 'hacia afuera'?"*

### 2. Cita de la fuente
> *"Temporal Decoupling Using Asynchronous Messaging."* — Cap. 11.

### 4. Explicación paso a paso
1. Eventos internos (`Asignado`, `SinStock`) viajan por el bus.
2. Un handler `publicar_asignado_al_exterior` publica un evento EXTERNO al canal.

### 9. Preguntas de recuerdo
1. ¿Diferencia entre evento interno y externo?

---

## Micro-paso 2 — Redis como adaptador fino

### 2. Cita de la fuente
> *"Redis Is Another Thin Adapter Around Our Message Bus."* — Cap. 11.

### 4. Explicación paso a paso
1. Salida: `cola_externa.publicar(canal, datos)` (en real: `redis.publish`).
2. Entrada: `consumir_externo(mensaje, uow)` traduce un mensaje externo a un comando interno.
3. Tests con el broker simulado: al asignar se publica un externo; un mensaje externo se
   consume como comando. 29 passed.

### 5. Diagrama (Mermaid — Figura 11-1/11-2)
```mermaid
flowchart LR
    EXT1["mensaje externo"] --> AD1["consumir_externo (entrada)"]
    AD1 --> BUS["bus de mensajes"]
    BUS --> AD2["publicar (salida)"]
    AD2 --> EXT2["canal → otros servicios"]
```

### 6. Árbol de archivos
```
fase-1/capitulos/11-microservicios-eventos/proyecto/
├── cola_externa.py (broker simulado) · mensajeria.py (publicar/consumir) · ...
└── test_integracion_externa.py · ...
```

### 8. Comprobación
```bash
uv run pytest fase-1/capitulos/11-microservicios-eventos/proyecto/ -q      # 29 passed
```

### 9. Preguntas de recuerdo
1. ¿Qué hace el adaptador de entrada y el de salida?
2. ¿Por qué Redis es un adaptador "fino"?

---

> **Capítulo 11 completo.** Siguiente: **Capítulo 12 — CQRS**.
