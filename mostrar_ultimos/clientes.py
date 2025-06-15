def mostrar_ultimos_clientes(archivo):
    with open(archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
    ultimos = lineas[-3:]
    if ultimos == "":
          print()
    else:
        print(f"{'ID':<10}{'Nombre':<20}{'Telefono':<20}")
        for linea in ultimos:
            idcliente,nombre,telefono = linea.strip().split(";")
            print(f"{idcliente:<10}{nombre:<20}{telefono:<20}")