# encapsulacion.py

class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self._cantidad = cantidad   # el "_" avisa: PRIVADO, no tocar desde afuera

    # Puerta para LEER el dato protegido.
    def cantidad_disponible(self):
        return self._cantidad

    # Puerta para CAMBIARLO, aplicando la regla (no asignar más de lo que hay).
    def asignar(self, pedido):
        if pedido > self._cantidad:
            raise ValueError("No hay stock suficiente")
        self._cantidad = self._cantidad - pedido


lote = Lote("LOTE-001", 20)
print(lote.cantidad_disponible())   # 20  -> leemos por la puerta controlada

lote.asignar(5)                     # cambiamos SOLO con el método válido
print(lote.cantidad_disponible())   # 15

# Si intentamos algo inválido, la regla nos protege el estado:
try:
    lote.asignar(999)
except ValueError as e:
    print("Bloqueado:", e)

print(lote.cantidad_disponible())   # sigue 15: el dato no se corrompió
