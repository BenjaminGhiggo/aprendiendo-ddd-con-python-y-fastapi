# Ejercicio 3 — Separar decisión de I/O

> Cap. 3 · micro-paso 1 · refuerzo. Cita: *"Functional Core, Imperative Shell ... a
> 'core' of code that has no dependencies on external state."* — Cap. 3.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena**
([`solucion_buena/main.py`](solucion_buena/main.py)): la mala mezcla la lógica con el
efecto/entrada externa; la buena aísla un núcleo puro que recibe datos y devuelve datos. 🟢

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
