def mostrar_ultimos_clientes(archivo):
    with open(archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
    ultimos = lineas[-3:]
    for linea in ultimos:
        id, nombre, telefono = linea.strip().split(";")
        print(f"ID: {id} Nombre: {nombre} Telefono: {telefono}")
