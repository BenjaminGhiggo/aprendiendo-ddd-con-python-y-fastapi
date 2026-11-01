# test_tienda.py  -> las PRUEBAS de tienda.py

# IMPORT: traemos la función asignar desde el módulo tienda (otro archivo).
from tienda import asignar

# Una prueba es una función que empieza con "test_" y usa assert
# (assert = "afirmo que esto es verdad; si no, la prueba falla").
def test_asignar_resta_del_stock():
    assert asignar(20, 5) == 15

def test_asignar_sin_pedido_no_cambia():
    assert asignar(20, 0) == 20
