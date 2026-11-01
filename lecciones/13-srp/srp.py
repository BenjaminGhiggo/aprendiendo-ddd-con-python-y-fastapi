# srp.py  -> SRP: cada pieza tiene UNA sola responsabilidad (una sola razón para cambiar).

# La clase Pedido SOLO conoce la regla del negocio: calcular su total.
class Pedido:
    def __init__(self, precios):
        self.precios = precios          # lista de precios
    def total(self):
        return sum(self.precios)

# La PRESENTACIÓN (cómo se muestra) es OTRA responsabilidad -> función aparte.
def formatear_recibo(pedido):
    return f"Total a pagar: {pedido.total()}"

pedido = Pedido([10, 20, 30])
print(pedido.total())            # 60   (regla de negocio)
print(formatear_recibo(pedido))  # Total a pagar: 60   (presentación)
