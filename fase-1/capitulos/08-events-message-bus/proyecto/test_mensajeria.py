import eventos
import mensajeria


def test_el_bus_llama_al_manejador_del_evento():
    mensajeria.notificaciones_enviadas.clear()
    mensajeria.manejar(eventos.SinStock("MESA"))
    assert mensajeria.notificaciones_enviadas == ["MESA"]
