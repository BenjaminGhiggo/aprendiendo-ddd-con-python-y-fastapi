# Ejercicio 1 — Clasificar una edad

> Lección 02 · refuerzo. Cita (regla 6): *"When we allocate, if we have enough
> available quantity, we just add to the set."* — Cap. 1.

**Problema:**
1. Dada una `edad`, guarda en `resultado` el texto `"menor"` si es < 18, `"adulto"` entre 18
   y 64, y `"adulto mayor"` desde 65. Imprímelo.
2. Prueba con 10, 30 y 70 (cambia el valor y vuelve a ejecutar).

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
edad = 30
resultado = ""
if edad < 18:
    resultado = "menor"
if edad >= 18 and edad < 65:
    resultado = "adulto"
if edad >= 65:
    resultado = "adulto mayor"
print(resultado)
```
🔴 **Qué hace mal:** usa tres `if` separados, así que Python evalúa **todas** las
condiciones aunque una ya acertó; además repite la comparación `>= 18`.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
edad = 30
if edad < 18:
    resultado = "menor"
elif edad < 65:
    resultado = "adulto"
else:
    resultado = "adulto mayor"
print(resultado)
```
🟢 **Qué mejoró:** con `elif`, en cuanto una condición acierta **se detiene**; no repite
`>= 18`: si llegó al `elif`, ya se sabe que no es menor.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
