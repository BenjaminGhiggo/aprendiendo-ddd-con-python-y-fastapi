# Ejercicio 2 — Costo de envío por país

> Lección 14 · refuerzo (OCP).

**Problema:**
1. Devolver el costo de envío según el país, y poder sumar países nuevos.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def costo_envio(pais):
    if pais == "PE":
        return 10
    elif pais == "CL":
        return 15
    return 0
```
🔴 **Qué hace mal:** cada país nuevo es otro `elif` dentro de la función.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
COSTOS = {"PE": 10, "CL": 15}

def costo_envio(pais):
    return COSTOS.get(pais, 0)
```
🟢 **Qué mejoró:** los costos viven en una tabla. Agregar un país es añadir una entrada,
sin tocar la función.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
