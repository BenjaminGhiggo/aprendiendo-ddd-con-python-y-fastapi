# paso4_tu_turno_solucion.py — PASO 4 de la Lección 16: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/16-isp/paso3_tu_turno.py lecciones/16-isp/paso4_tu_turno_solucion.py
# Si tu versión es distinta pero los tests pasan, también está bien.
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
    escritor.agregar(ref)
    return "respaldado: " + ref


class SoloLectura(Lector):
    """Implementa SOLO Lector: no debe tener agregar()."""

    def obtener(self, ref):
        # TODO 2: devuelve el texto "solo-lectura:" seguido de ref (sin espacio).
        return "solo-lectura:" + ref


class Repositorio(Lector, Escritor):
    """Cumple las DOS interfaces pequeñas (receta I3/I6)."""

    def __init__(self):
        # TODO 3: crea un diccionario vacío en self._datos.
        self._datos = {}

    def agregar(self, ref):
        # TODO 4: guarda ref en self._datos (clave y valor: ref).
        self._datos[ref] = ref

    def obtener(self, ref):
        # TODO 5: devuelve el valor guardado para ref, o None si no está (usa .get).
        return self._datos.get(ref)
