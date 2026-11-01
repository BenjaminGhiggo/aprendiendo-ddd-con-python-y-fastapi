# Ej3 — MALA (funciona): un "repo base" con métodos vacíos, instanciable.
class RepositorioBase:
    def agregar(self, lote):
        pass            # no obliga a nadie; se puede usar y no guardar nada

repo = RepositorioBase()
repo.agregar("L1")
print("guardado?:", getattr(repo, "_lotes", "no existe"))   # bug silencioso
