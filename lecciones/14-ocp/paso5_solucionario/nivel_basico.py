# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10, Lección 14 · OCP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/14-ocp/paso5_solucionario/nivel_basico.py

# Problema 1: ¿qué significa "abierto a extensión, cerrado a modificación"?
print("P1: agregar comportamiento NUEVO escribiendo código NUEVO, sin editar el que ya funciona")


# Problema 2: un descuento del 20 % sin tocar precio_final (receta O1).
def precio_final(precio, regla):
    return regla(precio)


def descuento_20(precio):
    return precio * 80 / 100


print("P2:", precio_final(100, descuento_20))          # 80.0


# Problema 3: ¿viola OCP? Para agregar "triangulo" hay que EDITAR esta función -> sí.
def area_con_if(figura, a, b):
    if figura == "rectangulo":
        return a * b
    elif figura == "cuadrado":
        return a * a
    return 0


print("P3: sí viola OCP: cada figura nueva obliga a agregar otro elif en area_con_if")


# Problema 4: agregar el idioma "pt" a un registro, sin tocar saludar (receta O3).
def hola_es(nombre):
    return f"Hola, {nombre}"


def hola_en(nombre):
    return f"Hello, {nombre}"


SALUDOS = {"es": hola_es, "en": hola_en}


def saludar(idioma, nombre):
    return SALUDOS[idioma](nombre)


def hola_pt(nombre):
    return f"Olá, {nombre}"


SALUDOS["pt"] = hola_pt
print("P4:", saludar("pt", "Ana"))                      # Olá, Ana
