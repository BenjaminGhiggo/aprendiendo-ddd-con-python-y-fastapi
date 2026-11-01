# MALA: "preparamos" el handler con late binding en un bucle -> todos capturan el ULTIMO valor.
def asignar(cmd, uow): return f"{cmd}->{uow}"
preparados = []
for u in ["UoW-A", "UoW-B"]:
    preparados.append(lambda cmd: asignar(cmd, u))   # 'u' se lee al llamar, no al crear
print([p("x") for p in preparados])   # ambos usan UoW-B (bug clasico de late binding)
