# Proyecto — Sistema de asignación (allocation)

Este es el **proyecto único que crece** de la Fase 1 (§4 de la metodología): el
sistema de *allocation* del libro *Architecture Patterns with Python*, construido
capítulo a capítulo con **TDD**.

- `modelo.py` — el modelo de dominio (crece con cada capítulo).
- `test_modelo.py` — las pruebas del dominio.
- La **explicación** de cada capítulo (la clase) está en `../capitulos/NN-nombre/`.

## Correr las pruebas
```bash
uv run pytest fase-1/proyecto/ -q
```

## Glosario del dominio (lenguaje del negocio)
| Español (nuestro código) | Inglés (libro) | Qué es |
|---|---|---|
| LineaPedido | OrderLine | una línea de un pedido (sku + cantidad) |
| Lote | Batch | stock comprado que llega o está en almacén |
| asignar | allocate | reservar una línea contra un lote |
| cantidad_disponible | available_quantity | lo que queda libre en el lote |
