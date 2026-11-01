# BUENA: preguntar no cambia nada; encender es un command aparte. CQS puro.
class Cuarto:
    def __init__(self): self.luz = False
    def luces_encendidas(self):     # query: solo responde
        return self.luz
    def encender(self):             # command: cambia estado
        self.luz = True
c = Cuarto()
print("pregunto (sin tocar):", c.luces_encendidas())
c.encender()
print("tras encender:", c.luces_encendidas())
