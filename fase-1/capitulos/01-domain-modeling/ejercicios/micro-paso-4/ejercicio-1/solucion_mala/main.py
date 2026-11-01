# Ej1 — MALA (funciona): "elegir entre varios lotes" metido como método de Lote.
class Lote:
    def __init__(self, ref, disponible):
        self.ref = ref
        self.disponible = disponible
    def asignar_entre(self, otros_lotes, cantidad):
        # un lote no debería saber de "los otros lotes": no es su responsabilidad
        for lote in [self] + otros_lotes:
            if lote.disponible >= cantidad:
                lote.disponible -= cantidad
                return lote.ref

a = Lote("A", 0)
b = Lote("B", 10)
print(a.asignar_entre([b], 5))   # "B"
