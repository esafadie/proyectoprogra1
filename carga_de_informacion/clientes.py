import re
ids_cargados = set()  # Creamos un conjunto vacío


def cargar_clientes(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if partes:
                    ids_cargados.add(partes[0])

    try:
        arch = open(archivo,"a",encoding="UTF-8")
        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente) or id_cliente in ids_cargados:
            id_cliente = input("ID inválido o repetido. Ingrese otro (ej: CL001): ")
        nombre = input("Nombre del cliente: ")
        telefono = input("Teléfono: ")
        arch.write(id_cliente + ";" + nombre + ";" + telefono+"\n")
        ids_cargados.add(id_cliente)
    except OSError as mensaje:
        print("No se puede grabar el archivo:",mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass