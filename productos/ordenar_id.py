import json

def ordenar_productos_por_id(archivo):
    try:
        arch = open(archivo, "r", encoding="utf-8")
        productos = json.load(arch)

        if not productos:
            print("No hay productos cargados")
            return

        # Ordena los productos por ID numérico (extrae el número de 'PR001' → 1)
        ordenados = sorted(productos, key=lambda x: int(x['ID'][2:]))

        # Guarda los productos ordenados nuevamente en el archivo
        with open(archivo, "w", encoding="utf-8") as modificar:
            json.dump(ordenados, modificar, indent=4)

        # Muestra los productos con formato
        print("Productos ordenados por ID:")
        print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")

        # ▶ Función recursiva para mostrar productos uno a uno
        def mostrar_productos(ordenados, indice=0):
            if indice >= len(ordenados):
                return  # ⛔ Caso base: termina cuando ya no hay más productos
            p = ordenados[indice]
            print(f"{p['ID']:<10}{p['nombre']:<20}{p['proveedor']:<20}{p['stock']:<10}")
            mostrar_productos(ordenados, indice + 1)  # 🔁 Caso recursivo: pasa al siguiente producto

        mostrar_productos(ordenados)

    except Exception as e:
        print("No se puede abrir el archivo:", e)

    finally:
        try:
            arch.close()
        except Exception as e:
            print(f"No se puede cerrar el archivo correctamente: {e}")
