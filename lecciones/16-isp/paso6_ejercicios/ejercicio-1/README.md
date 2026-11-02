# Ejercicio 1 — No obligar a implementar de más

> Lección 16 · refuerzo (ISP). Cita (regla 6): *"a repository is any object that has
> add(thing) and get(id) methods."* — Cap. 2.

**Problema:**
1. Impresoras, escáneres y multifuncionales.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Maquina(ABC):
    @abstractmethod
    def imprimir(self, doc): ...
    @abstractmethod
    def escanear(self, doc): ...
    @abstractmethod
    def enviar_fax(self, doc): ...
```
🔴 **Qué hace mal:** una interfaz gigante obliga a la `ImpresoraSimple` a implementar
`escanear` y `enviar_fax` que no hace (con `NotImplementedError`).

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Impresora(ABC):
    @abstractmethod
    def imprimir(self, doc): ...
class Escaner(ABC):
    @abstractmethod
    def escanear(self, doc): ...
```
🟢 **Qué mejoró:** interfaces pequeñas. La impresora simple implementa solo `Impresora`;
la multifuncional, `Impresora` y `Escaner`.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
