import re

def Registrar_compras(productos):
    Id_cargado = set()

    id_compra = input("ID de la compra (formato CO001): ")
    while not re.match(r'^CO[0-9]{3}$', id_compra) or id_compra in Id_cargado:
        id_compra = input("ID inválido o repetido. Ingrese otro (ej: CO001): ")
    id_producto = input("ID del producto (formato PR001): ")
    while not re.match(r'^PR[0-9]{3}$', id_producto):
        id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")
    cantidad_compra = int(input("Cantidad de productos: "))
    proveedor = input("Proveedor: ")
    # Actualizar stock
    for producto in productos:
        if producto['ID'] == id_producto:
            producto['stock'] += cantidad_compra
            
    Id_cargado.add(id_compra)
    lista_CO = ([(id_compra), id_producto, cantidad_compra, proveedor])

    return lista_CO