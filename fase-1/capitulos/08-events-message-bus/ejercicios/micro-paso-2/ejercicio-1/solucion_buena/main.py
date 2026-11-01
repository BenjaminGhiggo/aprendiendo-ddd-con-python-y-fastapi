# BUENA: un diccionario de manejadores (agregar un evento = una entrada).
from dataclasses import dataclass
@dataclass
class SinStock: sku: str
def notificar(e): print("notificar", e.sku)
MANEJADORES = {SinStock: [notificar]}
def manejar(e):
    for m in MANEJADORES[type(e)]: m(e)
manejar(SinStock("MESA"))
