def mostrar_ultimas_ventas(archivo):
    with open(archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
    ultimos = lineas[-3:]
    print(f"{'ID Venta':<20}{'ID Cliente':<20}{'ID Producto':<20}{'Cantidad':<20}")
    for linea in ultimos:
        idventa, idcliente, idproducto, cantidad = linea.strip().split(";")
        print(f"{idventa:20}{idcliente:20}{idproducto:20}{cantidad:20}")