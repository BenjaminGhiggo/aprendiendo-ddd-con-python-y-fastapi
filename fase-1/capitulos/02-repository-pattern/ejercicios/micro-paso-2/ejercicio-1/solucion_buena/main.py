# Ej1 — BUENA: unsafe_hash mantiene igualdad por valor y hash, pero permite escribir.
from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Linea:
    sku: str
    cantidad: int

l = Linea("MESA", 2)
l.sku = "SILLA"           # el ORM sí puede escribir
print("escrito:", l.sku)
print("igualdad por valor:", Linea("A", 1) == Linea("A", 1))
print("en set:", len({Linea("A", 1), Linea("A", 1)}))
