# Ejercicio 3 — Saludo del día

> Lección 14 · refuerzo (OCP).

**Problema:**
1. Devolver un saludo según el día de la semana.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def saludo(dia):
    if dia == "lunes":
        return "¡Ánimo, es lunes!"
    elif dia == "viernes":
        return "¡Por fin viernes!"
    else:
        return "Hola"
```
🔴 **Qué hace mal:** un `if` por cada día con mensaje especial; agregar uno obliga a editar
la función.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
SALUDOS = {"lunes": "¡Ánimo, es lunes!", "viernes": "¡Por fin viernes!"}

def saludo(dia):
    return SALUDOS.get(dia, "Hola")
```
🟢 **Qué mejoró:** los saludos especiales están en un diccionario. Agregar uno es una
entrada más, sin tocar `saludo`.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
