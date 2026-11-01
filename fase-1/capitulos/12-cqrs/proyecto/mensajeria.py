# mensajeria.py — el bus distingue COMANDOS de EVENTOS:
#   - comando: un handler; si falla, el error PROPAGA.
#   - evento: varios handlers; si uno falla, se AÍSLA (no rompe el flujo).
from sqlalchemy import text

import comandos
import eventos
import cola_externa
from modelo import LineaPedido

notificaciones_sin_stock = []
asignaciones_registradas = []


class SkuInvalido(Exception):
    pass


def manejar(mensaje, uow):
    resultados = []
    cola = [mensaje]
    while cola:
        m = cola.pop(0)
        if isinstance(m, comandos.Comando):
            resultados.append(_manejar_comando(m, uow, cola))
        else:
            _manejar_evento(m, uow, cola)
    return resultados


def _manejar_comando(comando, uow, cola):
    manejador = MANEJADORES_COMANDO[type(comando)]
    resultado = manejador(comando, uow)                 # si falla, PROPAGA
    cola.extend(uow.recolectar_eventos_nuevos())
    return resultado


def _manejar_evento(evento, uow, cola):
    for manejador in MANEJADORES_EVENTO[type(evento)]:
        try:
            manejador(evento, uow)
            cola.extend(uow.recolectar_eventos_nuevos())
        except Exception:
            continue                                     # AISLADO: no rompe el flujo


# --- handlers de comandos ---
def asignar(comando, uow):
    linea = LineaPedido(comando.id_pedido, comando.sku, comando.cantidad)
    with uow:
        producto = uow.productos.obtener(comando.sku)
        if producto is None:
            raise SkuInvalido(f"Sku inválido {comando.sku}")
        referencia = producto.asignar(linea)
        uow.comprometer()
    return referencia


def crear_lote(comando, uow):
    from modelo import Producto, Lote
    with uow:
        producto = uow.productos.obtener(comando.sku)
        if producto is None:
            producto = Producto(comando.sku, lotes=[])
            uow.productos.agregar(producto)
        producto.lotes.append(Lote(comando.referencia, comando.sku, comando.cantidad, comando.eta))
        uow.comprometer()


def cambiar_cantidad_lote(comando, uow):
    with uow:
        producto = next(
            p for p in uow.productos._productos
            if any(l.referencia == comando.referencia for l in p.lotes)
        )
        producto.cambiar_cantidad_lote(comando.referencia, comando.cantidad)
        uow.comprometer()


# --- handlers de eventos ---
def notificar_sin_stock(evento, uow):
    notificaciones_sin_stock.append(evento.sku)


def registrar_asignacion(evento, uow):
    asignaciones_registradas.append(evento.referencia)


def publicar_asignado_al_exterior(evento, uow):
    # EVENTO EXTERNO: avisamos a otros servicios por el canal (Redis en producción).
    cola_externa.publicar("linea_asignada", {"id_pedido": evento.id_pedido, "sku": evento.sku, "ref": evento.referencia})


def agregar_asignacion_a_vista(evento, uow):
    # CQRS: actualizar el modelo de LECTURA cuando se asigna (lado escritura dispara el read).
    # Un INSERT simple en la tabla desnormalizada; el GET luego solo hace un SELECT.
    with uow:
        uow.sesion.execute(
            text(
                "INSERT INTO asignaciones_vista (id_pedido, sku, referencia) "
                "VALUES (:id_pedido, :sku, :referencia)"
            ),
            dict(id_pedido=evento.id_pedido, sku=evento.sku, referencia=evento.referencia),
        )
        uow.comprometer()


def quitar_asignacion_de_vista(evento, uow):
    # Al desasignar, borramos esa fila del modelo de lectura para mantenerlo al día.
    with uow:
        uow.sesion.execute(
            text(
                "DELETE FROM asignaciones_vista "
                "WHERE id_pedido = :id_pedido AND sku = :sku"
            ),
            dict(id_pedido=evento.id_pedido, sku=evento.sku),
        )
        uow.comprometer()


def reasignar(evento, uow):
    # un Desasignado dispara una nueva asignación de esa línea
    linea = LineaPedido(evento.id_pedido, evento.sku, evento.cantidad)
    with uow:
        producto = uow.productos.obtener(evento.sku)
        producto.asignar(linea)
        uow.comprometer()


MANEJADORES_COMANDO = {
    comandos.Asignar: asignar,
    comandos.CrearLote: crear_lote,
    comandos.CambiarCantidadLote: cambiar_cantidad_lote,
}

MANEJADORES_EVENTO = {
    eventos.SinStock: [notificar_sin_stock],
    eventos.Asignado: [registrar_asignacion, publicar_asignado_al_exterior, agregar_asignacion_a_vista],
    eventos.Desasignado: [reasignar, quitar_asignacion_de_vista],
}


def consumir_externo(mensaje, uow):
    # ADAPTADOR DE ENTRADA: traduce un mensaje externo (dict) a un comando interno.
    comando = comandos.CambiarCantidadLote(mensaje["referencia"], mensaje["cantidad"])
    return manejar(comando, uow)
