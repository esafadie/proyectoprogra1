import json
def buscar_producto(archivo):
    try:
        archivo = open(archivo,"r")
        productos = json.load(archivo)
        if not productos:
            print("No hay productos cargados.")
            return
        id_buscar = input("Ingrese el ID del producto a buscar (formato PR001): ")
        filtro = list(filter(lambda prod: prod['ID'] == id_buscar, productos))
        if not filtro:
            print("Producto no encontrado")
        else:
            prod = filtro[0]
            print(f"ID: {prod['ID']}, Nombre: {prod['nombre']}, Proveedor: {prod['proveedor']}, Stock: {prod['stock']}")
            return
    except:
        print("No se puede abrir el archivo")
    finally:
        try:
            archivo.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
