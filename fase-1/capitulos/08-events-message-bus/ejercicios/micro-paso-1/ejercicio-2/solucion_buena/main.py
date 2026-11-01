# BUENA: evento como dataclass con tipo e igualdad por valor.
from dataclasses import dataclass
@dataclass
class SinStock: sku: str
e = SinStock("MESA")
print("sku:", e.sku, "| igualdad:", e == SinStock("MESA"))
