# Ejercicio 2 — Devolver en vez de imprimir

> Lección 04 · refuerzo.

**Problema:**
1. Función `total_con_igv(precio)` que calcule el precio con 18% de IGV.
2. Debe poder **reutilizarse** (por ejemplo, sumar dos totales).

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def total_con_igv(precio):
    print(precio * 1.18)

total_con_igv(100)
```
🔴 **Qué hace mal:** la función **imprime** adentro y no **devuelve** nada. Solo sirve
para mostrar; no puedes usar el resultado (sumarlo, guardarlo, compararlo).

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def total_con_igv(precio):
    return precio * 1.18

print(total_con_igv(100))
print(total_con_igv(100) + total_con_igv(50))
```
🟢 **Qué mejoró:** la función **devuelve** el número. Quien la llama decide qué hacer:
imprimirlo, sumarlo, etc. Es mucho más reutilizable.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
