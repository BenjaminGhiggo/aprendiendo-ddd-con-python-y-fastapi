# Ejercicios de refuerzo — Capítulo 12 (CQRS)

| Micro-paso | Tema | Carpeta |
|---|---|---|
| 1 | CQS: leer y escribir son distintos | [micro-paso-1](micro-paso-1/) |
| 2 | CQRS: read model mantenido por eventos | [micro-paso-2](micro-paso-2/) |

Cada ejercicio trae una **solución mala** (funciona pero mezcla/ineficiente) y una
**solución buena** (separa reads de writes). Compáralas con:
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
