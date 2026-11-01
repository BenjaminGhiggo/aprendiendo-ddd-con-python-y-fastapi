# Ej3 — MALA (funciona): nombres sin significado del negocio.
from dataclasses import dataclass

@dataclass(frozen=True)
class Datos:
    a: str
    b: int

d = Datos("MESA", 2)
print(d.a, d.b)   # ¿qué son "a" y "b"? hay que adivinar
