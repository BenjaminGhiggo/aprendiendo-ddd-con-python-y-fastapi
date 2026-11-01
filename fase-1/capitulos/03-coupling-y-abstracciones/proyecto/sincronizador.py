# sincronizador.py — ejemplo del Cap. 3 (interludio sobre abstracciones).
# Núcleo FUNCIONAL (sin I/O): decide QUÉ hacer a partir de dos diccionarios
# {hash -> nombre_archivo}. No toca el disco, así que es trivial de probar.
from pathlib import Path


def determinar_acciones(hashes_origen, hashes_destino, carpeta_origen, carpeta_destino):
    for h, nombre in hashes_origen.items():
        if h not in hashes_destino:
            # está en origen y no en destino -> copiar
            yield "COPIAR", Path(carpeta_origen) / nombre, Path(carpeta_destino) / nombre
        elif hashes_destino[h] != nombre:
            # mismo contenido, distinto nombre -> renombrar (mover) en destino
            yield "MOVER", Path(carpeta_destino) / hashes_destino[h], Path(carpeta_destino) / nombre

    for h, nombre in hashes_destino.items():
        if h not in hashes_origen:
            # está en destino y no en origen -> borrar
            yield "BORRAR", Path(carpeta_destino) / nombre


# --- Cáscara IMPERATIVA (todo el I/O vive aquí) ---
import hashlib
import os
import shutil

BLOQUE = 65536


def hash_archivo(ruta):
    hasher = hashlib.sha1()
    with open(ruta, "rb") as f:
        buf = f.read(BLOQUE)
        while buf:
            hasher.update(buf)
            buf = f.read(BLOQUE)
    return hasher.hexdigest()


def leer_rutas_y_hashes(carpeta):
    hashes = {}
    for carpeta_actual, _, archivos in os.walk(carpeta):
        for nombre in archivos:
            hashes[hash_archivo(Path(carpeta_actual) / nombre)] = nombre
    return hashes


def sincronizar(origen, destino):
    # 1. reunir entradas (I/O)
    hashes_origen = leer_rutas_y_hashes(origen)
    hashes_destino = leer_rutas_y_hashes(destino)
    # 2. llamar al núcleo funcional (sin I/O)
    acciones = determinar_acciones(hashes_origen, hashes_destino, origen, destino)
    # 3. aplicar salidas (I/O)
    for accion, *rutas in acciones:
        if accion == "COPIAR":
            shutil.copyfile(*rutas)
        elif accion == "MOVER":
            shutil.move(*rutas)
        elif accion == "BORRAR":
            os.remove(rutas[0])
