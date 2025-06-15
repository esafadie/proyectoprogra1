def mostrar_ultimas_compras(archivo):
    with open(archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
    ultimos = lineas[-3:]
    if ultimos == "":
          print()
    else:
        print(f"{'ID Compra':<10}{'ID Producto':<20}{'Cantidad':<20}{'Proveedor':<20}")
        for linea in ultimos:
            idcompra, idproducto, cantidad, proveedor = linea.strip().split(";")
            print(f"{idcompra:10}{idproducto:20}{cantidad:20}{proveedor:20}")