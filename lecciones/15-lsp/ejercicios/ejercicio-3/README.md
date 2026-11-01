# Ejercicio 3 — No romper lo que promete el padre

> Lección 15 · refuerzo (LSP).

**Problema:**
1. Patos que hacen sonido; poder juntarlos en un "coro".

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class PatoDeHule(Pato):
    def hacer_sonido(self):
        raise Exception("¡Soy de hule, no sueno!")
```
🔴 **Qué hace mal:** `PatoDeHule` hereda de `Pato` pero **rompe** lo que `Pato` promete
(hacer un sonido). Al meterlo en el coro, revienta. No es sustituible.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class PatoBebe(Pato):
    def hacer_sonido(self):
        return "cuac suave"
```
🟢 **Qué mejoró:** toda subclase de `Pato` sigue cumpliendo su promesa (devolver un
sonido). Cualquiera es sustituible por `Pato`.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
