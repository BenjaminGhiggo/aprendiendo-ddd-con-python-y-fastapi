# Ejercicio 2 — Sumar una lista de precios

> Lección 03 · refuerzo.

**Problema:**
1. Suma los precios `[10, 20, 30]` y muestra el total.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
precios = [10, 20, 30]
total = precios[0] + precios[1] + precios[2]
print(total)
```
🔴 **Qué hace mal:** suma por posiciones fijas (`[0]`, `[1]`, `[2]`). Si la lista tiene
2 o 5 precios, da mal o se rompe.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
precios = [10, 20, 30]
total = 0
for precio in precios:
    total = total + precio
print(total)
```
🟢 **Qué mejoró:** el `for` acumula sumando uno por uno. Funciona con **cualquier**
cantidad de precios.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
