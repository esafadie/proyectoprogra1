import re
import json

def submenu_modificacion_producto(prod):
    print("\n¿Qué desea modificar?")
    print("1. Nombre")
    print("2. Proveedor")
    print("3. Stock")
    print("4. Todos los campos")
    print("5. Volver al menú principal")
    try:
        try:
            opcion = int(input("Seleccione una opción: "))
            if not 1 <= opcion <= 5:
                print("Opción inválida. No se realizaron modificaciones.")
                return False
        except ValueError:
            print("Debe ingresar un número válido. Se volverá al menú principal.")
            return False
        
        if opcion == 1:
            prod['nombre'] = input("Nuevo nombre del producto: ")
        elif opcion == 2:
            prod['proveedor'] = input("Nuevo proveedor del producto: ")
        elif opcion == 3:
            while True:
                try:
                    prod['stock'] = int(input("Nuevo stock del producto: "))
                    if prod['stock'] <= 0:
                        print("El stock tiene que ser positivo. Intente nuevamente.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Se esperaba un número entero.")
        elif opcion == 4:
            prod['nombre'] = input("Nuevo nombre del producto: ")
            prod['proveedor'] = input("Nuevo proveedor del producto: ")
            while True:
                try:
                    prod['stock'] = int(input("Nuevo stock del producto: "))
                    if prod['stock'] <= 0:
                        print("El stock tiene que ser positivo. Intente nuevamente.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Se esperaba un número entero.")
        elif opcion == 5:
            print("\n\nModificación cancelada.")
            print("Volviendo al menú principal...")
            return False
        else:
            print("Opción inválida. No se realizaron modificaciones.")
            return False
        return True
    except ValueError:
        print("Entrada inválida. Se esperaba un número.")
        return False
    
def modificar_producto(archivo):
    try:
        with open(archivo,"r",encoding="utf-8") as arch:
            productos = json.load(arch)
            
        if not productos:
            print("No hay productos cargados.")
            return
        
        id_producto = ('PR' + input("ID del producto a modificar (Formato 001): "))
        while not re.match(r'^PR[0-9]{3}$', id_producto):
            id_producto = ('PR' + input("ID inválido o repetido. Ingrese otro (Formato 001): "))

        producto_encontrado = False

        for prod in productos:
            if prod['ID'] == id_producto:
                producto_encontrado = True
                producto_original = prod.copy()  # Guardar el producto original
                print(f"\nProducto encontrado: {prod['ID']}")
                print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
                print(f"{prod['ID']:<10}{prod['nombre']:<20}{prod['proveedor']:<20}{prod['stock']:<10}")
                print("-" * 60)
                if submenu_modificacion_producto(prod):
                    print("\nProducto original:")
                    print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
                    print(f"{producto_original['ID']:<10}{producto_original['nombre']:<20}{producto_original['proveedor']:<20}{producto_original['stock']:<10}")
                    print("-" * 60)
                    print("\nProducto modificado exitosamente")
                    print(f"\nProducto actualizado:")
                    print(f"{'ID':<10}{'Nombre':<20}{'Proveedor':<20}{'Stock':<10}")
                    print(f"{prod['ID']:<10}{prod['nombre']:<20}{prod['proveedor']:<20}{prod['stock']:<10}")
                break

            
        if not producto_encontrado:
            print("\nERROR: Producto inexistente")
            print("No se modificó ningún producto")

        
        with open(archivo, "w", encoding="utf-8") as modificar:
            json.dump(productos, modificar)
    except OSError:
        print("No se puede abrir el archivo")
    
    