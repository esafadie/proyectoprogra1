import json
def mostrar_ultimos_productos(archivo):
    try:
        with open(archivo,"r", encoding="utf-8") as arch:
            productos = json.load(arch)
        if not productos:
            print("No hay productos cargados.")
            return
        ultimos = productos[-3:]  # Slicing para obtener los últimos 3
        print("Últimos productos cargados:")
        for p in ultimos:
            print(f"ID: {p['ID']}, Nombre: {p['nombre']}, Stock: {p['stock']}")
    except OSError:
        print("No se puede abrir el archivo")
    
    
    
