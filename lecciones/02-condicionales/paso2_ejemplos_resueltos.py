# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 02.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/02-condicionales/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: ¿mayor de edad? (fácil) ---")
edad = 20                                # Paso 1: el dato
if edad >= 18:                           # Paso 2: la condición da True o False (C4)
    print("Eres mayor de edad")          # Paso 3: este bloque corre si es True
else:
    print("Eres menor de edad")          #         este, si es False (F2)

print()
print("--- Ejemplo 2: ¿par o impar? (fácil) ---")
numero = 7                               # Paso 1: el dato
resto = numero % 2                       # Paso 2: el resto de dividir entre 2 -> 1
if resto == 0:                           # Paso 3: par si el resto es 0 (C12)
    print(numero, "es par")
else:
    print(numero, "es impar")            # -> 7 es impar

print()
print("--- Ejemplo 3: clasificar una nota (intermedio) ---")
nota = 14                                # Paso 1: el dato
if nota >= 18:                           # Paso 2: ¿14 >= 18? False -> se salta
    print("excelente")
elif nota >= 11:                         # Paso 3: ¿14 >= 11? True -> entra aquí
    print("aprobado")
else:                                    # Paso 4: ya entró en uno: el else se salta
    print("desaprobado")

print()
print("--- Ejemplo 4: ¿se puede asignar la línea al lote?, como can_allocate del libro (avanzado) ---")
sku_lote = "SMALL-TABLE"                 # Paso 1: datos del lote
disponible = 20
sku_linea = "SMALL-TABLE"                # Paso 2: datos de la línea de pedido
cantidad = 2
puede = sku_lote == sku_linea and disponible >= cantidad   # Paso 3: las DOS reglas (C1, C4, C8)
print("¿Puede asignar?", puede)          # -> True
if puede:                                # Paso 4: decidir con el booleano (F5)
    disponible = disponible - cantidad
    print("Asignado. Disponible:", disponible)   # -> 18
else:
    print("No se puede asignar")
