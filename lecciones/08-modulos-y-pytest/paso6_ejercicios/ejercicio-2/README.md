# Ejercicio 2 — Separar el módulo de su prueba

> Lección 08 · refuerzo.

**Problema:**
1. Función `total(precios)` que sume una lista.
2. Organiza código y prueba.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def total(precios):
    return sum(precios)

print(total([10, 20, 30]))   # miro si sale 60
```
🔴 **Qué hace mal:** la lógica y la "prueba" (un `print`) están mezcladas en el mismo
archivo, y la comprobación es manual.

**Solución buena** — [`solucion_buena/`](solucion_buena/) (`tienda.py` + `test_tienda.py`):
```python
# test_tienda.py
from tienda import total

def test_suma_los_precios():
    assert total([10, 20, 30]) == 60

def test_lista_vacia_es_cero():
    assert total([]) == 0
```
🟢 **Qué mejoró:** el **módulo** (`tienda.py`) tiene la lógica, el **test** la comprueba
por separado y con varios casos. Córrelo con `uv run pytest solucion_buena -q`.
