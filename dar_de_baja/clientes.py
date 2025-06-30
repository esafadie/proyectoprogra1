import re

def dar_de_baja_clientes(archivo):
    try:
        nuevas_lineas = []

        with open(archivo, "r", encoding="UTF-8") as arch:
            linea = arch.readline()
            while linea:
                id_cliente, nombre, telefono = linea.strip().split(";")
                nuevas_lineas.append((id_cliente, linea))  
                linea = arch.readline()

        id_borrar = ('CL' + input("Digite el ID a eliminar (Formato 002): ").strip())
        eliminado = False

        with open(archivo, "w", encoding="UTF-8") as arch:
            for id_cliente, linea in nuevas_lineas:
                if id_cliente != id_borrar:
                    arch.write(linea)
                else:
                    print(f"Cliente eliminado: {linea.strip()}")
                    eliminado = True

        if not eliminado:
            print("No se encontró un cliente con ese ID.")

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception:
        print("Error al procesar el archivo.")
