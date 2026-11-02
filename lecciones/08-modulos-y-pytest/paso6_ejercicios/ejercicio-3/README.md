# Ejercicio 3 — Una prueba que de verdad comprueba

> Lección 08 · refuerzo.

**Problema:**
1. Función `doble(n)` que devuelva `n * 2`.
2. Escribe una prueba que **falle** si el resultado es incorrecto.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def doble(n):
    return n + n

print("doble(5):", doble(5))
```
🔴 **Qué hace mal:** "prueba" con un `print`. Aunque la función diera un resultado
equivocado, el programa **nunca falla**: solo muestra un número y tú tienes que notarlo.

**Solución buena** — [`solucion_buena/`](solucion_buena/) (`codigo.py` + `test_codigo.py`):
```python
# test_codigo.py
from codigo import doble

def test_doble():
    assert doble(5) == 10
```
🟢 **Qué mejoró:** el `assert` **falla** (FAILED) si el resultado no es el esperado. La
prueba realmente comprueba, no solo muestra. Córrelo con `uv run pytest solucion_buena -q`.
