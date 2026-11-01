# BUENA: registrar un evento (el flujo normal sigue; la reaccion se decide aparte).
from dataclasses import dataclass
@dataclass
class SinStock: sku: str
eventos = []
def asignar(hay_stock, sku):
    if not hay_stock: eventos.append(SinStock(sku))
asignar(False, "MESA"); print(eventos)
