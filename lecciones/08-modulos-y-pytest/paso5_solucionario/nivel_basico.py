# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta con python (imprime las respuestas):
#   uv run python lecciones/08-modulos-y-pytest/paso5_solucionario/nivel_basico.py
# o con pytest (corre las funciones test_...):
#   uv run pytest lecciones/08-modulos-y-pytest/paso5_solucionario/nivel_basico.py -v

# Problema 1: importar el módulo entero (M2).
import calculos

# Problema 2: importar un solo nombre (M3).
from calculos import doble

# Problema 3: un módulo de la biblioteca estándar (M6), el mismo que usa el libro.
from datetime import date


# Problema 4: una prueba con assert (T2 + T3).
def test_doble():
    assert doble(3) == 6


if __name__ == "__main__":
    print("P1:", calculos.doble(4))                  # 8
    print("P2:", doble(5))                           # 10
    print("P3:", date(2024, 1, 15).year)             # 2024
    test_doble()
    print("P4: test_doble pasó")
