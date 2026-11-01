# Ej3 — BUENA: un contrato Notificador garantiza que todos tengan enviar().
from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, msg): ...

class NotificadorEmail(Notificador):
    def enviar(self, msg):
        return "email: " + msg

class NotificadorSMS(Notificador):
    def enviar(self, msg):
        return "sms: " + msg

def avisar(notificador: Notificador, msg):
    return notificador.enviar(msg)

print(avisar(NotificadorEmail(), "hola"))
print(avisar(NotificadorSMS(), "hola"))
