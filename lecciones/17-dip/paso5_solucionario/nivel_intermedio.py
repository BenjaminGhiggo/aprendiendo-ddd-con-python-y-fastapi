# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10, Lección 17 · DIP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/17-dip/paso5_solucionario/nivel_intermedio.py
from abc import ABC, abstractmethod


class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

    @abstractmethod
    def obtener(self, ref): ...


class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


# Problema 5: inyección por constructor (receta DIP4).
class Tienda:
    def __init__(self, repo):
        self.repo = repo

    def vender(self, producto):
        self.repo.agregar(producto)
        return f"vendido: {self.repo.obtener(producto)}"


print("P5:", Tienda(RepositorioEnMemoria()).vender("mesa"))


# Problema 6: inyectar una FUNCIÓN para el aviso (receta DIP7).
def registrar_venta(monto, notificar):
    notificar(f"venta de {monto}")


buzon_falso = []
registrar_venta(100, buzon_falso.append)    # en el test: se guarda en una lista
registrar_venta(200, print)                 # "en producción": se muestra
print("P6: buzón falso =", buzon_falso)


# Problema 7: pasar la CLASE en vez de una INSTANCIA. Mensaje real:
def registrar_lote(repo, referencia):
    repo.agregar(referencia)
    return repo.obtener(referencia)


try:
    registrar_lote(RepositorioEnMemoria, "L1")          # ¡faltan los paréntesis!
except TypeError as error:
    print("P7: error ->", error)
print("P7: corregido ->", registrar_lote(RepositorioEnMemoria(), "L1"))


# Problema 8: una abstracción que "filtra" el detalle (ejecutar_sql) sigue atando a SQL.
# Rediseño: métodos con nombres del NEGOCIO; el SQL queda escondido en el detalle.
class RepositorioPedidos(ABC):
    @abstractmethod
    def guardar(self, pedido): ...

    @abstractmethod
    def buscar(self, id_pedido): ...


class RepositorioPedidosEnMemoria(RepositorioPedidos):
    def __init__(self):
        self._pedidos = {}

    def guardar(self, pedido):
        self._pedidos[pedido["id"]] = pedido

    def buscar(self, id_pedido):
        return self._pedidos.get(id_pedido)


repo = RepositorioPedidosEnMemoria()
repo.guardar({"id": "o1", "total": 50})
print("P8: buscar('o1') ->", repo.buscar("o1"), "| la lógica no ve ningún SQL")
