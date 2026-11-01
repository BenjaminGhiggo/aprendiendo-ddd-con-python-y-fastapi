# Ejercicio 2 — Nombres de variables con significado

> Lección 01 · refuerzo. Cita (regla 6): *"We ... agree on a glossary and some rules
> ..."* — Cap. 1, *Exploring the Domain Language*. Las variables usan las palabras
> de ese glosario.

**Problema:**
1. Guarda en variables el producto (`Mesa`), su precio (`100`) y la cantidad (`3`).
2. Muéstralos en pantalla, cada uno con su etiqueta.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
x = "Mesa"
a = 100
b = 3
print("Producto: " + x)
print("Precio:")
print(a)
print("Cantidad:")
print(b)
```
🔴 **Qué hace mal:** `x`, `a` y `b` no dicen qué guardan. Para entender el código hay
que adivinar que `a` es el precio y `b` la cantidad, y es fácil confundirlas.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
producto = "Mesa"
precio = 100
cantidad = 3
print("Producto: " + producto)
print("Precio:")
print(precio)
print("Cantidad:")
print(cantidad)
```
🟢 **Qué mejoró:** cada variable se llama como el **concepto del negocio** que guarda.
El código se lee solo, sin adivinar.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
