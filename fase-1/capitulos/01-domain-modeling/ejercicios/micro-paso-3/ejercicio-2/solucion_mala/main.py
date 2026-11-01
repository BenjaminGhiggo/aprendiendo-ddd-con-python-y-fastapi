# Ej2 — MALA (funciona): guarda las asignaciones en una LISTA; permite duplicados.
from dataclasses import dataclass

@dataclass(frozen=True)
class LineaPedido:
    id_pedido: str
    cantidad: int

class Lote:
    def __init__(self, cantidad):
        self._comprada = cantidad
        self._asignaciones = []          # lista: admite la misma línea dos veces
    def asignar(self, linea):
        self._asignaciones.append(linea)
    @property
    def disponible(self):
        return self._comprada - sum(l.cantidad for l in self._asignaciones)

lote = Lote(20)
linea = LineaPedido("p1", 2)
lote.asignar(linea)
lote.asignar(linea)
print(lote.disponible)   # 16 -> MAL
