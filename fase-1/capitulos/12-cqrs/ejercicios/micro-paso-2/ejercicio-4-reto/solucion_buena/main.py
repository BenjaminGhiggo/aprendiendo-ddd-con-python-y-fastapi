# BUENA: la vista habla con un "almacen de lectura" por una interfaz. Cambiar dict -> "redis"
# no toca el dominio ni los tests (solo el adaptador). "easy to change the implementation".
class VistaDict:
    def __init__(self): self.d = {}
    def set(self, pedido, ref): self.d[pedido] = ref
    def get(self, pedido): return self.d.get(pedido)
class VistaRedisSimulada:
    def __init__(self): self.h = {}
    def set(self, pedido, ref): self.h[pedido] = ref      # seria r.hset(...)
    def get(self, pedido): return self.h.get(pedido)      # seria r.hgetall(...)
def ver(almacen, pedido):            # misma vista, cualquier motor
    return almacen.get(pedido)
for motor in (VistaDict(), VistaRedisSimulada()):
    motor.set("p1", "l1")
    print(type(motor).__name__, "-> ver('p1'):", ver(motor, "p1"))
