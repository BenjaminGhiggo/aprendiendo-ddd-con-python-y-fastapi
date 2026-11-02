# Ejercicio 1 — Comprobar con pytest, no a ojo

> Lección 08 · refuerzo. Cita (regla 6): *"We use TDD at work, so we tend to show
> listings of tests first, followed by implementation."* — Preface.

**Problema:**
1. Función `es_par(n)` que diga si un número es par.
2. Comprueba que funciona.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def es_par(n):
    return n % 2 == 0

print("es_par(4) ->", es_par(4), "(debería ser True)")
print("es_par(7) ->", es_par(7), "(debería ser False)")
```
🔴 **Qué hace mal:** la comprobación es **mirar la salida a ojo**. Si un día cambias el
código y rompes algo, nadie te avisa: tienes que acordarte de leer cada número.

**Solución buena** — [`solucion_buena/`](solucion_buena/) (`codigo.py` + `test_codigo.py`):
```python
# test_codigo.py
from codigo import es_par

def test_par():
    assert es_par(4) is True

def test_impar():
    assert es_par(7) is False
```
🟢 **Qué mejoró:** `pytest` ejecuta las comprobaciones **automáticamente** y marca
`FAILED` si algo deja de cumplirse. Córrelo con:
```bash
uv run pytest solucion_buena -q
```
