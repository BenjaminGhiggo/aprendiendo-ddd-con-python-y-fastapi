# Ejercicio 3 — No repetir la condición

> Lección 02 · refuerzo.

**Problema:**
1. Función `total_a_pagar(monto)`: si el monto es ≥ 100, avisa "Aplica descuento" y
   cobra el 90%; si no, cobra el monto completo.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def total_a_pagar(monto):
    if monto >= 100:
        print("Aplica descuento")
    if monto >= 100:
        return monto * 0.9
    return monto
```
🔴 **Qué hace mal:** evalúa `monto >= 100` **dos veces**. Si mañana cambia el umbral,
hay que acordarse de tocarlo en los dos sitios.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def total_a_pagar(monto):
    if monto >= 100:
        print("Aplica descuento")
        return monto * 0.9
    else:
        return monto
```
🟢 **Qué mejoró:** una sola decisión agrupa todo lo que pasa cuando hay descuento.
La condición vive en un solo lugar.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
