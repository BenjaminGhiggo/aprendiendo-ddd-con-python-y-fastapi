# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/10-herencia/paso5_solucionario/nivel_intermedio.py


# Problema 5: reutilizar el constructor del padre y agregar un dato (H4, H5).
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def saludo(self):
        return f"Hola, soy {self.nombre}"


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, area):
        super().__init__(nombre, sueldo)
        self.area = area

    # Problema 6: EXTENDER el saludo del padre (H8).
    def saludo(self):
        return super().saludo() + f" y dirijo {self.area}"


ana = Gerente("Ana", 3000, "Ventas")
print("P5:", ana.nombre, ana.sueldo, ana.area)    # Ana 3000 Ventas
print("P6:", Empleado("Luis", 2000).saludo())     # Hola, soy Luis
print("P6:", ana.saludo())                        # Hola, soy Ana y dirijo Ventas


# Problema 7: SOBRESCRIBIR por completo (H7): el pingüino no vuela.
class Pajaro:
    def mover(self):
        return "vuela"


class Pinguino(Pajaro):
    def mover(self):
        return "nada"


print("P7:", Pajaro().mover(), "|", Pinguino().mover())   # vuela | nada


# Problema 8: el error de olvidar super().__init__ (X1).
class GerenteMalo(Empleado):
    def __init__(self, nombre, sueldo, area):
        self.area = area                          # ¡falta super().__init__(nombre, sueldo)!


try:
    GerenteMalo("Eva", 2500, "TI").saludo()
except AttributeError as error:
    print("P8:", error)
