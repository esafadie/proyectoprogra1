import re
import json

def generar_nuevo_id(arch_compras):
    max_Id = 0
    try:
        with open(arch_compras, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if partes and re.match(r"CO\d{3}", partes[0]):
                    num = int(partes[0][2:])  # Obtener el número después de CO
                    if num > max_id:
                        max_id = num
    except FileNotFoundError:
        pass  # Si el archivo no existe aún, arrancamos desde CO001
    return f"CO{max_Id + 1:03}"


def registrar_compra(arch_compras, arch_productos):
    try:
        id_compra = generar_nuevo_id(arch_compras)
        print(f"ID generado automáticamente: {id_compra}")

        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")

        while True:
            try:
                cantidad_compra = int(input("Cantidad de productos: "))
                if cantidad_compra > 0:
                    break
                else:
                    print("La cantidad debe ser un número entero positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero positivo.")


        # Leer productos
        with open(arch_productos, "r", encoding="utf-8") as archivo_productos:
            productos = json.load(archivo_productos)

        # Buscar y actualizar producto
        producto_encontrado = False
        for producto in productos:
            if producto['ID'] == id_producto:
                producto['stock'] += cantidad_compra
                nombre_producto = producto['nombre']
                producto_encontrado = True
                break

        if not producto_encontrado:
            print("\nOperación de compra cancelada.")
            print("ERROR:Producto no encontrado")
            return
        else:
            print("\nProducto encontrado y stock actualizado.")
            print(f"Producto seleccionado: {id_producto} - {nombre_producto}")
            proveedor = producto.get('proveedor', 'Proveedor no especificado')
            print(f"Proveedor: {proveedor}")
            print(f"Cantidad comprada: {cantidad_compra}")
            print(f"Nuevo stock del producto {id_producto}: {producto['stock']}")

        # Guardar compra
        with open(arch_compras, "a", encoding="utf-8") as arch:
            arch.write(f"{id_compra};{id_producto};{nombre_producto};{cantidad_compra};{proveedor}\n")

        # Guardar productos actualizados
        with open(arch_productos, "w", encoding="utf-8") as archivo_productos:
            json.dump(productos, archivo_productos, indent=4)

        print("Compra registrada con éxito.")

    except OSError as e:
        print("Error de acceso a archivo:", e)
