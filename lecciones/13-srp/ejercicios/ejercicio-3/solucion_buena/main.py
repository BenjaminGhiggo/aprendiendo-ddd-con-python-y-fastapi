# Ej3 — BUENA: Usuario solo tiene los datos; enviar correos es otra responsabilidad.
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class ServicioCorreo:
    def enviar_bienvenida(self, usuario):
        print("Enviando correo a " + usuario.email)

u = Usuario("Ana", "ana@mail.com")
ServicioCorreo().enviar_bienvenida(u)
