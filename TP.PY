import re

def generar_productos(cantidad_productos):
    lista = []
    Talle_valido = False
    Talle_permitidos = ["xs","s","m","l",'xl']
    for i in range(cantidad_productos):
        id = (input("Digite el ID del producto: "))
        
        nombre = input("Digite el nombre del producto: ")
        categoria = input("Digite categoria del producto: ").lower()
        precio = int(input("Digite el precio del producto: "))
        stock = int(input("Digite el stock del producto: "))
        
        while not Talle_valido: #corregir tema talles, necesito diccionario?
          talle = input("Digite el talle del producto: ").lower()
          if talle in Talle_permitidos:
            Talle_valido = True
          else:
           print("Talle inválido. Intente nuevamente") 
            
        mini_lista = [id, nombre, categoria, precio, stock, talle] #Yo haria la lista asi para ahorrar lineas.
        lista.append(mini_lista)

    return lista

def Pedir_Mercaderia(cantidad_proveedores): #Hace falta esto? 
    lista = []

    for i in range(cantidad_proveedores):
        Nombre = input("Digite el nombre del proveedor: ") 
        Id_producto = input("Digite el id del producto: ") #Pedir nombre y apellido directo
        if re.match(r'^[A-Za-z]{2}[0-9]{3}$', Id_producto) is None:
            while re.match(r'^[A-Za-z]{2}[0-9]{3}$', Id_producto) is None:
                Id_producto = input("ID inválido. Debe contener dos letras seguidas de tres números: ")
            print("ID inválido. Debe contener solo números.")
        else:
            print("ID válido.")
        Cant_prod = int(input("Digite la cantidad de productos: "))
        print()

        mini_lista = [Nombre,Id_producto,Cant_prod]        
        lista.append(mini_lista)
    return lista


def verificar_stock_compra(Cant_comprar,categoria,lista): #no entendi funcion
    booleano = True
    stock = 0
    for i in lista:
        if i[2].lower() == categoria.lower():
            if i[4] >= Cant_comprar:
                booleano=True
            else:
                booleano=False
                stock = i[4]
    return booleano, stock


def generar_clientes(lista_productos):
    lista = []

    mini_lista = []
    Nombre = input("Digite el nombre del cliente: ")
    Apellido = input("Digite el apellido del cliente: ") #nombre y apellido directo
    dni = int(input("Digite el dni del cliente: "))
    Telefono = int(input("Digite el telefono del cliente:"))
    categoria = input("Digite la categoria del producto: ") #La categoria no importa, importa el id.
    cantidad = int(input("Digite la cantidad a comprar: ")) #Es para mayoristas?
    verificar, stock = verificar_stock_compra(cantidad,categoria,lista_productos) #no entiendo esta parte
    while verificar==False: #se puede ahorrar este while? y ponerlo en la funcion anterior
        print(f"Cantidad no disponible, stock actual: {stock}") 
        cantidad = int(input("Digite la cantidad a comprar: "))
    print()

    mini_lista.append(Nombre)
    mini_lista.append(Apellido)
    mini_lista.append(dni)
    mini_lista.append(Telefono)
    mini_lista.append(categoria)
    mini_lista.append(cantidad)
        

    lista.append(mini_lista)
    return lista

#ACA NO EMPIEZA EL PROGRAMA PRINCIPAL?
cantidad_productos = int(input("Digite la cantidad de productos a cargar: "))
lista_productos = generar_productos(cantidad_productos) #Agregar a las opciones?
print()
 #agregar a las opciones?

#MENU

elegir_opcion= int(input("""
1. Cargar Cliente
2. Ver informacion segun ID de producto
3. 
4.
5.
6.
7. Salir
Eliga una opcion: """))

#CARGA DE FUNCION
while elegir_opcion!=7:
    if elegir_opcion == 1:
        clientes = []
        lista_clientes = generar_clientes(lista_productos)
        clientes.append(lista_clientes)
    elif elegir_opcion == 2:
        id = int(input("Digite el ID del producto: "))
        for i in lista_productos:
            if i[0] == id:
                print(f"id: {i[0]} Categoria:{i[2]} Precio por unidad:{i[3]} Stock:{i[4]}")
