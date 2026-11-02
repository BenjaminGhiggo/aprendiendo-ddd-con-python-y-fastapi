# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/02-condicionales/paso5_solucionario/nivel_intermedio.py

# Problema 5: tres caminos con if/elif/else (F3).
numero = -4
if numero > 0:
    print("P5: positivo")
elif numero < 0:
    print("P5: negativo")
else:
    print("P5: cero")

# Problema 6: si se cumple la condición, se cambia el total; si no, queda igual.
monto = 150
total = monto
if monto >= 100:
    total = monto - monto * 10 / 100
print("P6:", total)

# Problema 7: rangos en orden; el primero que sea True gana (F3, P4).
edad = 70
if edad < 18:
    print("P7: menor")
elif edad <= 64:
    print("P7: adulto")
else:
    print("P7: adulto mayor")

# Problema 8: basta que se cumpla UNA de las dos -> or (C9).
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("P8: Fin de semana")
else:
    print("P8: Día laboral")
