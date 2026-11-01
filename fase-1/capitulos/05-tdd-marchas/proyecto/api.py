# api.py — el ENTRYPOINT web con FastAPI (el libro usa Flask; regla 4: FastAPI).
# El endpoint es "fino": traduce HTTP y delega en la capa de servicios.
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

import modelo
import servicios
from repositorio import RepositorioSQLAlchemy

app = FastAPI()


def obtener_sesion():
    # En producción aquí se devolvería una sesión contra la BD real.
    # En los tests se reemplaza con app.dependency_overrides.
    raise RuntimeError("Configura una sesión (o usa dependency_overrides en tests).")


class PedidoEntrada(BaseModel):
    id_pedido: str
    sku: str
    cantidad: int


@app.post("/asignar", status_code=201)
def asignar_endpoint(pedido: PedidoEntrada, sesion=Depends(obtener_sesion)):
    repo = RepositorioSQLAlchemy(sesion)
    try:
        referencia = servicios.asignar(
            pedido.id_pedido, pedido.sku, pedido.cantidad, repo, sesion
        )
    except (servicios.SkuInvalido, modelo.SinStock) as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"referencia": referencia}
