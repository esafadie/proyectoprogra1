def mostrar_ultimos_clientes(archivo):
    try:
        lineas = []

        with open(archivo, "r", encoding="UTF-8") as file:
            linea = file.readline()
            while linea:
                lineas.append(linea.strip())
                linea = file.readline()

        ultimos = lineas[-3:]  

        if not ultimos:
            print("No hay clientes cargados.")
        else:
            print(f"{'ID':<10}{'Nombre':<20}{'Telefono':<20}")
            for linea in ultimos:
                idcliente, nombre, telefono = linea.split(";")
                print(f"{idcliente:<10}{nombre:<20}{telefono:<20}")

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception:
        print("Error al mostrar clientes:")
