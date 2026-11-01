from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

import comandos
import mensajeria
import vistas

app = FastAPI()


def obtener_uow():
    raise RuntimeError("Configura una UoW (o usa dependency_overrides en tests).")


class PedidoEntrada(BaseModel):
    id_pedido: str
    sku: str
    cantidad: int


# LADO ESCRITURA (command): modifica estado. Aplicando CQS, YA NO devuelve la referencia;
# responde un OK simple. "functions should either modify state or answer questions,
# but never both" (cap. 12, Post/Redirect/Get and CQS).
@app.post("/asignar", status_code=202)
def asignar_endpoint(pedido: PedidoEntrada, uow=Depends(obtener_uow)):
    comando = comandos.Asignar(pedido.id_pedido, pedido.sku, pedido.cantidad)
    try:
        mensajeria.manejar(comando, uow)
    except mensajeria.SkuInvalido as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"ok": True}


# LADO LECTURA (query): solo responde preguntas. Consulta el modelo de lectura vía vistas.py.
@app.get("/asignaciones/{id_pedido}")
def ver_asignaciones_endpoint(id_pedido: str, uow=Depends(obtener_uow)):
    resultado = vistas.asignaciones(id_pedido, uow)
    if not resultado:
        raise HTTPException(status_code=404, detail="no encontrado")
    return resultado
