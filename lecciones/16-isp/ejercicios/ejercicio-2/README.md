# Ejercicio 2 — Un reporte que solo lee

> Lección 16 · refuerzo (ISP).

**Problema:**
1. Un reporte que solo necesita leer datos.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def reporte(repo):
    return "Reporte: " + str(repo.obtener("L1"))
```
🔴 **Qué hace mal:** el reporte recibe un repositorio **completo** (con `agregar`,
`borrar`…) aunque solo use `obtener`. Queda acoplado a métodos que no le incumben.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Lector(ABC):
    @abstractmethod
    def obtener(self, ref): ...

def reporte(lector: Lector):
    return "Reporte: " + str(lector.obtener("L1"))
```
🟢 **Qué mejoró:** el reporte depende solo de `Lector` (la interfaz pequeña que necesita).

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
