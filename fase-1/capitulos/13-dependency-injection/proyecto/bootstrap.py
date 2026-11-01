# bootstrap.py — el COMPOSITION ROOT ("bootstrap script"): el único lugar donde se hace
# la inyección de dependencias y la inicialización que la app necesita una sola vez.
#
# Queremos que el bootstrap (cap. 13, "A Bootstrap Script"):
#   1. Declare dependencias por defecto, pero permita sobreescribirlas.
#   2. Haga el "init" (arrancar el ORM).
#   3. Inyecte las dependencias en los handlers.
#   4. Devuelva el objeto central de la app: el bus de mensajes.
import inspect

import orm
import cola_externa
import mensajeria
import notificaciones as notif


def inyectar_dependencias(manejador, dependencias):
    # DI inspeccionando la firma: casamos por NOMBRE los parámetros del handler con las deps.
    parametros = inspect.signature(manejador).parameters
    deps = {nombre: dep for nombre, dep in dependencias.items() if nombre in parametros}
    # Devolvemos una función que solo pide el mensaje: las deps ya están "bindeadas".
    return lambda mensaje: manejador(mensaje, **deps)


def bootstrap(
    iniciar_orm=True,
    uow=None,
    notificaciones=None,
    publicar=cola_externa.publicar,
):
    if iniciar_orm:
        orm.iniciar_mapeos()                 # init que se hace una vez al arrancar la app
    if notificaciones is None:
        notificaciones = notif.NotificacionesEmail()   # default de producción

    dependencias = {"uow": uow, "notificaciones": notificaciones, "publicar": publicar}

    manejadores_evento_inyectados = {
        tipo: [inyectar_dependencias(h, dependencias) for h in manejadores]
        for tipo, manejadores in mensajeria.MANEJADORES_EVENTO.items()
    }
    manejadores_comando_inyectados = {
        tipo: inyectar_dependencias(h, dependencias)
        for tipo, h in mensajeria.MANEJADORES_COMANDO.items()
    }

    return mensajeria.BusMensajes(
        uow=uow,
        manejadores_evento=manejadores_evento_inyectados,
        manejadores_comando=manejadores_comando_inyectados,
    )
