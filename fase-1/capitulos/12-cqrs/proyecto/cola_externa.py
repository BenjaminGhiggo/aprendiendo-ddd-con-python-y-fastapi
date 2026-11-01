# cola_externa.py — ADAPTADOR EXTERNO (simula Redis pub/sub con un broker en memoria).
# En producción, publicar() haría redis.publish() y el consumidor haría redis.subscribe().
mensajes_publicados = []     # lo que se envió a otros servicios (para los tests)


def publicar(canal, datos):
    mensajes_publicados.append((canal, datos))


def limpiar():
    mensajes_publicados.clear()
