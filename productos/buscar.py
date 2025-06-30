import json
import re
def buscar_producto(archivo):
    try:
        with open(archivo,"r",encoding="utf-8") as archivo:
            productos = json.load(archivo)
        
        if not productos:
            print("No hay productos cargados.")
            return

        id_buscar = ('PR' + input("Ingrese el ID del producto a buscar (formato 001): "))
        while not re.match(r'^PR[0-9]{3}$', id_buscar):
            id_buscar = ('PR' + input("ID inválido. Formato 001: "))

        filtro = list(filter(lambda prod: prod['ID'] == id_buscar, productos))
        
        if not filtro:
            print("Producto no encontrado")
        else:
            prod = filtro[0]
            print()
            print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
            print(f"{prod['ID']:<10}{prod['nombre']:<20}{prod['proveedor']:<20}{prod['stock']:<10}")
            return
        
    except OSError:
        print("No se puede abrir el archivo")
    
