# Ej2 — MALA (funciona): el servicio instancia el notificador concreto.
class NotificadorEmail:
    def enviar(self, msg):
        print("email: " + msg)

def avisar_compra():
    notificador = NotificadorEmail()   # atado a email; cambiarlo obliga a tocar esto
    notificador.enviar("Compra realizada")

avisar_compra()
