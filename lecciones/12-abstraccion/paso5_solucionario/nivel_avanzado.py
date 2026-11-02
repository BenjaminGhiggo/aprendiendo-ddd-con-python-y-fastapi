# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/12-abstraccion/paso5_solucionario/nivel_avanzado.py
import abc


# Problema 9: abstracto pagar() + concreto confirmar() que lo usa (A8).
class MetodoPago(abc.ABC):
    @abc.abstractmethod
    def pagar(self, monto):
        raise NotImplementedError

    def confirmar(self, monto):
        return f"OK: {self.pagar(monto)}"


class Efectivo(MetodoPago):
    def pagar(self, monto):
        return f"pagó {monto} en efectivo"


class Tarjeta(MetodoPago):
    def pagar(self, monto):
        return f"pagó {monto} con tarjeta"


for metodo in [Efectivo(), Tarjeta()]:
    print("P9:", metodo.confirmar(50))


# Problema 10: dos repositorios con el mismo contrato y un cliente que no cambia.
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad


class RepositorioAbstracto(abc.ABC):
    @abc.abstractmethod
    def agregar(self, lote):
        raise NotImplementedError

    @abc.abstractmethod
    def obtener(self, referencia):
        raise NotImplementedError


class RepositorioDiccionario(RepositorioAbstracto):
    def __init__(self):
        self._lotes = {}

    def agregar(self, lote):
        self._lotes[lote.referencia] = lote

    def obtener(self, referencia):
        return self._lotes.get(referencia)


class RepositorioLista(RepositorioAbstracto):
    def __init__(self):
        self._lotes = []

    def agregar(self, lote):
        self._lotes.append(lote)

    def obtener(self, referencia):
        for lote in self._lotes:
            if lote.referencia == referencia:
                return lote
        return None


def buscar_cantidad(repo, referencia):            # el cliente solo conoce el contrato
    return repo.obtener(referencia).cantidad


for repo in [RepositorioDiccionario(), RepositorioLista()]:
    repo.agregar(Lote("L1", 10))
    print("P10:", type(repo).__name__, buscar_cantidad(repo, "L1"))   # 10 en ambos


# Problema 11: "método plantilla": la abstracta arma el resultado; las hijas ponen las partes.
class Reporte(abc.ABC):
    def generar(self):
        return f"{self.titulo()} | {self.cuerpo()}"

    @abc.abstractmethod
    def titulo(self):
        raise NotImplementedError

    @abc.abstractmethod
    def cuerpo(self):
        raise NotImplementedError


class ReporteVentas(Reporte):
    def titulo(self):
        return "VENTAS"

    def cuerpo(self):
        return "3 pedidos"


class ReporteStock(Reporte):
    def titulo(self):
        return "STOCK"

    def cuerpo(self):
        return "25 unidades"


for reporte in [ReporteVentas(), ReporteStock()]:
    print("P11:", reporte.generar())


# Problema 12 (puente al libro): "class AbstractRepository(abc.ABC):" con métodos
# "@abc.abstractmethod ... raise NotImplementedError" (cap. 2), y un repositorio falso
# para probar una función de asignación sin base de datos.
class RepositorioConListar(abc.ABC):
    @abc.abstractmethod
    def agregar(self, lote):
        raise NotImplementedError

    @abc.abstractmethod
    def obtener(self, referencia):
        raise NotImplementedError

    @abc.abstractmethod
    def listar(self):
        raise NotImplementedError


class RepositorioFalso(RepositorioConListar):
    def __init__(self, lotes):
        self._lotes = list(lotes)

    def agregar(self, lote):
        self._lotes.append(lote)

    def obtener(self, referencia):
        for lote in self._lotes:
            if lote.referencia == referencia:
                return lote
        return None

    def listar(self):
        return self._lotes


def asignar(referencia, pedido, repo):
    lote = repo.obtener(referencia)
    if pedido > lote.cantidad:
        raise ValueError("No hay stock suficiente")
    lote.cantidad = lote.cantidad - pedido
    return lote.cantidad


falso = RepositorioFalso([Lote("L1", 10), Lote("L2", 5)])
print("P12:", "L1 queda con", asignar("L1", 3, falso))     # L1 queda con 7
try:
    asignar("L2", 50, falso)
except ValueError as error:
    print("P12:", error)
print("P12: lotes en el repo:", len(falso.listar()))      # 2
