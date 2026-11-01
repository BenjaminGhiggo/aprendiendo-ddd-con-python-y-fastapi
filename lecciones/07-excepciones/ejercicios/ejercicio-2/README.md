# Ejercicio 2 — Atrapar solo lo esperado

> Lección 07 · refuerzo.

**Problema:**
1. `convertir_a_entero(texto)`: devuelve el número, o `0` si el texto no es un número.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def convertir_a_entero(texto):
    try:
        return int(texto)
    except:
        return 0
```
🔴 **Qué hace mal:** el `except:` sin tipo atrapa **cualquier** error (incluso un error
de programación tuyo), y lo esconde devolviendo `0`. Los bugs se vuelven invisibles.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def convertir_a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return 0
```
🟢 **Qué mejoró:** atrapa **solo** `ValueError` (texto no numérico). Cualquier otro error
sí sale a la luz, como debe ser.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
