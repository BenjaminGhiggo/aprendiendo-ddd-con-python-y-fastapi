from fastapi.testclient import TestClient
from modelo import Lote
from repositorio import RepositorioFalso
from unidad_de_trabajo import UnidadDeTrabajoAbstracta
from api import app, obtener_uow


class UoWFalsa(UnidadDeTrabajoAbstracta):
    def __init__(self):
        self.lotes = RepositorioFalso([])
        self.comprometido = False
    def comprometer(self):
        self.comprometido = True
    def deshacer(self):
        pass


def _uow_con_lote():
    uow = UoWFalsa()
    uow.lotes.agregar(Lote("lote-api", "SOFA", 100, eta=None))
    return uow


def test_la_api_asigna_y_devuelve_201():
    uow = _uow_con_lote()
    app.dependency_overrides[obtener_uow] = lambda: uow
    cliente = TestClient(app)
    r = cliente.post("/asignar", json={"id_pedido": "o1", "sku": "SOFA", "cantidad": 10})
    assert r.status_code == 201
    assert r.json()["referencia"] == "lote-api"
    app.dependency_overrides.clear()


def test_la_api_400_si_sku_no_existe():
    uow = _uow_con_lote()
    app.dependency_overrides[obtener_uow] = lambda: uow
    cliente = TestClient(app)
    r = cliente.post("/asignar", json={"id_pedido": "o1", "sku": "XXX", "cantidad": 10})
    assert r.status_code == 400
    app.dependency_overrides.clear()
