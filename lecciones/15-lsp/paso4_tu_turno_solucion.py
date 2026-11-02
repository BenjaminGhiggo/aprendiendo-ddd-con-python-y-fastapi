# paso4_tu_turno_solucion.py — PASO 4 de la Lección 15: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/15-lsp/paso3_tu_turno.py lecciones/15-lsp/paso4_tu_turno_solucion.py
# Si tu versión es distinta pero los tests pasan, también está bien.
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
        self._datos = []

    def agregar(self, ref):
        # TODO 2: agrega ref a la lista (receta LS1: misma firma que la madre).
        self._datos.append(ref)

    def obtener(self, ref):
        # TODO 3: si ref está en la lista devuelve ref; si no, devuelve None (receta LS4).
        if ref in self._datos:
            return ref
        return None


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
        self.lado = lado

    def area(self):
        return self.lado * self.lado
