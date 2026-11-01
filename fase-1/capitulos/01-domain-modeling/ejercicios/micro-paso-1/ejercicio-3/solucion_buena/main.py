# Ej3 — BUENA: nombres tomados del lenguaje del negocio.
from dataclasses import dataclass

@dataclass(frozen=True)
class LineaPedido:
    sku: str
    cantidad: int

linea = LineaPedido("MESA", 2)
print(linea.sku, linea.cantidad)
