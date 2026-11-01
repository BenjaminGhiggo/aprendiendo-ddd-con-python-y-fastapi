# Ej2 — BUENA: una LineaPedido agrupa los datos; las funciones reciben el objeto.
from dataclasses import dataclass

@dataclass(frozen=True)
class LineaPedido:
    sku: str
    cantidad: int

def describir(linea):
    return "Pedido de " + str(linea.cantidad) + " x " + linea.sku

def es_grande(linea):
    return linea.cantidad >= 100

linea = LineaPedido("MESA", 2)
print(describir(linea))
print(es_grande(linea))
