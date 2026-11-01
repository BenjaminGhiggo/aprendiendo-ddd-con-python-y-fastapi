# Ejercicio 3 — Cáscara imperativa

> Cap. 3 · micro-paso 2 · refuerzo. Cita: *"gather inputs, call our logic, apply outputs."* — Cap. 3.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena**
([`solucion_buena/main.py`](solucion_buena/main.py)): la mala mezcla leer/decidir/aplicar
o mete reglas de negocio en la cáscara; la buena separa el núcleo (decide) de la cáscara (aplica). 🟢

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
