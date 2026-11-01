# BUENA: el bus usa una COLA y recoge eventos nuevos (cascada).
nuevos = ["email"]               # eventos que surgen tras procesar
def manejar(evento):
    cola = [evento]
    while cola:
        e = cola.pop(0)
        print("manejar", e)
        cola.extend(nuevos); nuevos.clear()
manejar("asignacion")
