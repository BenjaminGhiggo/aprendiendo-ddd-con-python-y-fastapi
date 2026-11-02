# Ej2 — MALA (funciona): se puede crear un repo "base" vacío que no hace nada.
class RepositorioBase:
    def agregar(self, ref):
        pass            # no obliga a nadie; se puede instanciar e ignorar

repo = RepositorioBase()
repo.agregar("L1")      # "funciona" pero no guarda nada: bug silencioso
print("guardado?:", getattr(repo, "datos", "no existe"))
