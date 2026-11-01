# eventos.py — EVENTOS de dominio: dataclasses simples que describen "algo que pasó".
from dataclasses import dataclass


class Evento:
    pass


@dataclass
class SinStock(Evento):
    sku: str
