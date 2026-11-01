# test_vistas.py — test de INTEGRACIÓN del lado de lectura (CQRS).
# Igual que en el libro: el setup usa el bus de mensajes (el entrypoint público), así el
# test queda desacoplado de CÓMO se guarda; solo afirma contra la vista.
import comandos
import mensajeria
import vistas
from unidad_de_trabajo import UnidadDeTrabajoSQLAlchemy


def test_la_vista_muestra_las_asignaciones_del_pedido(fabrica_sesion):
    uow = UnidadDeTrabajoSQLAlchemy(fabrica_sesion)
    mensajeria.manejar(comandos.CrearLote("lote-mesa", "MESA", 50, None), uow)
    mensajeria.manejar(comandos.CrearLote("lote-silla", "SILLA", 50, None), uow)
    mensajeria.manejar(comandos.Asignar("pedido1", "MESA", 20), uow)
    mensajeria.manejar(comandos.Asignar("pedido1", "SILLA", 20), uow)
    # pedido distinto, para comprobar que filtra bien
    mensajeria.manejar(comandos.Asignar("otro-pedido", "MESA", 5), uow)

    assert vistas.asignaciones("pedido1", uow) == [
        {"sku": "MESA", "referencia": "lote-mesa"},
        {"sku": "SILLA", "referencia": "lote-silla"},
    ]


def test_la_vista_de_un_pedido_sin_asignaciones_esta_vacia(fabrica_sesion):
    uow = UnidadDeTrabajoSQLAlchemy(fabrica_sesion)
    assert vistas.asignaciones("fantasma", uow) == []
