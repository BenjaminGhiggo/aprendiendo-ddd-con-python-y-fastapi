# Ejercicio 2 — `list` vs `set` (idempotencia)

> Cap. 1 · micro-paso 3 · refuerzo.

**Problema:** registrar las líneas asignadas de un lote.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
self._asignaciones = []
def asignar(self, linea):
    self._asignaciones.append(linea)
```
🔴 **Qué hace mal:** una lista admite la misma línea dos veces, y el disponible se
descuadra.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
self._asignaciones = set()
def asignar(self, linea):
    self._asignaciones.add(linea)
```
🟢 **Qué mejoró:** el `set` descarta la línea repetida (gracias a la igualdad por valor
del value object). Asignar dos veces = una.

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
