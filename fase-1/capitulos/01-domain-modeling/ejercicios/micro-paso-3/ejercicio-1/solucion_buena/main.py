# Ej1 — BUENA: disponible se CALCULA desde el conjunto de líneas asignadas.
from dataclasses import dataclass

@dataclass(frozen=True)
class LineaPedido:
    id_pedido: str
    cantidad: int

class Lote:
    def __init__(self, cantidad):
        self._comprada = cantidad
        self._asignaciones = set()
    def asignar(self, linea):
        self._asignaciones.add(linea)   # set: la misma línea no se duplica
    @property
    def disponible(self):
        return self._comprada - sum(l.cantidad for l in self._asignaciones)

lote = Lote(20)
linea = LineaPedido("p1", 2)
lote.asignar(linea)
lote.asignar(linea)    # misma línea: no cuenta doble
print(lote.disponible) # 18
