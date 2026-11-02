# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/01-variables-y-tipos/paso5_solucionario/nivel_intermedio.py

# Problema 5: f-string con varias variables y una cuenta adentro (T14).
producto = "Silla"
precio = 50
cantidad = 4
print("P5:", f"{producto}: {cantidad} x {precio} = {cantidad * precio}")

# Problema 6: un número no se puede unir con + a un texto: primero str() (T12).
stock = 20
print("P6:", "Stock: " + str(stock))

# Problema 7: horas con // (cuántas veces caben 60) y minutos con % (lo que sobra) (T7, T8).
minutos_totales = 125
horas = minutos_totales // 60
minutos = minutos_totales % 60
print("P7:", horas, "h", minutos, "min")

# Problema 8: texto -> número con int() (T13), y recién ahí se puede sumar.
edad_texto = "30"
edad = int(edad_texto)
print("P8:", edad + 1)
