# clases.py

# 1. Una CLASE es un MOLDE: describe qué datos y qué acciones tendrá un objeto.
class Lote:
    def __init__(self, referencia, sku, cantidad):
        # __init__ se ejecuta AL CREAR el objeto. "self" es "este objeto".
        self.referencia = referencia   # guardo los datos DENTRO del objeto
        self.sku = sku
        self.cantidad = cantidad

    # Un MÉTODO es una función que vive dentro de la clase y usa los datos del objeto.
    def puede_asignar(self, pedido_cantidad):
        if self.cantidad >= pedido_cantidad:
            return True
        else:
            return False

# 2. Creamos una INSTANCIA: un lote concreto hecho con el molde.
lote = Lote("LOTE-001", "MESA", 20)

# 3. "lote" es un OBJETO. Leemos sus datos y usamos su comportamiento.
print(lote.referencia)         # LOTE-001
print(lote.cantidad)           # 20
print(lote.puede_asignar(5))   # True  -> 20 >= 5
print(lote.puede_asignar(25))  # False -> 20 < 25
