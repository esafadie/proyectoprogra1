import re 

def cargar_ventas(productos):
    lista_VE = []
    cantidad = int(input("Ingrese la cantidad de ventas a registrar: "))

    for _ in range(cantidad):
        id_venta = input("ID de la venta (formato VE001): ")
        while not re.match(r'^VE[0-9]{3}$', id_venta) or any(v[0] == id_venta for v in lista_VE):
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
                if producto['STOCK'] >= cantidad_venta:
                    producto['STOCK'] -= cantidad_venta
                else:
                    print(f"Stock insuficiente para el producto {id_producto}. Solo hay {producto[3]} unidades.")
                break

        lista_VE.append([(id_venta), id_cliente, id_producto, cantidad_venta])
    return lista_VE