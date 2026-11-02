# Ejercicio 2 — Buscar un precio

> Lección 05 · refuerzo.

**Problema:**
1. Busca y muestra el precio de "lampara".

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
productos = ["mesa", "silla", "lampara"]
precios = [100, 50, 30]
buscado = "lampara"
i = 0
while i < 3:
    if productos[i] == buscado:
        print(precios[i])
    i = i + 1
```
🔴 **Qué hace mal:** para encontrar un precio recorre toda la lista con un índice manual.
Mucho código para algo que debería ser directo.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
precios = {"mesa": 100, "silla": 50, "lampara": 30}
print(precios["lampara"])
```
🟢 **Qué mejoró:** el diccionario busca por clave en una línea. Sin bucle ni índices.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
