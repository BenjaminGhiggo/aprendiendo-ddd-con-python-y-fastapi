from fastapi.testclient import TestClient
import comandos
import bootstrap
from modelo import Producto, Lote
from repositorio import RepositorioFalso
from unidad_de_trabajo import UnidadDeTrabajoAbstracta, UnidadDeTrabajoSQLAlchemy
from api import app, obtener_bus


class UoWFalsa(UnidadDeTrabajoAbstracta):
    def __init__(self):
        self.productos = RepositorioFalso([])
        self.comprometido = False
    def comprometer(self):
        self.comprometido = True
    def deshacer(self):
        pass


def _bus_con_producto():
    uow = UoWFalsa()
    uow.productos.agregar(Producto("SOFA", [Lote("lote-api", "SOFA", 100, eta=None)]))
    return bootstrap.bootstrap(iniciar_orm=False, uow=uow, publicar=lambda *a: None)


def test_la_api_asigna_y_devuelve_202():
    app.dependency_overrides[obtener_bus] = lambda: _bus_con_producto()
    r = TestClient(app).post("/asignar", json={"id_pedido": "o1", "sku": "SOFA", "cantidad": 10})
    assert r.status_code == 202
    assert r.json() == {"ok": True}
    app.dependency_overrides.clear()


def test_la_api_400_si_sku_no_existe():
    app.dependency_overrides[obtener_bus] = lambda: _bus_con_producto()
    r = TestClient(app).post("/asignar", json={"id_pedido": "o1", "sku": "XXX", "cantidad": 10})
    assert r.status_code == 400
    app.dependency_overrides.clear()


def test_post_y_luego_get_devuelve_la_asignacion(fabrica_sesion):
    bus = bootstrap.bootstrap(
        iniciar_orm=False,
        uow=UnidadDeTrabajoSQLAlchemy(fabrica_sesion),
        publicar=lambda *a: None,
    )
    bus.manejar(comandos.CrearLote("lote-web", "SILLA", 50, None))
    app.dependency_overrides[obtener_bus] = lambda: bus
    cliente = TestClient(app)

    r = cliente.post("/asignar", json={"id_pedido": "pedido-web", "sku": "SILLA", "cantidad": 5})
    assert r.status_code == 202

    r = cliente.get("/asignaciones/pedido-web")
    assert r.status_code == 200
    assert r.json() == [{"sku": "SILLA", "referencia": "lote-web"}]

    r = cliente.get("/asignaciones/no-existe")
    assert r.status_code == 404
    app.dependency_overrides.clear()
