# Ejercicio 3 — Agregar a una lista

> Lección 05 · refuerzo.

**Problema:**
1. Tienes `["mesa", "silla"]` y quieres añadir `"lampara"`.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
productos = ["mesa", "silla"]
productos = ["mesa", "silla", "lampara"]
print(productos)
```
🔴 **Qué hace mal:** para agregar uno, **reescribe toda la lista** a mano. Con muchos
elementos es insostenible y propenso a errores.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
productos = ["mesa", "silla"]
productos.append("lampara")
print(productos)
```
🟢 **Qué mejoró:** `append` agrega al final sin tocar lo que ya había.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
