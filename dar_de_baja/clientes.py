import re
import os

def cargar_ids_desde_archivo(): # cargar el conjunto de IDs si querés validar IDs únicos en otras partes.
    ids_cargados = set()
    if os.path.exists("cliente_cargado.txt"):
        try:
            with open("cliente_cargado.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                for linea in lineas[2:]:  # saltar encabezado y separador
                    partes = linea.strip().split(maxsplit=1)
                    if partes:
                        ids_cargados.add(partes[0])
        except Exception as e:
            print("Error al leer archivo existente:", e)
    return ids_cargados

def guardar_todos_los_clientes(clientes):
    try:
        with open("cliente_cargado.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"{'ID':<8} {'Nombre':<25} {'Teléfono':<15}\n")
            archivo.write("-" * 50 + "\n")
            for cliente in clientes:
                archivo.write(f"{cliente[0]:<8} {cliente[1]:<25} {cliente[2]:<15}\n")
    except Exception as e:
        print("Error al guardar los clientes:", e)

def dar_de_baja_clientes(clientes):
    if not clientes:
        print("No hay clientes cargados")
        return

    id_cliente = input("Digite el ID del cliente (formato CL001): ").strip()
    while not re.match(r'^CL[0-9]{3}$', id_cliente):
        id_cliente = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ").strip()

    # Buscar el cliente para eliminar
    i = 0
    encontrado = False
    while i < len(clientes):
        if clientes[i][0] == id_cliente:
            encontrado = True
            confirmacion = input(f"¿Está seguro que desea eliminar al cliente {clientes[i][1]} (ID: {id_cliente})? (s/n): ").lower()
            if confirmacion == 's':
                clientes.pop(i)
                print(f"Cliente {id_cliente} eliminado correctamente.")
                guardar_todos_los_clientes(clientes)
            else:
                print("Operación cancelada.")
            break
        i += 1

    if not encontrado:
        print(f"No se encontró el cliente con ID {id_cliente}.")