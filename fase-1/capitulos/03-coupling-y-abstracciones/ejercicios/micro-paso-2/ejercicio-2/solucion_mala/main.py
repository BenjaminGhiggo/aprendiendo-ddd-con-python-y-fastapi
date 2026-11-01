# Ej2 — MALA: para probar la lógica, hay que montar datos reales y mirar efectos.
import os, tempfile
d = tempfile.mkdtemp()
open(os.path.join(d, "sobra.txt"), "w").close()
# "test": listar y comprobar... mucho andamiaje para una regla simple
print("archivos:", os.listdir(d))
