# mensajeria.py — capítulo 13:
#   - Los handlers declaran DEPENDENCIAS EXPLÍCITAS (uow, notificaciones, publicar):
#     "Explicit is better than implicit" (Zen of Python) + principio de inversión de
#     dependencias (dependemos de una abstracción, no de un detalle concreto).
#   - El bus deja de ser un módulo estático y pasa a ser una CLASE configurable: recibe
#     los handlers ya inyectados (solo necesitan el mensaje) — ver bootstrap.py.
from sqlalchemy import text

import comandos
import eventos
from modelo import LineaPedido

asignaciones_registradas = []     # lo que registró un handler interno (para los tests)


class SkuInvalido(Exception):
    pass


class BusMensajes:
    # El bus ahora es una clase: se le DAN los handlers ya inyectados en tiempo de ejecución.
    def __init__(self, uow, manejadores_evento, manejadores_comando):
        self.uow = uow
        self.manejadores_evento = manejadores_evento
        self.manejadores_comando = manejadores_comando

    def manejar(self, mensaje):
        self.cola = [mensaje]
        resultados = []
        while self.cola:
            m = self.cola.pop(0)
            if isinstance(m, comandos.Comando):
                resultados.append(self._manejar_comando(m))
            else:
                self._manejar_evento(m)
        return resultados

    def _manejar_comando(self, comando):
        manejador = self.manejadores_comando[type(comando)]
        resultado = manejador(comando)                      # ya trae sus deps inyectadas
        self.cola.extend(self.uow.recolectar_eventos_nuevos())
        return resultado

    def _manejar_evento(self, evento):
        for manejador in self.manejadores_evento[type(evento)]:
            try:
                manejador(evento)                           # ya trae sus deps inyectadas
                self.cola.extend(self.uow.recolectar_eventos_nuevos())
            except Exception:
                continue                                    # AISLADO: no rompe el flujo


# --- handlers de COMANDOS (dependencia explícita: uow) ---
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


# --- handlers de EVENTOS (cada uno declara SOLO las deps que necesita) ---
def notificar_sin_stock(evento, notificaciones):
    # Depende de la ABSTRACCIÓN NotificacionesAbstractas, no de un email concreto.
    notificaciones.enviar("stock@ejemplo.com", f"Sin stock para {evento.sku}")


def registrar_asignacion(evento):
    # Sin dependencias: el bootstrap no le inyecta nada.
    asignaciones_registradas.append(evento.referencia)


def publicar_asignado_al_exterior(evento, publicar):
    # 'publicar' es un Callable inyectado (en real: redis.publish).
    publicar("linea_asignada", {"id_pedido": evento.id_pedido, "sku": evento.sku, "ref": evento.referencia})


def agregar_asignacion_a_vista(evento, uow):
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
    linea = LineaPedido(evento.id_pedido, evento.sku, evento.cantidad)
    with uow:
        producto = uow.productos.obtener(evento.sku)
        producto.asignar(linea)
        uow.comprometer()


# REGISTRO: qué handlers atienden cada mensaje. El bootstrap los inyecta y se los da al bus.
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


def consumir_externo(mensaje, bus):
    # ADAPTADOR DE ENTRADA: traduce un mensaje externo (dict) a un comando interno y lo mete al bus.
    comando = comandos.CambiarCantidadLote(mensaje["referencia"], mensaje["cantidad"])
    return bus.manejar(comando)
