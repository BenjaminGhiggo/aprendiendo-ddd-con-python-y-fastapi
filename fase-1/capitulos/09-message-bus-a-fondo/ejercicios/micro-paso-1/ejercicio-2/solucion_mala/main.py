# MALA: el bus procesa UN solo mensaje; ignora eventos nuevos.
def manejar(evento):
    print("manejar", evento)     # no recoge eventos que surjan despues
manejar("asignacion")
