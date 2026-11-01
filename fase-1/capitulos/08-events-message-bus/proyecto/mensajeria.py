# mensajeria.py — el BUS DE MENSAJES: mapea cada tipo de evento a sus manejadores.
import eventos

# Registro para que los tests comprueben qué notificaciones se enviaron.
notificaciones_enviadas = []


def enviar_notificacion_sin_stock(evento):
    notificaciones_enviadas.append(evento.sku)


MANEJADORES = {
    eventos.SinStock: [enviar_notificacion_sin_stock],
}


def manejar(evento):
    for manejador in MANEJADORES[type(evento)]:
        manejador(evento)
