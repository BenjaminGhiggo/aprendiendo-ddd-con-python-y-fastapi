# MALA: la regla "no asignar de mas" vive fuera del agregado (se puede saltar).
class Producto:
    def __init__(self): self.stock=5
p = Producto()
p.stock -= 10          # nadie lo impide: queda negativo
print(p.stock)
