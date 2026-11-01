# Ejercicio 3 — Un contador que solo sube

> Lección 09 · refuerzo.

**Problema:**
1. Un contador empieza en 0 y solo debería poder incrementarse.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Contador:
    def __init__(self):
        self.valor = 0

c = Contador()
c.valor = -5
print(c.valor)
```
🔴 **Qué hace mal:** `valor` es público; cualquiera lo pone en `-5`, algo que un contador
nunca debería permitir.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Contador:
    def __init__(self):
        self._valor = 0
    def valor(self):
        return self._valor
    def incrementar(self):
        self._valor = self._valor + 1
```
🟢 **Qué mejoró:** el valor es privado y solo cambia por `incrementar()`. No hay forma de
dejarlo en un estado inválido.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
