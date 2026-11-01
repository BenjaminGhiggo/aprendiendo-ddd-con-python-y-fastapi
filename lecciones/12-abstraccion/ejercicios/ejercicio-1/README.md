# Ejercicio 1 — Un contrato común

> Lección 12 · refuerzo. Cita (regla 6): *"class AbstractRepository(abc.ABC):"* — Cap. 2.

**Problema:**
1. Dos repositorios (memoria y lista) que deberían guardar de la misma forma.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class RepoMemoria:
    def guardar(self, ref): ...
class RepoLista:
    def add(self, ref): ...
```
🔴 **Qué hace mal:** sin contrato, uno llama `guardar` y otro `add`. Quien los use tiene
que recordar el nombre de cada uno; es fácil equivocarse.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

class RepoMemoria(RepositorioAbstracto):
    def agregar(self, ref): ...
class RepoLista(RepositorioAbstracto):
    def agregar(self, ref): ...
```
🟢 **Qué mejoró:** la ABC obliga a ambos a tener `agregar`. Todos se usan igual.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
