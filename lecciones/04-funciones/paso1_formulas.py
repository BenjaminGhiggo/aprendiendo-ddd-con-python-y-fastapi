# paso1_formulas.py — PASO 1 de la Lección 04.
# Cada bloque es una "fórmula" de la tabla del README (§5), con su código (F1, F2...).
# Ejecuta:  uv run python lecciones/04-funciones/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.

print("========== FUNCIONES ==========")


# F1 · Definir una función SIN parámetros: def + nombre + () + dos puntos.
#      Lo de adentro va con sangría (4 espacios). Definir NO la ejecuta.
def saludar_a_todos():
    print("Hola a todos")


# F2 · Llamar (ejecutar) la función: su nombre + paréntesis.
print("F2  llamar:")
saludar_a_todos()


# F3 · Con un PARÁMETRO: la "cajita" que recibe el dato al llamarla.
def saludar(nombre):
    return "Hola, " + nombre


print("F3  saludar('Ana'):        ", saludar("Ana"))


# F4 · Con VARIOS parámetros, separados por comas.
def sumar(a, b):
    return a + b


print("F4  sumar(2, 3):           ", sumar(2, 3))

# F5 · return DEVUELVE un valor a quien llamó. F6 · Ese valor se puede GUARDAR.
resultado = sumar(10, 5)
print("F6  resultado = sumar(10,5):", resultado)


# F7 · Una función SIN return devuelve None ("nada").
def solo_imprime():
    print("     (solo imprimo, no devuelvo)")


r = solo_imprime()
print("F7  lo devuelto:            ", r)


# F8 · Parámetro POR DEFECTO: si no lo pasas, usa ese valor.
def saludar_con(nombre, saludo="Hola"):
    return saludo + ", " + nombre


print("F8  saludar_con('Ana'):     ", saludar_con("Ana"))
print("F8  saludar_con('Ana','Buenas'):", saludar_con("Ana", "Buenas"))

# F9 · Argumento POR NOMBRE: el orden ya no importa.
print("F9  por nombre:             ", saludar_con(saludo="Chau", nombre="Luis"))


# F10 · Devolver un booleano (True/False): la función "responde una pregunta".
def es_mayor(edad):
    return edad >= 18


print("F10 es_mayor(20):           ", es_mayor(20))
print("F10 es_mayor(15):           ", es_mayor(15))


# F11 · return TEMPRANO: al llegar a un return, la función TERMINA ahí.
def clasificar(cantidad):
    if cantidad == 0:
        return "agotado"      # si entra aquí, no sigue
    return "disponible"


print("F11 clasificar(0):          ", clasificar(0))
print("F11 clasificar(7):          ", clasificar(7))


# F12 · Una función puede LLAMAR a otra.
def calcular_total(precio, cantidad):
    return precio * cantidad


def total_con_envio(precio, cantidad):
    return calcular_total(precio, cantidad) + 5


print("F12 total_con_envio(10, 3): ", total_con_envio(10, 3))


# F13 · ANOTACIONES de tipo (como en el libro): ": int" y "-> int" DOCUMENTAN qué
#       tipo se espera y qué tipo se devuelve. Python NO las obliga; son para leer.
def asignar(disponible: int, pedido: int) -> int:
    return disponible - pedido


print("F13 asignar(20, 5):         ", asignar(20, 5))


# F14 · Las variables creadas DENTRO de una función son LOCALES: no existen afuera.
def armar_mensaje():
    mensaje = "soy local"
    return mensaje


print("F14 armar_mensaje():        ", armar_mensaje())

# F15 · Llamarla dentro de un for: la reutilizamos en cada vuelta.
print("F15 en un for:")
for persona in ["Benjamin", "Carla"]:
    print("     ", saludar(persona))

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# print(saludar())             # E3 -> TypeError: saludar() missing 1 required positional argument: 'nombre'
# print(saludar("Ana", "Luis")) # E4 -> TypeError: saludar() takes 1 positional argument but 2 were given
# print(mensaje)               # E6 -> NameError: name 'mensaje' is not defined
# print(despedir("Ana"))       # E1 -> NameError: name 'despedir' is not defined
# Y este NO revienta, pero está mal (E2): imprime la función en vez de llamarla.
# print(saludar)               # E2 -> <function saludar at 0x...>
# ---------------------------------------------------------------------------
