# BUENA: una UoW (context manager) agrupa repo + commit.
class UoW:
    def __init__(self): self.datos=[]; self.confirmado=False
    def __enter__(self): return self
    def __exit__(self, *a): pass
    def comprometer(self): self.confirmado=True
def servicio(dato, uow):
    with uow:
        uow.datos.append(dato)
        uow.comprometer()
u=UoW(); servicio("x", u); print(u.datos, u.confirmado)
