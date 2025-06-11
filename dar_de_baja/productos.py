import re
import json
def dar_de_baja_productos(archivo):
    try:
        arch = open(archivo,"r")
        productos = json.load(arch)
        if not productos:
            print("No hay productos cargados")
            return
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
                with open(archivo, "w", encoding="utf-8") as modificar:
                    json.dump(productos, modificar)
    except:
        print("No se puede abrir el archivo")
    finally:
        try:
            arch.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
    