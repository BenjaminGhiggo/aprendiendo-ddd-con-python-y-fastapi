# Ejercicio 2 — Cuadrado no es un Rectángulo (sustituible)

> Lección 15 · refuerzo (LSP).

**Problema:**
1. Modelar rectángulo y cuadrado y calcular áreas.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
```
🔴 **Qué hace mal:** hereda `Cuadrado` de `Rectangulo`, pero una función que "ensancha"
un rectángulo (cambia solo el ancho) deja al cuadrado en un estado incoherente. El
cuadrado **no** es sustituible por un rectángulo.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Rectangulo:
    def area(self): return self.ancho * self.alto
class Cuadrado:
    def area(self): return self.lado * self.lado
```
🟢 **Qué mejoró:** no se fuerza una herencia que rompe la expectativa. Cada forma es su
clase, y se usan por su interfaz común (`area()`).

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
