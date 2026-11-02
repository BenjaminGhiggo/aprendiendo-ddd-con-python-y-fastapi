# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/12-abstraccion/paso5_solucionario/nivel_basico.py
import abc


# Problema 1: un contrato con un método abstracto; no se puede instanciar (A2, A3, A4).
class Figura(abc.ABC):
    @abc.abstractmethod
    def area(self):
        raise NotImplementedError


try:
    Figura()
except TypeError as error:
    print("P1:", error)


# Problema 2: una figura concreta que cumple el contrato (A5).
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


print("P2:", Cuadrado(3).area())                              # 9

# Problema 3: la concreta ES del tipo del contrato (A7).
print("P3:", isinstance(Cuadrado(3), Figura), "|", issubclass(Cuadrado, Figura))   # True | True


# Problema 4: una figura que NO implementa area() (A6).
class FiguraIncompleta(Figura):
    pass


try:
    FiguraIncompleta()
except TypeError as error:
    print("P4:", error)
