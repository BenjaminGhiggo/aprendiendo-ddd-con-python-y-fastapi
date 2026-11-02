# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/04-funciones/paso5_solucionario/nivel_intermedio.py


# Problema 5: devolver un booleano (F10). "%" da el RESTO de una división: 8 % 2 es 0.
def es_par(n):
    return n % 2 == 0


print("P5:", es_par(8), es_par(7))                       # True False


# Problema 6: parámetro por defecto (F8).
def precio_con_descuento(precio, descuento=0):
    return precio - descuento


print("P6:", precio_con_descuento(100), precio_con_descuento(100, 20))   # 100 80


# Problema 7: devolver el mayor de dos números usando if (sin max).
def mayor(a, b):
    if a > b:
        return a
    return b                                             # return temprano (F11)


print("P7:", mayor(3, 9))                                # 9


# Problema 8: una función que solo imprime... ¿qué devuelve? (F7)
def contar_hasta(n):
    i = 1
    while i <= n:
        print("P8: contando", i)
        i = i + 1


lo_que_devuelve = contar_hasta(3)
print("P8: devuelve", lo_que_devuelve)                   # None
