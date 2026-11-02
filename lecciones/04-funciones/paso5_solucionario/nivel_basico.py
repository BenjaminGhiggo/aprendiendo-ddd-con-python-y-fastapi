# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/04-funciones/paso5_solucionario/nivel_basico.py


# Problema 1: una función que devuelve el doble (F3 + F5).
def doble(n):
    return n * 2


print("P1:", doble(4))                    # 8


# Problema 2: devolver un texto armado.
def despedir(nombre):
    return "Adiós, " + nombre


print("P2:", despedir("Ana"))             # Adiós, Ana


# Problema 3: dos parámetros (F4).
def area_rectangulo(base, altura):
    return base * altura


print("P3:", area_rectangulo(3, 4))       # 12


# Problema 4: reutilizar la misma función dentro de un for (F15).
def saludar(nombre):
    return "Hola, " + nombre


for nombre in ["Ana", "Luis", "Eva"]:
    print("P4:", saludar(nombre))
