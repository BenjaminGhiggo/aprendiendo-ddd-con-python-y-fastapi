# Aprendiendo DDD con Python y FastAPI

Aprendizaje guiado **desde cero en Python** hasta los patrones de arquitectura
(DDD, TDD, arquitectura dirigida por eventos) del libro
*Architecture Patterns with Python* de Harry Percival y Bob Gregory
([Cosmic Python](https://www.cosmicpython.com/)), adaptando los ejemplos de
**Flask a FastAPI**.

## Cómo está organizado

```
aprendiendo-ddd-con-python-y-fastapi/
├── README.md
├── METODOLOGIA.md          # las 9 reglas del aprendizaje
├── CLAUDE.md               # para que el asistente siga la metodología
├── docs/
│   └── fuente/
│       ├── Architecture-Patterns-with-Python.md   # fuente citable
│       └── Architecture-Patterns-with-Python.pdf  # PDF generado del .md
└── lecciones/              # cada lección en lecciones/NN-nombre/
```

## Metodología

El detalle completo está en [`METODOLOGIA.md`](METODOLOGIA.md). En resumen:
primero Python, luego arquitectura; cada patrón se introduce **cuando el
proyecto empieza a doler**, siempre justificado y **citando la fuente**, con
pasos numerados, árbol de archivos, diagramas Mermaid, dependencias con `uv` y
FastAPI en lugar de Flask.

## Herramientas

- **Python 3.12+**
- [**uv**](https://docs.astral.sh/uv/) para entorno y dependencias
- **FastAPI** para la capa web
- **pytest** para las pruebas

## Licencia de la fuente

El contenido del libro se usa bajo licencia **Creative Commons CC BY-NC-ND**
(ver `METODOLOGIA.md`). Atribución a Harry Percival y Bob Gregory, O'Reilly 2020.
