# Ej2 — MALA (funciona): un reporte recibe un repo completo pero solo lee.
class Repositorio:
    def __init__(self):
        self.datos = {"L1": "Lote 1"}
    def agregar(self, ref, valor):
        self.datos[ref] = valor
    def borrar(self, ref):
        del self.datos[ref]
    def obtener(self, ref):
        return self.datos.get(ref)

def reporte(repo):
    # solo necesita obtener(), pero depende de TODO el repo (agregar, borrar...)
    return "Reporte: " + str(repo.obtener("L1"))

print(reporte(Repositorio()))
