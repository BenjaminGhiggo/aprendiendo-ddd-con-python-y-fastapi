# MALA: probar la MISMA regla dos veces (dominio y servicio) duplica tests fragiles.
def regla(disponible, pedido): return disponible >= pedido
def test_dominio(): assert regla(10, 5) is True
def test_servicio(): assert regla(10, 5) is True   # duplicado innecesario
test_dominio(); test_servicio(); print("2 tests para 1 regla")
