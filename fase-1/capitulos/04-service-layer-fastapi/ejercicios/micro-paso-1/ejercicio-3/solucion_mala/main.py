# MALA: el servicio olvida confirmar (commit); los cambios no persisten.
class Sesion:
    comprometida = False
    def commit(self): self.comprometida = True
def servicio(sesion):
    pass   # hace el trabajo... pero nunca llama sesion.commit()
s = Sesion(); servicio(s); print("comprometida:", s.comprometida)   # False
