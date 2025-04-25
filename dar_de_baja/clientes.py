import re
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