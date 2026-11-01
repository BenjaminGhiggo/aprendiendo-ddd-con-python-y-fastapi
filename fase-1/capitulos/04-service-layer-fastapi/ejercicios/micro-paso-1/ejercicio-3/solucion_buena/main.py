# BUENA: el servicio confirma al final.
class Sesion:
    comprometida = False
    def commit(self): self.comprometida = True
def servicio(sesion):
    sesion.commit()
s = Sesion(); servicio(s); print("comprometida:", s.comprometida)   # True
