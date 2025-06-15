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
            print()
            print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
            print(f"{prod['ID']:<10}{prod['nombre']:<20}{prod['proveedor']:<20}{prod['stock']:<10}")
            return
    except:
        print("No se puede abrir el archivo")
    finally:
        try:
            archivo.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
