# Ejercicio 1 — Producto y su precio

> Lección 05 · refuerzo. Cita (regla 6): *"HANDLERS = { events.OutOfStock:
> [send_out_of_stock_notification] }"* — Cap. 8.

**Problema:**
1. Guarda productos y sus precios, y muestra cuánto cuesta la silla.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
productos = ["mesa", "silla", "lampara"]
precios = [100, 50, 30]
print(productos[1], "cuesta", precios[1])
```
🔴 **Qué hace mal:** usa **dos listas paralelas** que hay que mantener sincronizadas por
posición. Si una se desordena, "silla" queda con el precio equivocado.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
precios = {"mesa": 100, "silla": 50, "lampara": 30}
print("silla", "cuesta", precios["silla"])
```
🟢 **Qué mejoró:** un diccionario une producto y precio en un solo lugar. Se consulta
por nombre, sin depender de posiciones.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
