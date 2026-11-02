# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 14 (OCP).
# Los 4 ejemplos resueltos del README (§9): VIOLACIÓN -> REFACTOR -> EXTENSIÓN sin editar.
# Ejecuta:  uv run python lecciones/14-ocp/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: descuentos con if/elif (fácil) ---")


# Paso 1 (violación): para agregar un descuento hay que EDITAR esta función.
def precio_con_if(precio, tipo):
    if tipo == "ninguno":
        return precio
    elif tipo == "10":
        return precio * 0.9
    return precio


print(precio_con_if(100, "10"))


# Paso 2 (refactor): cada regla es una función; el núcleo recibe la regla.
def sin_descuento(precio):
    return precio


def descuento_10(precio):
    return precio * 0.9


def precio_final(precio, regla):
    return regla(precio)


# Paso 3 (extender): un descuento nuevo es SOLO código nuevo.
def descuento_black_friday(precio):
    return precio * 0.5


print(precio_final(100, sin_descuento), precio_final(100, descuento_10), precio_final(100, descuento_black_friday))

print()
print("--- Ejemplo 2: un registro (diccionario) de descuentos (fácil) ---")
# Paso 1: el registro guarda nombre -> función.
DESCUENTOS = {"ninguno": sin_descuento, "10": descuento_10}


# Paso 2: el núcleo busca en el registro; no conoce los descuentos de antemano.
def precio_con_codigo(precio, codigo):
    return DESCUENTOS[codigo](precio)


# Paso 3 (extender): agregar "vip" es agregar UNA entrada al registro.
def descuento_vip(precio):
    return precio * 70 / 100


DESCUENTOS["vip"] = descuento_vip
print(precio_con_codigo(100, "10"), precio_con_codigo(100, "vip"))

print()
print("--- Ejemplo 3: tipos de envío con polimorfismo (intermedio) ---")


# Paso 1 (violación): el núcleo pregunta el tipo con if/elif.
def costo_envio_con_if(tipo):
    if tipo == "normal":
        return 10
    elif tipo == "express":
        return 20
    return 0


print(costo_envio_con_if("express"))


# Paso 2 (refactor): una clase base y una subclase por tipo.
class Envio:
    def costo(self):
        return 0


class EnvioNormal(Envio):
    def costo(self):
        return 10


class EnvioExpress(Envio):
    def costo(self):
        return 20


def total_con_envio(precio, envio):
    return precio + envio.costo()


# Paso 3 (extender): Internacional es una clase NUEVA; total_con_envio no se toca.
class EnvioInternacional(Envio):
    def costo(self):
        return 50


for envio in [EnvioNormal(), EnvioExpress(), EnvioInternacional()]:
    print(type(envio).__name__, "->", total_con_envio(100, envio))

print()
print("--- Ejemplo 4: un mini message bus, como en el cap. 8 (avanzado) ---")


# Paso 1: el registro evento -> LISTA de manejadores (como HANDLERS del libro).
def avisar_email(sku):
    print("EMAIL: sin stock de", sku)


MANEJADORES = {"SinStock": [avisar_email]}


# Paso 2: el núcleo (como handle()) recorre la lista; NUNCA cambia.
def manejar(evento, dato):
    for manejador in MANEJADORES[evento]:
        manejador(dato)


manejar("SinStock", "MESA")


# Paso 3 (extender): un aviso nuevo y un evento nuevo, sin tocar manejar().
def avisar_sms(sku):
    print("SMS: sin stock de", sku)


def registrar_asignacion(referencia):
    print("REGISTRO: asignado en", referencia)


MANEJADORES["SinStock"].append(avisar_sms)
MANEJADORES["Asignado"] = [registrar_asignacion]
manejar("SinStock", "MESA")
manejar("Asignado", "lote-1")
