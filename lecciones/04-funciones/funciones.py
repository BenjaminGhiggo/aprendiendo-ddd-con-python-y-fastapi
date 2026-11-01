# funciones.py

# 1. Una FUNCIÓN empaqueta código con un nombre para reutilizarlo.
#    def = "definir una función". Entre paréntesis van los PARÁMETROS (lo que recibe).
def saludar(nombre):
    mensaje = "Hola, " + nombre
    return mensaje   # return = "devuelve este valor a quien llamó la función"

# 2. Definir NO ejecuta. La función corre cuando la LLAMAMOS por su nombre.
saludo_de_ana = saludar("Ana")
print(saludo_de_ana)

# 3. Como está empaquetada, la reutilizamos cuantas veces queramos (incluso en un for).
for nombre in ["Benjamin", "Carla"]:
    print(saludar(nombre))
