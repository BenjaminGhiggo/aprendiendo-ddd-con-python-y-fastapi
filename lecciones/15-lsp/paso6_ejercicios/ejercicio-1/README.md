# Ejercicio 1 — Un falso que imita al real

> Lección 15 · refuerzo (LSP). Cita (regla 6): *"class FakeRepository(AbstractRepository):"* — Cap. 2.

**Problema:**
1. Un repo falso para pruebas, usable en lugar del real.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class RepoFalso:
    def obtener(self, ref):
        return "DUMMY"   # SIEMPRE devuelve algo, aunque no exista
```
🔴 **Qué hace mal:** el falso no se comporta como el real (el real devuelve `None` si no
está). Al sustituirlo, `existe(...)` da `True` cuando debería ser `False`: la prueba miente.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class RepoFalso:
    def __init__(self):
        self.datos = {}
    def obtener(self, ref):
        return self.datos.get(ref)   # mismo comportamiento que el real
```
🟢 **Qué mejoró:** el falso respeta el mismo contrato que el real, así que es
**sustituible** sin cambiar el resultado. Eso es LSP.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
