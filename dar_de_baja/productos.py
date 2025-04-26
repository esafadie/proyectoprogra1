import re
def dar_de_baja_productos(productos):
        if not productos:
            print("No hay productos cargados")
            return
        id_producto = input("Digite el ID del producto. Debe tener el formato PR seguido de tres números (ej: PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")
        for i in productos:
            if i['ID'] == id_producto:
                productos.remove(i)
                print("Producto eliminado exitosamente")