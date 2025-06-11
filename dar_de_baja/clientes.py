import re

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
