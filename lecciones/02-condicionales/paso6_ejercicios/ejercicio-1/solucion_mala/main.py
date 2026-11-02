# Ej1 — MALA (funciona): tres if separados, evalúa todos aunque uno ya acertó.
# Cambia el valor de 'edad' (10, 30, 70) y vuelve a ejecutar.
edad = 30
resultado = ""
if edad < 18:
    resultado = "menor"
if edad >= 18 and edad < 65:
    resultado = "adulto"
if edad >= 65:
    resultado = "adulto mayor"
print(resultado)
