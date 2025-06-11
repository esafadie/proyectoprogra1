def mostrar_ultimas_ventas(archivo):
    with open(archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
    ultimos = lineas[-3:]
    for linea in ultimos:
        idventa, idcliente, idproducto, cantidad = linea.strip().split(";")
        print(f"ID VENTA: {idventa}, ID CLIENTE: {idcliente}, ID PRODUCTO: {idproducto}, CANTIDAD: {cantidad}")