# BUENA: al salir sin confirmar, __exit__ deshace.
class UoW:
    def __init__(self): self.datos=[]; self._pendiente=[]
    def __enter__(self): return self
    def __exit__(self, *a): self._pendiente.clear()   # rollback de lo pendiente
    def agregar(self, x): self._pendiente.append(x)
    def comprometer(self): self.datos.extend(self._pendiente); self._pendiente.clear()
with UoW() as uow:
    uow.agregar("a medias")               # no confirmado
print("quedó:", uow.datos)                # [] -> deshecho
