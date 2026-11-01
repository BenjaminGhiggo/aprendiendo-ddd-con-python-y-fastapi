from collections import defaultdict

import pytest
import comandos
import bootstrap
import mensajeria
import notificaciones
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


class NotificacionesFalsas(notificaciones.NotificacionesAbstractas):
    def __init__(self):
        self.enviadas = defaultdict(list)
    def enviar(self, destino, mensaje):
        self.enviadas[destino].append(mensaje)


def _bus(uow, notifs=None):
    # Igual que en el libro: en los tests llamamos a bootstrap con defaults sobreescritos.
    return bootstrap.bootstrap(
        iniciar_orm=False,                       # la fake UoW no usa ORM
        uow=uow,
        notificaciones=notifs or NotificacionesFalsas(),
        publicar=lambda *args: None,             # no publicamos de verdad en los tests
    )


def _uow_con_producto(cantidad=100):
    uow = UoWFalsa()
    uow.productos.agregar(Producto("MESA", [Lote("l1", "MESA", cantidad, eta=None)]))
    return uow


def test_comando_asignar_registra_la_asignacion():
    mensajeria.asignaciones_registradas.clear()
    bus = _bus(_uow_con_producto())
    bus.manejar(comandos.Asignar("o1", "MESA", 10))
    assert mensajeria.asignaciones_registradas == ["l1"]


def test_los_errores_de_comandos_propagan():
    bus = _bus(UoWFalsa())                        # sin producto
    with pytest.raises(mensajeria.SkuInvalido):
        bus.manejar(comandos.Asignar("o1", "XXX", 10))


def test_sin_stock_envia_notificacion_con_el_adaptador_inyectado():
    # Ejemplo trabajado de DI: inyectamos una NotificacionesFalsas y comprobamos qué se envió.
    notifs = NotificacionesFalsas()
    bus = _bus(_uow_con_producto(5), notifs)      # hay 5, se piden 10 -> SinStock
    bus.manejar(comandos.Asignar("o1", "MESA", 10))
    assert notifs.enviadas["stock@ejemplo.com"] == ["Sin stock para MESA"]
