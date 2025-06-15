import re
import json
id_cargado = set()

def cargar_ventas(archivo_ventas,archivo_productos):
    
    with open(archivo_ventas, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if partes:
                    id_cargado.add(partes[0])

    try:
        arch = open(archivo_ventas,"a",encoding="UTF-8")
        id_venta = input("ID de la venta (formato VE001): ")
        while not re.match(r'^VE[0-9]{3}$', id_venta) or id_venta in id_cargado:
            id_venta = input("ID inválido o repetido. Ingrese otro (ej: VE001): ")
        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente):
            id_cliente = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ")
        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")
        while True:
            try:
                cantidad_venta = int(input("Cantidad de productos: "))
                if cantidad_venta > 0:
                    break
                else:
                    print("La cantidad debe ser un número entero positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero positivo.")

        #abrir archivo productos
        with open(archivo_productos, "r", encoding="utf-8") as info_productos:
            productos = json.load(info_productos)
        if not productos:
            print("No hay productos cargados.")
            return
        # Descontar stock
        producto_encontrado = False
        for producto in productos:
            if producto['ID'] == id_producto:
                if producto['stock'] >= cantidad_venta:
                    producto['stock'] -= cantidad_venta
                    producto_encontrado = True
                else:
                    print(f"Stock insuficiente para el producto {id_producto}. Solo hay {producto['stock']} unidades.")
        
        if producto_encontrado == False:
            print("Producto no encontrado")
        else:
            with open(archivo_productos, "w", encoding="utf-8") as modificar:
                json.dump(productos, modificar)
            arch.write(id_venta + ";" + id_cliente + ";" + id_producto + ";" + str(cantidad_venta) + "\n")
                
                
    except OSError as mensaje:
        print("")
    finally:
        try:
            arch.close()
        except NameError:
            pass
    id_cargado.add(id_venta)
