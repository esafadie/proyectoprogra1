import re
import json

Id_cargado = set()


def registrar_compra(arch_compras,arch_productos):
    try:
        arch = open(arch_compras,"a",encoding="UTF-8")
        id_compra = input("ID de la compra (formato CO001): ")
        while not re.match(r'^CO[0-9]{3}$', id_compra) or id_compra in Id_cargado:
            id_compra = input("ID inválido o repetido. Ingrese otro (ej: CO001): ")
        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")
        cantidad_compra = int(input("Cantidad de productos: "))
        proveedor = input("Proveedor: ")

        info_productos = open(arch_productos,"r")
        productos = json.load(info_productos)

        producto_encontrado = False
        for producto in productos:
            if producto['ID'] == id_producto:
                producto['stock'] += cantidad_compra
                producto_encontrado = True
        if producto_encontrado == False:
            print("Producto no encontrado")
        else:
            arch.write(id_compra + ";" + id_producto + ";" + str(cantidad_compra) + ";" + proveedor + "\n")

        with open(arch_productos, "w", encoding="utf-8") as modificar:
            json.dump(productos,modificar)
            info_productos.write(id_compra + ";" + id_producto + ";" + str(cantidad_compra) + ";" + proveedor + "\n")

    except OSError as mensaje:
        print("")
    finally:
        try:
            arch.close()
        except NameError:
            pass

    Id_cargado.add(id_compra)