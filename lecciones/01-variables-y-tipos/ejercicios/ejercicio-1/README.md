# Ejercicio 1 — El mismo nombre en varios mensajes

> Lección 01 · refuerzo.

**Problema:**
1. Muestra tres mensajes para una clienta llamada Ana:
   `Hola, Ana` · `Ana, tu pedido está listo` · `Gracias por tu compra, Ana`.
2. Si mañana la clienta es otra, el cambio debe hacerse en **un solo lugar**.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
print("Hola, Ana")
print("Ana, tu pedido está listo")
print("Gracias por tu compra, Ana")
```
🔴 **Qué hace mal:** el nombre está escrito a mano **tres veces**. Si la clienta cambia,
hay que editar tres líneas, y basta olvidar una para mostrar un nombre equivocado.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
nombre = "Ana"
print("Hola, " + nombre)
print(nombre + ", tu pedido está listo")
print("Gracias por tu compra, " + nombre)
```
🟢 **Qué mejoró:** el nombre vive en **una variable**. Cambiar `nombre = "Ana"` por otro
valor actualiza los tres mensajes a la vez.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
