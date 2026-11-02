# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10, Lección 17 · DIP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/17-dip/paso5_solucionario/nivel_avanzado.py
from abc import ABC, abstractmethod


class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

    @abstractmethod
    def obtener(self, ref): ...


# Problema 9: cambiar de almacenamiento (memoria -> "archivo") SIN tocar la lógica.
class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


class RepositorioArchivo(RepositorioAbstracto):   # simula líneas de un archivo de texto
    def __init__(self):
        self.lineas = []

    def agregar(self, ref):
        self.lineas.append(ref)

    def obtener(self, ref):
        return ref if ref in self.lineas else None


def registrar_lote(repo, referencia):       # la lógica: NO cambia
    repo.agregar(referencia)
    return repo.obtener(referencia)


for repo in [RepositorioEnMemoria(), RepositorioArchivo()]:
    print("P9:", type(repo).__name__, "->", registrar_lote(repo, "LOTE-9"))


# Problema 10: probar el servicio sin base de datos, con un falso.
class ServicioPedidos:
    def __init__(self, repo):
        self.repo = repo

    def registrar(self, ref):
        self.repo.agregar(ref)
        return self.repo.obtener(ref)


class RepositorioFalso(RepositorioAbstracto):
    def __init__(self):
        self._datos = set()

    def agregar(self, ref):
        self._datos.add(ref)

    def obtener(self, ref):
        return ref if ref in self._datos else None


falso = RepositorioFalso()
servicio = ServicioPedidos(falso)
assert servicio.registrar("P1") == "P1"
assert servicio.repo is falso
assert falso.obtener("NO") is None
print("P10: OK (3 asserts sin base de datos)")


# Problema 11: componer en UN solo lugar (un mini "bootstrap", como en el cap. 13).
def armar_app(modo):
    if modo == "test":
        repo = RepositorioFalso()
    else:
        repo = RepositorioEnMemoria()        # en el libro: el repositorio de SQLAlchemy
    return ServicioPedidos(repo)


print("P11:", type(armar_app("test").repo).__name__, "|", type(armar_app("produccion").repo).__name__)


# Problema 12 (puente al libro, caps. 2 y 4): AbstractRepository + FakeRepository + un servicio.
class AbstractRepository(ABC):
    @abstractmethod
    def add(self, lote): ...

    @abstractmethod
    def get(self, referencia): ...


class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad


class FakeRepository(AbstractRepository):   # como en el libro: guarda en un set
    def __init__(self, lotes):
        self._lotes = set(lotes)

    def add(self, lote):
        self._lotes.add(lote)

    def get(self, referencia):
        for lote in self._lotes:
            if lote.referencia == referencia:
                return lote
        return None


def reservar(referencia, cantidad, repo: AbstractRepository):   # alto nivel
    lote = repo.get(referencia)
    if lote is None or lote.cantidad < cantidad:
        return "no se pudo"
    lote.cantidad = lote.cantidad - cantidad
    return f"reservado; quedan {lote.cantidad}"


repo = FakeRepository([Lote("lote-1", 10)])
print("P12:", reservar("lote-1", 4, repo))   # reservado; quedan 6
print("P12:", reservar("lote-1", 9, repo))   # no se pudo
print("P12:", reservar("lote-X", 1, repo))   # no se pudo
