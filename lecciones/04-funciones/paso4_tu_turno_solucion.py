# paso4_tu_turno_solucion.py — PASO 4 de la Lección 04: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index paso3_tu_turno.py paso4_tu_turno_solucion.py
# Si tu versión es distinta pero da la MISMA salida, también está bien.

# TODO 1: define despedir(nombre) que DEVUELVA "Adiós, " + nombre (F3 + F5).
def despedir(nombre):
    return "Adiós, " + nombre


# TODO 2: imprime despedir("Ana").
print(despedir("Ana"))


# TODO 3: define area(base, altura) que devuelva base * altura (F4).
def area(base, altura):
    return base * altura


# TODO 4: guarda area(3, 4) en una variable y luego imprímela (F6).
resultado = area(3, 4)
print(resultado)


# TODO 5: define es_mayor_de_edad(edad) que devuelva True o False (F10).
def es_mayor_de_edad(edad):
    return edad >= 18


# TODO 6: imprime es_mayor_de_edad(17).
print(es_mayor_de_edad(17))


# TODO 7: define precio_final(precio, descuento=0) que devuelva precio - descuento (F8).
def precio_final(precio, descuento=0):
    return precio - descuento


# TODO 8: imprime precio_final(100) y luego precio_final(100, 30).
print(precio_final(100))
print(precio_final(100, 30))

# Salida esperada:
# Adiós, Ana
# 12
# False
# 100
# 70
