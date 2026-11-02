# paso1_formulas.py — PASO 1 de la Lección 08.
# Cada bloque es una "fórmula" de las tablas del README (§5 módulos y §6 pytest),
# con su código (M1..., T1...).
# Ejecuta:  uv run python lecciones/08-modulos-y-pytest/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de las tablas.

print("========== MÓDULOS (import) ==========")

# M1 · Un MÓDULO es simplemente un archivo .py. Aquí usamos tienda.py (está al lado).
# M2 · import modulo  ->  se usa como modulo.nombre
import tienda

print("M2  tienda.asignar(20, 5):  ", tienda.asignar(20, 5))

# M3 · from modulo import nombre  ->  se usa directo, sin "tienda."
from tienda import asignar

print("M3  asignar(20, 5):         ", asignar(20, 5))

# M4 · Importar VARIOS nombres a la vez, separados por comas.
from tienda import puede_asignar, SinStock

print("M4  puede_asignar(20, 25):  ", puede_asignar(20, 25))

# M5 · Alias: import modulo as nombre_corto
import tienda as t

print("M5  t.asignar(10, 3):       ", t.asignar(10, 3))

# M6 · La BIBLIOTECA ESTÁNDAR de Python ya trae módulos. El libro usa date (fechas).
from datetime import date

llegada = date(2024, 1, 15)
print("M6  date(2024, 1, 15).year: ", llegada.year)

# M7 · __name__: vale "__main__" en el archivo que ejecutas, y el nombre del módulo
#      en los que importas. Por eso el bloque "if __name__ == '__main__':" de tienda.py
#      NO se imprimió arriba al hacer "import tienda".
print("M7  __name__ aquí:          ", __name__)
print("M7  tienda.__name__:        ", tienda.__name__)

print()
print("========== PRUEBAS (assert y pytest) ==========")

# T3 · assert condición: si es True, no pasa nada; si es False, lanza AssertionError.
assert asignar(20, 5) == 15
print("T3  assert asignar(20, 5) == 15 -> pasó (no dijo nada)")

# T4 · Un assert que FALLA lanza AssertionError (lo atrapamos para seguir, Lección 07).
try:
    assert asignar(20, 5) == 99
except AssertionError:
    print("T4  assert asignar(20, 5) == 99 -> AssertionError (falló)")

# T5 · Afirmar booleanos: "is True" / "is False".
assert puede_asignar(20, 5) is True
assert puede_asignar(20, 25) is False
print("T5  puede_asignar: True y False comprobados")

# T6 · pytest.raises: afirmar que un código LANZA cierto error (Lección 07).
#      "with ...:" abre un bloque que ESPERA ese error; si no ocurre, la prueba falla.
import pytest

with pytest.raises(SinStock):
    tienda.asignar_estricto(10, 25)
print("T6  pytest.raises(SinStock) -> el error ocurrió, como se esperaba")

# T7 · match="texto": además, el mensaje del error debe contener ese texto.
with pytest.raises(SinStock, match="piden 25"):
    tienda.asignar_estricto(10, 25)
print("T7  pytest.raises(..., match='piden 25') -> mensaje correcto")

# T1, T2, T8 y los comandos de uv (U1–U4) se practican en la terminal:
#   uv run pytest lecciones/08-modulos-y-pytest/test_tienda.py -v

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# import tiendaa                  # E1 -> ModuleNotFoundError: No module named 'tiendaa'
# from tienda import vender       # E2 -> ImportError: cannot import name 'vender' from 'tienda' (...)
# print(asignar_estricto(1, 2))   # E3 -> NameError: name 'asignar_estricto' is not defined
# assert asignar(20, 5) == 99     # E4 -> AssertionError
# ---------------------------------------------------------------------------
