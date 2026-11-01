# Ej1 — MALA (funciona): la lógica CREA la base de datos adentro (acoplada al detalle).
class BaseDeDatos:
    def guardar(self, dato):
        print("guardando en MySQL: " + dato)

def registrar(dato):
    db = BaseDeDatos()     # el alto nivel depende de una clase concreta
    db.guardar(dato)       # no puedo probarlo sin una base real, ni cambiarla

registrar("L1")
