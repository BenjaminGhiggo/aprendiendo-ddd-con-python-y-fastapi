# Ejercicio 2 — Devolver un booleano

> Lección 02 · refuerzo.

**Problema:**
1. Función `es_mayor_de_edad(edad)` que devuelve `True` o `False`.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
```
🔴 **Qué hace mal:** usa un `if/else` entero solo para devolver `True`/`False`.
La comparación `edad >= 18` **ya es** un booleano: todo ese bloque sobra.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def es_mayor_de_edad(edad):
    return edad >= 18
```
🟢 **Qué mejoró:** se devuelve directamente el booleano de la comparación. Una línea,
sin `if/else` innecesario.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
