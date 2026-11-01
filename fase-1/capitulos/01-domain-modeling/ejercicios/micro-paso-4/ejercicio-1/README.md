# Ejercicio 1 — Método vs función de dominio

> Cap. 1 · micro-paso 4 · refuerzo. Cita (regla 6): *"A thing that allocates an order
> line, given a set of batches, sounds a lot like a function ... just make it a function."* — Cap. 1.

**Problema:** elegir, entre varios lotes, cuál asigna una línea.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Lote:
    def asignar_entre(self, otros_lotes, cantidad): ...
```
🔴 **Qué hace mal:** mete "conocer a los otros lotes" dentro de un `Lote`. Un lote no
debería saber de los demás; esa decisión no es su responsabilidad.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def asignar(cantidad, lotes):
    for lote in lotes: ...
```
🟢 **Qué mejoró:** "elegir entre lotes" es una **función** de dominio, no un método. Más
claro y sin responsabilidades fuera de lugar.

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
