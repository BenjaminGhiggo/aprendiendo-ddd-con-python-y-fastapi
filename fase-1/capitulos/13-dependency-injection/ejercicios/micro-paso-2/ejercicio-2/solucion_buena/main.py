# BUENA: una ABC define la API; email/SMS son implementaciones intercambiables.
import abc
class Notificaciones(abc.ABC):
    @abc.abstractmethod
    def enviar(self, mensaje): ...
class Email(Notificaciones):
    def enviar(self, mensaje): print("EMAIL:", mensaje)
class SMS(Notificaciones):
    def enviar(self, mensaje): print("SMS:", mensaje)
def avisar(notif: Notificaciones, mensaje):   # depende de la ABSTRACCION
    notif.enviar(mensaje)
avisar(Email(), "sin stock MESA")
avisar(SMS(), "sin stock MESA")   # cambiar de canal = pasar otra implementacion
