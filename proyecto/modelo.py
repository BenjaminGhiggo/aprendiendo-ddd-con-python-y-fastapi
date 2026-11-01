# modelo.py — el modelo de dominio del sistema de asignación (allocation).
# Lenguaje del negocio (glosario):
#   - LineaPedido (OrderLine): una línea de un pedido: qué sku y cuánta cantidad.
#   - Lote (Batch): stock comprado que llega (o ya está) al almacén.
#   - asignar (allocate): reservar una línea de pedido contra un lote.
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class LineaPedido:
    id_pedido: str
    sku: str
    cantidad: int


class Lote:
    def __init__(self, referencia: str, sku: str, cantidad: int, eta: Optional[date]):
        self.referencia = referencia
        self.sku = sku
        self.eta = eta                       # fecha estimada de llegada (puede ser None)
        self.cantidad_disponible = cantidad

    def asignar(self, linea: LineaPedido):
        self.cantidad_disponible -= linea.cantidad
