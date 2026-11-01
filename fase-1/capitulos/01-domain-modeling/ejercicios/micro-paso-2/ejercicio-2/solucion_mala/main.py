# Ej2 — MALA (funciona): un Lote como dataclass compara por TODOS sus campos.
from dataclasses import dataclass

@dataclass
class Lote:
    referencia: str
    stock: int

a = Lote("L1", 20)
b = Lote("L1", 5)     # mismo lote (misma ref), distinto stock
print(a == b)         # False -> MAL: deberían ser el mismo
