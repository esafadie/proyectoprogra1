import re
import json

def generar_id_venta(arch_vtas):
    max_Id = 0
    try:
        with open(arch_vtas, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if partes and re.match(r"VE\d{3}", partes[0]):
                    num = int(partes[0][2:])
                    if num > max_Id:
                        max_Id = num
    except FileNotFoundError:
        pass
    return f"VE{max_Id + 1:03}"

def cargar_ventas(arch_ventas, archivo_productos, arch_clientes):
    id_venta = generar_id_venta(arch_ventas)
    print(f"ID de la venta generado: {id_venta}")

    # Validación de cliente 
    nombre_cliente = None
    while True:
        id_cliente = ('CL' + input("ID del cliente (formato 001): ").strip())
        if not re.match(r'^CL[0-9]{3}$', id_cliente):
            print("Formato inválido. Intente nuevamente.")
            continue
        try:
            with open(arch_clientes, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split(";")
                    if len(partes) >= 2 and partes[0] == id_cliente:
                        nombre_cliente = partes[1]
                        break
        except FileNotFoundError:
            print("Archivo de clientes no encontrado.")
            return
        except OSError:
            print("Error al abrir el archivo de clientes.")
            return

        if nombre_cliente:
            print(f"Cliente encontrado: {id_cliente} - {nombre_cliente}")
            break
        else:
            print("Cliente no encontrado. Intente con otro ID.")

    # Validación de producto 
    nombre_producto = None
    producto = None
    while True:
        id_producto = ('PR' + input("ID del producto (Formato 002): ").strip())
        if not re.match(r'^PR[0-9]{3}$', id_producto):
            print("Formato inválido. Intente nuevamente.")
            continue
        try:
            with open(archivo_productos, "r", encoding="utf-8") as info_productos:
                productos = json.load(info_productos)
        except FileNotFoundError:
            print("Error: La lista de productos está vacía. No hay productos cargados en el sistema.")
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

    # Validar cantidad y actualizar stock
    while True:
        try:
            cantidad_venta = int(input("Cantidad de productos: "))
            if cantidad_venta > 0:
                break
            else:
                print("La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")

    if producto["stock"] >= cantidad_venta:
        producto["stock"] -= cantidad_venta
        print("\nProducto encontrado y stock actualizado.")
        print(f"Producto vendido: {id_producto} - {nombre_producto}")
        print(f"Cliente: {id_cliente} - {nombre_cliente}")
        print(f"Cantidad vendida: {cantidad_venta}")
        print(f"Nuevo stock del producto {id_producto}: {producto['stock']}")
    else:
        print(f"Stock insuficiente. Solo hay {producto['stock']} unidades disponibles para {producto['ID']}.")
        return

    # Guardar cambios
    try:
        with open(archivo_productos, "w", encoding="utf-8") as modificar:
            json.dump(productos, modificar, indent=4)
        with open(arch_ventas, "a", encoding="utf-8") as arch:
            arch.write(f"\n{id_venta};{id_cliente};{nombre_cliente};{id_producto};{nombre_producto};{cantidad_venta}\n")
            print("\n\nVenta registrada correctamente.")
            print('\n' + f"Cliente: {nombre_cliente} - Producto: {nombre_producto} - Cantidad: {cantidad_venta}")
    except OSError:
        print("Error al guardar los archivos.")
