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

        nombre = input("Nombre del cliente: ")
        while not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$", nombre.strip()):
            print("Nombre inválido. Solo letras y espacios son permitidos.")
            nombre = input("Nombre del cliente: ")
            
        telefono = input("Teléfono (solo números, entre 6 y 15 dígitos): ")
        while not re.match(r"^\d{6,15}$", telefono.strip()):
            print("Teléfono inválido. Ingrese solo números (6-15 dígitos).")
            telefono = input("Teléfono (solo números, entre 6 y 15 dígitos): ")

        with open(archivo, "a", encoding="utf-8") as arch:
            arch.write(f"{id_cliente};{nombre};{telefono}\n")

        print("Cliente registrado con éxito.")

    except OSError:
        print("Cliente no registrado")
        print("ERROR: No se puede grabar el archivo")