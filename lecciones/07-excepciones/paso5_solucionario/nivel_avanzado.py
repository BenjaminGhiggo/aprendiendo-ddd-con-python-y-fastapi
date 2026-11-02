# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/07-excepciones/paso5_solucionario/nivel_avanzado.py


# Problema 9: un error propio + un ValueError, con dos except.
class SaldoInsuficiente(Exception):
    pass


def retirar(saldo, monto):
    if monto <= 0:
        raise ValueError("monto inválido")
    if monto > saldo:
        raise SaldoInsuficiente("saldo insuficiente")
    return saldo - monto


for monto in [30, -5, 500]:
    try:
        print("P9:", monto, "-> queda", retirar(100, monto))
    except ValueError as e:
        print("P9:", monto, "->", e)
    except SaldoInsuficiente as e:
        print("P9:", monto, "->", e)


# Problema 10: un método de una clase (Lección 06) que lanza el error.
class SinStock(Exception):
    pass


class Lote:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def asignar(self, pedido):
        if pedido > self.cantidad:
            raise SinStock("sin stock para pedido " + str(pedido))
        self.cantidad = self.cantidad - pedido


lote = Lote(20)
for pedido in [5, 30, 10]:
    try:
        lote.asignar(pedido)
        print("P10: asignado", pedido, "queda", lote.cantidad)
    except SinStock as e:
        print("P10:", e)


# Problema 11: traducir un error técnico (KeyError) a uno del negocio (raise dentro del except).
class ProductoNoExiste(Exception):
    pass


def obtener_stock(stock, nombre):
    try:
        return stock[nombre]
    except KeyError:
        raise ProductoNoExiste("no existe: " + nombre)


try:
    obtener_stock({"mesa": 10}, "sofá")
except ProductoNoExiste as e:
    print("P11:", e)


# Problema 12 (puente al libro): como
# "raise OutOfStock(f'Out of stock for sku {line.sku}')" del cap. 1.
class Lote2:
    def __init__(self, referencia, sku, cantidad):
        self.referencia = referencia
        self.sku = sku
        self.cantidad = cantidad


def allocate(sku, cantidad, lotes):
    for lote in lotes:
        if lote.sku == sku and lote.cantidad >= cantidad:
            lote.cantidad = lote.cantidad - cantidad
            return lote.referencia
    raise SinStock("Out of stock for sku " + sku)


lotes = [Lote2("batch1", "SMALL-FORK", 10)]
print("P12:", allocate("SMALL-FORK", 10, lotes))     # batch1
try:
    allocate("SMALL-FORK", 1, lotes)                 # ya no queda
except SinStock as e:
    print("P12:", e)                                 # Out of stock for sku SMALL-FORK
