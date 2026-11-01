# mensajeria.py — el BUS es el punto de entrada. Procesa una cola y recolecta los
# eventos NUEVOS de la UoW tras cada handler (cascada). Devuelve los resultados.
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
        for manejador in MANEJADORES[type(m)]:
            resultados.append(manejador(m, uow))
            cola.extend(uow.recolectar_eventos_nuevos())
    return resultados


def asignar(evento, uow):
    linea = LineaPedido(evento.id_pedido, evento.sku, evento.cantidad)
    with uow:
        producto = uow.productos.obtener(evento.sku)
        if producto is None:
            raise SkuInvalido(f"Sku inválido {evento.sku}")
        referencia = producto.asignar(linea)
        uow.comprometer()
    return referencia


def cambiar_cantidad_lote(evento, uow):
    with uow:
        producto = next(
            p for p in uow.productos._productos
            if any(l.referencia == evento.referencia for l in p.lotes)
        )
        producto.cambiar_cantidad_lote(evento.referencia, evento.cantidad)
        uow.comprometer()


def notificar_sin_stock(evento, uow):
    notificaciones_sin_stock.append(evento.sku)


def registrar_asignacion(evento, uow):
    asignaciones_registradas.append(evento.referencia)


MANEJADORES = {
    eventos.AsignacionRequerida: [asignar],
    eventos.CambiarCantidadLote: [cambiar_cantidad_lote],
    eventos.SinStock: [notificar_sin_stock],
    eventos.Asignado: [registrar_asignacion],
}
