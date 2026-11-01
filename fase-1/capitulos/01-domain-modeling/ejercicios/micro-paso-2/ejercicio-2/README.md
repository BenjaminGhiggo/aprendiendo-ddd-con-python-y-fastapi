# Ejercicio 2 — Entidad por identidad

> Cap. 1 · micro-paso 2 · refuerzo. Cita (regla 6): *"an entity has attributes that may
> vary over time and it will still be the same entity."* — Cap. 1.

**Problema:** un lote es "el mismo" si comparte referencia, aunque cambie su stock.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
@dataclass
class Lote:
    referencia: str
    stock: int
print(Lote("L1",20) == Lote("L1",5))   # False
```
🔴 **Qué hace mal:** `@dataclass` compara por **todos** los campos; al cambiar el stock
"deja de ser el mismo lote". Trata una entidad como value object.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def __eq__(self, other):
    return isinstance(other, Lote) and other.referencia == self.referencia
def __hash__(self):
    return hash(self.referencia)
```
🟢 **Qué mejoró:** compara por **referencia** (identidad). Cambia el stock, sigue siendo
el mismo lote.

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
