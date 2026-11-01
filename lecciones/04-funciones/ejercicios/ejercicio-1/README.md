# Ejercicio 1 — Un saludo reutilizable

> Lección 04 · refuerzo. Cita (regla 6): *"def allocate(orderid: str, sku: str,
> qty: int, ...) -> str:"* — Cap. 4.

**Problema:**
1. Saluda a Ana, Benjamin y Carla con el mismo formato de bienvenida.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
print("Hola, Ana. ¡Bienvenida!")
print("Hola, Benjamin. ¡Bienvenido!")
print("Hola, Carla. ¡Bienvenida!")
```
🔴 **Qué hace mal:** el formato del saludo está escrito a mano en cada línea. Si quieres
cambiar "¡Bienvenido!" por otra cosa, editas las tres.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def saludar(nombre):
    return "Hola, " + nombre + ". ¡Bienvenido/a!"

print(saludar("Ana"))
print(saludar("Benjamin"))
print(saludar("Carla"))
```
🟢 **Qué mejoró:** el saludo se arma en **una** función. Un cambio en `saludar` afecta a
todos los saludos a la vez.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
