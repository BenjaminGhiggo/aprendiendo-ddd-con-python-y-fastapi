# Ejercicio 1 — Área sin preguntar el tipo

> Lección 11 · refuerzo. Cita (regla 6): *"To a Pythonista, a repository is any
> object that has add(thing) and get(id) methods."* — Cap. 2.

**Problema:**
1. Calcular el área de un cuadrado y un círculo.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def area(figura):
    if isinstance(figura, Cuadrado):
        return figura.lado * figura.lado
    elif isinstance(figura, Circulo):
        return 3.14 * figura.radio * figura.radio
```
🔴 **Qué hace mal:** un `if` por cada tipo de figura. Agregar un triángulo obliga a tocar
esta función. No escala.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Cuadrado:
    def area(self):
        return self.lado * self.lado
class Circulo:
    def area(self):
        return 3.14 * self.radio * self.radio

for figura in [Cuadrado(4), Circulo(3)]:
    print(figura.area())
```
🟢 **Qué mejoró:** cada figura sabe calcular su área. El código que las usa llama
`figura.area()` sin preguntar el tipo (polimorfismo).

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
