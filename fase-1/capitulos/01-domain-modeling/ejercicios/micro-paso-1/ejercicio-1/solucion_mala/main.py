# Ej1 — MALA (funciona): una línea de pedido mutable (se le puede cambiar la cantidad).
class LineaPedido:
    def __init__(self, sku, cantidad):
        self.sku = sku
        self.cantidad = cantidad

linea = LineaPedido("MESA", 2)
linea.cantidad = 999   # una LÍNEA de pedido no debería poder cambiar: aquí sí puede
print(linea.cantidad)
