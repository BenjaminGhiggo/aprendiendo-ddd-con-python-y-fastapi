# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 08.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/08-modulos-y-pytest/paso2_ejemplos_resueltos.py
#
# Nota: las pruebas de los ejemplos 2–4 son funciones test_... normales. pytest las
# encuentra y ejecuta SOLAS; aquí, para verlas correr con python, las llamamos a mano.
import pytest

print("--- Ejemplo 1: usar un módulo de dos maneras (fácil) ---")
import tienda                                   # Paso 1: traer el módulo entero (M2)
from tienda import puede_asignar                # Paso 2: traer un solo nombre (M3)

print(tienda.asignar(20, 5))                    # Paso 3: con prefijo   -> 15
print(puede_asignar(20, 5))                     # Paso 4: sin prefijo   -> True

print()
print("--- Ejemplo 2: tu primera prueba (fácil) ---")


def test_asignar_resta_del_stock():             # Paso 1: nombre que empieza con test_ (T2)
    resultado = tienda.asignar(20, 5)           # Paso 2: ejecutar con datos conocidos
    assert resultado == 15                      # Paso 3: afirmar lo esperado (T3)


test_asignar_resta_del_stock()                  # (pytest la llamaría solo)
print("test_asignar_resta_del_stock: pasó")

print()
print("--- Ejemplo 3: probar que se LANZA un error (intermedio) ---")


def test_sin_stock_lanza_error():
    with pytest.raises(tienda.SinStock, match="piden 25"):   # Paso 1: espero este error (T6 + T7)
        tienda.asignar_estricto(10, 25)                      # Paso 2: el código que debe lanzarlo


test_sin_stock_lanza_error()
print("test_sin_stock_lanza_error: pasó")

print()
print("--- Ejemplo 4: TDD rojo -> verde, como hace el libro (avanzado) ---")


# Paso 1: escribo la PRUEBA primero, para una función que todavía no existe bien.
def test_stock_total():
    assert stock_total([10, 5, 3]) == 18


# Paso 2: una versión vacía de la función (todavía no hace nada) -> la prueba FALLA (ROJO).
def stock_total(cantidades):
    pass


try:
    test_stock_total()
except AssertionError:
    print("ROJO: test_stock_total falló (la función aún no suma)")


# Paso 3: implemento lo mínimo para que pase.
def stock_total(cantidades):
    total = 0
    for c in cantidades:
        total = total + c
    return total


test_stock_total()                               # Paso 4: ahora pasa (VERDE)
print("VERDE: test_stock_total pasó ->", stock_total([10, 5, 3]))
