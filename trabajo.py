import re
import json
from carga_de_informacion import *
import time
from mostrar_ultimos import *

from productos import *

from dar_de_baja import *


def menu():

    opciones = 4
    opcion = ""
    while opcion != "0":  # Salir solo si la opción es 0
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
        if not opcion in [str(i) for i in range(0, opciones + 1)]:
            print("Opción inválida. Por favor, seleccione una opción del menú.")
            time.sleep(1)
            continue

        if opcion in [str(i) for i in range(0, opciones + 1)]:
            if opcion == "0":
                print("Saliendo del programa...")

            elif opcion == "1": #producto
                try:
                    archivo = open("carga_de_informacion/productos.json","r")
                    productos = json.load(archivo)
                    if productos == []:
                        print("")
                    else:
                        print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
                    def mostrar_productos(productos, indice=0): #recursividad
                        if indice >= len(productos):
                            return #caso base: Cuando el índice alcanza el largo de la lista, se detiene la recursión
                        p = productos[indice]
                        print(f"{p['ID']:<10}{p['nombre']:<20}{p['proveedor']:<20}{p['stock']:<10}")
                        mostrar_productos(productos, indice + 1) #Caso recursivo: La función se llama a sí misma avanzando al siguiente índice.
                    mostrar_productos(productos)
                except FileNotFoundError:
                    print("No hay productos cargados")


                print("---------------------------")
                print("1. Cargar producto")
                print("2. Borrar producto")
                print("3. Modificar producto") 
                print("4. Mostrar producto segun ID")
                print("5. Ordenar segun stock")
                print("6. Ordenar segun ID")
                print("7. Volver al menu principal")
                print("---------------------------")
                print()
                
                try:
                    sub_opcion = int(input("Digite una opcion: "))
                    if not 1 <= sub_opcion <= 7:
                        print("Opción fuera de rango. Se volverá al menú principal.")
                        time.sleep(1)
                        continue
                except ValueError:
                    print("Debe ingresar un número válido. Se volverá al menú principal.")
                    time.sleep(1)
                    continue

                if sub_opcion == 1:
                    producto = cargar_productos()
                    productos.append(producto)
                elif sub_opcion == 2:
                    dar_de_baja_productos("carga_de_informacion/productos.json")
                elif sub_opcion == 3:
                    modificar_producto("carga_de_informacion/productos.json")
                elif sub_opcion == 4:
                    buscar_producto("carga_de_informacion/productos.json")
                elif sub_opcion == 5:
                    ordenar_productos_por_stock("carga_de_informacion/productos.json")
                elif sub_opcion == 6:
                    ordenar_productos_por_id("carga_de_informacion/productos.json")
                elif sub_opcion == 7:
                    continue

            elif opcion == "2": #cliente
                try:
                    with open("carga_de_informacion/clientes.txt","r",encoding="UTF-8") as file:
                        linea = file.readline()
                        if linea == "":
                            print("")
                        else:
                            print(f"{'ID':<10}{'Nombre':<20}{'Telefono':<20}")
                        while linea:
                            idcliente,nombre,telefono = linea.strip().split(";")
                            print(f"{idcliente:<10}{nombre:<20}{telefono:<20}")
                            linea = file.readline()
                except OSError:
                        print("No se pudo abrir el archivo")
                print("---------------------------")
                print("1. Cargar cliente")
                print("2. Borrar cliente")
                print("3. Mostrar ultimos clientes")
                print("4. Volver al menu principal")
                print("---------------------------")
                print()
                
                try:
                    sub_opcion = int(input("Digite una opcion: "))
                    if not 1 <= sub_opcion <= 4:
                        print("Opción fuera de rango. Se volverá al menú principal.")
                        time.sleep(1)
                        continue
                except ValueError:
                    print("Debe ingresar un número válido. Se volverá al menú principal.")
                    time.sleep(1)
                    continue
                
                if sub_opcion == 1:
                    cliente = cargar_clientes("carga_de_informacion/clientes.txt")
                elif sub_opcion == 2:
                    dar_de_baja_clientes("carga_de_informacion/clientes.txt")
                elif sub_opcion == 3:
                    mostrar_ultimos_clientes("carga_de_informacion/clientes.txt")
                elif sub_opcion == 4:
                    continue

            elif opcion == "3": #compra
                try:
                    with open("carga_de_informacion/compras.txt","r",encoding="UTF-8") as file:
                        linea = file.readline()
                        if linea == "":
                            print("")
                        else:
                            print(f"{'ID Compra':<10}{'ID Producto':<20}{'Cantidad':<20}{'Proveedor':<20}")
                        while linea:
                            idcompra,idprod,cantidad,proveedor = linea.strip().split(";")
                            print(f"{idcompra:10}{idprod:20}{cantidad:20}{proveedor:20}")
                            linea = file.readline()
                except OSError:
                    print("No se pudo abrir el archivo")
                print("---------------------------")
                print("1. Cargar compra")
                print("2. Mostrar ultimas compras")
                print("3. Volver al menu principal")
                print("---------------------------")
                print()
                
                try:
                    sub_opcion = int(input("Digite una opcion: "))
                    if not 1 <= sub_opcion <= 3:
                        print("Opción fuera de rango. Se volverá al menú principal.")
                        time.sleep(1)
                        continue
                except ValueError:
                    print("Debe ingresar un número válido. Se volverá al menú principal.")
                    time.sleep(1)
                    continue
                
                if sub_opcion == 1:
                    compra = registrar_compra("carga_de_informacion/compras.txt","carga_de_informacion/productos.json")
                elif sub_opcion == 2:
                    mostrar_ultimas_compras("carga_de_informacion/compras.txt")
                elif sub_opcion == 3:
                    continue

            elif opcion == "4": #venta
                try:
                    with open("carga_de_informacion/ventas.txt","r",encoding="UTF-8") as file:
                        linea = file.readline()
                        if linea == "":
                            print("")
                        else:
                            print(f"{'ID Venta':<20}{'ID Cliente':<20}{'ID Producto':<20}{'Cantidad':<20}")
                        while linea:
                            idventa,idcliente,idproducto,cantidad = linea.strip().split(";")
                            print(f"{idventa:20}{idcliente:20}{idproducto:20}{cantidad:20}")
                            linea = file.readline()
                except OSError:
                    print("No se pudo abrir el archivo")
                print("---------------------------")
                print("1. Cargar venta")
                print("2. Mostrar ultimas ventas")
                print("3. Volver al menu principal")
                print("---------------------------")
                print()
                
                try:
                    sub_opcion = int(input("Digite una opcion: "))
                    if not 1 <= sub_opcion <= 3:
                        print("Opción fuera de rango. Se volverá al menú principal.")
                        time.sleep(1)
                        continue
                except ValueError:
                    print("Debe ingresar un número válido. Se volverá al menú principal.")
                    time.sleep(1)
                    continue
                
                if sub_opcion == 1:
                    ventas = cargar_ventas("carga_de_informacion/ventas.txt","carga_de_informacion/productos.json")
                elif sub_opcion == 2:
                    mostrar_ultimas_ventas("carga_de_informacion/ventas.txt")
                elif sub_opcion == 3:
                    continue
                else:
                    input("Opción inválida.Presione ENTER para volver a seleccionar. ")
            
            print("\n\n")

#Carga usuario
carga_usuarios()

# Ejecutar el menú
menu()