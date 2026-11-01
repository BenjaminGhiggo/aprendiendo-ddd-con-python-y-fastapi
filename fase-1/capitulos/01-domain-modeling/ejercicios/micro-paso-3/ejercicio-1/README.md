# Ejercicio 1 — Disponible guardado vs calculado

> Cap. 1 · micro-paso 3 · refuerzo. Cita (regla 6): *"available_quantity is now a
> calculated property: purchased quantity minus allocated quantity."* — Cap. 1.

**Problema:** el stock disponible de un lote al asignar líneas.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def asignar(self, cantidad_linea):
    self.disponible -= cantidad_linea
```
🔴 **Qué hace mal:** resta siempre; no sabe si la línea ya estaba asignada. Asignar dos
veces la misma descuenta doble.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
@property
def disponible(self):
    return self._comprada - sum(l.cantidad for l in self._asignaciones)
```
🟢 **Qué mejoró:** disponible se **calcula** desde el `set` de líneas; la misma línea no
cuenta doble.

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
