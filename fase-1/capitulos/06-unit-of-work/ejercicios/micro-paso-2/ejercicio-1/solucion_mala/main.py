# MALA: dos operaciones con un commit cada una (no atómico: si la 2a falla, la 1a queda).
class Sesion:
    def __init__(self): self.datos=[]
    def commit(self): pass
def operar(sesion):
    sesion.datos.append("op1"); sesion.commit()
    sesion.datos.append("op2"); sesion.commit()
s=Sesion(); operar(s); print(s.datos)
