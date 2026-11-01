# test_bootstrap.py — prueba la inyección de dependencias en sí.
from bootstrap import inyectar_dependencias


def test_inyecta_solo_las_deps_que_el_handler_pide():
    recibido = {}

    def handler(mensaje, uow, publicar):      # pide uow y publicar
        recibido["mensaje"] = mensaje
        recibido["uow"] = uow
        recibido["publicar"] = publicar

    dependencias = {"uow": "UOW", "publicar": "PUB", "notificaciones": "NOTIF"}
    preparado = inyectar_dependencias(handler, dependencias)

    preparado("hola")                          # solo pasamos el mensaje
    assert recibido == {"mensaje": "hola", "uow": "UOW", "publicar": "PUB"}
    # 'notificaciones' NO se inyectó porque el handler no lo pedía en su firma.


def test_un_handler_sin_deps_se_puede_llamar_solo_con_el_mensaje():
    vistos = []

    def handler(mensaje):                      # sin dependencias
        vistos.append(mensaje)

    preparado = inyectar_dependencias(handler, {"uow": "UOW"})
    preparado("evento")
    assert vistos == ["evento"]
