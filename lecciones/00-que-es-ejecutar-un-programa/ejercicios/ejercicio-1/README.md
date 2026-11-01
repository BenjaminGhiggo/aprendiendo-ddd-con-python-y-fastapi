# Ejercicio 1 — Ficha de dirección

> Lección 00 · refuerzo. Cita (regla 6): *"the best way to learn about code is to code."*

**Problema:**
1. Muestra dos líneas: una con la calle, otra con la ciudad.
2. Formato: `Calle: Siempre Viva 742` y `Ciudad: Lima`.
3. Usa `print`.

**Solución mala (funciona)** — [`mala/solucion.py`](mala/solucion.py):
```python
print("Calle" + ":" + " " + "Siempre Viva 742")
print("Ciudad" + ":" + " " + "Lima")
```
🔴 **Qué hace mal:** parte un texto constante en muchos pedacitos y los pega con `+`.
Es más largo, más difícil de leer y fácil de equivocarse con los espacios.

**Solución buena** — [`buena/solucion.py`](buena/solucion.py):
```python
print("Calle: Siempre Viva 742")
print("Ciudad: Lima")
```
🟢 **Qué mejoró:** si el texto es fijo, va de una sola pieza entre comillas. Sin
concatenaciones inútiles.
