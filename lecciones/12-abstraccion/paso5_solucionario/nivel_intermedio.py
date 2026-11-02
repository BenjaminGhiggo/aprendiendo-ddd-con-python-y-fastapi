# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/12-abstraccion/paso5_solucionario/nivel_intermedio.py
import abc


# Problema 5: un contrato y dos implementaciones; se recorren igual (A5 + Lección 11).
class Notificador(abc.ABC):
    @abc.abstractmethod
    def enviar(self, mensaje):
        raise NotImplementedError


class Email(Notificador):
    def enviar(self, mensaje):
        return f"EMAIL: {mensaje}"


class SMS(Notificador):
    def enviar(self, mensaje):
        return f"SMS: {mensaje}"


for notificador in [Email(), SMS()]:
    print("P5:", notificador.enviar("hola"))


# Problema 6: un método CONCRETO en la abstracta que usa el método abstracto (A8).
class Figura(abc.ABC):
    @abc.abstractmethod
    def area(self):
        raise NotImplementedError

    def describir(self):
        return f"Figura con área {self.area()}"


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


print("P6:", Cuadrado(3).describir())                         # Figura con área 9


# Problema 7: un contrato con DOS métodos abstractos.
class Almacen(abc.ABC):
    @abc.abstractmethod
    def guardar(self, clave, valor):
        raise NotImplementedError

    @abc.abstractmethod
    def leer(self, clave):
        raise NotImplementedError


class AlmacenDiccionario(Almacen):
    def __init__(self):
        self._datos = {}

    def guardar(self, clave, valor):
        self._datos[clave] = valor

    def leer(self, clave):
        return self._datos.get(clave)


almacen = AlmacenDiccionario()
almacen.guardar("mesa", 10)
print("P7:", almacen.leer("mesa"), "|", almacen.leer("silla"))   # 10 | None


# Problema 8: @abc.abstractmethod SIN heredar de abc.ABC no protege nada (X4).
class SinABC:
    @abc.abstractmethod
    def agregar(self, lote):
        raise NotImplementedError


objeto = SinABC()
print("P8: se creó", type(objeto).__name__, "sin error: la protección NO funciona")
