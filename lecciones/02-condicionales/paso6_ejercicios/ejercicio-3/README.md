# Ejercicio 3 — No repetir la condición

> Lección 02 · refuerzo.

**Problema:**
1. Dado un `monto`: si es ≥ 100, avisa "Aplica descuento" y el `total` es el 90%; si no,
   el `total` es el monto completo. Imprime el total.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
monto = 100
total = monto
if monto >= 100:
    print("Aplica descuento")
if monto >= 100:
    total = monto * 0.9
print(total)
```
🔴 **Qué hace mal:** evalúa `monto >= 100` **dos veces**. Si mañana cambia el umbral,
hay que acordarse de tocarlo en los dos sitios.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
monto = 100
if monto >= 100:
    print("Aplica descuento")
    total = monto * 0.9
else:
    total = monto
print(total)
```
🟢 **Qué mejoró:** una sola decisión agrupa todo lo que pasa cuando hay descuento.
La condición vive en un solo lugar.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
