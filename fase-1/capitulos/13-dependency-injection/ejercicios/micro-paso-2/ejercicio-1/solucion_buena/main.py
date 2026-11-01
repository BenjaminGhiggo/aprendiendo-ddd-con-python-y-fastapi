# BUENA: el bus es una CLASE que recibe sus handlers ya inyectados -> configurable.
class BusMensajes:
    def __init__(self, manejadores):
        self.manejadores = manejadores
    def manejar(self, msg, tipo):
        return self.manejadores[tipo](msg)
# produccion
bus = BusMensajes({"asignar": lambda m: f"asignado {m} (real)"})
print(bus.manejar("o1", "asignar"))
# test: mismo bus, otros handlers
bus_test = BusMensajes({"asignar": lambda m: f"asignado {m} (fake)"})
print(bus_test.manejar("o1", "asignar"))
