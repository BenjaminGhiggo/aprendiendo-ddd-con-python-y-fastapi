# Ejercicio 4 (opcional) — Reto para ti ✍️

> Lección 09 · refuerzo. Lo resuelves tú.

**Problema:**
1. Clase `CuentaAhorro` con un saldo.
2. `depositar(monto)` suma al saldo; el saldo nunca debería quedar negativo.

**Tu turno:**
- Versión mala en [`solucion_mala/main.py`](solucion_mala/main.py) (saldo público modificable directo).
- Versión buena en [`solucion_buena/main.py`](solucion_buena/main.py) (saldo privado + métodos con regla).

**Para compararlas** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
