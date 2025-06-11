def mostrar_ultimas_compras(archivo):
    with open(archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
    ultimos = lineas[-3:]
    for linea in ultimos:
        idcompra, idproducto, cantidad, proveedor = linea.strip().split(";")
        print(f"ID Compra: {idcompra} ID producto: {idproducto} cantidad: {cantidad} Proveedor: {proveedor}")