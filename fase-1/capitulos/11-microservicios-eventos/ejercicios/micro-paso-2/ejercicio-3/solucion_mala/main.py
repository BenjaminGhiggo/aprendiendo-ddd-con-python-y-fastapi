# MALA: publicar directamente desde el dominio (acopla el modelo al transporte).
class Producto:
    def asignar(self):
        print("redis.publish(...)")   # el dominio conoce Redis
Producto().asignar()
