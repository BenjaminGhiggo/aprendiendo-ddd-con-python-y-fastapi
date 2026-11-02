# Ejercicio 3 — Dejar de pasar los mismos datos

> Lección 06 · refuerzo.

**Problema:**
1. Un lote tiene referencia y cantidad.
2. Necesitas `descripcion()` y `esta_vacio()`.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def descripcion(referencia, cantidad):
    return "Lote " + referencia + " con " + str(cantidad)

def esta_vacio(referencia, cantidad):
    return cantidad == 0

print(descripcion("LOTE-001", 20))
print(esta_vacio("LOTE-001", 20))
```
🔴 **Qué hace mal:** cada función recibe los mismos datos una y otra vez. Es fácil pasar
una referencia que no corresponde a esa cantidad.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad
    def descripcion(self):
        return "Lote " + self.referencia + " con " + str(self.cantidad)
    def esta_vacio(self):
        return self.cantidad == 0

lote = Lote("LOTE-001", 20)
print(lote.descripcion())
print(lote.esta_vacio())
```
🟢 **Qué mejoró:** los métodos ya conocen los datos del objeto por `self`. No hay que
pasarlos a cada rato.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
