# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10, Lección 16 · ISP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/16-isp/paso5_solucionario/nivel_avanzado.py
from abc import ABC, abstractmethod


# Problema 9: Almacen gordo (agregar, obtener, listar, borrar, exportar_csv) con dos clientes:
#   - reporte usa obtener + listar   -> Consulta
#   - importador usa agregar         -> Carga
class Consulta(ABC):
    @abstractmethod
    def obtener(self, ref): ...

    @abstractmethod
    def listar(self): ...


class Carga(ABC):
    @abstractmethod
    def agregar(self, ref): ...


class Almacen(Consulta, Carga):
    def __init__(self):
        self._datos = []

    def agregar(self, ref):
        self._datos.append(ref)

    def obtener(self, ref):
        return ref if ref in self._datos else None

    def listar(self):
        return list(self._datos)


def importar(carga: Carga, refs):           # cliente que solo carga
    for ref in refs:
        carga.agregar(ref)


def reporte(consulta: Consulta):            # cliente que solo consulta
    return f"{len(consulta.listar())} lotes: {consulta.listar()}"


almacen = Almacen()
importar(almacen, ["L1", "L2"])
print("P9:", reporte(almacen))


# Problema 10: duck typing. La función solo LLAMA obtener(); sirve cualquier objeto que lo tenga.
class Catalogo:                             # no hereda de nada
    def obtener(self, ref):
        return {"L1": "mesa"}.get(ref)


def describir(cualquiera, ref):
    return f"{ref} es {cualquiera.obtener(ref)}"


print("P10:", describir(Catalogo(), "L1"), "| ¿hereda de Consulta?", isinstance(Catalogo(), Consulta))


# Problema 11: Notificaciones combina dos ABC pequeñas; cada cliente pide solo la suya.
class Correo(ABC):
    @abstractmethod
    def enviar_correo(self, texto): ...


class Sms(ABC):
    @abstractmethod
    def enviar_sms(self, texto): ...


class Notificaciones(Correo, Sms):
    def enviar_correo(self, texto):
        return "correo: " + texto

    def enviar_sms(self, texto):
        return "sms: " + texto


def boletin(correo: Correo):
    return correo.enviar_correo("ofertas")


def alerta(sms: Sms):
    return sms.enviar_sms("pedido listo")


n = Notificaciones()
print("P11:", boletin(n), "|", alerta(n))


# Problema 12 (puente al libro, cap. 2): "a repository is any object that has add(thing)
# and get(id) methods". Ninguna herencia: solo los dos métodos que el cliente usa.
class RepositorioCasero:
    def __init__(self):
        self._lotes = {}

    def add(self, lote):
        self._lotes[lote] = lote

    def get(self, referencia):
        return self._lotes.get(referencia)


def guardar_lote(repo, lote):               # solo usa add y get
    repo.add(lote)
    return repo.get(lote)


print("P12:", guardar_lote(RepositorioCasero(), "lote-7"))
