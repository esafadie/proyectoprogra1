def mostrar_ultimas_ventas(archivo):
    lineas = []
    try:
        with open(archivo, "r", encoding="UTF-8") as archivo:
            linea = archivo.readline()
            while linea:
                lineas.append(linea.strip())
                linea = archivo.readline()
                
        ultimos = lineas[-3:]
        
        if not ultimos:
            print("\nOperación de venta cancelada.")
            print("ERROR:No hay ventas cargadas")

        else:
            print(f"{'ID Venta':<20}{'ID Cliente':<20}{'Nombre Cliente':<20}{'ID Producto':<20}{'Nombre Producto':<20}{'Cantidad':<20}")
            for linea in ultimos:
                try:
                    idventa, idcliente, nombre_cliente, idproducto, nombre_producto, cantidad = linea.strip().split(";")
                    print(f"{idventa:20}{idcliente:20}{nombre_cliente:20}{idproducto:20}{nombre_producto:20}{cantidad:20}")
                except ValueError:
                    print(f"Línea con formato inválido: {linea}")
    except OSError:
        print("No se pudo abrir el archivo de ventas.")
