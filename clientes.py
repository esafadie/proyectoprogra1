import re

def cargar_clientes():
    lista_CL = []
    cantidad = int(input("Ingrese la cantidad de clientes a cargar: "))

    for _ in range(cantidad):
        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente) or any(c[0] == id_cliente for c in lista_CL):
            id_cliente = input("ID inválido o repetido. Ingrese otro (ej: CL001): ")

        nombre = input("Nombre del cliente: ")
        telefono = input("Teléfono: ")

        lista_CL.append([id_cliente, nombre, telefono])
    return lista_CL