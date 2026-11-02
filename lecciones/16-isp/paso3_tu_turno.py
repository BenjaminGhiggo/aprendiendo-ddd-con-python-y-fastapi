# paso3_tu_turno.py — PASO 3 de la Lección 16 (ISP · pair programming).
# La comprobación es con PYTEST (TDD): los tests ya están en test_paso3_tu_turno.py y
# empiezan en ROJO. Completa los # TODO hasta verlos en VERDE:
#   uv run pytest lecciones/16-isp -q
# Meta: cada pieza depende SOLO de la interfaz pequeña que usa.
from abc import ABC, abstractmethod


class Lector(ABC):
    @abstractmethod
    def obtener(self, ref): ...


class Escritor(ABC):
    @abstractmethod
    def agregar(self, ref): ...


def reporte(lector: Lector, ref):
    return f"Encontrado: {lector.obtener(ref)}"


def respaldo(escritor: Escritor, ref):
    # TODO 1: llama a escritor.agregar(ref) y devuelve el texto "respaldado: " + ref.
    #         (este cliente solo necesita ESCRIBIR: receta I4)
    return None


class SoloLectura(Lector):
    """Implementa SOLO Lector: no debe tener agregar()."""

    def obtener(self, ref):
        # TODO 2: devuelve el texto "solo-lectura:" seguido de ref (sin espacio).
        return None


class Repositorio(Lector, Escritor):
    """Cumple las DOS interfaces pequeñas (receta I3/I6)."""

    def __init__(self):
        # TODO 3: crea un diccionario vacío en self._datos.
        pass

    def agregar(self, ref):
        # TODO 4: guarda ref en self._datos (clave y valor: ref).
        pass

    def obtener(self, ref):
        # TODO 5: devuelve el valor guardado para ref, o None si no está (usa .get).
        return None
