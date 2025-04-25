import re

def modificar_producto(productos):
    if not productos:
        print("No hay productos cargados.")
        return
    id_producto = input("ID del producto a modificar (formato PR001): ")
    while not re.match(r'^PR[0-9]{3}$', id_producto):
        id_producto = input("ID inválido o repetido. Ingrese otro (ej: PR001): ")
    
    for prod in productos:
        if prod['ID'] == id_producto:
            nombre_nuevo = input("Nuevo nombre del producto: ")
            proveedor_nuevo = input("Proveedor del producto: ")
            stock_nuevo = int(input("Stock actual del producto: "))

            prod['nombre'] = nombre_nuevo
            prod['proveedor'] = proveedor_nuevo
            prod['stock'] = stock_nuevo
            print("Producto modificado exitosamente")
        else:
            print("Producto no encontrado")