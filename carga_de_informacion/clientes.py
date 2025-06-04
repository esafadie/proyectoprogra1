import re
ids_cargados = set()  # Creamos un conjunto vacío


def cargar_clientes():

    id_cliente = input("ID del cliente (formato CL001): ")
    while not re.match(r'^CL[0-9]{3}$', id_cliente) or id_cliente in ids_cargados:
        id_cliente = input("ID inválido o repetido. Ingrese otro (ej: CL001): ")
    nombre = input("Nombre del cliente: ")
    telefono = input("Teléfono: ")
    Lista_CL = ([id_cliente, nombre, telefono])
    return Lista_CL
