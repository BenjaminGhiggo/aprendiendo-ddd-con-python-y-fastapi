# MALA: el agregado cambia estado pero NO sube la version (concurrencia insegura).
class Producto:
    def __init__(self): self.stock=100; self.version=0
    def asignar(self, c): self.stock -= c      # olvida subir version
p = Producto(); p.asignar(10); print("version:", p.version)   # 0
