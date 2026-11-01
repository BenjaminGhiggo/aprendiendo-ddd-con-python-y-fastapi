# Ejercicio 3 — Datos y correos no son lo mismo

> Lección 13 · refuerzo (SRP).

**Problema:**
1. Un usuario tiene nombre y email, y se le envía un correo de bienvenida.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Usuario:
    def __init__(self, nombre, email): ...
    def enviar_bienvenida(self):
        print("Enviando correo a " + self.email)
```
🔴 **Qué hace mal:** `Usuario` guarda datos **y** envía correos. Si cambia cómo se mandan
los correos, hay que tocar la clase que modela al usuario.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Usuario:
    def __init__(self, nombre, email): ...

class ServicioCorreo:
    def enviar_bienvenida(self, usuario):
        print("Enviando correo a " + usuario.email)
```
🟢 **Qué mejoró:** `Usuario` solo tiene los datos; enviar correos vive en `ServicioCorreo`.
Cada uno cambia por su propia razón.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
