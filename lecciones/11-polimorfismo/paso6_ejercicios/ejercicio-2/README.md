# Ejercicio 2 — El sonido de cada animal

> Lección 11 · refuerzo.

**Problema:**
1. Un perro hace "Guau" y un gato "Miau".

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def sonido(animal):
    if animal.tipo == "perro":
        return "Guau"
    elif animal.tipo == "gato":
        return "Miau"
```
🔴 **Qué hace mal:** decide el sonido con un `if` según un campo `tipo`. Cada animal nuevo
suma otro `elif`.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Perro:
    def sonido(self):
        return "Guau"
class Gato:
    def sonido(self):
        return "Miau"

for animal in [Perro(), Gato()]:
    print(animal.sonido())
```
🟢 **Qué mejoró:** cada clase define su `sonido()`. Nada de `if` por tipo.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
