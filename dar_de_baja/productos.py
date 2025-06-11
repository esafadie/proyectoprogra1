import re
import json
def eliminar_por_id(lista, id_buscado, i=0):
    if i >= len(lista):
        return lista
    if lista[i]['ID'] == id_buscado:
        lista.pop(i)
        return lista
    return eliminar_por_id(lista, id_buscado, i + 1)

def dar_de_baja_productos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as arch:
            productos = json.load(arch)

        if not productos:
            print("No hay productos cargados")
            return

        id_producto = input("Digite el ID del producto. Debe tener el formato PR seguido de tres números (ej: PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")

        productos_actualizados = eliminar_por_id(productos, id_producto)

        with open(archivo, "w", encoding="utf-8") as modificar:
            json.dump(productos_actualizados, modificar)

        print(f"Producto con ID {id_producto} eliminado (si existia).")
    except:
        print("No se puede abrir el archivo")
    finally:
        try:
            arch.close()
        except Exception as e:
            print(f"No se puede abrie el archivo correctamente: {e}")
    