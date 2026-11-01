# BUENA: la UoW cierra la sesión al salir.
class Sesion:
    def __init__(self): self.abierta=True
    def close(self): self.abierta=False
class UoW:
    def __init__(self,s): self.s=s
    def __enter__(self): return self
    def __exit__(self,*a): self.s.close()
s=Sesion()
with UoW(s): pass
print("abierta:", s.abierta)               # False
