# Ej1 — BUENA: @dataclass da igualdad por valor gratis.
from dataclasses import dataclass

@dataclass(frozen=True)
class LineaPedido:
    sku: str
    cantidad: int

print(LineaPedido("MESA", 2) == LineaPedido("MESA", 2))   # True
