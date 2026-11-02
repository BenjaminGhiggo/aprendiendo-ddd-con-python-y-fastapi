# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10, Lección 17 · DIP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/17-dip/paso5_solucionario/nivel_basico.py
from abc import ABC, abstractmethod

# Problema 1: clasificar alto nivel (lo que le importa al negocio) y bajo nivel (detalles técnicos).
piezas = {
    "calcular_descuento": "alto nivel",
    "guardar_en_mysql": "bajo nivel",
    "enviar_email_smtp": "bajo nivel",
    "reglas_de_stock": "alto nivel",
}
for pieza, nivel in piezas.items():
    print("P1:", pieza, "->", nivel)

# Problema 2: ¿dónde está la inyección? En  registrar_lote(repo, "L1")  el repo se crea AFUERA
# y se PASA como argumento: eso es inyectar la dependencia.
print("P2: el repositorio se crea afuera y se pasa como argumento a registrar_lote")


# Problema 3: la función creaba RepositorioEnMemoria() adentro. Ahora lo recibe.
class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

    @abstractmethod
    def obtener(self, ref): ...


class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


def registrar_lote(repo, referencia):       # ya no dice  repo = RepositorioEnMemoria()
    repo.agregar(referencia)
    return repo.obtener(referencia)


print("P3:", registrar_lote(RepositorioEnMemoria(), "LOTE-001"))


# Problema 4: inyectar un falso a la MISMA función, sin cambiarla.
class RepositorioFalso(RepositorioAbstracto):
    def __init__(self):
        self._datos = set()

    def agregar(self, ref):
        self._datos.add(ref)

    def obtener(self, ref):
        return ref if ref in self._datos else None


print("P4:", registrar_lote(RepositorioFalso(), "LOTE-002"))
