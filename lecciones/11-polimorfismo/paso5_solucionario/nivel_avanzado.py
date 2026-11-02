# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/11-polimorfismo/paso5_solucionario/nivel_avanzado.py


# Problema 9: polimorfismo CON herencia (P5): cada tipo de trabajador calcula su pago.
class Empleado:
    def __init__(self, sueldo):
        self.sueldo = sueldo

    def pago(self):
        return self.sueldo


class Freelance(Empleado):
    def __init__(self, horas, tarifa):
        super().__init__(0)
        self.horas = horas
        self.tarifa = tarifa

    def pago(self):
        return self.horas * self.tarifa


class Pasante(Empleado):
    def __init__(self):
        super().__init__(0)

    def pago(self):
        return 500


nomina = [Empleado(2000), Freelance(10, 30), Pasante()]
total = 0
for persona in nomina:
    total = total + persona.pago()
print("P9: total nómina", total)                         # 2800


# Problema 10: notificadores intercambiables; agregar uno nuevo no cambia la función.
class Email:
    def enviar(self, mensaje):
        return f"EMAIL: {mensaje}"


class SMS:
    def enviar(self, mensaje):
        return f"SMS: {mensaje}"


class Chat:                                              # el nuevo
    def enviar(self, mensaje):
        return f"CHAT: {mensaje}"


def avisar_a_todos(notificadores, mensaje):
    for notificador in notificadores:
        print("P10:", notificador.enviar(mensaje))


avisar_a_todos([Email(), SMS(), Chat()], "sin stock de MESA")


# Problema 11: reemplazar un "if por tipo" por polimorfismo; ambos dan lo mismo.
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(3.14 * self.radio * self.radio, 2)


def total_con_ifs(figuras):                              # ANTES
    total = 0
    for figura in figuras:
        if isinstance(figura, Cuadrado):
            total = total + figura.lado * figura.lado
        elif isinstance(figura, Circulo):
            total = total + round(3.14 * figura.radio * figura.radio, 2)
    return round(total, 2)


def total_polimorfico(figuras):                          # DESPUÉS
    total = 0
    for figura in figuras:
        total = total + figura.area()
    return round(total, 2)


figuras = [Cuadrado(2), Circulo(1)]
print("P11: con ifs", total_con_ifs(figuras), "| polimórfico", total_polimorfico(figuras))   # 7.14 | 7.14


# Problema 12 (puente al libro): "To a Pythonista, a repository is any object that has
# add(thing) and get(id) methods" (cap. 2). Dos repositorios SIN parentesco, mismo contrato.
class RepositorioEnMemoria:
    def __init__(self):
        self._lotes = {}

    def agregar(self, lote):
        self._lotes[lote] = lote

    def obtener(self, referencia):
        return self._lotes.get(referencia)


class RepositorioQueRegistra:
    def __init__(self):
        self._lotes = {}
        self.registro = []

    def agregar(self, lote):
        self._lotes[lote] = lote
        self.registro.append(f"agregado {lote}")

    def obtener(self, referencia):
        self.registro.append(f"buscado {referencia}")
        return self._lotes.get(referencia)


def guardar_lotes(repo, referencias):                    # solo usa agregar() y obtener()
    for referencia in referencias:
        repo.agregar(referencia)
    return repo.obtener(referencias[-1])


memoria = RepositorioEnMemoria()
registra = RepositorioQueRegistra()
print("P12:", guardar_lotes(memoria, ["L1", "L2"]))      # L2
print("P12:", guardar_lotes(registra, ["L1", "L2"]))     # L2
print("P12:", registra.registro)                         # ['agregado L1', 'agregado L2', 'buscado L2']
