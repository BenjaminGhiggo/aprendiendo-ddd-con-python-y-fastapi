# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/11-polimorfismo/paso5_solucionario/nivel_basico.py


# Problema 1: dos clases SIN parentesco, mismo método sonido() (P1, P6).
class Perro:
    def sonido(self):
        return "Guau"


class Gato:
    def sonido(self):
        return "Miau"


animales = [Perro(), Gato()]
for animal in animales:
    print("P1:", animal.sonido())                 # Guau / Miau


# Problema 2: una clase nueva entra en la MISMA lista; el for no cambia (P4).
class Vaca:
    def sonido(self):
        return "Muu"


animales.append(Vaca())
for animal in animales:
    print("P2:", animal.sonido())                 # Guau / Miau / Muu

# Problema 3: len() es polimórfico (P7).
print("P3:", len("hola"), len([1, 2, 3]), len({"a": 1, "b": 2}))   # 4 3 2

# Problema 4: "+" es polimórfico (P8).
print("P4:", 10 + 5, "ab" + "cd", [1] + [2, 3])                   # 15 abcd [1, 2, 3]
