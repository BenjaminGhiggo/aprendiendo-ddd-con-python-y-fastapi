# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta con python (imprime las respuestas):
#   uv run python lecciones/08-modulos-y-pytest/paso5_solucionario/nivel_intermedio.py
# o con pytest (corre las funciones test_...):
#   uv run pytest lecciones/08-modulos-y-pytest/paso5_solucionario/nivel_intermedio.py -v
import pytest

# Problema 6: alias (M5).
import calculos as c


# Problema 5: dos pruebas, una para True y otra para False (T5).
def test_es_par_con_4():
    assert c.es_par(4) is True


def test_es_par_con_7():
    assert c.es_par(7) is False


# Problema 7: probar que se lanza un error (T6).
def test_dividir_entre_cero_lanza_error():
    with pytest.raises(ZeroDivisionError):
        c.dividir(1, 0)


if __name__ == "__main__":
    test_es_par_con_4()
    test_es_par_con_7()
    print("P5: test_es_par_con_4 y test_es_par_con_7 pasaron")
    print("P6:", c.doble(7))                          # 14
    test_dividir_entre_cero_lanza_error()
    print("P7: test_dividir_entre_cero_lanza_error pasó")
    # Problema 8: al IMPORTAR calculos (arriba) no se imprimió "probando calculos";
    # solo se imprime si ejecutas calculos.py directamente (M7).
    print("P8: c.__name__ =", c.__name__, "| este archivo:", __name__)
