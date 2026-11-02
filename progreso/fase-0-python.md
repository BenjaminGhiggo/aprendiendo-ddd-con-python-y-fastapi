# Fase 0 — Python desde cero

> No está en el libro: es el cimiento (regla 5) para poder leerlo.
> 🏠 [Inicio](../README.md) · 📖 [Cómo estudiar](../COMO-ESTUDIAR.md) · 📚 [Índice de lecciones](../lecciones/README.md)

Este archivo tiene **dos partes** que no hay que confundir:

1. **Mi avance (lo marcas tú)**: lo que **tú ya estudiaste** y su semáforo.
2. **Material construido**: si la lección **ya está escrita** en el repo (lo mantiene el asistente).

---

## 1. Mi avance (lo marcas tú)

Al terminar una lección, mira su **semáforo 🚦** (§16 de su README). Cambia ⬜ por ✅ en
*Estudiada*, anota el color, cuántos problemas acertaste y la fecha, y haz commit:
```bash
git add progreso/fase-0-python.md
git commit -m "avance: lección NN en verde"
```

| Orden | Lección | Estudiada | Semáforo (🟢/🟡/🔴) | Problemas acertados (/12) | Fecha |
|:-:|---|:-:|:-:|:-:|---|
| 1 | 00 · ¿Qué es ejecutar un programa? | ⬜ | | | |
| 2 | 01 · Variables y tipos | ⬜ | | | |
| 3 | 02 · Condicionales | ⬜ | | | |
| 4 | 03 · Bucles | ⬜ | | | |
| 5 | 04 · Funciones | ⬜ | | | |
| 6 | 05 · Listas y diccionarios | ⬜ | | | |
| 7 | 06 · Clases y objetos | ⬜ | | | |
| 8 | 07 · Excepciones | ⬜ | | | |
| 9 | 08 · Módulos, `uv` y primer pytest | ⬜ | | | |
| 10 | 09 · Encapsulación | ⬜ | | | |
| 11 | 10 · Herencia | ⬜ | | | |
| 12 | 11 · Polimorfismo | ⬜ | | | |
| 13 | 12 · Abstracción | ⬜ | | | |
| 14 | 13 · SRP | ⬜ | | | |
| 15 | 14 · OCP | ⬜ | | | |
| 16 | 15 · LSP | ⬜ | | | |
| 17 | 16 · ISP | ⬜ | | | |
| 18 | 17 · DIP ⭐ | ⬜ | | | |

> Si quedaste en 🟡 o 🔴, deja ⬜ en *Estudiada* pero anota el color: así ves tu progreso.

---

## 2. Material construido (lo mantiene el asistente)

Cada lección está en formato **formulario** (README paso 0 + `paso1`…`paso6`) y se marca
✅ cuando su material está escrito y **verificado** (todos los scripts corren, claves sacadas
de la salida real, Mermaid válido, citas comprobadas contra la fuente).

### Python básico (00–08)
- [ ] **00 — ¿Qué es ejecutar un programa?** (instalar Python + `uv`)
- [ ] **01 — Variables y tipos**
- [ ] **02 — Condicionales (`if`/`else`)**
- [ ] **03 — Bucles (`for`/`while`)**
- [ ] **04 — Funciones**
- [x] **05 — Listas y diccionarios** — ✅ formulario (14 + 11 fórmulas, 12 problemas)
- [ ] **06 — Clases y objetos** (clase→instancia→objeto→uso, §3.6; Figura 1-3)
- [ ] **07 — Excepciones**
- [ ] **08 — Módulos, entorno con `uv` y primer `pytest`**

### Programación Orientada a Objetos (POO) — a fondo
> Continúa desde la Lección 06 (Clases y objetos). Base del modelo de dominio del libro.

- [ ] **09 — Encapsulación** (proteger el estado del objeto)
- [ ] **10 — Herencia** (reutilizar/extender una clase)
- [ ] **11 — Polimorfismo** (misma interfaz, distintos comportamientos)
- [ ] **12 — Abstracción** (clases abstractas, `ABC`)

### SOLID — los 5 principios (foco en SRP y DIP, los que usa el libro)
> La Introducción del libro trata Encapsulation/Abstractions, Layering y el DIP.

- [ ] **13 — SRP** (Responsabilidad única)
- [ ] **14 — OCP** (Abierto/Cerrado)
- [ ] **15 — LSP** (Sustitución de Liskov)
- [ ] **16 — ISP** (Segregación de interfaces)
- [ ] **17 — DIP** (Inversión de dependencias) ⭐ clave para el libro

## Bitácora de preguntas (§3.5)
| Fecha | Lección | La pregunta (W → X) |
|-------|---------|---------------------|
|       |         |                     |
