# Ej1 — BUENA: la lógica RECIBE el almacenamiento (inyección); no sabe cuál es.
def registrar(almacen, dato):
    almacen.guardar(dato)

class BaseDeDatos:
    def guardar(self, dato):
        print("guardando en MySQL: " + dato)

class AlmacenFalso:
    def guardar(self, dato):
        print("guardando en memoria (prueba): " + dato)

registrar(BaseDeDatos(), "L1")
registrar(AlmacenFalso(), "L1")   # para probar, sin base real
