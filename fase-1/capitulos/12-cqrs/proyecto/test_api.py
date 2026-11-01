from fastapi.testclient import TestClient
from modelo import Producto, Lote
from repositorio import RepositorioFalso
from unidad_de_trabajo import UnidadDeTrabajoAbstracta, UnidadDeTrabajoSQLAlchemy
import comandos
import mensajeria
from api import app, obtener_uow


class UoWFalsa(UnidadDeTrabajoAbstracta):
    def __init__(self):
        self.productos = RepositorioFalso([])
        self.comprometido = False
    def comprometer(self):
        self.comprometido = True
    def deshacer(self):
        pass


def _uow_con_producto():
    uow = UoWFalsa()
    uow.productos.agregar(Producto("SOFA", [Lote("lote-api", "SOFA", 100, eta=None)]))
    return uow


def test_la_api_asigna_y_devuelve_202():
    # CQS: el POST modifica estado y responde OK simple (ya NO devuelve la referencia).
    app.dependency_overrides[obtener_uow] = lambda: _uow_con_producto()
    r = TestClient(app).post("/asignar", json={"id_pedido": "o1", "sku": "SOFA", "cantidad": 10})
    assert r.status_code == 202
    assert r.json() == {"ok": True}
    app.dependency_overrides.clear()


def test_la_api_400_si_sku_no_existe():
    app.dependency_overrides[obtener_uow] = lambda: _uow_con_producto()
    r = TestClient(app).post("/asignar", json={"id_pedido": "o1", "sku": "XXX", "cantidad": 10})
    assert r.status_code == 400
    app.dependency_overrides.clear()


def test_post_y_luego_get_devuelve_la_asignacion(fabrica_sesion):
    # Flujo CQRS de punta a punta: POST (write) y luego GET (read) del modelo de lectura.
    uow = UnidadDeTrabajoSQLAlchemy(fabrica_sesion)
    mensajeria.manejar(comandos.CrearLote("lote-web", "SILLA", 50, None), uow)
    app.dependency_overrides[obtener_uow] = lambda: uow
    cliente = TestClient(app)

    r = cliente.post("/asignar", json={"id_pedido": "pedido-web", "sku": "SILLA", "cantidad": 5})
    assert r.status_code == 202

    r = cliente.get("/asignaciones/pedido-web")
    assert r.status_code == 200
    assert r.json() == [{"sku": "SILLA", "referencia": "lote-web"}]

    r = cliente.get("/asignaciones/no-existe")
    assert r.status_code == 404
    app.dependency_overrides.clear()
