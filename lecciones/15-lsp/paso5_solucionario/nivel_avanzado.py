# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10, Lección 15 · LSP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/15-lsp/paso5_solucionario/nivel_avanzado.py
from abc import ABC, abstractmethod


def probar_contrato(repo):
    repo.agregar("Lote-A")
    assert repo.obtener("Lote-A") == "Lote-A", "lo agregado se debe poder obtener"
    assert repo.obtener("NO") is None, "lo no agregado debe dar None"
    return "OK"


# Problema 9: un falso "con trampa" (guarda en minúsculas). El test de contrato lo detecta.
class RepoBueno:
    def __init__(self):
        self._s = set()

    def agregar(self, ref):
        self._s.add(ref)

    def obtener(self, ref):
        return ref if ref in self._s else None


class RepoConTrampa:
    def __init__(self):
        self._s = set()

    def agregar(self, ref):
        self._s.add(ref.lower())             # ¡cambia el dato!

    def obtener(self, ref):
        return ref if ref in self._s else None


for repo in [RepoBueno(), RepoConTrampa()]:
    try:
        print("P9:", type(repo).__name__, "->", probar_contrato(repo))
    except AssertionError as error:
        print("P9:", type(repo).__name__, "-> FALLA:", error)


# Problema 10: Notificador.enviar() promete devolver True si envió. Un falso que devuelve
# None rompe a quien hace "if notificador.enviar(...)" (promete MENOS: LS4).
class Notificador:
    def enviar(self, mensaje):
        print("    (enviando)", mensaje)
        return True


class NotificadorFalsoMalo(Notificador):
    def enviar(self, mensaje):
        pass                                 # devuelve None


class NotificadorFalso(Notificador):
    def __init__(self):
        self.enviados = []

    def enviar(self, mensaje):
        self.enviados.append(mensaje)
        return True                          # cumple la misma promesa


def avisar(notificador, mensaje):
    if notificador.enviar(mensaje):
        return "avisado"
    return "NO avisado"


print("P10: real ->", avisar(Notificador(), "hola"))
print("P10: falso malo ->", avisar(NotificadorFalsoMalo(), "hola"))
falso = NotificadorFalso()
print("P10: falso bueno ->", avisar(falso, "hola"), falso.enviados)


# Problema 11: reemplazar una cadena de isinstance por subclases que cumplen el contrato.
class Empleado:
    def __init__(self, sueldo):
        self.sueldo = sueldo

    def pago(self):
        return self.sueldo


class Gerente(Empleado):
    def pago(self):
        return self.sueldo + 500             # su diferencia vive en SU clase


def planilla_con_isinstance(empleados):      # ANTES: pregunta el tipo
    total = 0
    for e in empleados:
        if isinstance(e, Gerente):
            total = total + e.sueldo + 500
        else:
            total = total + e.sueldo
    return total


def planilla(empleados):                     # DESPUÉS: confía en el contrato pago()
    total = 0
    for e in empleados:
        total = total + e.pago()
    return total


equipo = [Empleado(1000), Gerente(2000)]
print("P11:", planilla_con_isinstance(equipo), planilla(equipo))   # 3500 3500


# Problema 12 (puente al libro, cap. 2): "class FakeRepository(AbstractRepository):"
# con un set, intercambiable por el real en la función de alto nivel.
class AbstractRepository(ABC):
    @abstractmethod
    def add(self, lote):
        ...

    @abstractmethod
    def get(self, referencia):
        ...


class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad


class RepositorioDict(AbstractRepository):   # "real" (en el libro sería SQLAlchemy)
    def __init__(self):
        self._lotes = {}

    def add(self, lote):
        self._lotes[lote.referencia] = lote

    def get(self, referencia):
        return self._lotes[referencia]


class FakeRepository(AbstractRepository):    # como en el libro: guarda en un set
    def __init__(self, lotes):
        self._lotes = set(lotes)

    def add(self, lote):
        self._lotes.add(lote)

    def get(self, referencia):
        return next(l for l in self._lotes if l.referencia == referencia)


def cantidad_de(repo, referencia):           # alto nivel: le da igual cuál recibe
    return repo.get(referencia).cantidad


real = RepositorioDict()
real.add(Lote("lote-1", 20))
falso = FakeRepository([Lote("lote-1", 20)])
print("P12:", cantidad_de(real, "lote-1"), cantidad_de(falso, "lote-1"))   # 20 20
