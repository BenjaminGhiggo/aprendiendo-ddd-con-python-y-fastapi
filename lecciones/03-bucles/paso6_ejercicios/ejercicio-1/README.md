# Ejercicio 1 — Saludar a varias personas

> Lección 03 · refuerzo. Cita (regla 6): *"batch = next(b for b in sorted(batches)
> if b.can_allocate(line))"* — Cap. 1.

**Problema:**
1. Saluda a Ana, Benjamin y Carla, cada uno en su línea.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
print("Hola, Ana")
print("Hola, Benjamin")
print("Hola, Carla")
```
🔴 **Qué hace mal:** un `print` copiado por persona. Si la lista crece a 100 nombres,
son 100 líneas; si cambia el saludo, hay que editarlas todas.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
nombres = ["Ana", "Benjamin", "Carla"]
for nombre in nombres:
    print("Hola, " + nombre)
```
🟢 **Qué mejoró:** un `for` repite la misma instrucción por cada elemento. Agregar o
quitar nombres solo cambia la lista.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
