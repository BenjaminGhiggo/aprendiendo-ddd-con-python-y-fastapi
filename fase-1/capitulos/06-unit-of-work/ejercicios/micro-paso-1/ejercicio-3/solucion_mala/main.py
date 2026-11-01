# MALA: el servicio olvida comprometer dentro del with.
class UoW:
    def __init__(self): self.confirmado=False
    def __enter__(self): return self
    def __exit__(self, *a): pass
    def comprometer(self): self.confirmado=True
def servicio(uow):
    with uow:
        pass                              # no llama comprometer()
u=UoW(); servicio(u); print(u.confirmado) # False
