import re

def cargar_productos():
    lista_PR = []
    cantidad = int(input("Ingrese la cantidad de productos a cargar: "))

    for _ in range(cantidad):
        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto) or any(p[0] == id_producto for p in lista_PR):
            id_producto = input("ID inválido o repetido. Ingrese otro (ej: PR001): ")

        nombre = input("Nombre del producto: ")
        proveedor = input("Proveedor: ")
        stock = int(input("Stock del producto: "))

        lista_PR.append([id_producto, nombre, proveedor, stock])

    return lista_PR

def Registrar_compras(productos):
    lista_CO = []
    cantidad = int(input("Ingrese la cantidad de compras a registrar: "))

    for _ in range(cantidad):
        id_compra = input("ID de la compra (formato CO001): ")
        while not re.match(r'^CO[0-9]{3}$', id_compra) or any(c[0] == id_compra for c in lista_CO):
            id_compra = input("ID inválido o repetido. Ingrese otro (ej: CO001): ")

        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")

        cantidad_compra = int(input("Cantidad de productos: "))
        proveedor = input("Proveedor: ")

        # Actualizar stock
        for producto in productos:
            if producto[0] == id_producto:
                producto[3] += cantidad_compra
                break

        lista_CO.append([id_compra, id_producto, cantidad_compra, proveedor])
    return lista_CO

def cargar_ventas(productos):
    lista_VE = []
    cantidad = int(input("Ingrese la cantidad de ventas a registrar: "))

    for _ in range(cantidad):
        id_venta = input("ID de la venta (formato VE001): ")
        while not re.match(r'^VE[0-9]{3}$', id_venta) or any(v[0] == id_venta for v in lista_VE):
            id_venta = input("ID inválido o repetido. Ingrese otro (ej: VE001): ")

        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente):
            id_cliente = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ")

        id_producto = input("ID del producto (formato PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")

        cantidad_venta = int(input("Cantidad vendida: "))

        # Descontar stock
        for producto in productos:
            if producto[0] == id_producto:
                if producto[3] >= cantidad_venta:
                    producto[3] -= cantidad_venta
                else:
                    print(f"Stock insuficiente para el producto {id_producto}. Solo hay {producto[3]} unidades.")
                break

        lista_VE.append([id_venta, id_cliente, id_producto, cantidad_venta])
    return lista_VE

