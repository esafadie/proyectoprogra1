import re
import json
def eliminar_por_id(lista, id_buscado, i=0):
    if i >= len(lista):
        return None
    if lista[i]['ID'] == id_buscado:
        return lista.pop(i)
    return eliminar_por_id(lista, id_buscado, i + 1)

def dar_de_baja_productos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as arch:
            productos = json.load(arch)

        if not productos:
            print("No hay productos cargados.")
            return

        id_producto = ('PR' + input("Digite el ID del producto (Formato 001): ").strip())
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = ('PR' + input("ID inválido.Ingrese nuevamente (Formato 001): ").strip())

        eliminado = eliminar_por_id(productos, id_producto)

        with open(archivo, "w", encoding="utf-8") as modificar:
            json.dump(productos, modificar, indent=4)

        if eliminado is not None:
            print(f"\nProducto eliminado:")
            print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
            print(f"{eliminado['ID']:<10}{eliminado['nombre']:<20}{eliminado['proveedor']:<20}{eliminado['stock']:<10}")
            if productos:
                print("-"*60)
                print("\nProductos restantes:")
                print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
                for p in productos:
                    print(f"{p['ID']:<10}{p['nombre']:<20}{p['proveedor']:<20}{p['stock']:<10}")
        else:
            print(f"No se encontró ningún producto con el ID {id_producto}.")


    except FileNotFoundError:
        print("El archivo de productos no existe.")
    except OSError:
        print(f"Error de archivo.")