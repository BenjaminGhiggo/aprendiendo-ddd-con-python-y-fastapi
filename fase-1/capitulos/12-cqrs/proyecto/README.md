# Proyecto — Sistema de asignación (allocation) · snapshot Capítulo 12

Snapshot del proyecto al final del **Capítulo 12 (CQRS)**. Parte del código del
Capítulo 11 y le separa el **lado de lectura** del **lado de escritura**.

Novedades de este capítulo:
- `vistas.py` — el **lado de lectura**: funciones que solo responden preguntas (CQS).
- `orm.py` — añade la tabla **desnormalizada** `asignaciones_vista` (modelo de lectura).
- `mensajeria.py` — handlers `agregar_asignacion_a_vista` / `quitar_asignacion_de_vista`
  que mantienen el modelo de lectura al día cuando ocurren eventos.
- `api.py` — aplica **CQS**: el POST ya no devuelve la referencia (responde `202 {"ok": true}`),
  y hay un GET `/asignaciones/{id_pedido}` de solo lectura.
- `test_vistas.py` — test de integración del lado de lectura.

## Correr las pruebas
```bash
uv run pytest fase-1/capitulos/12-cqrs/proyecto/ -q      # 32 passed
```

## Glosario del dominio (lenguaje del negocio)
| Español (nuestro código) | Inglés (libro) | Qué es |
|---|---|---|
| LineaPedido | OrderLine | una línea de un pedido (sku + cantidad) |
| Lote | Batch | stock comprado que llega o está en almacén |
| asignar | allocate | reservar una línea contra un lote |
| asignaciones_vista | allocations_view | tabla desnormalizada para LEER rápido |
| vistas | views | el lado de lectura (CQS) |
