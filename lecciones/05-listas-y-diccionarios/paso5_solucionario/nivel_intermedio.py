# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/05-listas-y-diccionarios/paso5_solucionario/nivel_intermedio.py

# Problema 5: cambiar un valor existente y agregar uno nuevo: ambos con d[clave] = valor (D5).
precios = {"pan": 1, "leche": 4}
precios["pan"] = 2          # la clave ya existe -> CAMBIA
precios["huevo"] = 6        # la clave no existe -> AGREGA
print("P5:", precios)       # {'pan': 2, 'leche': 4, 'huevo': 6}

# Problema 6: recorrer pares con .items() (D11).
print("P6:")
for producto, precio in precios.items():
    print(producto, "cuesta", precio)

# Problema 7: sumar con un for (sin sum) y sacar el promedio.
notas = [12, 15, 9, 18]
suma = 0                    # el acumulador empieza en 0
for nota in notas:
    suma = suma + nota      # vuelta a vuelta: 12, 27, 36, 54
promedio = suma / len(notas)
print("P7: suma", suma, "| promedio", promedio)   # 54 | 13.5

# Problema 8: preguntar si una CLAVE existe (D6) y decidir con if (Lección 02).
if "queso" not in precios:
    print("P8: no hay queso")
