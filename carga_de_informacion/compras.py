import re
import json

def generar_id_compra(arch_compras):
    max_Id = 0
    try:
        with open(arch_compras, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if partes and re.match(r"CO\d{3}$", partes[0]):
                    num = int(partes[0][2:])  # Obtener el número después de CO
                    if num > max_Id:
                        max_Id = num
    except FileNotFoundError:
        pass  # Si el archivo no existe aún, arrancamos desde CO001
    return f"CO{max_Id + 1:03}"


def registrar_compra(arch_compras, arch_productos):
    id_compra = generar_id_compra(arch_compras)
    print(f"ID generado automáticamente: {id_compra}")

    nombre_producto = None
    producto = None
    while True:
        id_producto = ('PR' + input("ID del producto (Formato 002): ").strip())
        if not re.match(r'^PR[0-9]{3}$', id_producto):
            print("Formato inválido. Intente nuevamente.")
            continue
        try:
            with open(arch_productos, "r", encoding="utf-8") as archivo_productos:
                productos = json.load(archivo_productos)
        except FileNotFoundError:
            print("Archivo de productos no encontrado.")
            return
        except OSError:
            print("Error al abrir el archivo de productos.")
            return

        if not productos:
            print("No hay productos cargados.")
            return

        for prod in productos:
            if prod["ID"] == id_producto:
                producto = prod
                nombre_producto = prod["nombre"]
                break

        if producto:
            print(f"Producto encontrado: {id_producto} - {nombre_producto}")
            break
        else:
            print("Producto no encontrado. Intente con otro ID.")

    while True:
        try:
            cantidad_compra = int(input("Cantidad de productos: "))
            if cantidad_compra > 0:
                break
            else:
                print("La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")

    producto["stock"] += cantidad_compra
    proveedor = producto.get('proveedor', 'Proveedor no especificado')
    print("\nProducto encontrado y stock actualizado.")
    print(f"Producto seleccionado: {id_producto} - {nombre_producto}")
    print(f"Proveedor: {proveedor}")
    print(f"Cantidad comprada: {cantidad_compra}")
    print(f"Nuevo stock del producto {id_producto}: {producto['stock']}")

    try:
        with open(arch_compras, "a", encoding="utf-8") as arch:
            arch.write(f"{id_compra};{id_producto};{nombre_producto};{cantidad_compra};{proveedor}\n")
        with open(arch_productos, "w", encoding="utf-8") as archivo_productos:
            json.dump(productos, archivo_productos, indent=4)
        print("\n\nCompra registrada con éxito.")
        print(f"{'ID Compra':<20}{'ID Producto':<20}{'Producto':<20}{'Cantidad':<20}{'Proveedor':<20}")
        print(f"{id_compra:<20}{id_producto:<20}{nombre_producto:<20}{cantidad_compra:<20}{proveedor:<20}")
        
    except OSError:
        print("Error al guardar los archivos.")
