# paso1_formulas.py — PASO 1 de la Lección 17 (DIP) ⭐.
# Cada bloque es una "receta" de la tabla del README (§5), con su código (DIP1...DIP7).
# Idea central: la LÓGICA (alto nivel) no crea sus detalles: los RECIBE (inyección),
# y todos dependen de una ABSTRACCIÓN.
# Ejecuta:  uv run python lecciones/17-dip/paso1_formulas.py
from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# DIP1 · La lógica crea el detalle ADENTRO -> recibirlo por PARÁMETRO (inyección)
# ---------------------------------------------------------------------------
class BaseDeDatosReal:                      # (imagina que necesita un servidor encendido)
    def __init__(self):
        self.filas = {}

    def insertar(self, clave):
        self.filas[clave] = clave


def registrar_lote_atado(referencia):       # ANTES: crea su detalle -> atada a él para siempre
    bd = BaseDeDatosReal()
    bd.insertar(referencia)
    return referencia in bd.filas


print("DIP1 antes  : funciona, pero SOLO con BaseDeDatosReal ->", registrar_lote_atado("L1"))


# ---------------------------------------------------------------------------
# DIP2 · Definir la ABSTRACCIÓN con lo que necesita el alto nivel (no el detalle)
# ---------------------------------------------------------------------------
class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

    @abstractmethod
    def obtener(self, ref): ...


# ---------------------------------------------------------------------------
# DIP3 · El DETALLE implementa la abstracción (la flecha apunta hacia arriba)
# ---------------------------------------------------------------------------
class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


def registrar_lote(repo: RepositorioAbstracto, referencia):   # DESPUÉS: recibe el detalle
    repo.agregar(referencia)
    return repo.obtener(referencia)


print("DIP1 después:", registrar_lote(RepositorioEnMemoria(), "L1"))
print("DIP2/3      : ¿RepositorioEnMemoria es un RepositorioAbstracto?", isinstance(RepositorioEnMemoria(), RepositorioAbstracto))


# ---------------------------------------------------------------------------
# DIP4 · Inyección por CONSTRUCTOR: la clase de servicio recibe el detalle en __init__
# ---------------------------------------------------------------------------
class ServicioLotes:
    def __init__(self, repo):
        self.repo = repo                    # no lo crea: lo recibe

    def registrar(self, referencia):
        self.repo.agregar(referencia)
        return self.repo.obtener(referencia)


print("DIP4 constructor:", ServicioLotes(RepositorioEnMemoria()).registrar("L2"))


# ---------------------------------------------------------------------------
# DIP5 · En los TESTS se inyecta un FALSO (como el FakeRepository del libro)
# ---------------------------------------------------------------------------
class RepositorioFalso(RepositorioAbstracto):
    def __init__(self):
        self._datos = set()

    def agregar(self, ref):
        self._datos.add(ref)

    def obtener(self, ref):
        return ref if ref in self._datos else None


assert ServicioLotes(RepositorioFalso()).registrar("T1") == "T1"
print("DIP5 falso  : test de ServicioLotes sin base de datos -> OK")


# ---------------------------------------------------------------------------
# DIP6 · Componer AFUERA, en UN solo lugar (el "bootstrap" del cap. 13)
# ---------------------------------------------------------------------------
def armar_servicio(modo):
    if modo == "test":
        return ServicioLotes(RepositorioFalso())
    return ServicioLotes(RepositorioEnMemoria())   # en el libro: SQLAlchemy


print("DIP6 componer:", type(armar_servicio("test").repo).__name__, "|", type(armar_servicio("produccion").repo).__name__)


# ---------------------------------------------------------------------------
# DIP7 · Para detalles SIMPLES basta inyectar una FUNCIÓN (como send_mail en el cap. 13)
# ---------------------------------------------------------------------------
def avisar_sin_stock(sku, enviar):          # 'enviar' es la dependencia inyectada
    enviar(f"Sin stock: {sku}")


enviados = []
avisar_sin_stock("MESA", enviados.append)   # en el test: una lista como "buzón falso"
avisar_sin_stock("MESA", print)             # en la vida real: imprimir (o mandar un email)
print("DIP7 función:", enviados)

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# registrar_lote(RepositorioEnMemoria, "L1")   # E4 -> TypeError: RepositorioEnMemoria.agregar() missing 1 required positional argument: 'ref'
# RepositorioAbstracto()                       # E5 -> TypeError: Can't instantiate abstract class RepositorioAbstracto without an implementation for abstract methods 'agregar', 'obtener'
# ---------------------------------------------------------------------------
