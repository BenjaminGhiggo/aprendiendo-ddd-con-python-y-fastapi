# Ejercicio 2 — Que no se pueda olvidar implementar

> Lección 12 · refuerzo.

**Problema:**
1. Un repositorio "base" del que heredan otros. No debe poder usarse a medio hacer.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class RepositorioBase:
    def agregar(self, ref):
        pass

repo = RepositorioBase()
repo.agregar("L1")   # "funciona" pero no guarda nada: bug silencioso
```
🔴 **Qué hace mal:** la base tiene un método vacío y **se puede instanciar**. Si alguien
la usa por error, no guarda nada y nadie se entera.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

RepositorioAbstracto()   # TypeError: no se puede instanciar
```
🟢 **Qué mejoró:** con `@abstractmethod`, Python **impide** crear la abstracta y obliga a
implementar `agregar` en cada subclase.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
