# MALA: cada entrypoint (web, consumidor, test) arma la UoW y pasa todo: duplicado.
def handler(cmd, uow): return f"{cmd} con {uow}"
# entrypoint web
uow_web = "UoW()"; print("web:", handler("asignar", uow_web))
# entrypoint consumidor (repite el armado)
uow_cons = "UoW()"; print("consumidor:", handler("asignar", uow_cons))
