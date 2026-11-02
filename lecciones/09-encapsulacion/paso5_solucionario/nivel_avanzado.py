# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/09-encapsulacion/paso5_solucionario/nivel_avanzado.py


# Problema 9: propiedad CALCULADA (P3) sobre una lista protegida (Lección 05).
class Carrito:
    def __init__(self):
        self._precios = []

    def agregar(self, precio):
        self._precios.append(precio)

    @property
    def total(self):
        suma = 0
        for precio in self._precios:
            suma = suma + precio
        return suma


carrito = Carrito()
carrito.agregar(10)
carrito.agregar(20)
carrito.agregar(5)
print("P9:", carrito.total)                        # 35


# Problema 10: setters que validan + propiedad calculada.
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho                         # pasan por los setters
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("Medida inválida")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("Medida inválida")
        self._alto = valor

    @property
    def area(self):
        return self._ancho * self._alto


r = Rectangulo(2, 3)
print("P10:", r.area)                              # 6
r.ancho = 5
print("P10:", r.area)                              # 15
try:
    r.alto = 0
except ValueError as error:
    print("P10:", error, "| área sigue en:", r.area)


# Problema 11: entregar una COPIA de la lista protegida, para que desde afuera
# no se pueda cambiar el historial sin pasar por los métodos.
class CuentaConHistorial:
    def __init__(self):
        self._movimientos = []

    def depositar(self, monto):
        self._movimientos.append(monto)

    def retirar(self, monto):
        self._movimientos.append(-monto)

    @property
    def movimientos(self):
        return list(self._movimientos)             # list(...) crea una lista NUEVA (copia)


cuenta = CuentaConHistorial()
cuenta.depositar(100)
cuenta.retirar(30)
print("P11:", cuenta.movimientos)                  # [100, -30]
copia = cuenta.movimientos
copia.append(999)                                  # cambio la COPIA...
print("P11: movimientos reales:", len(cuenta.movimientos))   # ...los reales siguen siendo 2


# Problema 12 (puente al libro): un Lote como el Batch del cap. 1:
#   self._purchased_quantity = qty
#   @property def available_quantity(self): return self._purchased_quantity - self.allocated_quantity
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self._cantidad_comprada = cantidad
        self._asignaciones = []                    # cantidades asignadas

    @property
    def cantidad_asignada(self):
        suma = 0
        for cantidad in self._asignaciones:
            suma = suma + cantidad
        return suma

    @property
    def cantidad_disponible(self):
        return self._cantidad_comprada - self.cantidad_asignada

    def asignar(self, cantidad):
        if cantidad > self.cantidad_disponible:
            raise ValueError("No hay stock suficiente")
        self._asignaciones.append(cantidad)


lote = Lote("LOTE-001", 20)
lote.asignar(5)
lote.asignar(3)
print("P12: asignada", lote.cantidad_asignada, "| disponible", lote.cantidad_disponible)   # 8 | 12
try:
    lote.asignar(50)
except ValueError as error:
    print("P12:", error, "| disponible", lote.cantidad_disponible)                      # ... | 12
