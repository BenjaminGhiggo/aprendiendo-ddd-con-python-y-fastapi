# Ejercicio 2 — Guardar un booleano

> Lección 02 · refuerzo.

**Problema:**
1. Dada una `edad`, guarda en `es_mayor_de_edad` el valor `True` o `False` e imprímelo.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
edad = 20
if edad >= 18:
    es_mayor_de_edad = True
else:
    es_mayor_de_edad = False
print(es_mayor_de_edad)
```
🔴 **Qué hace mal:** usa un `if/else` entero solo para guardar `True`/`False`.
La comparación `edad >= 18` **ya es** un booleano: todo ese bloque sobra.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
edad = 20
es_mayor_de_edad = edad >= 18
print(es_mayor_de_edad)
```
🟢 **Qué mejoró:** se guarda directamente el booleano de la comparación. Una línea,
sin `if/else` innecesario.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
