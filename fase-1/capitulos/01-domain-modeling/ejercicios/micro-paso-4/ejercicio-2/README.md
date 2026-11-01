# Ejercicio 2 — `return None` vs `raise`

> Cap. 1 · micro-paso 4 · refuerzo. Cita (regla 6): *"class OutOfStock(Exception): pass
> ... raise OutOfStock(...)"* — Cap. 1.

**Problema:** qué hacer cuando ningún lote puede asignar.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def asignar(cantidad, lotes):
    ...
    return None
```
🔴 **Qué hace mal:** devuelve `None` en el error. Si quien llama no chequea, el programa
sigue como si se hubiera asignado.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
raise SinStock(f"Sin stock para el sku {sku}")
```
🟢 **Qué mejoró:** una excepción de dominio con nombre del negocio; el error no se puede
ignorar por accidente.

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
