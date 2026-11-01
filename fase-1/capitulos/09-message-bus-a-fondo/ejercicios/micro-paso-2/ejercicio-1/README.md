# Ejercicio 1 — Registrar evento de reasignación

> Cap. 9 · micro-paso 2 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala reasigna a mano en el handler; la buena registra un evento y el bus reasigna.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
