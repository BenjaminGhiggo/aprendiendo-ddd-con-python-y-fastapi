# paso1_formulas.py — PASO 1 de la Lección 16 (ISP).
# Cada bloque es una "receta" de la tabla del README (§5), con su código (I1...I6).
# Idea central: cada CLIENTE depende solo de la interfaz PEQUEÑA que de verdad usa.
# Ejecuta:  uv run python lecciones/16-isp/paso1_formulas.py
from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# I1 · Interfaz "gorda" -> partirla por ROL (lo que cada cliente necesita)
# ---------------------------------------------------------------------------
class RepositorioGordo(ABC):                # ANTES: 4 métodos para todos, los usen o no
    @abstractmethod
    def agregar(self, ref): ...

    @abstractmethod
    def obtener(self, ref): ...

    @abstractmethod
    def borrar(self, ref): ...

    @abstractmethod
    def exportar_csv(self): ...


class Lector(ABC):                          # DESPUÉS: rol "leer"
    @abstractmethod
    def obtener(self, ref): ...


class Escritor(ABC):                        # DESPUÉS: rol "escribir"
    @abstractmethod
    def agregar(self, ref): ...


# (__abstractmethods__ es donde Python anota los métodos que una ABC OBLIGA a implementar;
#  sorted(...) los muestra como lista ordenada. Solo lo usamos para ver la evidencia.)
print("I1  antes  : métodos que impone RepositorioGordo =", sorted(RepositorioGordo.__abstractmethods__))
print("I1  después: Lector =", sorted(Lector.__abstractmethods__), "| Escritor =", sorted(Escritor.__abstractmethods__))


# ---------------------------------------------------------------------------
# I2 · Señal de alarma: métodos vacíos o que lanzan NotImplementedError "porque no aplica"
# ---------------------------------------------------------------------------
class Multifuncion(ABC):
    @abstractmethod
    def imprimir(self, texto): ...

    @abstractmethod
    def escanear(self): ...

    @abstractmethod
    def fax(self, numero): ...


class ImpresoraSimpleObligada(Multifuncion):   # obligada a "implementar" lo que no tiene
    def imprimir(self, texto):
        return "imprime " + texto

    def escanear(self):
        raise NotImplementedError("no escanea")

    def fax(self, numero):
        raise NotImplementedError("no tiene fax")


try:
    ImpresoraSimpleObligada().fax("123")
except NotImplementedError as error:
    print("I2  señal  : NotImplementedError ->", error, "(la interfaz es demasiado grande)")


# ---------------------------------------------------------------------------
# I3 · Una clase puede cumplir VARIAS interfaces pequeñas (herencia de varias ABC)
# I6 · Combinar roles: Repositorio = Lector + Escritor
# ---------------------------------------------------------------------------
class Repositorio(Lector, Escritor):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


repo = Repositorio()
print("I3  varias : ¿es Lector?", isinstance(repo, Lector), "| ¿es Escritor?", isinstance(repo, Escritor))


# ---------------------------------------------------------------------------
# I4 · El CLIENTE pide la interfaz mínima en su parámetro
# ---------------------------------------------------------------------------
def reporte(lector: Lector, ref):           # solo necesita LEER
    return f"Encontrado: {lector.obtener(ref)}"


def respaldo(escritor: Escritor, ref):      # solo necesita ESCRIBIR
    escritor.agregar(ref)
    return f"respaldado: {ref}"


print("I4  cliente:", respaldo(repo, "LOTE-001"), "|", reporte(repo, "LOTE-001"))


# ---------------------------------------------------------------------------
# I5 · Duck typing: el cliente solo LLAMA lo que necesita; sirve cualquier objeto que lo tenga
# ---------------------------------------------------------------------------
class TablaDePrecios:                       # NO hereda de Lector, pero tiene obtener()
    def obtener(self, ref):
        return {"LOTE-001": 50}.get(ref)


print("I5  pato   :", reporte(TablaDePrecios(), "LOTE-001"), "| ¿hereda de Lector?", isinstance(TablaDePrecios(), Lector))


# I6 · Combinar roles (ya visto arriba en Repositorio). Otro: un falso que SOLO lee.
class LectorFalso(Lector):                  # para tests de reporte: no necesita agregar
    def obtener(self, ref):
        return "falso-" + ref


print("I6  combinar/falso mínimo:", reporte(LectorFalso(), "X"), "| ¿tiene agregar?", hasattr(LectorFalso(), "agregar"))

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UN bloque, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# class RepoIncompleto(Lector, Escritor):     # E3: olvidé agregar()
#     def obtener(self, ref):
#         return ref
# RepoIncompleto()   # -> TypeError: Can't instantiate abstract class RepoIncompleto without an implementation for abstract method 'agregar'
# ---------------------------------------------------------------------------
