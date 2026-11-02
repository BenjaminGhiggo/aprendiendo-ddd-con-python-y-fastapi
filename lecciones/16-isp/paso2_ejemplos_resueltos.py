# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 16 (ISP).
# Los 4 ejemplos resueltos del README (§9).
# Ejecuta:  uv run python lecciones/16-isp/paso2_ejemplos_resueltos.py
from abc import ABC, abstractmethod

print("--- Ejemplo 1: Lector y Escritor (fácil) ---")


# Paso 1: dos interfaces pequeñas en vez de una grande.
class Lector(ABC):
    @abstractmethod
    def obtener(self, ref): ...


class Escritor(ABC):
    @abstractmethod
    def agregar(self, ref): ...


# Paso 2: el repositorio cumple ambas porque necesita ambas.
class Repositorio(Lector, Escritor):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


# Paso 3: el reporte solo pide un Lector.
def reporte(lector: Lector, ref):
    return f"Encontrado: {lector.obtener(ref)}"


repo = Repositorio()
repo.agregar("LOTE-001")
print(reporte(repo, "LOTE-001"))

print()
print("--- Ejemplo 2: la impresora multifunción (fácil) ---")


# Paso 1 (violación): una interfaz gorda obliga a la impresora simple a "implementar" fax.
class Multifuncion(ABC):
    @abstractmethod
    def imprimir(self, texto): ...

    @abstractmethod
    def escanear(self): ...

    @abstractmethod
    def fax(self, numero): ...


class ImpresoraSimpleMala(Multifuncion):
    def imprimir(self, texto):
        return "imprime " + texto

    def escanear(self):
        raise NotImplementedError("no escanea")

    def fax(self, numero):
        raise NotImplementedError("no tiene fax")


try:
    ImpresoraSimpleMala().escanear()
except NotImplementedError as error:
    print("ROMPE:", error)


# Paso 2 (refactor): una interfaz por capacidad.
class Imprimible(ABC):
    @abstractmethod
    def imprimir(self, texto): ...


class Escaneable(ABC):
    @abstractmethod
    def escanear(self): ...


class ImpresoraSimple(Imprimible):          # solo lo que tiene
    def imprimir(self, texto):
        return "imprime " + texto


class Multifuncional(Imprimible, Escaneable):   # la que tiene más, cumple más
    def imprimir(self, texto):
        return "imprime " + texto

    def escanear(self):
        return "escanea"


# Paso 3 (uso): cada cliente pide solo la capacidad que necesita.
def imprimir_todo(impresoras, texto):
    for impresora in impresoras:
        print(type(impresora).__name__, "->", impresora.imprimir(texto))


imprimir_todo([ImpresoraSimple(), Multifuncional()], "hola")
print("Multifuncional ->", Multifuncional().escanear())

print()
print("--- Ejemplo 3: un falso pequeño para probar el reporte (intermedio) ---")


# Paso 1: reporte depende solo de Lector, así que el falso solo necesita obtener().
class LectorFalso(Lector):
    def __init__(self, datos):
        self.datos = datos

    def obtener(self, ref):
        return self.datos.get(ref)


# Paso 2: el test no fabrica métodos que nunca se usan (agregar, borrar...).
falso = LectorFalso({"L1": "mesa"})
assert reporte(falso, "L1") == "Encontrado: mesa"
assert reporte(falso, "NO") == "Encontrado: None"

# Paso 3: listo, y el falso tiene SOLO lo necesario.
print("Test del reporte con LectorFalso: OK | ¿el falso tiene agregar?", hasattr(falso, "agregar"))

print()
print("--- Ejemplo 4: duck typing, como dice el cap. 2 (avanzado) ---")


# Paso 1: "a repository is any object that has add(thing) and get(id) methods".
class AlmacenEnLista:                       # NO hereda de ninguna ABC
    def __init__(self):
        self._lotes = []

    def add(self, lote):
        self._lotes.append(lote)

    def get(self, referencia):
        for lote in self._lotes:
            if lote == referencia:
                return lote
        return None


# Paso 2: la función de alto nivel solo LLAMA add y get.
def guardar_y_confirmar(repo, lote):
    repo.add(lote)
    return repo.get(lote) == lote


# Paso 3: funciona con cualquier objeto que tenga esos dos métodos.
print("¿Guardado?", guardar_y_confirmar(AlmacenEnLista(), "lote-9"))
print("¿Es un Lector (ABC)?", isinstance(AlmacenEnLista(), Lector))
