import re

def generar_nuevo_id_cliente(archivo):
    max_id = 0
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if partes and re.match(r'^CL\d{3}$', partes[0]):
                    num = int(partes[0][2:])  # extrae el número después de "CL"
                    if num > max_id:
                        max_id = num
    except FileNotFoundError:
        pass  # si el archivo no existe, empieza desde 0
    return f"CL{max_id + 1:03}"


def cargar_clientes(archivo):
    try:
        id_cliente = generar_nuevo_id_cliente(archivo)
        print(f"ID generado automáticamente para cliente: {id_cliente}")

        while True:
            nombre = input("Nombre del cliente: ").strip()
            if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$", nombre):
                break
            else:
                print("Nombre inválido. Solo letras y espacios son permitidos.")

        while True:
            telefono = input("Teléfono (6 a 15 dígitos, solo números): ").strip()
            if re.match(r"^\d{6,15}$", telefono):
                break
            else:
                print("Teléfono inválido. Ingrese solo números entre 6 y 15 dígitos.")

        # Escribir el nuevo cliente siempre en una nueva línea
        lineas = []
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                lineas = f.readlines()
        except FileNotFoundError:
            pass
        
        agregar_salto = False
        if lineas and not lineas[-1].endswith('\n'):
            agregar_salto = True

        with open(archivo, "a", encoding="utf-8") as arch:
            if agregar_salto:
                arch.write('\n')
            arch.write(f"{id_cliente};{nombre};{telefono}\n")

        print("\nCliente registrado con éxito:")
        print(f"{'ID Cliente':<10}{'Nombre':<20}{'Teléfono':<10}")
        print(f"{id_cliente:<10}{nombre:<20}{telefono:<10}")

    except OSError:
        print("Error al guardar el cliente en el archivo.")
