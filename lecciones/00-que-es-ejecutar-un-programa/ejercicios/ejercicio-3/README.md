# Ejercicio 3 — Una nota para ti mismo

> Lección 00 · refuerzo.

**Problema:**
1. El programa muestra `Calculando...`.
2. Quieres dejar una nota recordatoria en el código, que **no** debe aparecer en pantalla.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
print("Calculando...")
print("# recordar revisar esto luego")
```
🔴 **Qué hace mal:** mete la nota dentro de un `print`, así que **se imprime** como si
fuera salida del programa. El `#` ahí es solo texto, no un comentario.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
print("Calculando...")
# recordar revisar esto luego
```
🟢 **Qué mejoró:** la nota va como **comentario** con `#` fuera del `print`. Python la
ignora y **no** se muestra.
