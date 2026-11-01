# BUENA: un evento permite VARIOS handlers (sumar reacciones).
MANEJADORES = {"Asignado": [lambda e: print("registrar"), lambda e: print("notificar")]}
for m in MANEJADORES["Asignado"]: m("Asignado")
