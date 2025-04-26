import re

def cargar_productos():
    lista_PR = []
    cantidad = int(input("Ingrese la cantidad de productos a cargar: "))

    for _ in range(cantidad):
        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto) or any(p['ID'] == id_producto for p in lista_PR):
            id_producto = input("ID inválido o repetido. Ingrese otro (ej: PR001): ")

        nombre = input("Nombre del producto: ")
        proveedor = input("Proveedor: ")
        stock = int(input("Stock del producto: "))

        encabezados = ['ID','nombre','proveedor','stock']
        matriz = [(id_producto), nombre, proveedor, stock]
        lista_PR.append(dict(zip(encabezados,matriz)))

    return lista_PR