# Ej1 — BUENA: value object inmutable con @dataclass(frozen=True).
from dataclasses import dataclass

@dataclass(frozen=True)
class LineaPedido:
    sku: str
    cantidad: int

linea = LineaPedido("MESA", 2)
try:
    linea.cantidad = 999        # frozen=True lo impide
except Exception as e:
    print("inmutable:", type(e).__name__)
print(linea.cantidad)
