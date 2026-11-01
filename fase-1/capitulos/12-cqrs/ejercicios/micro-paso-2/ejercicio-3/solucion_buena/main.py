# BUENA: una sola consulta a la tabla de lectura. SELECT * FROM tabla WHERE clave=valor.
def query(sql):
    print("  SQL:", sql)
    return [{"sku": "MESA", "ref": "l1"}, {"sku": "SILLA", "ref": "l2"}]
filas = query("SELECT sku, ref FROM asignaciones_vista WHERE pedido='p1'")
print("buena -> consultas: 1 | filas:", filas)
