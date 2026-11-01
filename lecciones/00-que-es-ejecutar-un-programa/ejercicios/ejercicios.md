# Ejercicios de refuerzo — Lección 00 (¿Qué es ejecutar un programa?)

> Formato: **Problema** → **solución mala (funciona)** → **solución buena** (resalta
> lo que la mala hacía mal). Cita (regla 6): *"the best way to learn about code is to
> code."* (Preface → Example Code and Coding Along).
>
> Cada solución está también como `.py` ejecutable en esta carpeta.

---

## Ejercicio 1 — Ficha de dirección
**Problema:**
1. Muestra dos líneas: una con la calle, otra con la ciudad.
2. Formato: `Calle: Siempre Viva 742` y `Ciudad: Lima`.
3. Usa `print`.

**Solución mala (funciona)** — [`ej1_mala.py`](ej1_mala.py):
```python
print("Calle" + ":" + " " + "Siempre Viva 742")
print("Ciudad" + ":" + " " + "Lima")
```
🔴 **Qué hace mal:** parte un texto constante en muchos pedacitos y los pega con `+`.
Es más largo, más difícil de leer y fácil de equivocarse con los espacios.

**Solución buena** — [`ej1_buena.py`](ej1_buena.py):
```python
print("Calle: Siempre Viva 742")
print("Ciudad: Lima")
```
🟢 **Qué mejoró:** si el texto es fijo, va de una sola pieza entre comillas. Sin
concatenaciones inútiles.

---

## Ejercicio 2 — Un mensaje con comillas
**Problema:**
1. Muestra exactamente: `Ella gritó: "Alto!"` (con las comillas dobles incluidas).

**Solución mala (funciona)** — [`ej2_mala.py`](ej2_mala.py):
```python
print("Ella gritó: \"Alto!\"")
```
🔴 **Qué hace mal:** usa comillas dobles por fuera y por dentro, así que tiene que
"escapar" las de dentro con `\"`. Funciona, pero se lee feo y es fácil olvidar una barra.

**Solución buena** — [`ej2_buena.py`](ej2_buena.py):
```python
print('Ella gritó: "Alto!"')
```
🟢 **Qué mejoró:** usa **comillas simples por fuera**, así las dobles del texto van
tal cual, sin escapes.

---

## Ejercicio 3 — Una nota para ti mismo
**Problema:**
1. El programa muestra `Calculando...`.
2. Quieres dejar una nota recordatoria en el código, que **no** debe aparecer en pantalla.

**Solución mala (funciona)** — [`ej3_mala.py`](ej3_mala.py):
```python
print("Calculando...")
print("# recordar revisar esto luego")
```
🔴 **Qué hace mal:** mete la nota dentro de un `print`, así que **se imprime** como si
fuera salida del programa. El `#` ahí es solo texto, no un comentario.

**Solución buena** — [`ej3_buena.py`](ej3_buena.py):
```python
print("Calculando...")
# recordar revisar esto luego
```
🟢 **Qué mejoró:** la nota va como **comentario** con `#` fuera del `print`. Python la
ignora y **no** se muestra.

---

## Ejercicio 4 (opcional) — Reto para ti ✍️
Resuélvelo tú: escribe una **solución mala (que funcione)** y una **buena**.
Plantilla en [`ej4_reto.py`](ej4_reto.py).

**Problema:**
1. Muestra una mini factura en **dos líneas**.
2. Primera línea: `Producto: Mesa`.
3. Segunda línea: `Precio: "S/ 100"` (el monto entre comillas dobles).

> Cuando lo tengas, pásamelo y lo revisamos juntos (comparamos tu mala vs. tu buena).
