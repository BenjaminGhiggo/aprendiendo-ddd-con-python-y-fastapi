# mensajeria.py — el bus distingue COMANDOS de EVENTOS:
#   - comando: un handler; si falla, el error PROPAGA.
#   - evento: varios handlers; si uno falla, se AÍSLA (no rompe el flujo).
import comandos
import eventos
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
    eventos.Asignado: [registrar_asignacion],
    eventos.Desasignado: [reasignar],
}
