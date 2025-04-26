def mostrar_ultimas_ventas(ventas):
    if not ventas:
            print("No hay ventas cargadas")
            return
    ultimos = ventas[-3:]
    print("Últimas ventas cargadas:")
    for p in ultimos:
        print(f"ID VENTA: {p[0]}, ID CLIENTE: {p[1]}, ID PRODUCTO: {p[2]}, CANTIDAD: {p[3]}")