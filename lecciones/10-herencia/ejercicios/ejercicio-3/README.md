# Ejercicio 3 — Extender un método, no reescribirlo

> Lección 10 · refuerzo.

**Problema:**
1. `Gerente` saluda como un `Empleado` pero añadiendo "y soy gerente".

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Gerente(Empleado):
    def saludo(self):
        return "Hola, soy " + self.nombre + " y soy gerente"
```
🔴 **Qué hace mal:** reescribe el saludo del padre entero. Si el saludo base cambia, hay
que copiar el cambio aquí también.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Gerente(Empleado):
    def saludo(self):
        return super().saludo() + " y soy gerente"
```
🟢 **Qué mejoró:** `super().saludo()` reutiliza el saludo del padre y solo le suma lo nuevo.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
