import re

def cargar_clientes():
    lista_CL = []
    ids_cargados = set()  # Creamos un conjunto vacío
    cantidad = int(input("Ingrese la cantidad de clientes a cargar: "))

    for _ in range(cantidad):
        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente) or id_cliente in ids_cargados:
            id_cliente = input("ID inválido o repetido. Ingrese otro (ej: CL001): ")

        nombre = input("Nombre del cliente: ")
        telefono = input("Teléfono: ")

        lista_CL.append([id_cliente, nombre, telefono])
        ids_cargados.add(id_cliente)  # Agregamos el ID al conjunto
    return lista_CL
