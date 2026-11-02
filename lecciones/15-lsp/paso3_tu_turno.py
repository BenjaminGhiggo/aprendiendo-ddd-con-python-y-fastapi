# paso3_tu_turno.py — PASO 3 de la Lección 15 (LSP · pair programming).
# La comprobación es con PYTEST (TDD): los tests ya están en test_paso3_tu_turno.py y
# empiezan en ROJO. Completa los # TODO hasta verlos en VERDE:
#   uv run pytest lecciones/15-lsp -q
# Meta: tus clases nuevas deben poder SUSTITUIR a las que ya existen, sin sorpresas.
from abc import ABC, abstractmethod


class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref):
        ...

    @abstractmethod
    def obtener(self, ref):
        ...


class RepositorioEnMemoria(RepositorioAbstracto):
    """La implementación de referencia: tu clase debe comportarse IGUAL."""

    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


def guardar_y_leer(repo, ref):
    repo.agregar(ref)
    return repo.obtener(ref)


class RepositorioLista(RepositorioAbstracto):
    """Guarda las referencias en una LISTA, pero cumple el MISMO contrato."""

    def __init__(self):
        # TODO 1: crea una lista vacía en self._datos.
        pass

    def agregar(self, ref):
        # TODO 2: agrega ref a la lista (receta LS1: misma firma que la madre).
        pass

    def obtener(self, ref):
        # TODO 3: si ref está en la lista devuelve ref; si no, devuelve None (receta LS4).
        return "TODO"


class Figura:
    def area(self):
        return 0


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


# TODO 4: Cuadrado YA hereda de Figura, y NO de Rectangulo (receta LS6): no lo cambies.
#         Completa __init__ (guarda el lado en self.lado) y area (lado por lado).
class Cuadrado(Figura):
    def __init__(self, lado):
        pass

    def area(self):
        return None
