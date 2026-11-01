# Ejercicio 2 — Un mensaje con comillas

> Lección 00 · refuerzo.

**Problema:**
1. Muestra exactamente: `Ella gritó: "Alto!"` (con las comillas dobles incluidas).

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
print("Ella gritó: \"Alto!\"")
```
🔴 **Qué hace mal:** usa comillas dobles por fuera y por dentro, así que tiene que
"escapar" las de dentro con `\"`. Funciona, pero se lee feo y es fácil olvidar una barra.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
print('Ella gritó: "Alto!"')
```
🟢 **Qué mejoró:** usa **comillas simples por fuera**, así las dobles del texto van
tal cual, sin escapes.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
