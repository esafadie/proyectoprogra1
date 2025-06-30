def mostrar_ultimas_compras(archivo):
    lineas = []
    try:
        with open(archivo, "r", encoding="UTF-8") as archivo:
            linea = archivo.readline()
            while linea:
                lineas.append(linea.strip())
                linea = archivo.readline()
                
        ultimos = lineas[-3:]
        
        if not ultimos:
            print("\nOperación de compra cancelada.")
            print("ERROR:No hay compras cargadas")
            
        else:
            print(f"{'ID Compra':<20}{'ID Producto':<20}{'Producto':<20}{'Cantidad':<20}{'Proveedor':<20}")
            for linea in ultimos:
                try:
                    idcompra, idproducto, nombre_producto, cantidad, proveedor = linea.strip().split(";")
                    print(f"{idcompra:20}{idproducto:20}{nombre_producto:20}{cantidad:20}{proveedor:20}")
                except ValueError:
                    print(f"Línea con formato inválido: {linea}")
    except OSError:
        print("No se pudo abrir el archivo de compras.")
    