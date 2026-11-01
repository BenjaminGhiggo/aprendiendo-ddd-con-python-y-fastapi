# BUENA: ambas operaciones dentro de UNA UoW -> un solo commit atómico.
class UoW:
    def __init__(self): self.datos=[]; self._p=[]
    def __enter__(self): return self
    def __exit__(self,*a): self._p.clear()
    def agregar(self,x): self._p.append(x)
    def comprometer(self): self.datos.extend(self._p); self._p.clear()
def operar(uow):
    with uow:
        uow.agregar("op1"); uow.agregar("op2")
        uow.comprometer()                 # todo junto, o nada
u=UoW(); operar(u); print(u.datos)
