import re
import json

def modificar_producto(archivo):
    try:
        arch = open(archivo,"r")
        productos = json.load(arch)
        if not productos:
            print("No hay productos cargados.")
            return
        id_producto = input("ID del producto a modificar (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido o repetido. Ingrese otro (ej: PR001): ")

        producto_encontrado = False

        for prod in productos:
            if prod['ID'] == id_producto:
                nombre_nuevo = input("Nuevo nombre del producto: ")
                proveedor_nuevo = input("Proveedor del producto: ")
                stock_nuevo = int(input("Stock actual del producto: "))

                prod['nombre'] = nombre_nuevo
                prod['proveedor'] = proveedor_nuevo
                prod['stock'] = stock_nuevo
                producto_encontrado = True
        if producto_encontrado == True:
            print("Producto modificado exitosamente")
        else:
            print("No se pudo encontrar el producto deseado")

        
        with open(archivo, "w", encoding="utf-8") as modificar:
            json.dump(productos, modificar)
    except:
        print("No se puede abrir el archivo")
    finally:
        try:
            arch.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
    