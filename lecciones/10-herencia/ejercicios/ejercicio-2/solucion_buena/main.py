# Ej2 — BUENA: super() reutiliza el __init__ del padre.
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad

class LoteUrgente(Lote):
    def __init__(self, referencia, cantidad, prioridad):
        super().__init__(referencia, cantidad)
        self.prioridad = prioridad

u = LoteUrgente("L1", 10, "alta")
print(u.referencia, u.cantidad, u.prioridad)
