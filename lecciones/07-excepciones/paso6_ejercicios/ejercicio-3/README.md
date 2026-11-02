# Ejercicio 3 — Que el error no se pueda ignorar

> Lección 07 · refuerzo.

**Problema:**
1. `dividir(a, b)`: no se puede dividir entre cero.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def dividir(a, b):
    if b == 0:
        return None
    return a / b
```
🔴 **Qué hace mal:** devuelve `None` en el error. Si quien llama olvida chequear `None`,
el programa sigue con un valor inválido y falla más adelante, lejos del origen.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
```
🟢 **Qué mejoró:** con `raise`, el error **detiene** la ejecución hasta que alguien lo
maneje. No se puede ignorar por accidente.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
