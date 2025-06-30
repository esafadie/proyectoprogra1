import re
import json

def generar_id_producto(archivo_productos):
    max_id = 0
    try:
        with open(archivo_productos, "r", encoding="utf-8") as f:
            productos = json.load(f)
            for producto in productos:
                if "ID" in producto and re.match(r"PR\d{3}", producto["ID"]):
                    num = int(producto["ID"][2:])  # Extraer el número
                    if num > max_id:
                        max_id = num
    except FileNotFoundError:
        pass
    return f"PR{max_id + 1:03}"

def cargar_productos():

    archivo = "carga_de_informacion/productos.json"
    id_producto = generar_id_producto(archivo)
    print(f"ID generado automáticamente: {id_producto}")


    nombre = input("Nombre del producto: ")
    proveedor = input("Proveedor: ")
    while True:
        try:
            stock = int(input("Stock del producto: "))
            if stock >= 0:
                break
            else:
                print("El stock debe ser un número entero no negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero no negativo.")
            
    nuevo_producto = {
        "ID": id_producto,
        "nombre": nombre,
        "proveedor": proveedor,
        "stock": stock
    }

    try:
        with open(archivo,'r') as f:
            lista = json.load(f)
    except FileNotFoundError:
        lista = []
        
    lista.append(nuevo_producto)
   
    with open(archivo,"w") as f:
        json.dump(lista,f)
    
    print(f"\nProducto {nombre} cargado exitosamente con ID {id_producto}.")
    print(f"Proveedor: {proveedor}, Stock: {stock}")
    
    return nuevo_producto