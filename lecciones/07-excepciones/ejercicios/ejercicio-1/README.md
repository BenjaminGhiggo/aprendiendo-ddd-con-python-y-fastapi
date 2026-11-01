# Ejercicio 1 — Señalar un error de verdad

> Lección 07 · refuerzo. Cita (regla 6): *"class OutOfStock(Exception):"* — Cap. 1,
> *Exceptions Can Express Domain Concepts Too*.

**Problema:**
1. `asignar(disponible, pedido)`: si piden más de lo que hay, avisar que no se pudo.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def asignar(disponible, pedido):
    if pedido > disponible:
        return -1
    return disponible - pedido
```
🔴 **Qué hace mal:** usa `-1` como "valor mágico" de error. Quien llama tiene que saber
que `-1` significa fallo; si lo olvida, trata el error como si fuera un stock real.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class SinStock(Exception):
    pass

def asignar(disponible, pedido):
    if pedido > disponible:
        raise SinStock("No hay stock suficiente")
    return disponible - pedido
```
🟢 **Qué mejoró:** el error se señala con una **excepción con nombre**. Es imposible
confundirlo con un resultado válido.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
