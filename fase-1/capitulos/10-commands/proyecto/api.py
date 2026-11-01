from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

import comandos
import mensajeria

app = FastAPI()


def obtener_uow():
    raise RuntimeError("Configura una UoW (o usa dependency_overrides en tests).")


class PedidoEntrada(BaseModel):
    id_pedido: str
    sku: str
    cantidad: int


@app.post("/asignar", status_code=201)
def asignar_endpoint(pedido: PedidoEntrada, uow=Depends(obtener_uow)):
    comando = comandos.Asignar(pedido.id_pedido, pedido.sku, pedido.cantidad)
    try:
        resultados = mensajeria.manejar(comando, uow)
    except mensajeria.SkuInvalido as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"referencia": resultados[0]}
