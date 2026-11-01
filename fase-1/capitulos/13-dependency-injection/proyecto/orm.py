from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey, event
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

# MODELO DE LECTURA (CQRS): una tabla DESNORMALIZADA, optimizada para leer.
# Sin claves foráneas, solo strings: "no foreign keys, just strings, YOLO" (cap. 12).
# No se mapea a ninguna clase: se consulta con SQL crudo desde vistas.py y la
# mantienen al día los handlers de eventos. Separa reads (simples) de writes (complejos).
asignaciones_vista = Table(
    "asignaciones_vista", metadata,
    Column("id_pedido", String(255)),
    Column("sku", String(255)),
    Column("referencia", String(255)),
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

    # Al cargar un Producto de la BD, SQLAlchemy no llama a __init__, así que
    # inicializamos su lista de eventos aquí (sin ensuciar el modelo con imports de ORM).
    @event.listens_for(modelo.Producto, "load")
    def _init_eventos(producto, _contexto):
        producto.eventos = []
