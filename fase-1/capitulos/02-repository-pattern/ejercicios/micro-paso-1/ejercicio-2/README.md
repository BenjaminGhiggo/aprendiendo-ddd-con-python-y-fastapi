# Ejercicio 2 — El fake debe cumplir el contrato

> Cap. 2 · micro-paso 1 · refuerzo.

**Problema:** un repo falso para pruebas que obtenga por referencia.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): `obtener` devuelve siempre
el primero. 🔴 No imita al real; las pruebas mienten (LSP roto).

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): `obtener` busca por la
referencia. 🟢 Intercambiable con el real.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
