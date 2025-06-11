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
    except:
        print("No se puede abrir el archivo")
    finally:
        try:
            arch.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
    
