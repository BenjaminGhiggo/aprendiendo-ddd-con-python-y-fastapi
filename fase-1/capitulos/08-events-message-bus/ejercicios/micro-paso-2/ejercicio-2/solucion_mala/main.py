# MALA: el productor llama al manejador a mano (acoplado).
def notificar(sku): print("notificar", sku)
def asignar_fallido(sku):
    notificar(sku)          # el dominio/servicio conoce al manejador concreto
asignar_fallido("MESA")
