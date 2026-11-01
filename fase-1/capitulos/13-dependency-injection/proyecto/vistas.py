# vistas.py — EL LADO DE LECTURA (CQRS).
#
# CQS (command-query separation): "functions should either modify state or answer
# questions, but never both" (cap. 12). Aquí SOLO se responden preguntas (reads):
# ninguna función de este módulo cambia el estado del sistema.
#
# El libro consulta una tabla desnormalizada con SQL crudo porque el modelo de dominio
# "is not optimized for read operations" (cap. 12): está hecho para ESCRIBIR (reglas,
# invariantes, agregados), no para LEER rápido. Para leer basta un SELECT simple.
from sqlalchemy import text


def asignaciones(id_pedido, uow):
    # Lee del modelo de lectura (tabla desnormalizada), no del modelo de dominio.
    # SELECT * FROM tabla WHERE clave = valor: la consulta más rápida que existe.
    with uow:
        filas = list(
            uow.sesion.execute(
                text(
                    "SELECT sku, referencia FROM asignaciones_vista "
                    "WHERE id_pedido = :id_pedido"
                ),
                dict(id_pedido=id_pedido),
            )
        )
    return [{"sku": sku, "referencia": referencia} for sku, referencia in filas]
