# BUENA: el dominio registra un evento; un handler externo publica.
class Producto:
    def __init__(self): self.eventos=[]
    def asignar(self): self.eventos.append("Asignado")
def publicar_handler(evento): print("publicando", evento)
p = Producto(); p.asignar()
for e in p.eventos: publicar_handler(e)
