import re

def cargar_productos():
    lista_PR = []
    Id_cargado = set()
    cantidad = int(input("Ingrese la cantidad de productos a cargar: "))

    for _ in range(cantidad):
        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto) or id_producto in Id_cargado: 
            id_producto = input("ID inválido o repetido. Ingrese otro (ej: PR001): ")

        nombre = input("Nombre del producto: ")
        proveedor = input("Proveedor: ")
        stock = int(input("Stock del producto: "))

        encabezados = ['ID','nombre','proveedor','stock']
        matriz = [id_producto, nombre, proveedor, stock]
        Id_cargado.add(id_producto)
        lista_PR.append(dict(zip(encabezados,matriz)))

    return lista_PR