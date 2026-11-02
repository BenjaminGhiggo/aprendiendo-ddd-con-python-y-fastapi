# Ejercicio 3 — ¿Número o texto?

> Lección 01 · refuerzo.

**Problema:**
1. Guarda el stock de un producto: `20` unidades.
2. Ese dato se usará más adelante para **comparar** (¿hay suficiente?).
3. Muéstralo y comprueba su tipo con `type()`.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
stock = "20"
print(stock)        # 20
print(type(stock))  # <class 'str'>
```
🔴 **Qué hace mal:** guarda la cantidad **entre comillas**, o sea como **texto** (`str`).
En pantalla se ve igual (`20`), pero no es un número. En cuanto quieras compararlo
(lo harás en la Lección 02), falla:
```
>>> "20" >= 18
TypeError: '>=' not supported between instances of 'str' and 'int'
```

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
stock = 20
print(stock)        # 20
print(type(stock))  # <class 'int'>
```
🟢 **Qué mejoró:** una cantidad se guarda **sin comillas**, como número entero (`int`).
`type()` lo confirma, y luego se podrá comparar sin errores.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
