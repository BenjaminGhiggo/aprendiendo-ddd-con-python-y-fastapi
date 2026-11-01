# BUENA: para una reaccion nueva, se AGREGA un manejador (OCP, Leccion 14).
from dataclasses import dataclass
@dataclass
class SinStock: sku: str
def email(e): print("email", e.sku)
def sms(e): print("sms", e.sku)          # NUEVO manejador, sin tocar lo demas
MANEJADORES = {SinStock: [email, sms]}
def manejar(e):
    for m in MANEJADORES[type(e)]: m(e)
manejar(SinStock("MESA"))
