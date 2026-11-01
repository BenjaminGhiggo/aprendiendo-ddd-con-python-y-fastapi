# MALA: al salir del with, NO se deshace lo no confirmado (estado sucio).
class UoW:
    def __init__(self): self.datos=[]
    def __enter__(self): return self
    def __exit__(self, *a): pass          # no hace rollback
with UoW() as uow:
    uow.datos.append("a medias")          # no confirmado
print("quedó:", uow.datos)                # ['a medias'] -> MAL
