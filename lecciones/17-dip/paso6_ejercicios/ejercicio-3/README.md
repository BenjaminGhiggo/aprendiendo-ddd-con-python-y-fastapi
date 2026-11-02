# Ejercicio 3 — Los datos entran por parámetro

> Lección 17 · refuerzo (DIP).

**Problema:**
1. Calcular el total de ventas.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def total_ventas():
    ventas = [100, 200, 300]
    return sum(ventas)
```
🔴 **Qué hace mal:** los datos están "cableados" dentro de la función. No se puede calcular
el total con otras ventas sin editarla.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def total_ventas(ventas):
    return sum(ventas)
```
🟢 **Qué mejoró:** los datos entran por parámetro. La lógica no depende de su origen y se
reutiliza con cualquier fuente.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
