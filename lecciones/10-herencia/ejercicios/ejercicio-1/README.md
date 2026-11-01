# Ejercicio 1 — Clases casi iguales

> Lección 10 · refuerzo. Cita (regla 6): *"class FakeRepository(AbstractRepository):"* — Cap. 2.

**Problema:**
1. `Perro` y `Gato`, ambos con nombre y un método `describir()` idéntico.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    def describir(self):
        return self.nombre + " es un animal"

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
    def describir(self):
        return self.nombre + " es un animal"
```
🔴 **Qué hace mal:** el mismo código está duplicado en las dos clases. Un cambio en
`describir` hay que hacerlo dos veces.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def describir(self):
        return self.nombre + " es un animal"

class Perro(Animal):
    pass

class Gato(Animal):
    pass
```
🟢 **Qué mejoró:** lo común vive en `Animal`; `Perro` y `Gato` lo heredan. Cero duplicación.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
