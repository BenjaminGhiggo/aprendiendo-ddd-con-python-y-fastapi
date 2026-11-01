# Ej3 — MALA (funciona): una función exige saber qué clase concreta recibe.
class NotificadorEmail:
    def enviar(self, msg):
        return "email: " + msg

def avisar(notificador, msg):
    # si mañana llega un NotificadorSMS sin enviar(), esto peta en tiempo de ejecución
    return notificador.enviar(msg)

print(avisar(NotificadorEmail(), "hola"))
