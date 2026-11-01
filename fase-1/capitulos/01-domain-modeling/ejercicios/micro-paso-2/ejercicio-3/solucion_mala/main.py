# Ej3 — MALA (funciona): dataclass hace que el mismo lote cuente doble en un set.
from dataclasses import dataclass

@dataclass(frozen=True)
class Lote:
    referencia: str
    stock: int

lotes = {Lote("L1", 20), Lote("L1", 5)}   # mismo lote, distinto stock
print(len(lotes))     # 2 -> MAL
