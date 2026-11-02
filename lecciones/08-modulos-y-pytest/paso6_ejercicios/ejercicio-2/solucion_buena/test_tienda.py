from tienda import total

def test_suma_los_precios():
    assert total([10, 20, 30]) == 60

def test_lista_vacia_es_cero():
    assert total([]) == 0
