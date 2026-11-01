# eventos.py — EVENTOS: hechos ("esto pasó"). Varios handlers; si uno falla, se AÍSLA.
from dataclasses import dataclass


class Evento:
    pass


@dataclass
class Asignado(Evento):
    id_pedido: str
    sku: str
    cantidad: int
    referencia: str


@dataclass
class SinStock(Evento):
    sku: str


@dataclass
class Desasignado(Evento):
    id_pedido: str
    sku: str
    cantidad: int
