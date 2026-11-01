# api.py — el endpoint FastAPI ahora usa una Unidad de Trabajo (regla 4: FastAPI).
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

import modelo
import servicios

app = FastAPI()


def obtener_uow():
    # En producción devolvería una UnidadDeTrabajoSQLAlchemy(fabrica_sesion real).
    # En los tests se reemplaza con app.dependency_overrides.
    raise RuntimeError("Configura una UoW (o usa dependency_overrides en tests).")


class PedidoEntrada(BaseModel):
    id_pedido: str
    sku: str
    cantidad: int


@app.post("/asignar", status_code=201)
def asignar_endpoint(pedido: PedidoEntrada, uow=Depends(obtener_uow)):
    try:
        referencia = servicios.asignar(
            pedido.id_pedido, pedido.sku, pedido.cantidad, uow
        )
    except (servicios.SkuInvalido, modelo.SinStock) as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"referencia": referencia}
