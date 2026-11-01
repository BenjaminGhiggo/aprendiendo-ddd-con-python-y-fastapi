# BUENA: el servicio compromete al terminar el trabajo.
class UoW:
    def __init__(self): self.confirmado=False
    def __enter__(self): return self
    def __exit__(self, *a): pass
    def comprometer(self): self.confirmado=True
def servicio(uow):
    with uow:
        uow.comprometer()
u=UoW(); servicio(u); print(u.confirmado) # True
