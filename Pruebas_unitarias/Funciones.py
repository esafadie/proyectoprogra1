import re
ids_cargados = set()  #
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
        arch.write(id_cliente + ";" + nombre + ";" + telefono +"\n")
        ids_cargados.add(id_cliente)
    except OSError as mensaje:
        print("No se puede grabar el archivo:",mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

def dar_de_baja_clientes(archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        lineas = arch.readlines()
        arch.close()

        id_borrar = input("Digite el ID a eliminar (ej: CL002): ").strip()
        nuevas_lineas = []

        for linea in lineas:
            id, nombre, telefono = linea.strip().split(";")
            if id != id_borrar:
                nuevas_lineas.append(linea)
            else:
                print(f"Cliente eliminado: {linea.strip()}")

    
        arch = open(archivo, "w", encoding="UTF-8")
        arch.writelines(nuevas_lineas)
        arch.close()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Error al procesar el archivo:", e)
