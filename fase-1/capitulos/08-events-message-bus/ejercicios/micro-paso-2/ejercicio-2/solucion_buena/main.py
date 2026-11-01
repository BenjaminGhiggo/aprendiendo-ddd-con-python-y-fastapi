# BUENA: el productor solo emite el evento; el bus llama a los manejadores.
from dataclasses import dataclass
@dataclass
class SinStock: sku: str
def notificar(e): print("notificar", e.sku)
MANEJADORES = {SinStock: [notificar]}
def manejar(e):
    for m in MANEJADORES[type(e)]: m(e)
def asignar_fallido(sku):
    manejar(SinStock(sku))  # no conoce al manejador concreto
asignar_fallido("MESA")
