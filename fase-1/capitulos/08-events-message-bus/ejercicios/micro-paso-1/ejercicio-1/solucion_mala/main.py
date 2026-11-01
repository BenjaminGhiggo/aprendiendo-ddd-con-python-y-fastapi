# MALA: el dominio ENVÍA la notificación directamente (acoplado al email).
class Producto:
    def asignar(self, hay_stock):
        if not hay_stock:
            print("enviando email: sin stock")   # el dominio hace I/O de notificacion
Producto().asignar(False)
