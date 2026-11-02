# paso4_tu_turno_solucion.py — PASO 4 de la Lección 06: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index paso3_tu_turno.py paso4_tu_turno_solucion.py
# Si tu versión es distinta pero da la MISMA salida, también está bien.


# TODO 1: define la clase Alumno con __init__(self, nombre, nota) que guarde
#         ambos datos dentro del objeto (C1 + C2 + C3).
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    # TODO 2: dentro de Alumno, agrega el método aprobado(self) que devuelva
    #         True si self.nota >= 11 (C7).
    def aprobado(self):
        return self.nota >= 11

    # TODO 3: dentro de Alumno, agrega el método subir_nota(self, puntos) que le
    #         sume puntos a self.nota (C9).
    def subir_nota(self, puntos):
        self.nota = self.nota + puntos


# TODO 4: crea la instancia ana = Alumno("Ana", 9) e imprime ana.nombre (C4 + C5).
ana = Alumno("Ana", 9)
print(ana.nombre)

# TODO 5: imprime ana.aprobado() (C8).
print(ana.aprobado())

# TODO 6: llama ana.subir_nota(3) y luego imprime ana.nota y ana.aprobado().
ana.subir_nota(3)
print(ana.nota)
print(ana.aprobado())

# TODO 7: crea luis = Alumno("Luis", 15) e imprime luis.nota y ana.nota
#         para comprobar que cada objeto tiene sus propios datos (C10).
luis = Alumno("Luis", 15)
print(luis.nota)
print(ana.nota)

# Salida esperada:
# Ana
# False
# 12
# True
# 15
# 12
