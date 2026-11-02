# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 10.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/10-herencia/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: una hija que hereda todo (fácil) ---")


class Lote:                                       # Paso 1: la clase padre
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad

    def descripcion(self):
        return f"Lote {self.referencia} con {self.cantidad} unidades"

    def etiqueta(self):
        return "NORMAL"


class LoteSimple(Lote):                           # Paso 2: la hija, con el padre entre ()
    pass                                          # Paso 3: no escribe nada propio


simple = LoteSimple("L0", 3)                      # Paso 4: usa el __init__ del padre
print(simple.descripcion())                       # Paso 5: y su método -> Lote L0 con 3 unidades

print()
print("--- Ejemplo 2: reutilizar el constructor y agregar un dato (fácil) ---")


class LoteRefrigerado(Lote):
    def __init__(self, referencia, cantidad, temperatura):
        super().__init__(referencia, cantidad)    # Paso 1: el padre guarda referencia y cantidad
        self.temperatura = temperatura            # Paso 2: la hija guarda lo nuevo

    def etiqueta(self):                           # (lo usa el Ejemplo 3)
        return "FRÍO"

    def descripcion(self):                        # (lo usa el Ejemplo 3)
        return super().descripcion() + f" (a {self.temperatura}°C)"


frio = LoteRefrigerado("L2", 5, -18)
print(frio.referencia, frio.cantidad, frio.temperatura)   # Paso 3: -> L2 5 -18

print()
print("--- Ejemplo 3: sobrescribir vs extender (intermedio) ---")
normal = Lote("L1", 10)
print(normal.etiqueta(), "|", frio.etiqueta())            # sobrescribir: NORMAL | FRÍO
print(normal.descripcion())                               # Lote L1 con 10 unidades
print(frio.descripcion())                                 # extender: ... (a -18°C)

print()
print("--- Ejemplo 4: una lista mixta y isinstance (avanzado) ---")
lotes = [Lote("L1", 10), LoteRefrigerado("L2", 5, -18), LoteRefrigerado("L3", 7, 4)]  # Paso 1
refrigerados = 0                                          # Paso 2: contador
for lote in lotes:                                        # Paso 3: recorrer
    print(lote.descripcion())                             # Paso 4: cada uno usa SU versión
    if isinstance(lote, LoteRefrigerado):                 # Paso 5: ¿es refrigerado?
        refrigerados = refrigerados + 1
print("refrigerados:", refrigerados)                      # -> 2
print("¿todos son Lote?", isinstance(lotes[1], Lote))     # -> True (la hija ES un Lote)
