# MALA: preguntar "estan las luces encendidas?" ENCIENDE las luces (query con efecto).
class Cuarto:
    def __init__(self): self.luz = False
    def luces_encendidas(self):
        self.luz = True             # efecto secundario al preguntar: mal
        return self.luz
c = Cuarto()
print("pregunto 1:", c.luces_encendidas())
print("estado real:", c.luz, "(la pregunta cambio el estado)")
