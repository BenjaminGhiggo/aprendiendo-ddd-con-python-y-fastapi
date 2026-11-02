# paso1_formulas.py — PASO 1 de la Lección 14 (OCP).
# Cada bloque es una "receta" de la tabla del README (§5), con su código (O1...O6).
# En cada una: el NÚCLEO no cambia y agregamos un caso NUEVO solo con código nuevo.
# Ejecuta:  uv run python lecciones/14-ocp/paso1_formulas.py
from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# O1 · Cadena de if/elif por regla -> cada regla es una FUNCIÓN y se pasa como dato
# ---------------------------------------------------------------------------
def precio_con_if(precio, tipo):            # ANTES: cada descuento nuevo = editar aquí
    if tipo == "ninguno":
        return precio
    elif tipo == "10":
        return precio * 0.9
    return precio


def sin_descuento(precio):
    return precio


def descuento_10(precio):
    return precio * 0.9


def descuento_black_friday(precio):         # NUEVO: código nuevo, nada editado
    return precio * 0.5


def precio_final(precio, regla):            # DESPUÉS: el núcleo NO cambia nunca
    return regla(precio)


print("O1  antes  :", precio_con_if(100, "10"))
print("O1  después:", precio_final(100, descuento_10), precio_final(100, descuento_black_friday))


# ---------------------------------------------------------------------------
# O2 · if/elif por TIPO de objeto -> POLIMORFISMO (una subclase por caso)
# ---------------------------------------------------------------------------
class Envio:
    def costo(self):
        return 0


class EnvioNormal(Envio):
    def costo(self):
        return 10


class EnvioExpress(Envio):                  # NUEVO: una clase más, nada editado
    def costo(self):
        return 20


def total_con_envio(precio, envio):         # núcleo: no pregunta "¿qué tipo eres?"
    return precio + envio.costo()


print("O2  después:", total_con_envio(100, EnvioNormal()), total_con_envio(100, EnvioExpress()))


# ---------------------------------------------------------------------------
# O3 · if/elif por TEXTO -> un DICCIONARIO registro {nombre: función}
# ---------------------------------------------------------------------------
DESCUENTOS = {"ninguno": sin_descuento, "10": descuento_10}


def precio_con_codigo(precio, codigo):      # núcleo: busca en el registro
    return DESCUENTOS[codigo](precio)


DESCUENTOS["blackfriday"] = descuento_black_friday   # extender = agregar UNA entrada
print("O3  después:", precio_con_codigo(100, "10"), precio_con_codigo(100, "blackfriday"))


# ---------------------------------------------------------------------------
# O4 · Varias reglas a aplicar -> una LISTA de funciones que se recorre
# ---------------------------------------------------------------------------
def no_vacio(texto):
    return texto != ""


def max_10(texto):
    return len(texto) <= 10


VALIDACIONES = [no_vacio, max_10]


def es_valido(texto):                       # núcleo: recorre la lista, sea cual sea
    for regla in VALIDACIONES:
        if not regla(texto):
            return False
    return True


def sin_espacios(texto):                    # NUEVO
    return " " not in texto


VALIDACIONES.append(sin_espacios)           # extender = append
print("O4  después:", es_valido("ana"), es_valido("ana lopez"))


# ---------------------------------------------------------------------------
# O5 · Base ABSTRACTA (ABC) que obliga a cada extensión a cumplir el contrato
# ---------------------------------------------------------------------------
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, precio):
        ...


class DescuentoVip(Descuento):              # NUEVO: si olvido aplicar(), Python no deja crearla
    def aplicar(self, precio):
        return precio * 70 / 100


def cobrar(precio, descuento):
    return descuento.aplicar(precio)


print("O5  después:", cobrar(100, DescuentoVip()))


# ---------------------------------------------------------------------------
# O6 · Punto de extensión tipo "message bus" (cap. 8): un dict de LISTAS de funciones
# ---------------------------------------------------------------------------
def avisar_email(dato):
    print("O6        EMAIL:", dato)


MANEJADORES = {"SinStock": [avisar_email]}


def manejar(evento, dato):                  # como handle(): "for handler in HANDLERS[...]"
    for manejador in MANEJADORES[evento]:
        manejador(dato)


def avisar_sms(dato):                       # NUEVO
    print("O6        SMS  :", dato)


MANEJADORES["SinStock"].append(avisar_sms)  # extender = registrar otro manejador
print("O6  después: manejar('SinStock', 'MESA') ->")
manejar("SinStock", "MESA")

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# print(precio_final(100, descuento_10(100)))  # E5 -> TypeError: 'float' object is not callable
# print(precio_con_codigo(100, "black"))       # E4 -> KeyError: 'black'
# class DescuentoRoto(Descuento): pass
# DescuentoRoto()                              # E6 -> TypeError: Can't instantiate abstract class ...
# ---------------------------------------------------------------------------
