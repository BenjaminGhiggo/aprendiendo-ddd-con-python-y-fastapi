# Ej2 — BUENA: el notificador se inyecta; el servicio no depende de uno concreto.
def avisar_compra(notificador):
    notificador.enviar("Compra realizada")

class NotificadorEmail:
    def enviar(self, msg):
        print("email: " + msg)

class NotificadorSMS:
    def enviar(self, msg):
        print("sms: " + msg)

avisar_compra(NotificadorEmail())
avisar_compra(NotificadorSMS())
