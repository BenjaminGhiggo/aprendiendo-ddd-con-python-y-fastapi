# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10, Lección 13 · SRP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/13-srp/paso5_solucionario/nivel_basico.py

# Problema 1: ¿cuántas razones para cambiar tiene Reporte?
#   calcular() cambia si cambia la REGLA; imprimir() cambia si cambia el FORMATO.
#   -> 2 razones = viola el SRP.
class Reporte:
    def __init__(self, ventas):
        self.ventas = ventas

    def calcular(self):
        return sum(self.ventas)

    def imprimir(self):
        print("Ventas:", self.calcular())


razones = ["la regla del cálculo", "el formato de impresión"]
print("P1:", len(razones), "razones ->", razones)

# Problema 2: regla del "y". El nombre validar_y_guardar_usuario describe DOS cosas.
nombre = "validar_y_guardar_usuario"
print("P2: ¿viola SRP?", "_y_" in nombre)        # True


# Problema 3: separar saludar_y_contar en dos funciones.
def contar(nombres):
    return len(nombres)


def saludar(nombres):
    for n in nombres:
        print("P3: Hola,", n)


saludar(["Ana", "Luis"])
print("P3: cantidad =", contar(["Ana", "Luis"]))

# Problema 4: ¿qué responsabilidad tiene formatear_recibo?
print("P4: presentación (cómo se muestra el total), no la regla de negocio")
