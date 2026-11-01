# Ej1 — MALA: un value object frozen NO se puede "escribir" (el ORM necesita hacerlo).
from dataclasses import dataclass

@dataclass(frozen=True)
class Linea:
    sku: str
    cantidad: int

l = Linea("MESA", 2)
try:
    l.sku = "SILLA"       # el ORM haría algo así al cargar de la BD
except Exception as e:
    print("el ORM no podria escribir:", type(e).__name__)
