# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/10-herencia/paso5_solucionario/nivel_avanzado.py


class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def sueldo_total(self):
        return self.sueldo


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, area):
        super().__init__(nombre, sueldo)
        self.area = area

    # Problema 11: extender un cálculo del padre (H8): el gerente suma un bono de 500.
    def sueldo_total(self):
        return super().sueldo_total() + 500


# Problema 9: lista mixta; sumar sueldos y contar gerentes con isinstance (T1, T6).
plantilla = [Empleado("Luis", 2000), Gerente("Ana", 3000, "Ventas"), Empleado("Eva", 2500)]
total = 0
gerentes = 0
for persona in plantilla:
    total = total + persona.sueldo
    if isinstance(persona, Gerente):
        gerentes = gerentes + 1
print("P9: total", total, "| gerentes", gerentes)          # total 7500 | gerentes 1


# Problema 10: tres niveles de herencia, cada uno EXTIENDE al anterior.
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def describir(self):
        return self.marca


class Auto(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def describir(self):
        return super().describir() + f", {self.puertas} puertas"


class AutoElectrico(Auto):
    def __init__(self, marca, puertas, bateria):
        super().__init__(marca, puertas)
        self.bateria = bateria

    def describir(self):
        return super().describir() + f", batería {self.bateria} kWh"


tesla = AutoElectrico("Tesla", 4, 75)
print("P10:", Vehiculo("Tesla").describir())                # Tesla
print("P10:", Auto("Tesla", 4).describir())                 # Tesla, 4 puertas
print("P10:", tesla.describir())                            # Tesla, 4 puertas, batería 75 kWh
print("P10:", isinstance(tesla, Vehiculo))                  # True

# Problema 11: cada uno calcula su sueldo total a su manera.
for persona in plantilla:
    print("P11:", persona.nombre, persona.sueldo_total())   # Luis 2000 / Ana 3500 / Eva 2500


# Problema 12 (puente al libro): como "class FakeRepository(AbstractRepository):" (cap. 2),
# una hija que reutiliza al padre y EXTIENDE su método agregar.
class RepositorioBase:
    def __init__(self):
        self._lotes = {}

    def agregar(self, referencia, lote):
        self._lotes[referencia] = lote

    def obtener(self, referencia):
        return self._lotes.get(referencia)


class RepositorioConRegistro(RepositorioBase):
    def __init__(self):
        super().__init__()
        self.registro = []                                  # dato nuevo de la hija

    def agregar(self, referencia, lote):
        super().agregar(referencia, lote)                   # lo que ya hacía el padre...
        self.registro.append(referencia)                    # ...más lo nuevo


repo = RepositorioConRegistro()
repo.agregar("L1", "mesa x10")
repo.agregar("L2", "silla x25")
print("P12:", repo.obtener("L1"), "|", repo.registro)      # mesa x10 | ['L1', 'L2']
