# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 12.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/12-abstraccion/paso2_ejemplos_resueltos.py
import abc

print("--- Ejemplo 1: escribir el contrato y comprobar que no se instancia (fácil) ---")


class RepositorioAbstracto(abc.ABC):              # Paso 1: hereda de abc.ABC
    @abc.abstractmethod                           # Paso 2: marca cada método obligatorio
    def agregar(self, lote):
        raise NotImplementedError                 # Paso 3: sin "cómo": solo el "qué"

    @abc.abstractmethod
    def obtener(self, referencia):
        raise NotImplementedError


try:
    RepositorioAbstracto()                        # Paso 4: intentar crear un objeto
except TypeError as error:
    print("No se puede:", error)

print()
print("--- Ejemplo 2: una implementación concreta (fácil) ---")


class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad


class RepositorioEnMemoria(RepositorioAbstracto):  # Paso 1: hereda del contrato
    def __init__(self):
        self._lotes = {}                           # Paso 2: elige CÓMO guardar: un diccionario

    def agregar(self, lote):                       # Paso 3: implementa agregar
        self._lotes[lote.referencia] = lote

    def obtener(self, referencia):                 # Paso 4: implementa obtener
        return self._lotes.get(referencia)


memoria = RepositorioEnMemoria()                   # Paso 5: ahora SÍ se puede crear
memoria.agregar(Lote("L1", 10))
print(memoria.obtener("L1").cantidad)              # -> 10

print()
print("--- Ejemplo 3: otra implementación y un cliente que no cambia (intermedio) ---")


class RepositorioLista(RepositorioAbstracto):      # Paso 1: mismo contrato, otro CÓMO
    def __init__(self):
        self._lotes = []

    def agregar(self, lote):
        self._lotes.append(lote)

    def obtener(self, referencia):
        for lote in self._lotes:
            if lote.referencia == referencia:
                return lote
        return None


def asignar(repo, referencia, pedido):            # Paso 2: el cliente solo usa el contrato
    lote = repo.obtener(referencia)
    if pedido > lote.cantidad:
        raise ValueError("No hay stock suficiente")
    lote.cantidad = lote.cantidad - pedido
    return lote.cantidad


for repo in [RepositorioEnMemoria(), RepositorioLista()]:   # Paso 3: sirve con los dos
    repo.agregar(Lote("L1", 10))
    print(type(repo).__name__, "-> quedan", asignar(repo, "L1", 3))   # -> quedan 7

print()
print("--- Ejemplo 4: el repositorio del libro (avanzado) ---")


class RepositorioConListar(abc.ABC):               # Paso 1: contrato con 3 métodos
    @abc.abstractmethod
    def agregar(self, lote):
        raise NotImplementedError

    @abc.abstractmethod
    def obtener(self, referencia):
        raise NotImplementedError

    @abc.abstractmethod
    def listar(self):
        raise NotImplementedError

    def contar(self):                              # Paso 2: método CONCRETO que usa el contrato
        return len(self.listar())


class RepositorioFalso(RepositorioConListar):      # Paso 3: como el FakeRepository del cap. 2
    def __init__(self, lotes):
        self._lotes = list(lotes)                  # copia de la lista inicial

    def agregar(self, lote):
        self._lotes.append(lote)

    def obtener(self, referencia):
        for lote in self._lotes:
            if lote.referencia == referencia:
                return lote
        return None

    def listar(self):
        return self._lotes


falso = RepositorioFalso([Lote("L1", 10), Lote("L2", 5)])   # Paso 4: arranca con 2 lotes
falso.agregar(Lote("L3", 7))
print("contar:", falso.contar())                            # -> 3 (heredado de la abstracta)
print("obtener L2:", falso.obtener("L2").cantidad)          # -> 5
