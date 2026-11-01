# Ejercicio 3 — Identidad en un `set`

> Cap. 1 · micro-paso 2 · refuerzo.

**Problema:** meter dos veces "el mismo lote" (misma referencia) en un `set`.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
@dataclass(frozen=True)
class Lote:
    referencia: str
    stock: int
lotes = {Lote("L1",20), Lote("L1",5)}
print(len(lotes))   # 2
```
🔴 **Qué hace mal:** el `dataclass` calcula el hash por todos los campos, así que el mismo
lote con distinto stock cuenta como **dos**.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def __eq__(self, other):
    return isinstance(other, Lote) and other.referencia == self.referencia
def __hash__(self):
    return hash(self.referencia)
```
🟢 **Qué mejoró:** `__hash__` por referencia; el `set` lo cuenta **una** vez. (Esto es lo
que hace que asignar la misma línea dos veces no duplique.)

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
