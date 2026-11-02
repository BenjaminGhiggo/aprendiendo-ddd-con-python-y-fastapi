# Ej3 — MALA: la subclase cambia el SIGNIFICADO del método (rompe la expectativa).
class Pato:
    def hacer_sonido(self):
        return "Cuac"

class PatoDeHule(Pato):
    def hacer_sonido(self):
        raise Exception("¡Soy de hule, no sueno!")  # rompe lo que promete Pato

def coro(patos):
    return [p.hacer_sonido() for p in patos]

print(coro([Pato()]))
# print(coro([Pato(), PatoDeHule()]))  # esto REVIENTA: PatoDeHule no es sustituible
print("PatoDeHule rompe el contrato de Pato")
