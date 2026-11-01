# comandos.py — COMANDOS: órdenes imperativas ("haz esto"). Un solo handler; si falla,
# el error PROPAGA (quien dio la orden debe enterarse).
from dataclasses import dataclass


class Comando:
    pass


@dataclass
class Asignar(Comando):
    id_pedido: str
    sku: str
    cantidad: int


@dataclass
class CrearLote(Comando):
    referencia: str
    sku: str
    cantidad: int
    eta: object = None


@dataclass
class CambiarCantidadLote(Comando):
    referencia: str
    cantidad: int
