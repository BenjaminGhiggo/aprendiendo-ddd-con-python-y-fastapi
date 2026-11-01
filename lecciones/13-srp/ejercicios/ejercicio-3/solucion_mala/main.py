# Ej3 — MALA (funciona): Usuario guarda datos Y manda correos (dos trabajos distintos).
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def enviar_bienvenida(self):
        print("Enviando correo a " + self.email)

u = Usuario("Ana", "ana@mail.com")
u.enviar_bienvenida()
