import eventos
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


def test_asignar_por_el_bus_registra_la_asignacion():
    mensajeria.asignaciones_registradas.clear()
    uow = UoWFalsa()
    uow.productos.agregar(Producto("MESA", [Lote("l1", "MESA", 100, eta=None)]))
    mensajeria.manejar(eventos.AsignacionRequerida("o1", "MESA", 10), uow)
    assert mensajeria.asignaciones_registradas == ["l1"]   # cascada: Asignado -> registrar


def test_sin_stock_por_el_bus_notifica():
    mensajeria.notificaciones_sin_stock.clear()
    uow = UoWFalsa()
    uow.productos.agregar(Producto("MESA", [Lote("l1", "MESA", 5, eta=None)]))
    mensajeria.manejar(eventos.AsignacionRequerida("o1", "MESA", 10), uow)
    assert mensajeria.notificaciones_sin_stock == ["MESA"]


def test_cambiar_cantidad_reasigna_lo_que_ya_no_cabe():
    mensajeria.asignaciones_registradas.clear()
    uow = UoWFalsa()
    lote = Lote("l1", "MESA", 50, eta=None)
    producto = Producto("MESA", [lote])
    uow.productos.agregar(producto)
    mensajeria.manejar(eventos.AsignacionRequerida("o1", "MESA", 50), uow)   # usa todo
    # ahora el lote baja a 30: sobran 20, que deben re-asignarse (no hay otro lote)
    mensajeria.manejar(eventos.CambiarCantidadLote("l1", 30), uow)
    # la línea se re-encoló como AsignacionRequerida; sin otro lote, queda SinStock
    assert "l1" in mensajeria.asignaciones_registradas
