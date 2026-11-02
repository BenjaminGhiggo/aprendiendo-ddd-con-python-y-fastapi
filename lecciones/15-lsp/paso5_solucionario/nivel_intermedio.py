# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10, Lección 15 · LSP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/15-lsp/paso5_solucionario/nivel_intermedio.py


# Problema 5: CuentaSinRetiro(Cuenta) lanzaba error en retirar() -> violación (LS5).
# Solución: la madre solo promete lo común (depositar); retirar va en una rama aparte.
class Cuenta:
    def __init__(self):
        self.saldo = 0

    def depositar(self, monto):
        self.saldo = self.saldo + monto


class CuentaConRetiro(Cuenta):
    def retirar(self, monto):
        self.saldo = self.saldo - monto


class CuentaPlazoFijo(Cuenta):              # no promete retirar: no hay sorpresa
    pass


ahorro = CuentaConRetiro()
ahorro.depositar(100)
ahorro.retirar(30)
plazo = CuentaPlazoFijo()
plazo.depositar(500)
print("P5:", ahorro.saldo, plazo.saldo, "| ¿plazo fijo tiene retirar?", hasattr(plazo, "retirar"))


# Problema 6: mostrar el fallo de Rectángulo/Cuadrado con números (LS6).
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def poner_ancho(self, valor):
        self.ancho = valor

    def poner_alto(self, valor):
        self.alto = valor

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def poner_ancho(self, valor):
        self.ancho = valor
        self.alto = valor

    def poner_alto(self, valor):
        self.ancho = valor
        self.alto = valor


def agrandar(r):
    r.poner_ancho(5)
    r.poner_alto(4)
    return r.area()


print("P6: esperado 20 | Rectangulo:", agrandar(Rectangulo(1, 1)), "| Cuadrado:", agrandar(Cuadrado(1)))


# Problema 7: firma incompatible. La hija quitó el parámetro ref (LS1).
class Repo:
    def obtener(self, ref):
        return ref


class RepoRoto(Repo):
    def obtener(self):
        return "x"


try:
    RepoRoto().obtener("L1")
except TypeError as error:
    print("P7: error ->", error)


class RepoArreglado(Repo):
    def obtener(self, ref):                  # misma firma que la madre
        return ref


print("P7: corregido ->", RepoArreglado().obtener("L1"))


# Problema 8: un test de contrato que sirve para CUALQUIER repositorio.
class RepoDict:
    def __init__(self):
        self._d = {}

    def agregar(self, ref):
        self._d[ref] = ref

    def obtener(self, ref):
        return self._d.get(ref)


class RepoSet:
    def __init__(self):
        self._s = set()

    def agregar(self, ref):
        self._s.add(ref)

    def obtener(self, ref):
        return ref if ref in self._s else None


def probar_contrato(repo):
    repo.agregar("L1")
    assert repo.obtener("L1") == "L1"
    assert repo.obtener("NO") is None
    return "OK"


print("P8:", probar_contrato(RepoDict()), probar_contrato(RepoSet()))
