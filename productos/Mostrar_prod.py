
def mostrar_productos(productos, indice=0): #recursividad
    if indice >= len(productos):
        return #caso base: Cuando el índice alcanza el largo de la lista, se detiene la recursión
    p = productos[indice]
    print(f"{p['ID']:<10}{p['nombre']:<20}{p['proveedor']:<20}{p['stock']:<10}")
    mostrar_productos(productos, indice + 1) #Caso recursivo: La función se llama a sí misma avanzando al siguiente índice.