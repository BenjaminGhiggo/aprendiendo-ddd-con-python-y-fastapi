from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

import comandos
import mensajeria
import vistas

app = FastAPI()


# El entrypoint ya NO arma la UoW ni configura nada: pide un BUS ya listo (del bootstrap).
def obtener_bus():
    raise RuntimeError("Configura un bus (bootstrap) o usa dependency_overrides en tests.")


class PedidoEntrada(BaseModel):
    id_pedido: str
    sku: str
    cantidad: int


# LADO ESCRITURA (CQS): el POST modifica estado y responde OK simple.
@app.post("/asignar", status_code=202)
def asignar_endpoint(pedido: PedidoEntrada, bus=Depends(obtener_bus)):
    comando = comandos.Asignar(pedido.id_pedido, pedido.sku, pedido.cantidad)
    try:
        bus.manejar(comando)
    except mensajeria.SkuInvalido as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"ok": True}


# LADO LECTURA (CQS): usa la uow del propio bus para consultar el modelo de lectura.
@app.get("/asignaciones/{id_pedido}")
def ver_asignaciones_endpoint(id_pedido: str, bus=Depends(obtener_bus)):
    resultado = vistas.asignaciones(id_pedido, bus.uow)
    if not resultado:
        raise HTTPException(status_code=404, detail="no encontrado")
    return resultado
