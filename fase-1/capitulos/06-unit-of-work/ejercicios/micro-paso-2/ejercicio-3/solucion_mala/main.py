# MALA: commit implícito "mágico" (no se ve cuándo se confirma).
class UoW:
    def __init__(self): self.confirmado=False
    def __enter__(self): return self
    def __exit__(self,*a): self.confirmado=True   # confirma siempre al salir (implícito)
with UoW() as u: pass
print("confirmado:", u.confirmado)
