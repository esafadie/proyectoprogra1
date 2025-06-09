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


import re
import os

ids_cargados = set()

# Cargar IDs existentes desde el archivo
if os.path.exists("cliente_cargado.txt"):
    with open("cliente_cargado.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo.readlines()[2:]:  # Saltamos encabezado y línea de separación
            partes = linea.strip().split(maxsplit=1)
            if partes:
                ids_cargados.add(partes[0])

def cargar_clientes():
    id_cliente = input("ID del cliente (formato CL001): ")
    while not re.match(r'^CL[0-9]{3}$', id_cliente) or id_cliente in ids_cargados:
        id_cliente = input("ID inválido o repetido. Ingrese otro (ej: CL001): ")
    nombre = input("Nombre del cliente: ")
    telefono = input("Teléfono: ")
    Lista_CL = [id_cliente, nombre, telefono]
    return Lista_CL

def guardar_cliente_en_txt(cliente):
    try:
        # Si el archivo no existe, escribimos encabezado
        if not os.path.exists("cliente_cargado.txt"):
            with open("cliente_cargado.txt", "w", encoding="utf-8") as archivo:
                archivo.write(f"{'ID':<8} {'Nombre':<25} {'Teléfono':<15}\n")
                archivo.write("-" * 50 + "\n")
        
        # Agregamos el nuevo cliente
        with open("cliente_cargado.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{cliente[0]:<8} {cliente[1]:<25} {cliente[2]:<15}\n")
        
        print("Cliente guardado correctamente.")
        ids_cargados.add(cliente[0])
    except Exception as e:
        print("Error al guardar el cliente:", e)

# Ejemplo de uso:
cliente_nuevo = cargar_clientes()
guardar_cliente_en_txt(cliente_nuevo)
