# Ejercicio 3 — No repetir el mismo cálculo

> Lección 04 · refuerzo.

**Problema:**
1. Calcula el área de tres cuadrados de lados 4, 5 y 6.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
lado1 = 4
area1 = lado1 * lado1
print(area1)
lado2 = 5
area2 = lado2 * lado2
print(area2)
lado3 = 6
area3 = lado3 * lado3
print(area3)
```
🔴 **Qué hace mal:** repite el mismo cálculo tres veces con variables numeradas. Si la
fórmula del área cambiara, habría que corregir cada bloque.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def area_cuadrado(lado):
    return lado * lado

print(area_cuadrado(4))
print(area_cuadrado(5))
print(area_cuadrado(6))
```
🟢 **Qué mejoró:** la fórmula vive en **una** función. Se llama con cada lado y se
corrige en un solo lugar.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
