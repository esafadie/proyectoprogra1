import re
import time
from carga_de_informacion import *

from mostrar_ultimos import *

from productos import *

from dar_de_baja import *

from Datos_preexistentes.Clientes_cargados import *
from Datos_preexistentes.Compras_cargadas import *
from Datos_preexistentes.Productos_cargados import *
from Datos_preexistentes.Ventas_cargadas import *


def menu():

    clientes = cliente_cargado.copy()
    productos = producto_cargado.copy()
    ventas = venta_cargada.copy()
    compras = compra_cargada.copy()

    productos = []
    clientes = []
    compras = []
    ventas = []
    opciones = 4
    opcion = ""
    while opcion != "0":  # Salir solo si la opción es 0
        time.sleep(2) # Pausa de 2 segundos
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
            if opcion == "0":
                print("Saliendo del programa...")

            elif opcion == "1": #producto
                if not productos:
                    print("")
                else:
                    print("")
                    print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
                    for p in productos:
                        print(f"{p['ID']:<10}{p['nombre']:<20}{p['proveedor']:<20}{p['stock']:<10}")


                print("---------------------------")
                print("1. Cargar producto")
                print("2. Borrar producto")
                print("3. Modificar producto") 
                print("4. Mostrar productos") 
                print("5. Mostrar producto segun ID")
                print("6. Ordenar segun stock")
                print("7. Volver al menu principal")
                print("---------------------------")
                print()
                
               #try except para manejar errores de entrada
                try:
                    sub_opcion = int(input("Digite una opcion: "))
                    if sub_opcion == 1:
                        producto = cargar_productos()
                        productos.append(producto)
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
                    elif sub_opcion == 7:
                        continue
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Debe ingresar un número entre el 1 y 7. ")

            elif opcion == "2": #cliente
                if not clientes:
                    print("")
                else:
                    print("")
                    print(f"{'ID':<10}{'Nombre':<20}{'Telefono':<20}")
                    for p in clientes:
                        print(f"{p[0]:<10}{p[1]:<20}{p[2]:<20}")
                print("---------------------------")
                print("1. Cargar cliente")
                print("2. Borrar cliente")
                print("3. Mostrar ultimos clientes")
                print("4. Volver al menu principal")
                print("---------------------------")
                print()
                
                try:
                    sub_opcion = int(input("Digite una opcion: "))
                    if sub_opcion == 1:
                        cliente = cargar_clientes()
                        clientes.append(cliente)
                    elif sub_opcion == 2:
                        dar_de_baja_clientes(clientes)
                    elif sub_opcion == 3:
                        mostrar_ultimos_clientes(clientes)
                    elif sub_opcion == 4:
                        continue
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Debe ingresar un número entre el 1 y el 4.")

#    lista_CO.append([(id_compra), id_producto, cantidad_compra, proveedor])

            elif opcion == "3": #compra
                if not compras:
                    print("")
                else:
                    print("")
                    print(f"{'ID Compra':<10}{'ID Producto':<20}{'Cantidad':<20}{'Proveedor':<20}")
                    for p in compras:
                        print(f"{p[0]:<10}{p[1]:<20}{p[2]:<20}{p[3]:<20}")
                print("---------------------------")
                print("1. Cargar compra")
                print("2. Mostrar ultimas compras")
                print("3. Volver al menu principal")
                print("---------------------------")
                print()
                
                try:
                    sub_opcion = int(input("Digite una opcion: "))
                    if sub_opcion == 1:
                        compra = Registrar_compras(productos)
                        compras.append(compra)
                    elif sub_opcion == 2:
                        mostrar_ultimas_compras(compras)
                    elif sub_opcion == 3:
                        continue
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Debe ingresar un número entre el 1 y 3.")


            elif opcion == "4": #venta
                if not ventas:
                    print("")
                else:
                    print("")
                    print(f"{'ID Venta':<10}{'ID Cliente':<20}{'ID Producto':<20}{'Cantidad':<20}")
                    for p in ventas:
                        print(f"{p[0]:<10}{p[1]:<20}{p[2]:<20}{p[3]:<20}")
                print("---------------------------")
                print("1. Cargar venta")
                print("2. Mostrar ultimas ventas")
                print("3. Volver al menu principal")
                print("---------------------------")
                print()
                
                try:
                    sub_opcion = int(input("Eliga una opcion: "))
                    if sub_opcion == 1:
                        venta = cargar_ventas(productos)
                        ventas.append(venta)
                    elif sub_opcion == 2:
                        mostrar_ultimas_ventas(ventas)
                    elif sub_opcion == 3:
                        continue
                    else:
                        print("Opción inválida. Intente nuevamente.\n")
                except ValueError:
                    print("Debe ingresar un número entre el 1 y 3.")
            
            print("\n\n")

#Carga usuario
carga_usuarios()

# Ejecutar el menú
menu()