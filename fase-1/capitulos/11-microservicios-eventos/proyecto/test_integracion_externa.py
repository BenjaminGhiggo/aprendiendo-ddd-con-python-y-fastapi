import comandos
import cola_externa
import mensajeria
from modelo import Producto, Lote
from repositorio import RepositorioFalso
from unidad_de_trabajo import UnidadDeTrabajoAbstracta


class UoWFalsa(UnidadDeTrabajoAbstracta):
    def __init__(self):
        self.productos = RepositorioFalso([])
        self.comprometido = False
    def comprometer(self):
        self.comprometido = True
    def deshacer(self):
        pass


def _uow_con_producto(cantidad=100):
    uow = UoWFalsa()
    uow.productos.agregar(Producto("MESA", [Lote("l1", "MESA", cantidad, eta=None)]))
    return uow


def test_al_asignar_se_publica_un_evento_externo():
    cola_externa.limpiar()
    mensajeria.manejar(comandos.Asignar("o1", "MESA", 10), _uow_con_producto())
    assert cola_externa.mensajes_publicados == [
        ("linea_asignada", {"id_pedido": "o1", "sku": "MESA", "ref": "l1"})
    ]


def test_un_mensaje_externo_se_consume_como_comando_interno():
    uow = _uow_con_producto(50)
    mensajeria.manejar(comandos.Asignar("o1", "MESA", 50), uow)   # usa todo
    # llega un mensaje externo pidiendo bajar la cantidad del lote
    mensajeria.consumir_externo({"referencia": "l1", "cantidad": 30}, uow)
    # el lote baja a 30; el producto registró Desasignado y el bus reasignó
    assert uow.productos.obtener("MESA").lotes[0]._cantidad_comprada == 30
