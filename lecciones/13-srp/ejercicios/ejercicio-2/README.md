# Ejercicio 2 — Una función que hace de todo

> Lección 13 · refuerzo (SRP).

**Problema:**
1. A partir de un texto, validar que sea un número, convertirlo y formatear un mensaje.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def procesar_edad(texto):
    if not texto.isdigit():
        return "Edad inválida"
    edad = int(texto)
    return "Tienes " + str(edad) + " años"
```
🔴 **Qué hace mal:** una sola función valida, convierte y formatea. Si cambia cualquiera
de esas tres cosas, se toca la misma función, y no se pueden reutilizar por separado.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def es_numero(texto):
    return texto.isdigit()

def mensaje_edad(edad):
    return "Tienes " + str(edad) + " años"
```
🟢 **Qué mejoró:** cada responsabilidad en su función. Se combinan donde haga falta y se
reutilizan por separado.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
