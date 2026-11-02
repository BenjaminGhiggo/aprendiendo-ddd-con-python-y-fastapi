# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 17 (DIP) ⭐.
# Los 4 ejemplos resueltos del README (§9).
# Ejecuta:  uv run python lecciones/17-dip/paso2_ejemplos_resueltos.py
from abc import ABC, abstractmethod

print("--- Ejemplo 1: registrar un lote recibiendo el repositorio (fácil) ---")


# Paso 1: la abstracción (lo que la lógica necesita: agregar y obtener).
class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

    @abstractmethod
    def obtener(self, ref): ...


# Paso 2: un detalle que la implementa.
class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


# Paso 3: la lógica RECIBE el repositorio (inyección); no lo crea.
def registrar_lote(repo: RepositorioAbstracto, referencia):
    repo.agregar(referencia)
    return repo.obtener(referencia)


repo = RepositorioEnMemoria()                # decidimos AFUERA qué detalle usar
print(registrar_lote(repo, "LOTE-001"))

print()
print("--- Ejemplo 2: guardar notas sin atarse a un archivo (fácil) ---")


# Paso 1 (violación): la lógica crea su detalle adentro.
class ArchivoTexto:
    def __init__(self):
        self.lineas = []

    def escribir(self, texto):
        self.lineas.append(texto)


def guardar_nota_atada(texto):
    archivo = ArchivoTexto()                # ← no puedo cambiarlo ni revisarlo desde afuera
    archivo.escribir(texto.upper())
    return len(archivo.lineas)


print("atada:", guardar_nota_atada("hola"))


# Paso 2 (refactor): la lógica recibe DÓNDE guardar.
def guardar_nota(texto, almacenamiento):
    almacenamiento.escribir(texto.upper())


# Paso 3 (uso): ahora yo controlo el detalle y puedo revisar qué se guardó.
archivo = ArchivoTexto()
guardar_nota("hola", archivo)
guardar_nota("chau", archivo)
print("inyectada:", archivo.lineas)

print()
print("--- Ejemplo 3: servicio con inyección por constructor + test con falso (intermedio) ---")


# Paso 1: el servicio recibe el repositorio en __init__.
class ServicioPedidos:
    def __init__(self, repo):
        self.repo = repo

    def registrar(self, ref):
        self.repo.agregar(ref)
        return self.repo.obtener(ref)


# Paso 2: un falso que cumple el contrato (LSP de la Lección 15).
class RepositorioFalso(RepositorioAbstracto):
    def __init__(self):
        self._datos = set()

    def agregar(self, ref):
        self._datos.add(ref)

    def obtener(self, ref):
        return ref if ref in self._datos else None


# Paso 3: el test no necesita base de datos.
falso = RepositorioFalso()
servicio = ServicioPedidos(falso)
assert servicio.registrar("P1") == "P1"
assert servicio.repo is falso                # usa EXACTAMENTE el que le inyecté
print("Test de ServicioPedidos con RepositorioFalso: OK")

print()
print("--- Ejemplo 4: un mini service layer con FakeRepository, como en los caps. 2 y 4 (avanzado) ---")


# Paso 1: la abstracción del libro: add y get (cap. 2).
class AbstractRepository(ABC):
    @abstractmethod
    def add(self, lote): ...

    @abstractmethod
    def get(self, referencia): ...

    @abstractmethod
    def list(self): ...


class Lote:
    def __init__(self, referencia, sku, cantidad):
        self.referencia = referencia
        self.sku = sku
        self.cantidad = cantidad


# Paso 2: el FakeRepository del libro guarda en un set.
class FakeRepository(AbstractRepository):
    def __init__(self, lotes):
        self._lotes = set(lotes)

    def add(self, lote):
        self._lotes.add(lote)

    def get(self, referencia):
        return next(l for l in self._lotes if l.referencia == referencia)

    def list(self):
        return list(self._lotes)


# Paso 3: el servicio (alto nivel) recibe el repo; en producción sería SQLAlchemy.
def asignar(sku, cantidad, repo: AbstractRepository):
    referencias = []
    for lote in repo.list():                 # un set no tiene orden: juntamos las referencias
        referencias.append(lote.referencia)
    for referencia in sorted(referencias):   # ...y las recorremos en orden alfabético
        lote = repo.get(referencia)
        if lote.sku == sku and lote.cantidad >= cantidad:
            lote.cantidad = lote.cantidad - cantidad
            return lote.referencia
    return None


repo = FakeRepository([Lote("lote-1", "MESA", 10), Lote("lote-2", "MESA", 50)])
print("asignar MESA x 20 ->", asignar("MESA", 20, repo))
print("quedan en lote-2:", repo.get("lote-2").cantidad)
print("asignar SILLA x 1 ->", asignar("SILLA", 1, repo))
