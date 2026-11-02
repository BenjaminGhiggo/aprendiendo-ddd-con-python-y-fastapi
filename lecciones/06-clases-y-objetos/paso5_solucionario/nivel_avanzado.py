# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/06-clases-y-objetos/paso5_solucionario/nivel_avanzado.py


# Problema 9: un método que usa otro método del mismo objeto (C11).
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad

    def puede_asignar(self, pedido):
        return self.cantidad >= pedido

    def asignar(self, pedido):
        if self.puede_asignar(pedido):
            self.cantidad = self.cantidad - pedido


lote = Lote("L1", 10)
lote.asignar(4)
lote.asignar(8)          # no alcanza (quedan 6): no cambia
print("P9:", lote.cantidad)                       # 6


# Problema 10: un objeto que guarda una LISTA de otros objetos.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.items = []                   # empieza vacío (lista vacía, L2)

    def agregar(self, producto):
        self.items.append(producto)

    def total(self):
        suma = 0
        for p in self.items:
            suma = suma + p.precio
        return suma


carrito = Carrito()
carrito.agregar(Producto("pan", 1))
carrito.agregar(Producto("leche", 4))
print("P10:", len(carrito.items), carrito.total())   # 2 5


# Problema 11: dos contadores independientes (C10).
class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor = self.valor + 1


a = Contador()
b = Contador()
a.incrementar()
a.incrementar()
b.incrementar()
print("P11:", a.valor, b.valor)                  # 2 1


# Problema 12 (puente al libro): como can_allocate del cap. 1:
# "return self.sku == line.sku and self.available_quantity >= line.qty"
class LineaPedido:
    def __init__(self, id_pedido, sku, cantidad):
        self.id_pedido = id_pedido
        self.sku = sku
        self.cantidad = cantidad


class LoteDelLibro:
    def __init__(self, referencia, sku, cantidad):
        self.referencia = referencia
        self.sku = sku
        self.cantidad_disponible = cantidad

    def puede_asignar(self, linea):
        return self.sku == linea.sku and self.cantidad_disponible >= linea.cantidad


lote = LoteDelLibro("batch-001", "SMALL-TABLE", 20)
print("P12:", lote.puede_asignar(LineaPedido("o1", "SMALL-TABLE", 2)),     # True
      lote.puede_asignar(LineaPedido("o2", "BLUE-CUSHION", 2)),            # False (otro sku)
      lote.puede_asignar(LineaPedido("o3", "SMALL-TABLE", 25)))            # False (no alcanza)
