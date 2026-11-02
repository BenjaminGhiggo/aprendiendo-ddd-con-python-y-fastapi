"""main.py — punto de entrada para CORRER la API del proyecto allocation en tu computadora.

No modifica el código del capítulo: usa tal cual el snapshot del Capítulo 13
(fase-1/capitulos/13-dependency-injection/proyecto/) y solo lo "enchufa" a una base de
datos real con su propio bootstrap:

    "We want our bootstrap script to do the following: 1. Declare default dependencies
    but allow us to override them … 4. Give us back the core object for our app, the
    message bus" — Cap. 13

Agrega lo mínimo para que la API se pueda usar desde el navegador (/docs):
  - POST /lotes: crear stock. Es el equivalente del endpoint `add_batch` del libro
    ("A new service for add_batch (service_layer/services.py)" — Cap. 5).
  - Datos de ejemplo al arrancar (si la base está vacía).
  - GET /salud: chequeo de vida (responde {"estado": "ok"}).

Correr en local (desde la raíz del repo):
    uv run uvicorn main:app --app-dir despliegue/api --reload
"""
import os
import sys
from datetime import date, timedelta
from typing import Optional

PROYECTO = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "fase-1", "capitulos", "13-dependency-injection", "proyecto"))
sys.path.insert(0, PROYECTO)   # los módulos del capítulo se importan por su nombre (import modelo, ...)

from fastapi import HTTPException                     # noqa: E402
from fastapi.responses import RedirectResponse        # noqa: E402
from pydantic import BaseModel                        # noqa: E402
from sqlalchemy import create_engine                  # noqa: E402
from sqlalchemy.orm import sessionmaker               # noqa: E402

import bootstrap                                      # noqa: E402
import comandos                                       # noqa: E402
import orm                                            # noqa: E402
from api import app, obtener_bus                      # noqa: E402
from unidad_de_trabajo import UnidadDeTrabajoSQLAlchemy  # noqa: E402

# 1. La base de datos: SQLite en un archivo (/tmp/allocation.db). Es una demo: bórralo para empezar de cero.
#    Para algo persistente, definir DATABASE_URL con una URL de Postgres.
URL_BD = os.environ.get("DATABASE_URL", "sqlite:////tmp/allocation.db")
engine = create_engine(
    URL_BD,
    connect_args={"check_same_thread": False} if URL_BD.startswith("sqlite") else {},
)
orm.metadata.create_all(engine)

# 2. El bootstrap del Cap. 13 arma el bus con la UoW real (y arranca el ORM una sola vez).
bus = bootstrap.bootstrap(
    iniciar_orm=True,
    uow=UnidadDeTrabajoSQLAlchemy(sessionmaker(bind=engine)),
)

# 3. El api.py del capítulo pide el bus con Depends(obtener_bus); aquí le damos el real.
app.dependency_overrides[obtener_bus] = lambda: bus
app.title = "Allocation API · Cosmic Python con FastAPI"
app.description = (
    "El proyecto *allocation* del libro **Architecture Patterns with Python**, tal como queda "
    "al final del **Capítulo 13** (bootstrap + bus de mensajes + CQRS).\n\n"
    "**Prueba en orden:** 1) `GET /asignaciones/pedido-demo` (ya existe), 2) `POST /lotes`, "
    "3) `POST /asignar`, 4) `GET /asignaciones/{id_pedido}`.\n\n"
    "Lotes de ejemplo al arrancar: `lote-mesa-hoy` (MESA, 100, en almacén), "
    "`lote-mesa-manana` (MESA, 50, llega mañana) y `lote-silla-hoy` (SILLA, 20).\n\n"
    "⚠️ Demo: la base es un SQLite en /tmp/allocation.db; bórralo para empezar de cero."
)


class LoteEntrada(BaseModel):
    referencia: str
    sku: str
    cantidad: int
    eta: Optional[date] = None


@app.post("/lotes", status_code=201, tags=["escritura"])
def crear_lote_endpoint(lote: LoteEntrada):
    bus.manejar(comandos.CrearLote(lote.referencia, lote.sku, lote.cantidad, lote.eta))
    return {"ok": True}


@app.get("/salud", tags=["sistema"])
def salud():
    return {"estado": "ok"}


@app.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse("/docs")


def _cargar_datos_de_ejemplo():
    with bus.uow:
        ya_hay = bus.uow.productos.obtener("MESA") is not None
    if ya_hay:
        return
    manana = date.today() + timedelta(days=1)
    bus.manejar(comandos.CrearLote("lote-mesa-hoy", "MESA", 100, None))
    bus.manejar(comandos.CrearLote("lote-mesa-manana", "MESA", 50, manana))
    bus.manejar(comandos.CrearLote("lote-silla-hoy", "SILLA", 20, None))
    bus.manejar(comandos.Asignar("pedido-demo", "MESA", 10))
    print("[arranque] datos de ejemplo cargados", flush=True)


_cargar_datos_de_ejemplo()
