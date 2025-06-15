import json

def ordenar_productos_por_stock(archivo):
    try:
        arch = open(archivo,"r")
        productos = json.load(arch)
        if not productos:
            print("No hay productos cargados")
            return
        ordenados = sorted(productos, key=lambda x: int(x['stock']), reverse=True)  # Uso de lambda
        with open(archivo, "w", encoding="utf-8") as modificar:
            json.dump(ordenados, modificar)
        print("Productos ordenados por stock (descendente):")
        print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
        def mostrar_productos(productos, indice=0): #recursividad
            if indice >= len(productos):
                return #caso base: Cuando el índice alcanza el largo de la lista, se detiene la recursión
            p = productos[indice]
            print(f"{p['ID']:<10}{p['nombre']:<20}{p['proveedor']:<20}{p['stock']:<10}")
            mostrar_productos(productos, indice + 1) #Caso recursivo: La función se llama a sí misma avanzando al siguiente índice.
        mostrar_productos(productos)
    except:
        print("No se puede abrir el archivo")
    finally:
        try:
            arch.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
    
