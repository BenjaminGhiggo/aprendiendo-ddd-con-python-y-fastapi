# BUENA: commit EXPLÍCITO; si no se llama, se deshace.
class UoW:
    def __init__(self): self.confirmado=False
    def __enter__(self): return self
    def __exit__(self,*a):
        if not self.confirmado: pass      # deshace lo no confirmado
    def comprometer(self): self.confirmado=True
with UoW() as u:
    u.comprometer()                       # se ve claramente cuándo se confirma
print("confirmado:", u.confirmado)
