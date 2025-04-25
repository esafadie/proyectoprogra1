def mostrar_ultimas_compras(compras):
    if not compras:
            print("No hay compras cargadas")
            return
    ultimos = compras[-3:]
    print("Últimas compras cargadas:")
    for p in ultimos:
        print(f"ID COMPRA: {p[0]}, ID PRODUCTO: {p[1]}, CANTIDAD: {p[2]}, PROVEEDOR: {p[3]}")