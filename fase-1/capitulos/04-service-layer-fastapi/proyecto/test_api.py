from fastapi.testclient import TestClient
from modelo import Lote
from api import app, obtener_sesion


def test_la_api_asigna_y_devuelve_201(sesion):
    sesion.add(Lote("lote-api", "SOFA", 100, eta=None))
    sesion.commit()
    app.dependency_overrides[obtener_sesion] = lambda: sesion
    cliente = TestClient(app)
    respuesta = cliente.post(
        "/asignar", json={"id_pedido": "o1", "sku": "SOFA", "cantidad": 10}
    )
    assert respuesta.status_code == 201
    assert respuesta.json()["referencia"] == "lote-api"
    app.dependency_overrides.clear()


def test_la_api_devuelve_400_si_el_sku_no_existe(sesion):
    sesion.add(Lote("lote-api", "SOFA", 100, eta=None))
    sesion.commit()
    app.dependency_overrides[obtener_sesion] = lambda: sesion
    cliente = TestClient(app)
    respuesta = cliente.post(
        "/asignar", json={"id_pedido": "o1", "sku": "INEXISTENTE", "cantidad": 10}
    )
    assert respuesta.status_code == 400
    app.dependency_overrides.clear()
