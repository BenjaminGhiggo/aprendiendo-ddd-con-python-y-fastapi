# test_vistas.py — integración del lado de lectura, ahora montando el bus con bootstrap.
import comandos
import bootstrap
import vistas
from unidad_de_trabajo import UnidadDeTrabajoSQLAlchemy


def _bus(fabrica_sesion):
    return bootstrap.bootstrap(
        iniciar_orm=False,                  # el conftest ya arrancó el ORM
        uow=UnidadDeTrabajoSQLAlchemy(fabrica_sesion),
        publicar=lambda *a: None,
    )


def test_la_vista_muestra_las_asignaciones_del_pedido(fabrica_sesion):
    bus = _bus(fabrica_sesion)
    bus.manejar(comandos.CrearLote("lote-mesa", "MESA", 50, None))
    bus.manejar(comandos.CrearLote("lote-silla", "SILLA", 50, None))
    bus.manejar(comandos.Asignar("pedido1", "MESA", 20))
    bus.manejar(comandos.Asignar("pedido1", "SILLA", 20))
    bus.manejar(comandos.Asignar("otro-pedido", "MESA", 5))

    assert vistas.asignaciones("pedido1", bus.uow) == [
        {"sku": "MESA", "referencia": "lote-mesa"},
        {"sku": "SILLA", "referencia": "lote-silla"},
    ]


def test_la_vista_de_un_pedido_sin_asignaciones_esta_vacia(fabrica_sesion):
    bus = _bus(fabrica_sesion)
    assert vistas.asignaciones("fantasma", bus.uow) == []
