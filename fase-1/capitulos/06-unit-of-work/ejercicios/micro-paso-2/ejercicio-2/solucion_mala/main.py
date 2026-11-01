# MALA: la UoW no cierra la sesión (fuga de recursos).
class Sesion:
    def __init__(self): self.abierta=True
    def close(self): self.abierta=False
class UoW:
    def __init__(self,s): self.s=s
    def __enter__(self): return self
    def __exit__(self,*a): pass            # no cierra
s=Sesion()
with UoW(s): pass
print("abierta:", s.abierta)               # True -> MAL
