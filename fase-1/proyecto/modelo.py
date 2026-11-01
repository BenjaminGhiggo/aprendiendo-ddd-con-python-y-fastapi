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
        self._cantidad_comprada = cantidad   # lo que se compró (no cambia)
        self._asignaciones = set()           # conjunto de LineaPedido asignadas

    def asignar(self, linea: LineaPedido):
        if self.puede_asignar(linea):
            self._asignaciones.add(linea)    # es un set: asignar dos veces no duplica

    def desasignar(self, linea: LineaPedido):
        if linea in self._asignaciones:
            self._asignaciones.remove(linea)

    @property
    def cantidad_asignada(self) -> int:
        return sum(linea.cantidad for linea in self._asignaciones)

    @property
    def cantidad_disponible(self) -> int:
        # Se CALCULA: lo comprado menos lo ya asignado.
        return self._cantidad_comprada - self.cantidad_asignada

    def puede_asignar(self, linea: LineaPedido) -> bool:
        return self.sku == linea.sku and self.cantidad_disponible >= linea.cantidad

    # Igualdad por IDENTIDAD: dos lotes son "el mismo" si tienen la misma referencia,
    # sin importar que cambie el resto de sus datos.
    def __eq__(self, other):
        if not isinstance(other, Lote):
            return False
        return other.referencia == self.referencia

    # __hash__ controla cómo se comporta el objeto en sets y como clave de dict.
    # Para una entidad, se basa en su identidad (la referencia).
    def __hash__(self):
        return hash(self.referencia)
