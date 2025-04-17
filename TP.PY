

def generar_productos(cantidad_productos):
    lista = []
    Talle_valido = False
    Talle_permitidos = ["xs","s","m","l",'xl']
    for i in range(cantidad_productos):
        id = int(input("Digite el ID del producto: "))
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

def generar_proveedor(cantidad_proveedores): #Hace falta esto? 
    lista = []

    for i in range(cantidad_proveedores):
        mini_lista = []
        Nombre = input("Digite el nombre del proveedor: ") 
        Apellido = input("Digite el apellido del proveedor: ") #Pedir nombre y apellido directo
        Telefono = input("Digite el numero del proveedor: ")
        Categoria = input("Digite la categoria de productos que comercializa: ")
        precio = int(input("Digite el precio por unidad: "))
        stock= int(input("Digite el stock disponible del proveedor: ")) #Que es esto?
        print()

        mini_lista.append(Nombre)
        mini_lista.append(Apellido)
        mini_lista.append(Telefono)
        mini_lista.append(Categoria)
        mini_lista.append(precio)
        mini_lista.append(stock)

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
cantidad_proveedores = int(input("Digite la cantidad de proveedores a cargar: "))
lista_proveedores = generar_proveedor(cantidad_proveedores) #agregar a las opciones?

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
