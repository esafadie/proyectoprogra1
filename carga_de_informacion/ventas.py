import re 
id_cargado = set()

def cargar_ventas(archivo,productos):
    try:
        arch = open(archivo,"a",encoding="UTF-8")
        id_venta = input("ID de la venta (formato VE001): ")
        while not re.match(r'^VE[0-9]{3}$', id_venta) or id_venta in id_cargado:
            id_venta = input("ID inválido o repetido. Ingrese otro (ej: VE001): ")
        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente):
            id_cliente = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ")
        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")
        cantidad_venta = int(input("Cantidad vendida: "))
        # Descontar stock
        for producto in productos:
            if producto['ID'] == id_producto:
                if producto['stock'] >= cantidad_venta:
                    producto['stock'] -= cantidad_venta
                else:
                    print(f"Stock insuficiente para el producto {id_producto}. Solo hay {producto['stock']} unidades.")
        arch.write(id_venta + ";" + id_cliente + ";" + id_producto + ";" + str(cantidad_venta) + "\n")
    except OSError as mensaje:
        print("No se puede grabar el archivo:",mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    id_cargado.add(id_venta)
