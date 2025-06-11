import json
def mostrar_ultimos_productos(archivo):
    try:
        arch = open(archivo,"r")
        productos = json.load(arch)
        if not productos:
            print("No hay productos cargados.")
            return
        ultimos = productos[-3:]  # Slicing para obtener los últimos 3
        print("Últimos productos cargados:")
        for p in ultimos:
            print(f"ID: {p['ID']}, Nombre: {p['nombre']}, Stock: {p['stock']}")
    except:
        print("No se puede abrir el archivo")
    finally:
        try:
            arch.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
    
