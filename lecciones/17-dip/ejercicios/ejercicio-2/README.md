# Ejercicio 2 — El notificador se inyecta

> Lección 17 · refuerzo (DIP).

**Problema:**
1. Al comprar, enviar un aviso.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def avisar_compra():
    notificador = NotificadorEmail()
    notificador.enviar("Compra realizada")
```
🔴 **Qué hace mal:** el servicio crea el `NotificadorEmail` adentro. Cambiarlo por SMS
obliga a editar la función.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def avisar_compra(notificador):
    notificador.enviar("Compra realizada")

avisar_compra(NotificadorEmail())
avisar_compra(NotificadorSMS())
```
🟢 **Qué mejoró:** el notificador se inyecta. El servicio no depende de uno concreto.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
