# Ejercicio 3 — `puede_asignar` también mira el sku

> Cap. 1 · micro-paso 3 · refuerzo. Cita (regla 6): *"can_allocate ... self.sku ==
> line.sku and self.available_quantity >= line.qty"* — Cap. 1.

**Problema:** decidir si un lote puede asignar una línea.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def puede_asignar(self, sku_linea, cantidad_linea):
    return self.disponible >= cantidad_linea
```
🔴 **Qué hace mal:** solo comprueba la cantidad; ignora el `sku`. Asignaría un pedido de
TOSTADORA a un lote de MESA.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def puede_asignar(self, sku_linea, cantidad_linea):
    return self.sku == sku_linea and self.disponible >= cantidad_linea
```
🟢 **Qué mejoró:** comprueba `sku` **y** cantidad. No mezcla productos.

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
