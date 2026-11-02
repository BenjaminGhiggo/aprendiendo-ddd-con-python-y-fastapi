# paso1_formulas.py — PASO 1 de la Lección 15 (LSP).
# Cada bloque es una "receta" (regla del contrato) de la tabla del README (§5): LS1...LS6.
# La prueba de fuego en todas: una función escrita para la MADRE debe funcionar IGUAL con la HIJA.
# Ejecuta:  uv run python lecciones/15-lsp/paso1_formulas.py
from abc import ABC, abstractmethod


class RepositorioAbstracto(ABC):            # el CONTRATO: agregar(ref) y obtener(ref)
    @abstractmethod
    def agregar(self, ref):
        ...

    @abstractmethod
    def obtener(self, ref):
        ...


class RepositorioEnMemoria(RepositorioAbstracto):   # implementación "real"
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)          # si no está: None


class RepositorioFalso(RepositorioAbstracto):       # implementación para tests
    def __init__(self):
        self._datos = set()

    def agregar(self, ref):
        self._datos.add(ref)

    def obtener(self, ref):
        return ref if ref in self._datos else None


def guardar_y_leer(repo, ref):              # código escrito para la MADRE
    repo.agregar(ref)
    return repo.obtener(ref)


# LS1 · Misma FIRMA: mismos nombres de método y mismos parámetros.
print("LS1 misma firma   :", guardar_y_leer(RepositorioEnMemoria(), "L1"), guardar_y_leer(RepositorioFalso(), "L1"))

# LS2 · Mismo TIPO de respuesta: ambos devuelven el texto guardado (str), no otra cosa.
print("LS2 mismo tipo    :", type(guardar_y_leer(RepositorioEnMemoria(), "X")).__name__, type(guardar_y_leer(RepositorioFalso(), "X")).__name__)

# LS3 · No exigir MÁS (precondición): si la madre acepta cualquier referencia, la hija también.
print("LS3 acepta lo mismo:", guardar_y_leer(RepositorioFalso(), "lote con espacios"))

# LS4 · No prometer MENOS (postcondición): "lo que agrego, lo puedo obtener"; y lo que no
#       agregué devuelve None en AMBOS.
print("LS4 misma promesa :", RepositorioEnMemoria().obtener("NO"), RepositorioFalso().obtener("NO"))


# LS5 · No lanzar errores NUEVOS: una hija que "no sabe" hacer algo rompe a quien la usa.
class Ave:
    def volar(self):
        return "vuela"


class Pato(Ave):
    def volar(self):
        return "vuela bajito"


class Pinguino(Ave):                        # VIOLACIÓN: hereda volar() pero no puede
    def volar(self):
        raise NotImplementedError("los pingüinos no vuelan")


try:
    for ave in [Pato(), Pinguino()]:
        print("LS5 ave.volar()   :", ave.volar())
except NotImplementedError as error:
    print("LS5 VIOLACIÓN     : NotImplementedError ->", error)


# LS6 · Respetar las INVARIANTES de la madre (Rectángulo/Cuadrado).
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def poner_ancho(self, valor):
        self.ancho = valor

    def poner_alto(self, valor):
        self.alto = valor

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):                 # VIOLACIÓN: cambiar el alto cambia el ancho
    def __init__(self, lado):
        super().__init__(lado, lado)

    def poner_ancho(self, valor):
        self.ancho = valor
        self.alto = valor

    def poner_alto(self, valor):
        self.ancho = valor
        self.alto = valor


def agrandar(rectangulo):                   # escrito pensando en la MADRE: espera 5 x 4 = 20
    rectangulo.poner_ancho(5)
    rectangulo.poner_alto(4)
    return rectangulo.area()


print("LS6 invariante    : Rectangulo ->", agrandar(Rectangulo(1, 1)), "| Cuadrado ->", agrandar(Cuadrado(1)), "(¡esperaba 20!)")

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UN bloque, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# class RepoRoto(RepositorioEnMemoria):
#     def obtener(self):                      # E4: firma distinta (falta ref)
#         return None
# RepoRoto().obtener("L1")                    # -> TypeError: RepoRoto.obtener() takes 1 positional argument but 2 were given
# assert agrandar(Cuadrado(1)) == 20          # E1 -> AssertionError
# ---------------------------------------------------------------------------
