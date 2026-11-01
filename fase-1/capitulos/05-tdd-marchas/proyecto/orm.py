# orm.py — define el ESQUEMA de la base de datos aparte y lo mapea al modelo.
# El ORM "conoce" al modelo (lo importa); el modelo NO sabe nada del ORM.
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import registry, relationship

import modelo

mapper_registry = registry()
metadata = mapper_registry.metadata

lineas_pedido = Table(
    "lineas_pedido", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_pedido", String(255)),
    Column("sku", String(255)),
    Column("cantidad", Integer, nullable=False),
)

lotes = Table(
    "lotes", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("referencia", String(255)),
    Column("sku", String(255)),
    Column("_cantidad_comprada", Integer, nullable=False),
    Column("eta", Date, nullable=True),
)

asignaciones = Table(
    "asignaciones", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("linea_id", ForeignKey("lineas_pedido.id")),
    Column("lote_id", ForeignKey("lotes.id")),
)


def iniciar_mapeos():
    lineas_mapper = mapper_registry.map_imperatively(modelo.LineaPedido, lineas_pedido)
    mapper_registry.map_imperatively(
        modelo.Lote,
        lotes,
        properties={
            "_asignaciones": relationship(
                lineas_mapper, secondary=asignaciones, collection_class=set
            )
        },
    )
