import pytest
import comandos
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


def _uow_con_producto(cantidad=100):
    uow = UoWFalsa()
    uow.productos.agregar(Producto("MESA", [Lote("l1", "MESA", cantidad, eta=None)]))
    return uow


def test_comando_asignar_registra_la_asignacion():
    mensajeria.asignaciones_registradas.clear()
    mensajeria.manejar(comandos.Asignar("o1", "MESA", 10), _uow_con_producto())
    assert mensajeria.asignaciones_registradas == ["l1"]


def test_los_errores_de_comandos_propagan():
    uow = UoWFalsa()   # sin producto
    with pytest.raises(mensajeria.SkuInvalido):
        mensajeria.manejar(comandos.Asignar("o1", "XXX", 10), uow)


def test_los_errores_de_eventos_se_aislan():
    mensajeria.asignaciones_registradas.clear()
    def revienta(evento, uow):
        raise Exception("boom")
    mensajeria.MANEJADORES_EVENTO[eventos.Asignado].append(revienta)
    try:
        mensajeria.manejar(comandos.Asignar("o1", "MESA", 10), _uow_con_producto())
        # el comando se completó y el buen handler corrió, pese al que revienta
        assert mensajeria.asignaciones_registradas == ["l1"]
    finally:
        mensajeria.MANEJADORES_EVENTO[eventos.Asignado].pop()
