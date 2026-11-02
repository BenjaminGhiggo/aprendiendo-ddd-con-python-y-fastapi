# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10, Lección 14 · OCP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/14-ocp/paso5_solucionario/nivel_avanzado.py
from abc import ABC, abstractmethod


# Problema 9: exportadores con una ABC; agregar uno nuevo sin tocar exportar_todo (receta O5).
class Exportador(ABC):
    @abstractmethod
    def exportar(self, datos):
        ...


class ExportadorCSV(Exportador):
    def exportar(self, datos):
        return ",".join(datos)


class ExportadorLineas(Exportador):
    def exportar(self, datos):
        return " | ".join(datos)


def exportar_todo(datos, exportadores):     # núcleo: no cambia
    for exportador in exportadores:
        print("P9:", exportador.exportar(datos))


class ExportadorMayusculas(Exportador):     # NUEVO
    def exportar(self, datos):
        return ",".join(datos).upper()


exportar_todo(["mesa", "silla"], [ExportadorCSV(), ExportadorLineas(), ExportadorMayusculas()])


# Problema 10: un código desconocido no debe reventar: .get con un valor por defecto.
def sin_descuento(precio):
    return precio


def descuento_10(precio):
    return precio * 0.9


DESCUENTOS = {"ninguno": sin_descuento, "10": descuento_10}


def precio_con_codigo(precio, codigo):
    regla = DESCUENTOS.get(codigo, sin_descuento)
    return regla(precio)


print("P10:", precio_con_codigo(100, "10"), precio_con_codigo(100, "NO-EXISTE"))   # 90.0 100


# Problema 11: una función registrar() como único punto de extensión.
def registrar(nombre, funcion):
    DESCUENTOS[nombre] = funcion


def descuento_cumple(precio):
    return precio - 15


registrar("cumple", descuento_cumple)
print("P11:", sorted(DESCUENTOS), "->", precio_con_codigo(100, "cumple"))   # ... 85


# Problema 12 (puente al libro, cap. 8): un evento NUEVO con su manejador, sin tocar manejar().
def avisar_email(dato):
    print("P12: EMAIL ->", dato)


MANEJADORES = {"SinStock": [avisar_email]}


def manejar(evento, dato):                  # como handle(): for handler in HANDLERS[...]
    for manejador in MANEJADORES[evento]:
        manejador(dato)


def registrar_asignacion(dato):
    print("P12: REGISTRO -> asignado", dato)


def avisar_almacen(dato):
    print("P12: ALMACÉN -> preparar", dato)


MANEJADORES["Asignado"] = [registrar_asignacion, avisar_almacen]
manejar("SinStock", "MESA")
manejar("Asignado", "pedido o1 en lote-1")
