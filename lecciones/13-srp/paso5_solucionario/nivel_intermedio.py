# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10, Lección 13 · SRP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/13-srp/paso5_solucionario/nivel_intermedio.py


# Problema 5: Alumno calculaba Y imprimía el boletín. Separamos (receta S1).
class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)


def imprimir_boletin(alumno):
    print(f"P5: {alumno.nombre} -> promedio {alumno.promedio()}")


imprimir_boletin(Alumno("Ana", [14, 16, 18]))


# Problema 6: Inventario guardaba Y escribía el log. El log pasa a su propia clase.
class Registro:
    def __init__(self):
        self.lineas = []

    def anotar(self, texto):
        self.lineas.append(texto)


class Inventario:
    def __init__(self, registro):
        self.productos = []
        self.registro = registro            # el inventario USA el registro, no lo es

    def agregar(self, producto):
        self.productos.append(producto)
        self.registro.anotar(f"agregado {producto}")


reg = Registro()
inv = Inventario(reg)
inv.agregar("mesa")
inv.agregar("silla")
print("P6:", inv.productos, "| log:", reg.lineas)


# Problema 7: procesar_pedido calculaba total, aplicaba IGV e imprimía (receta S4).
def total(precios):
    return sum(precios)


def con_igv(monto):
    return monto * 118 / 100


def mostrar(monto):
    print("P7: Total con IGV:", monto)


mostrar(con_igv(total([50, 50])))           # Total con IGV: 118.0

# Problema 8: tras el refactor, ¿qué pieza toca cada cambio?
cambios = {
    "formato de moneda (S/ 118.00)": "mostrar",
    "la tasa de IGV pasa a 19%": "con_igv",
    "guardar el pedido en un archivo": "una pieza NUEVA (repositorio); no se toca ninguna",
}
for cambio, pieza in cambios.items():
    print("P8:", cambio, "->", pieza)
