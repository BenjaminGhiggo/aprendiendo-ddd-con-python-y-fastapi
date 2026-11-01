# Ejercicio 1 — El adaptador cumple el contrato

> Cap. 2 · micro-paso 3 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): el adaptador llama al método
`guardar` en vez de `agregar`. 🔴 El código que espera el contrato (`agregar`) no funciona.

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): implementa `agregar`. 🟢
Intercambiable con cualquier repositorio del contrato.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
