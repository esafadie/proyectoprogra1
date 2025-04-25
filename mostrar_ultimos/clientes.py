def mostrar_ultimos_clientes(clientes):
    if not clientes:
            print("No hay clientes cargados")
            return
    ultimos = clientes[-3:]
    print("Últimos clientes cargados:")
    for p in ultimos:
        print(f"ID: {p[0]}, Nombre: {p[1]}, Telefono: {p[2]}")