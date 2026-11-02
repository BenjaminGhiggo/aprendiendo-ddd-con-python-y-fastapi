# Ejercicio 4 (opcional) — Reto para ti ✍️

> Lección 16 · refuerzo (ISP). Lo resuelves tú.

**Problema:**
1. Dispositivos: unos solo reproducen audio, otros audio y video.
2. Un reproductor de solo audio no debería tener que implementar video.

**Tu turno:**
- Versión mala en [`solucion_mala/main.py`](solucion_mala/main.py) (una interfaz con audio y video juntos).
- Versión buena en [`solucion_buena/main.py`](solucion_buena/main.py) (interfaces `Audio` y `Video` separadas).

**Para compararlas** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
