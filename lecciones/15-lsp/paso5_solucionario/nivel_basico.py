# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10, Lección 15 · LSP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/15-lsp/paso5_solucionario/nivel_basico.py

# Problema 1: LSP en una frase.
print("P1: si el código funciona con la madre, debe funcionar IGUAL con cualquier hija")


# Problema 2: describir(animal) funciona con cualquier Animal que cumpla hablar().
class Animal:
    def hablar(self):
        return "..."


class Perro(Animal):
    def hablar(self):
        return "guau"


class Gato(Animal):
    def hablar(self):
        return "miau"


def describir(animal):
    return f"dice {animal.hablar()}"


for animal in [Perro(), Gato()]:
    print("P2:", describir(animal))

# Problema 3: una hija que lanza NotImplementedError en un método de la madre NO cumple LSP:
# quien use la madre no espera ese error.
print("P3: no cumple: lanza un error que la madre no lanzaba (receta LS5)")


# Problema 4: el falso debe devolver lo mismo que el real cuando la referencia NO existe.
class RepositorioReal:
    def __init__(self):
        self._datos = {}

    def obtener(self, ref):
        return self._datos.get(ref)          # None si no existe


class RepositorioFalso:
    def __init__(self):
        self._datos = set()

    def obtener(self, ref):
        if ref in self._datos:
            return ref
        return None                          # igual que el real


print("P4:", RepositorioReal().obtener("X"), RepositorioFalso().obtener("X"))   # None None
