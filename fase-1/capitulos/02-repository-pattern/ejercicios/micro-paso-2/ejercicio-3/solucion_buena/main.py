# Ej3 — BUENA: unsafe_hash da igualdad por valor y hash -> el set deduplica.
from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Linea:
    sku: str
    cantidad: int

print(len({Linea("MESA", 2), Linea("MESA", 2)}))   # 1
