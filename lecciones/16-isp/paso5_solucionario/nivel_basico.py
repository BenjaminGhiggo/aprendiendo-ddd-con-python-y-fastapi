# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10, Lección 16 · ISP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/16-isp/paso5_solucionario/nivel_basico.py
from abc import ABC, abstractmethod

# Problema 1: ISP en una frase.
print("P1: ningún cliente debe depender de métodos que no usa: interfaces pequeñas, por rol")

# Problema 2: ¿qué métodos usa reporte(lector, ref)? Solo llama a lector.obtener(ref).
print("P2: solo obtener()")

# Problema 3: una clase con  def fax(self): raise NotImplementedError  delata una interfaz gorda.
print("P3: señal de interfaz 'gorda': la obligan a tener un método que no puede cumplir (receta I2)")


# Problema 4: interfaz Imprimible y una impresora simple que la cumple.
class Imprimible(ABC):
    @abstractmethod
    def imprimir(self, texto): ...


class ImpresoraSimple(Imprimible):
    def imprimir(self, texto):
        return "imprime " + texto


print("P4:", ImpresoraSimple().imprimir("factura"))
