import re
from carga_de_informacion import *

from mostrar_ultimos import *

from productos import *

from dar_de_baja import *



def menu():
    productos = []
    clientes = []
    compras = []
    ventas = []

    while True:
        while True:
            opciones = 4
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("1. Productos")
            print("2. Clientes")
            print("3. Compras")
            print("4. Ventas")
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
            print("---------------------------")
            print("1. Cargar producto")
            print("2. Borrar producto")
            print("3. Modificar producto") #HACER FUNCION
            print("4. Mostrar productos") 
            print("5. Mostrar producto segun ID")
            print("6. Ordenar segun stock")
            print("---------------------------")
            print()
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
            elif sub_opcion == 6:
                ordenar_productos_por_stock(productos)

        elif opcion == "2":
            print("---------------------------")
            print("1. Cargar cliente")
            print("2. Borrar cliente")
            print("3. Mostrar ultimos clientes")
            print("---------------------------")
            print()
            sub_opcion = int(input("Digite una opcion: "))
            if sub_opcion == 1:
                clientes = cargar_clientes()
            elif sub_opcion == 2:
                dar_de_baja_clientes(clientes)
            elif sub_opcion == 3:
                mostrar_ultimos_clientes(clientes)

        elif opcion == "3":
            print("---------------------------")
            print("1. Cargar compra")
            print("2. Mostrar ultimas compras")
            print("---------------------------")
            print()
            sub_opcion = int(input("Digite una opcion: "))
            if sub_opcion == 1:
                compras = Registrar_compras(productos)
                print("Compras registradas correctamente.")
            elif sub_opcion == 2:
                mostrar_ultimas_compras(compras)

        elif opcion == "4":
            print("---------------------------")
            print("1. Cargar venta")
            print("2. Mostrar ultimas ventas")
            print("---------------------------")
            print()
            sub_opcion = int(input("Eliga una opcion: "))
            if sub_opcion == 1:
                ventas = cargar_ventas(productos)
            elif sub_opcion == 2:
                mostrar_ultimas_ventas(ventas)
        print("\n\n")

#Carga usuario
carga_usuario()

# Ejecutar el menú
menu()