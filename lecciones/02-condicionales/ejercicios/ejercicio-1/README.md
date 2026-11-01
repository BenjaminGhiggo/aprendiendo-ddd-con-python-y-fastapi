# Ejercicio 1 — Clasificar una edad

> Lección 02 · refuerzo. Cita (regla 6): *"When we allocate, if we have enough
> available quantity, we just add to the set."* — Cap. 1.

**Problema:**
1. Función `clasificar(edad)`.
2. Devuelve `"menor"` si <18, `"adulto"` entre 18 y 64, `"adulto mayor"` desde 65.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def clasificar(edad):
    resultado = ""
    if edad < 18:
        resultado = "menor"
    if edad >= 18 and edad < 65:
        resultado = "adulto"
    if edad >= 65:
        resultado = "adulto mayor"
    return resultado
```
🔴 **Qué hace mal:** usa tres `if` separados, así que Python evalúa **todas** las
condiciones aunque una ya acertó; repite comparaciones y usa una variable temporal.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def clasificar(edad):
    if edad < 18:
        return "menor"
    elif edad < 65:
        return "adulto"
    else:
        return "adulto mayor"
```
🟢 **Qué mejoró:** con `elif`, en cuanto una condición acierta **se detiene**; no repite
`>= 18` (ya se sabe por el orden) y devuelve directo.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
