# Ejercicio 3 — Recorrer sin contar a mano

> Lección 03 · refuerzo.

**Problema:**
1. Muestra cada nombre de la lista `["Ana", "Benjamin", "Carla"]`.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
nombres = ["Ana", "Benjamin", "Carla"]
i = 0
while i < 3:
    print(nombres[i])
    i = i + 1
```
🔴 **Qué hace mal:** usa un `while` con índice manual y el número `3` escrito a mano.
Es fácil equivocarse con el índice (bucle infinito, salirse de la lista) y el `3` queda
desactualizado si la lista cambia.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
nombres = ["Ana", "Benjamin", "Carla"]
for nombre in nombres:
    print(nombre)
```
🟢 **Qué mejoró:** el `for` recorre la lista directamente, sin índice ni contar a mano,
y se detiene solo al terminar.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
