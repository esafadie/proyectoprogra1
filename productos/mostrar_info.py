import json

def mostrar_nombres_productos(archivo):
   try:
        arch = open(archivo,"r")
        productos = json.load(arch)
        if not productos:
            print("No hay productos cargados")
            return
        print("Nombres de productos cargados:")
        for nombre in productos:
            print(f"ID: {nombre['ID']} | Nombre: {nombre['nombre']} | Proveedor: {nombre['proveedor']} | Stock: {nombre['stock']}")
   except:
        print("No se puede abrir el archivo")
   finally:
        try:
            arch.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
    
