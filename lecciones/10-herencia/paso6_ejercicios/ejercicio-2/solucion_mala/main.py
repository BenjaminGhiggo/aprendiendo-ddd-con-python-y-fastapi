# Ej2 — MALA (funciona): copia el __init__ del padre a mano en la subclase.
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad

class LoteUrgente(Lote):
    def __init__(self, referencia, cantidad, prioridad):
        self.referencia = referencia   # repite lo que ya hace Lote.__init__
        self.cantidad = cantidad
        self.prioridad = prioridad

u = LoteUrgente("L1", 10, "alta")
print(u.referencia, u.cantidad, u.prioridad)
