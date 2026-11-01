# BUENA: el canal se elige en UN lugar (el bootstrap) y se inyecta a todos los handlers.
import abc
class Notif(abc.ABC):
    @abc.abstractmethod
    def enviar(self, msg): ...
class Email(Notif):
    def enviar(self, msg): print("EMAIL:", msg)
class Slack(Notif):
    def enviar(self, msg): print("SLACK:", msg)
def handler_1(msg, notif): notif.enviar(msg)
def handler_2(msg, notif): notif.enviar(msg)
def bootstrap(notif):   # <-- UNICA linea a cambiar: Email() -> Slack()
    return [lambda m: handler_1(m, notif), lambda m: handler_2(m, notif)]
for h in bootstrap(Slack()):
    h("hola")
