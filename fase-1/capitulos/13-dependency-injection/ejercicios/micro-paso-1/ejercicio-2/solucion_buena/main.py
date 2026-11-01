# BUENA: un bootstrap arma las deps UNA vez y devuelve algo listo para usar.
def handler(cmd, uow): return f"{cmd} con {uow}"
def bootstrap(uow="UoW()"):
    return lambda cmd: handler(cmd, uow)   # dep ya inyectada
usar = bootstrap()
print("web:", usar("asignar"))
print("consumidor:", usar("asignar"))     # sin repetir el armado
