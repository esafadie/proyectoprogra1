import re

def cargar_cliente(id_cliente, nombre, telefono, archivo, ids_cargados):
    if not re.match(r'^CL[0-9]{3}$', id_cliente):
        return "ID inválido"
    if id_cliente in ids_cargados:
        return "ID repetido"
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{id_cliente};{nombre};{telefono}\n")
        ids_cargados.add(id_cliente)
    return "Cliente cargado"

def dar_de_baja_cliente(id_borrar, archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        nuevas = []
        encontrado = False
        for l in lineas:
            if l.startswith(id_borrar + ";"):
                encontrado = True
                continue
            nuevas.append(l)
        with open(archivo, "w", encoding="utf-8") as f:
            f.writelines(nuevas)
        return "Cliente eliminado" if encontrado else "No encontrado"
    except FileNotFoundError:
        return "Archivo no encontrado"