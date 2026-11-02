# inventario.py — módulo de apoyo de los problemas 10–12 (README §10).


class SinStock(Exception):
    pass


def asignar_sku(sku, disponible, pedido):
    if pedido > disponible:
        raise SinStock("Sin stock para " + sku)
    return disponible - pedido


class LineaPedido:
    def __init__(self, id_pedido, sku, cantidad):
        self.id_pedido = id_pedido
        self.sku = sku
        self.cantidad = cantidad


class Lote:
    def __init__(self, referencia, sku, cantidad):
        self.referencia = referencia
        self.sku = sku
        self.cantidad_disponible = cantidad

    def puede_asignar(self, linea):
        return self.sku == linea.sku and self.cantidad_disponible >= linea.cantidad

    def asignar(self, linea):
        if self.puede_asignar(linea):
            self.cantidad_disponible = self.cantidad_disponible - linea.cantidad
