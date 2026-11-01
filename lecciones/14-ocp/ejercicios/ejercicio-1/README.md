# Ejercicio 1 — Descuentos sin tocar el núcleo

> Lección 14 · refuerzo (OCP). Cita (regla 6): *"...open for extension but closed for
> modification..."* — Cap. 1.

**Problema:**
1. Calcular el precio final según el descuento, y poder agregar descuentos nuevos.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def precio_final(precio, tipo):
    if tipo == "ninguno":
        return precio
    elif tipo == "normal":
        return precio * 0.9
    return precio
```
🔴 **Qué hace mal:** cada descuento nuevo obliga a **editar** `precio_final` con otro
`elif`. Se toca código que ya funcionaba.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def descuento_black_friday(precio):
    return precio * 0.5

def precio_final(precio, regla):
    return regla(precio)
```
🟢 **Qué mejoró:** `precio_final` queda **cerrado**; agregar `descuento_black_friday` es
solo **sumar** una función. Abierto a extensión, cerrado a modificación.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
