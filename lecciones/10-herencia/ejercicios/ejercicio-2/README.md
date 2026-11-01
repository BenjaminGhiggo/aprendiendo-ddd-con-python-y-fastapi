# Ejercicio 2 — Reutilizar el constructor del padre

> Lección 10 · refuerzo.

**Problema:**
1. `LoteUrgente` es un `Lote` con un dato extra: `prioridad`.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class LoteUrgente(Lote):
    def __init__(self, referencia, cantidad, prioridad):
        self.referencia = referencia
        self.cantidad = cantidad
        self.prioridad = prioridad
```
🔴 **Qué hace mal:** copia a mano lo que ya hace `Lote.__init__`. Si el padre agrega un
campo, la subclase se queda desincronizada.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class LoteUrgente(Lote):
    def __init__(self, referencia, cantidad, prioridad):
        super().__init__(referencia, cantidad)
        self.prioridad = prioridad
```
🟢 **Qué mejoró:** `super().__init__(...)` reutiliza el constructor del padre; la subclase
solo agrega lo nuevo.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
