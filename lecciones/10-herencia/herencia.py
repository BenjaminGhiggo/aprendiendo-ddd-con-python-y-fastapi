# herencia.py

class Lote:                       # clase PADRE (base)
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad
    def descripcion(self):
        return f"Lote {self.referencia} con {self.cantidad} unidades"

class LoteRefrigerado(Lote):      # clase HIJA: hereda de Lote
    def __init__(self, referencia, cantidad, temperatura):
        super().__init__(referencia, cantidad)   # reutiliza el __init__ del padre
        self.temperatura = temperatura            # agrega lo nuevo
    def descripcion(self):                        # EXTIENDE el método del padre
        base = super().descripcion()
        return base + f" (a {self.temperatura}°C)"

normal = Lote("L1", 10)
frio = LoteRefrigerado("L2", 5, -18)
print(normal.descripcion())
print(frio.descripcion())
