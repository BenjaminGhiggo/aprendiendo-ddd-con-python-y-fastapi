# notificaciones.py — ejemplo trabajado: convertir una dependencia implícita (importar
# 'email' y llamarlo directo) en un ADAPTADOR "de verdad": una ABC + implementación real.
#
# Receta del libro (cap. 13, "DI and Bootstrap recap"):
#   1. Define tu API con una ABC.   2. Implementa la real.
#   3. Haz una fake para los tests.  4/5. Prueba la "casi real".
import abc


class NotificacionesAbstractas(abc.ABC):
    # La ABSTRACCIÓN: el resto del código depende de esto, no de un email concreto.
    @abc.abstractmethod
    def enviar(self, destino, mensaje):
        raise NotImplementedError


class NotificacionesEmail(NotificacionesAbstractas):
    # La implementación REAL (aquí solo imprime; en producción usaría smtplib).
    # El constructor NO tiene efectos secundarios, así sirve como default del bootstrap.
    def enviar(self, destino, mensaje):
        print(f"[EMAIL] para {destino}: {mensaje}")
