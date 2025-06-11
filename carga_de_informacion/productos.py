import re
import json

Id_cargado = set()
def cargar_productos():

    id_producto = input("ID del producto (formato PR001): ")
    while not re.match(r'^PR[0-9]{3}$', id_producto) or id_producto in Id_cargado: 
        id_producto = input("ID inválido o repetido. Ingrese otro (ej: PR001): ")

    nombre = input("Nombre del producto: ")
    proveedor = input("Proveedor: ")
    stock = int(input("Stock del producto: "))
    encabezados = ['ID','nombre','proveedor','stock']
    matriz = [id_producto, nombre, proveedor, stock]
    Id_cargado.add(id_producto)
    diccionario = (dict(zip(encabezados,matriz)))

    try:
        with open('carga_de_informacion/productos.json','r') as f:
            lista = json.load(f)
    except FileNotFoundError:
        lista = []
    lista.append(diccionario)
   
    with open("carga_de_informacion/productos.json","w") as f:
        json.dump(lista,f)
