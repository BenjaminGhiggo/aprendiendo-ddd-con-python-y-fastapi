# Ejercicio 3 — Notificadores con un contrato

> Lección 12 · refuerzo.

**Problema:**
1. Enviar un aviso por email y, más adelante, por SMS.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class NotificadorEmail:
    def enviar(self, msg):
        return "email: " + msg

def avisar(notificador, msg):
    return notificador.enviar(msg)
```
🔴 **Qué hace mal:** nada garantiza que un futuro `NotificadorSMS` tenga `enviar`. Si no
lo tiene, el error aparece en tiempo de ejecución, lejos de donde se definió.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, msg): ...

class NotificadorEmail(Notificador):
    def enviar(self, msg):
        return "email: " + msg
class NotificadorSMS(Notificador):
    def enviar(self, msg):
        return "sms: " + msg
```
🟢 **Qué mejoró:** el contrato `Notificador` garantiza que todos tengan `enviar`. El error
se detecta al crear la clase, no al ejecutarla.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
