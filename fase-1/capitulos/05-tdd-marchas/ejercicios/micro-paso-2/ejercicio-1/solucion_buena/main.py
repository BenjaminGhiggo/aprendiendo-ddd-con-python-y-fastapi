# BUENA: la regla se prueba UNA vez (marcha baja, dominio); el servicio se prueba aparte.
def regla(disponible, pedido): return disponible >= pedido
def test_regla_en_dominio(): assert regla(10, 5) is True
test_regla_en_dominio(); print("1 test de la regla en su nivel")
