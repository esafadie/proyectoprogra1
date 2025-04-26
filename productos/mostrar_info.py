def mostrar_nombres_productos(productos):
    if not productos:
        print("No hay productos cargados.")
        return
    print("Nombres de productos cargados:")
    for nombre in productos:
        print(f"ID: {nombre['ID']} | Nombre: {nombre['nombre']} | Proveedor: {nombre['proveedor']} | Stock: {nombre['stock']}")