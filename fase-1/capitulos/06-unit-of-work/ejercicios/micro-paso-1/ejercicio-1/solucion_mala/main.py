# MALA: el servicio maneja repo y "commit" sueltos (acoplado a la persistencia).
class Sesion:
    def __init__(self): self.datos=[]; self.confirmado=False
    def commit(self): self.confirmado=True
def servicio(dato, sesion):
    sesion.datos.append(dato)
    sesion.commit()
s=Sesion(); servicio("x", s); print(s.datos, s.confirmado)
