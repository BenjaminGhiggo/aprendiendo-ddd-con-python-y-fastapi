# paso1_formulas.py — PASO 1 de la Lección 06.
# Cada bloque es una "fórmula" de la tabla del README (§5), con su código (C1, C2...).
# Ejecuta:  uv run python lecciones/06-clases-y-objetos/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.

print("========== CLASES Y OBJETOS ==========")


# C1 · Definir una CLASE (el molde). Por convención el nombre va en MayúsculaInicial.
# C2 · __init__ se ejecuta SOLO al crear cada objeto. "self" es "este objeto".
# C3 · self.atributo = valor guarda el dato DENTRO del objeto.
class Lote:
    def __init__(self, referencia, sku, cantidad):
        self.referencia = referencia
        self.sku = sku
        self.cantidad = cantidad

    # C7 · Un MÉTODO es una función que vive dentro de la clase. Su 1.er parámetro es self.
    def puede_asignar(self, pedido):
        return self.cantidad >= pedido

    # C9 · Un método puede CAMBIAR los datos del objeto.
    # C11 · Y puede usar OTRO método del mismo objeto con self.otro_metodo(...).
    def asignar(self, pedido):
        if self.puede_asignar(pedido):
            self.cantidad = self.cantidad - pedido


# C4 · Crear una INSTANCIA (un objeto concreto): NombreClase(argumentos). Sin "self".
lote = Lote("LOTE-001", "MESA", 20)
print("C4  creado:               ", lote.referencia)

# C5 · Leer un atributo: objeto.atributo
print("C5  lote.cantidad:        ", lote.cantidad)

# C6 · Cambiar un atributo desde afuera.
lote.sku = "MESA-GRANDE"
print("C6  lote.sku cambiado:    ", lote.sku)
lote.sku = "MESA"                       # lo devolvemos para las siguientes fórmulas

# C8 · Llamar a un método: objeto.metodo(argumentos). self se pasa SOLO.
print("C8  puede_asignar(5):     ", lote.puede_asignar(5))
print("C8  puede_asignar(25):    ", lote.puede_asignar(25))

# C9/C11 · El método asignar cambia el estado usando puede_asignar por dentro.
lote.asignar(5)
print("C9  tras asignar(5):      ", lote.cantidad)
lote.asignar(100)                       # no alcanza: no cambia
print("C11 tras asignar(100):    ", lote.cantidad)

# C10 · Cada instancia tiene SUS PROPIOS datos: cambiar una no toca la otra.
otro = Lote("LOTE-002", "SILLA", 50)
print("C10 lote / otro:          ", lote.cantidad, "/", otro.cantidad)

# C12 · ¿Este objeto es de esta clase?  isinstance(objeto, Clase)
print("C12 isinstance(lote, Lote):", isinstance(lote, Lote))
print("C12 isinstance(5, Lote):  ", isinstance(5, Lote))

# C13 · type(objeto) dice de qué clase es.
print("C13 type(lote):           ", type(lote).__name__)

# C14 · Objetos dentro de una LISTA (Lección 05) y recorrerlos llamando a un método.
lotes = [lote, otro]
print("C14 recorrer objetos:")
for l in lotes:
    print("      ", l.referencia, "puede 30?", l.puede_asignar(30))

# C15 · print(objeto) muestra algo como <__main__.Lote object at 0x...>: es NORMAL
#       (en el libro, cap. 1, se aprende a personalizar esto con "métodos mágicos").
print("C15 print(lote) empieza con:", str(lote)[:22])

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# Lote("L1")             # E3 -> TypeError: Lote.__init__() missing 2 required positional arguments: 'sku' and 'cantidad'
# print(Lote.cantidad)   # E5 -> AttributeError: type object 'Lote' has no attribute 'cantidad'
# print(lote.precio)     # E2 -> AttributeError: 'Lote' object has no attribute 'precio'
# Y este NO revienta, pero está mal (E4): muestra el método en vez de llamarlo.
# print(lote.puede_asignar)   # E4 -> <bound method Lote.puede_asignar of <__main__.Lote object at 0x...>>
# ---------------------------------------------------------------------------
