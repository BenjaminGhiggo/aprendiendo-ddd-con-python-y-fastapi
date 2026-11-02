# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/10-herencia/paso5_solucionario/nivel_basico.py


# Problema 1: una hija que hereda TODO sin escribir nada (H2, H3).
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        return f"Soy {self.nombre}"


class Perro(Animal):
    pass


print("P1:", Perro("Toby").describir())          # Soy Toby


# Problema 2: una hija con un método NUEVO (H6).
class Gato(Animal):
    def maullar(self):
        return "Miau"


mishi = Gato("Mishi")
print("P2:", mishi.describir(), "|", mishi.maullar())   # Soy Mishi | Miau

# Problema 3: la hija ES el padre, pero el padre NO es la hija (T2, T3).
print("P3:", isinstance(Perro("Toby"), Animal), "|", isinstance(Animal("x"), Perro))  # True | False

# Problema 4: preguntar por la clase (T4, T5).
print("P4:", issubclass(Gato, Animal), "|", type(mishi).__name__)   # True | Gato
