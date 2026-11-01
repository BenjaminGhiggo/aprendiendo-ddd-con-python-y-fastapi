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
    Column("producto_sku", ForeignKey("productos.sku")),
)

asignaciones = Table(
    "asignaciones", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("linea_id", ForeignKey("lineas_pedido.id")),
    Column("lote_id", ForeignKey("lotes.id")),
)

productos = Table(
    "productos", metadata,
    Column("sku", String(255), primary_key=True),
    Column("numero_version", Integer, nullable=False),
)


def iniciar_mapeos():
    lineas_mapper = mapper_registry.map_imperatively(modelo.LineaPedido, lineas_pedido)
    lotes_mapper = mapper_registry.map_imperatively(
        modelo.Lote, lotes,
        properties={
            "_asignaciones": relationship(
                lineas_mapper, secondary=asignaciones, collection_class=set
            )
        },
    )
    mapper_registry.map_imperatively(
        modelo.Producto, productos,
        properties={"lotes": relationship(lotes_mapper)},
    )
