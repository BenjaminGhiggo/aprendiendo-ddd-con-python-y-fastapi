# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 15 (LSP).
# Los 4 ejemplos resueltos del README (§9).
# Ejecuta:  uv run python lecciones/15-lsp/paso2_ejemplos_resueltos.py
from abc import ABC, abstractmethod

print("--- Ejemplo 1: dos repositorios intercambiables (fácil) ---")


# Paso 1: el contrato (la madre abstracta).
class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref):
        ...

    @abstractmethod
    def obtener(self, ref):
        ...


# Paso 2: dos hijas que cumplen el MISMO contrato (guardan distinto por dentro).
class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


class RepositorioFalso(RepositorioAbstracto):
    def __init__(self):
        self._datos = set()

    def agregar(self, ref):
        self._datos.add(ref)

    def obtener(self, ref):
        return ref if ref in self._datos else None


# Paso 3: la función escrita para la madre funciona igual con las dos.
def guardar_y_leer(repo, ref):
    repo.agregar(ref)
    return repo.obtener(ref)


print(guardar_y_leer(RepositorioEnMemoria(), "LOTE-001"))
print(guardar_y_leer(RepositorioFalso(), "LOTE-001"))

print()
print("--- Ejemplo 2: el pingüino que no vuela (fácil) ---")


# Paso 1 (violación): Pinguino hereda volar() pero lanza un error que la madre no lanzaba.
class AveMala:
    def volar(self):
        return "vuela"


class PinguinoMalo(AveMala):
    def volar(self):
        raise NotImplementedError("los pingüinos no vuelan")


try:
    for ave in [AveMala(), PinguinoMalo()]:
        print(ave.volar())
except NotImplementedError as error:
    print("ROMPE:", error)


# Paso 2 (refactor): la madre solo promete lo que TODAS cumplen; volar va en otra rama.
class Ave:
    def comer(self):
        return "come"


class AveVoladora(Ave):
    def volar(self):
        return "vuela"


class Pato(AveVoladora):
    pass


class Pinguino(Ave):                        # ya no promete volar
    def nadar(self):
        return "nada"


# Paso 3 (uso): quien necesita volar pide AveVoladora; nadie se lleva sorpresas.
for ave in [Pato(), Pinguino()]:
    print(type(ave).__name__, "->", ave.comer())
for voladora in [Pato()]:
    print(type(voladora).__name__, "->", voladora.volar())

print()
print("--- Ejemplo 3: Rectángulo y Cuadrado (intermedio) ---")


# Paso 1 (violación): Cuadrado "es un" rectángulo en geometría, pero NO en el código.
class RectanguloMalo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def poner_ancho(self, valor):
        self.ancho = valor

    def poner_alto(self, valor):
        self.alto = valor

    def area(self):
        return self.ancho * self.alto


class CuadradoMalo(RectanguloMalo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def poner_ancho(self, valor):
        self.ancho = valor
        self.alto = valor

    def poner_alto(self, valor):
        self.ancho = valor
        self.alto = valor


def agrandar(r):
    r.poner_ancho(5)
    r.poner_alto(4)
    return r.area()


print("Rectángulo:", agrandar(RectanguloMalo(1, 1)), "| Cuadrado:", agrandar(CuadradoMalo(1)), "<- esperaba 20")


# Paso 2 (refactor): hermanas, no madre e hija. Comparten solo lo que ambas cumplen: area().
class Figura:
    def area(self):
        return 0


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


# Paso 3 (uso): cualquier Figura se usa donde se espera una Figura.
def area_total(figuras):
    total = 0
    for figura in figuras:
        total = total + figura.area()
    return total


print("Área total:", area_total([Rectangulo(5, 4), Cuadrado(3)]))   # 20 + 9

print()
print("--- Ejemplo 4: un test de contrato para el real y el falso, como en el cap. 2 (avanzado) ---")


# Paso 1: UNA función de prueba que describe el contrato.
def probar_contrato(repo):
    repo.agregar("L1")
    assert repo.obtener("L1") == "L1", "lo agregado se debe poder obtener"
    assert repo.obtener("NO-EXISTE") is None, "lo no agregado debe dar None"
    return "OK"


# Paso 2: la pasamos a cada implementación.
print("RepositorioEnMemoria:", probar_contrato(RepositorioEnMemoria()))
print("RepositorioFalso    :", probar_contrato(RepositorioFalso()))


# Paso 3: un falso "con trampa" que guarda en minúsculas NO cumple el contrato.
class RepositorioFalsoConTrampa(RepositorioAbstracto):
    def __init__(self):
        self._datos = set()

    def agregar(self, ref):
        self._datos.add(ref.lower())

    def obtener(self, ref):
        return ref if ref in self._datos else None


try:
    probar_contrato(RepositorioFalsoConTrampa())
except AssertionError as error:
    print("RepositorioFalsoConTrampa: FALLA ->", error)