def cargar_clientes():
    lista_CL = []
    cantidad = int(input("Ingrese la cantidad de clientes a cargar: "))

    for _ in range(cantidad):
        id_cliente = input("ID del cliente (formato CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente) or any(c[0] == id_cliente for c in lista_CL):
            id_cliente = input("ID inválido o repetido. Ingrese otro (ej: CL001): ")

        nombre = input("Nombre del cliente: ")
        telefono = input("Teléfono: ")

        lista_CL.append([id_cliente, nombre, telefono])
    return lista_CL

<<<<<<< HEAD
def buscar_producto(lista_productos):
    id_buscar = input("Ingrese el ID del producto a buscar (formato PR001): ")
    for prod in lista_productos:
=======
def buscar_producto(productos):
    if not productos:
        print("No hay productos cargados.")
        return
    id_buscar = input("Ingrese el ID del producto a buscar (formato PR001): ")
    for prod in productos:
>>>>>>> b989364 (Agregue nueva funcion (Modificar producto), separe funciones y achique el menu para que sea mas intuitivo)
        if prod[0] == id_buscar:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Proveedor: {prod[2]}, Stock: {prod[3]}")
            return
    print("Producto no encontrado.")

def mostrar_nombres_productos(productos):
    if not productos:
        print("No hay productos cargados.")
        return
<<<<<<< HEAD
    nombres = [p[1] for p in productos]  # Lista de comprensión
    print("Nombres de productos cargados:")
    for nombre in nombres:
        print("-", nombre)
=======
    print("Nombres de productos cargados:")
    for nombre in productos:
        print(f"ID: {nombre[0]} | Nombre: {nombre[1]} | Proveedor: {nombre[2]} | Stock: {nombre[3]}")
>>>>>>> b989364 (Agregue nueva funcion (Modificar producto), separe funciones y achique el menu para que sea mas intuitivo)

def ordenar_productos_por_stock(productos):
    if not productos:
        print("No hay productos cargados.")
        return
    ordenados = sorted(productos, key=lambda x: x[3], reverse=True)  # Uso de lambda
    print("Productos ordenados por stock (descendente):")
    for p in ordenados:
        print(f"ID: {p[0]}, Nombre: {p[1]}, Stock: {p[3]}")

<<<<<<< HEAD
def mostrar_ultimos_productos(sub_opcion,productos,clientes,compras,ventas):
    if sub_opcion==1:
=======
def mostrar_ultimos_productos(productos):
>>>>>>> b989364 (Agregue nueva funcion (Modificar producto), separe funciones y achique el menu para que sea mas intuitivo)
        if not productos:
            print("No hay productos cargados.")
            return
        ultimos = productos[-3:]  # Slicing para obtener los últimos 3
        print("Últimos productos cargados:")
        for p in ultimos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Stock: {p[3]}")
<<<<<<< HEAD
    if sub_opcion ==2:
        if not clientes:
            print("No hay clientes cargados")
            return
        ultimos = clientes[-3:]
        print("Últimos clientes cargados:")
        for p in ultimos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Telefono: {p[2]}")
    if sub_opcion ==3:
        if not compras:
            print("No hay compras cargadas")
            return
        ultimos = compras[-3:]
        print("Últimas compras cargadas:")
        for p in ultimos:
            print(f"ID Compra: {p[0]}, ID Producto: {p[1]}, Cantidad: {p[2]}, Proveedor: {p[3]}")
    if sub_opcion ==4:
        if not ventas:
            print("No hay ventas cargadas")
            return
        ultimos = ventas[-3:]
        print("Últimas ventas cargadas:")
        for p in ultimos:
            print(f"ID Venta: {p[0]}, ID Cliente: {p[1]}, ID Producto: {p[2]}, Cantidad: {p[3]}")


def dar_de_baja(opcion,clientes,productos):

    if opcion == 1:
        id_cliente = input("Digite el ID del cliente. Debe tener el formato CL seguido de tres números (ej: CL001): ")
        while not re.match(r'^CL[0-9]{3}$', id_cliente):
            id_cliente = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ")
        for i in clientes:
            if i[0] == id_cliente:
                clientes.remove(i)

    elif opcion == 2:
        id_producto = input("Digite el ID del producto. Debe tener el formato CL seguido de tres números (ej: CL001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ")
=======

def mostrar_ultimos_clientes(clientes):
    if not clientes:
            print("No hay clientes cargados")
            return
    ultimos = clientes[-3:]
    print("Últimos clientes cargados:")
    for p in ultimos:
        print(f"ID: {p[0]}, Nombre: {p[1]}, Telefono: {p[2]}")

def mostrar_ultimas_compras(compras):
    if not compras:
            print("No hay compras cargadas")
            return
    ultimos = compras[-3:]
    print("Últimas compras cargadas:")
    for p in ultimos:
        print(f"ID COMPRA: {p[0]}, ID PRODUCTO: {p[1]}, CANTIDAD: {p[2]}, PROVEEDOR: {p[3]}")

def mostrar_ultimas_ventas(ventas):
    if not ventas:
            print("No hay ventas cargadas")
            return
    ultimos = ventas[-3:]
    print("Últimas ventas cargadas:")
    for p in ultimos:
        print(f"ID VENTA: {p[0]}, ID CLIENTE: {p[1]}, ID PRODUCTO: {p[2]}, CANTIDAD: {p[3]}")

def dar_de_baja_clientes(clientes):
    if not clientes:
            print("No hay clientes cargados")
            return
    if not clientes:
        print("No hay clientes cargados")
    id_cliente = input("Digite el ID del cliente. Debe tener el formato CL seguido de tres números (ej: CL001): ")
    while not re.match(r'^CL[0-9]{3}$', id_cliente):
        id_cliente = input("ID inválido. Debe tener el formato CL seguido de tres números (ej: CL001): ")
    for i in clientes:
        if i[0] == id_cliente:
            clientes.remove(i)

def dar_de_baja_productos(productos):
        if not productos:
            print("No hay productos cargados")
            return
        id_producto = input("Digite el ID del producto. Debe tener el formato PR seguido de tres números (ej: PR001): ")
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = input("ID inválido. Debe tener el formato PR seguido de tres números (ej: PR001): ")
>>>>>>> b989364 (Agregue nueva funcion (Modificar producto), separe funciones y achique el menu para que sea mas intuitivo)
        for i in productos:
            if i[0] == id_producto:
                productos.remove(i)

<<<<<<< HEAD
=======
def modificar_producto(productos):
    if not productos:
        print("No hay productos cargados.")
        return
    id_producto = input("ID del producto a modificar (formato PR001): ")
    while not re.match(r'^PR[0-9]{3}$', id_producto):
        id_producto = input("ID inválido o repetido. Ingrese otro (ej: PR001): ")
    
    for prod in productos:
        if prod[0] == id_producto:
            nombre_nuevo = input("Nuevo nombre del producto: ")
            proveedor_nuevo = input("Proveedor del producto: ")
            stock_nuevo = int(input("Stock actual del producto: "))

            prod[1] = nombre_nuevo
            prod[2] = proveedor_nuevo
            prod[3] = stock_nuevo
            print("Producto modificado exitosamente")
>>>>>>> b989364 (Agregue nueva funcion (Modificar producto), separe funciones y achique el menu para que sea mas intuitivo)

def menu():
    productos = []
    clientes = []
    compras = []
    ventas = []

    while True:
        while True:
<<<<<<< HEAD
            opciones = 9
=======
            opciones = 4
>>>>>>> b989364 (Agregue nueva funcion (Modificar producto), separe funciones y achique el menu para que sea mas intuitivo)
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
<<<<<<< HEAD
            print("1. Alta de productos ")
            print("2. Alta de clientes")
            print("3. Registro de compras ")
            print("4. Registro de ventas")
            print("5. Consulta de producto por ID")
            print("6. Mostrar nombres de productos")
            print("7. Ordenar productos por stock")
            print("8. Mostrar últimos Cl/Co/V/P")
            print("9. Dar de baja")
=======
            print("1. Productos")
            print("2. Clientes")
            print("3. Ventas")
            print("4. Compras")
>>>>>>> b989364 (Agregue nueva funcion (Modificar producto), separe funciones y achique el menu para que sea mas intuitivo)
            print("---------------------------")
            print("0. Salir del programa")
            print("---------------------------")
            print()

            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0":
            exit()

        elif opcion == "1":
<<<<<<< HEAD
            productos = cargar_productos()
            print("Productos cargados correctamente.")
        elif opcion == "2":
            clientes = cargar_clientes()
            print("Clientes cargados correctamente.")
        elif opcion == "3":
            compras = Registrar_compras(productos)
            print("Compras registradas correctamente.")
        elif opcion == "4":
            ventas = cargar_ventas(productos)
            print("Ventas registradas correctamente.")
        elif opcion == "5":
            buscar_producto(productos)
            input("\nPresione ENTER para volver al menú.")
        elif opcion == "6":
            mostrar_nombres_productos(productos)
            input("\nPresione ENTER para volver al menú.")
        elif opcion == "7":
            ordenar_productos_por_stock(productos)
            input("\nPresione ENTER para volver al menú.")
        elif opcion == "8":
            print()
            print("---------------------------")
            print("1. Ultimos Productos ")
            print("2. Ultimos Clientes")
            print("3. Ultimas Compras")
            print("4. Ultimas Ventas")
            print("---------------------------")
            print()
            sub_opcion = int(input("Digite la opcion: "))
            mostrar_ultimos_productos(sub_opcion,productos,clientes,compras,ventas)
            input("\nPresione ENTER para volver al menú.")
        elif opcion == "9":
            print()
            print("---------------------------")
            print("1. Dar de baja cliente ")
            print("2. Dar de baja producto")
            print("---------------------------")
            print()
            sub_opcion = int(input("Digite la opcion: "))
            dar_de_baja(sub_opcion,clientes,productos)
            print(productos)
=======
            print("1. Cargar producto")
            print("2. Borrar producto")
            print("3. Modificar producto") #HACER FUNCION
            print("4. Mostrar productos") 
            print("5. Mostrar producto segun ID")
            sub_opcion = int(input("Digite una opcion: "))
            if sub_opcion == 1:
                productos = cargar_productos()
            elif sub_opcion == 2:
                dar_de_baja_productos(productos)
            elif sub_opcion == 3:
                modificar_producto(productos)
            elif sub_opcion == 4:
                mostrar_nombres_productos(productos)
            elif sub_opcion == 5:
                buscar_producto(productos)

        elif opcion == "2":
            print("1. Cargar cliente")
            print("2. Borrar cliente")
            print("3. Mostrar ultimos clientes")
            sub_opcion = int(input("Digite una opcion: "))
            if sub_opcion == 1:
                clientes = cargar_clientes()
            elif sub_opcion == 2:
                dar_de_baja_clientes(clientes)
            elif sub_opcion == 3:
                mostrar_ultimos_clientes(clientes)

        elif opcion == "3":
            print("1. Cargar compra")
            print("2. Mostrar ultimas compras")
            sub_opcion = int(input("Digite una opcion: "))
            if sub_opcion == 1:
                compras = Registrar_compras()
                print("Compras registradas correctamente.")
            elif sub_opcion == 2:
                mostrar_ultimas_compras(compras)

        elif opcion == "4":
            print("1. Cargar venta")
            print("2. Mostrar ultimas ventas")
            sub_opcion = int(input("Eliga una opcion: "))
            if sub_opcion == 1:
                ventas = cargar_ventas(productos)
                print("Ventas registradas correctamente.")
            elif sub_opcion == 2:
                mostrar_ultimas_ventas(ventas)
>>>>>>> b989364 (Agregue nueva funcion (Modificar producto), separe funciones y achique el menu para que sea mas intuitivo)
        print("\n\n")

# Ejecutar el menú
menu()