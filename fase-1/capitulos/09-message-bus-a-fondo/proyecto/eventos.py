# eventos.py — eventos de dominio y mensajes de entrada.
from dataclasses import dataclass


class Evento:
    pass


@dataclass
class AsignacionRequerida(Evento):   # mensaje de ENTRADA: "quiero asignar"
    id_pedido: str
    sku: str
    cantidad: int


@dataclass
class CambiarCantidadLote(Evento):   # nuevo requisito: cambia la cantidad comprada
    referencia: str
    cantidad: int


@dataclass
class Asignado(Evento):              # algo pasó: se asignó
    id_pedido: str
    sku: str
    cantidad: int
    referencia: str


@dataclass
class SinStock(Evento):
    sku: str
