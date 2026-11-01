# BUENA: cada cambio sube numero_version (marca de cambio para concurrencia optimista).
class Producto:
    def __init__(self): self.stock=100; self.version=0
    def asignar(self, c): self.stock -= c; self.version += 1
p = Producto(); p.asignar(10); print("version:", p.version)   # 1
