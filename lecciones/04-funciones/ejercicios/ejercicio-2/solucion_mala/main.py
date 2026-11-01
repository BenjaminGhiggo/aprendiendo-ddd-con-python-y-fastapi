# Ej2 — MALA (funciona): la función imprime adentro; no se puede reutilizar su valor.
def total_con_igv(precio):
    print(precio * 1.18)   # solo imprime; no devuelve nada aprovechable

total_con_igv(100)
# Si quisiera SUMAR dos totales, no puedo: la función no devuelve el número.
