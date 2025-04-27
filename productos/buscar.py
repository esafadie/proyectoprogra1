def buscar_producto(productos):
    if not productos:
        print("No hay productos cargados.")
        return
    id_buscar = input("Ingrese el ID del producto a buscar (formato PR001): ")
    filtro = list(filter(lambda prod: prod['ID'] == id_buscar, productos))
    prod = filtro[0]
    if not filtro:
        print("Producto no encontrado")
    else:
        print(f"ID: {prod['ID']}, Nombre: {prod['nombre']}, Proveedor: {prod['proveedor']}, Stock: {prod['stock']}")
        return