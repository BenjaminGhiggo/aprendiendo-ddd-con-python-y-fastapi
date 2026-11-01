# BUENA: inyectamos una implementacion FALSA (fake) que guarda lo enviado. Sin parches.
import abc
class Notificaciones(abc.ABC):
    @abc.abstractmethod
    def enviar(self, mensaje): ...
class NotificacionesFalsas(Notificaciones):
    def __init__(self): self.enviadas = []
    def enviar(self, mensaje): self.enviadas.append(mensaje)
def avisar(notif, sku): notif.enviar(f"sin stock {sku}")
fake = NotificacionesFalsas()
avisar(fake, "MESA")
print("buena -> enviadas:", fake.enviadas)
