# Ej3 — BUENA: toda subclase de Pato cumple lo que Pato promete.
class Pato:
    def hacer_sonido(self):
        return "Cuac"

class PatoBebe(Pato):
    def hacer_sonido(self):
        return "cuac suave"   # distinto, pero sigue siendo un sonido válido

def coro(patos):
    return [p.hacer_sonido() for p in patos]

print(coro([Pato(), PatoBebe()]))   # ambos son sustituibles por Pato
