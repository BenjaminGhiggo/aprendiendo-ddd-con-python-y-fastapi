# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 11.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/11-polimorfismo/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: el mismo mensaje, distintas respuestas (fácil) ---")


class Cuadrado:                                   # Paso 1: una clase con area()
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Circulo:                                    # Paso 2: OTRA clase, también con area()
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(3.14 * self.radio * self.radio, 2)


figuras = [Cuadrado(4), Circulo(3)]               # Paso 3: una lista con objetos distintos
for figura in figuras:                            # Paso 4: el mismo código para todos
    print(figura.area())                          # -> 16 / 28.26

print()
print("--- Ejemplo 2: una función que sirve para cualquier figura (fácil) ---")


def total_areas(figuras):                         # Paso 1: no pregunta el tipo
    total = 0                                     # Paso 2: acumulador
    for figura in figuras:
        total = total + figura.area()             # Paso 3: solo exige area()
    return round(total, 2)                        # Paso 4: redondea a 2 decimales


print(total_areas([Cuadrado(4), Circulo(3)]))     # -> 44.26

print()
print("--- Ejemplo 3: de 'if por tipo' a polimorfismo (intermedio) ---")


def area_con_ifs(figura):                         # ANTES: la función conoce cada tipo
    if isinstance(figura, Cuadrado):
        return figura.lado * figura.lado
    elif isinstance(figura, Circulo):
        return round(3.14 * figura.radio * figura.radio, 2)
    # ...un tipo nuevo obliga a agregar otro elif AQUÍ


class Rectangulo:                                 # DESPUÉS: el tipo nuevo trae su area()
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


print("con ifs, Rectangulo:", area_con_ifs(Rectangulo(2, 3)))       # -> None (¡lo olvidó!)
print("polimórfico:", total_areas([Cuadrado(4), Circulo(3), Rectangulo(2, 3)]))  # -> 50.26

print()
print("--- Ejemplo 4: duck typing con repositorios, como el libro (avanzado) ---")


class RepositorioDiccionario:                     # Paso 1: guarda en un diccionario
    def __init__(self):
        self._lotes = {}

    def agregar(self, referencia):
        self._lotes[referencia] = referencia

    def obtener(self, referencia):
        return self._lotes.get(referencia)


class RepositorioLista:                           # Paso 2: guarda en una lista (sin parentesco)
    def __init__(self):
        self._lotes = []

    def agregar(self, referencia):
        self._lotes.append(referencia)

    def obtener(self, referencia):
        for lote in self._lotes:
            if lote == referencia:
                return lote
        return None


def cargar_y_buscar(repo, referencias, buscada):  # Paso 3: solo usa agregar() y obtener()
    for referencia in referencias:
        repo.agregar(referencia)
    return repo.obtener(buscada)


for repo in [RepositorioDiccionario(), RepositorioLista()]:   # Paso 4: sirve con los dos
    print(type(repo).__name__, "->", cargar_y_buscar(repo, ["L1", "L2"], "L2"))
