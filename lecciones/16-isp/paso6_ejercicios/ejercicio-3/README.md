# Ejercicio 3 — Trabajar y cobrar no siempre van juntos

> Lección 16 · refuerzo (ISP).

**Problema:**
1. Empleados (trabajan y cobran) y voluntarios (solo trabajan).

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self): ...
    @abstractmethod
    def cobrar_sueldo(self): ...
```
🔴 **Qué hace mal:** `Voluntario` se ve obligado a implementar `cobrar_sueldo`, aunque no
cobra, y tiene que lanzar `NotImplementedError`.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Trabaja(ABC):
    @abstractmethod
    def trabajar(self): ...
class Cobra(ABC):
    @abstractmethod
    def cobrar_sueldo(self): ...
```
🟢 **Qué mejoró:** se separan las capacidades. El voluntario implementa solo `Trabaja`;
el empleado, `Trabaja` y `Cobra`.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
