# BUENA: el consumidor traduce el mensaje externo a un comando interno.
class CambiarCantidad:
    def __init__(self, ref, cantidad): self.ref=ref; self.cantidad=cantidad
def consumir(mensaje_crudo):
    return CambiarCantidad(mensaje_crudo["ref"], mensaje_crudo["qty"])
c = consumir({"ref": "l1", "qty": 5})
print(c.ref, c.cantidad)
