import re

def cargar_productos():
    lista_PR = []
    cantidad = int(input("Ingrese la cantidad de productos a cargar: "))

    for _ in range(cantidad):
        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")

        nombre = input("Nombre del producto: ")
        proveedor = input("Proveedor: ")
        stock = int(input("Stock del producto: "))

        lista_PR.append([id_producto, nombre, proveedor, stock])

    return lista_PR

def cargar_compras():
    lista_CO = []
    cantidad = int(input("Ingrese la cantidad de compras a registrar: "))

    for _ in range(cantidad):
        id_compra = input("ID de la compra (formato CO001): ")
        while not re.match(r'^CO[0-9]{3}$', id_compra):
            id_compra = input("ID inválido. Debe tener el formato CO seguido de tres números (ej: CO001): ")

        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")

        cantidad = int(input("Cantidad de productos: "))
        proveedor = input("Proveedor: ")

        lista_CO.append([id_compra, id_producto, cantidad, proveedor])
    return lista_CO

def cargar_ventas():
    lista_VE = []
    cantidad = int(input("Ingrese la cantidad de ventas a registrar: "))

    for _ in range(cantidad):
        id_venta = input("ID de la venta (formato VE001): ")
        while not re.match(r'^VE[0-9]{3}$', id_venta):
            id_venta = input("ID inválido. Debe tener el formato VE seguido de tres números (ej: VE001): ")

        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente):
            id_cliente = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ")

        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")

        cantidad = int(input("Cantidad vendida: "))

        lista_VE.append([id_venta, id_cliente, id_producto, cantidad])
    return lista_VE

def cargar_clientes():
    lista_CL = []
    cantidad = int(input("Ingrese la cantidad de clientes a cargar: "))

    for _ in range(cantidad):
        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente):
            id_cliente = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ")

        nombre = input("Nombre del cliente: ")
        telefono = input("Teléfono: ")

        lista_CL.append([id_cliente, nombre, telefono])
    return lista_CL

def buscar_producto(lista_productos):
    id_buscar = input("Ingrese el ID del producto a buscar (formato PR001): ")
    for prod in lista_productos:
        if prod[0] == id_buscar:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Proveedor: {prod[2]}, Stock: {prod[3]}")
            return
    print("Producto no encontrado.")

def menu():
    productos = []
    clientes = []
    compras = []
    ventas = []

while True:
        while True:
            opciones = 6
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("1. Alta de productos ")
            print("2. Alta de clientes")
            print("3. Registro de compras ")
            print("4. Registro de ventas")
            print("5. Consulta de producto por ID")
            print("---------------------------")
            print("0. Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit()

        elif opcion == "1":   # Opción 1
            ...
        elif opcion == "2":   # Opción 2
            ...
        elif opcion == "3":   # Opción 3
            ...
        elif opcion == "4":   # Opción 4
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")
        
