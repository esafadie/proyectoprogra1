import re

def carga_usuarios():
    lista_usuarios = []
    emails_cargados = set()  # Para evitar emails repetidos
    cantidad = int(input("Ingrese la cantidad de usuarios a cargar: "))

    for _ in range(cantidad):
        email = input("Ingrese el email del usuario: ")
        # Validamos que el email sea correcto y no repetido
        while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) or email in emails_cargados: #
            email = input("Email inválido o repetido. Ingrese otro: ")

        nombre = input("Nombre del usuario: ")
        edad = int(input("Edad: "))

        matriz = (email, {"nombre": nombre, "edad": edad})
        lista_usuarios.append(matriz)
        emails_cargados.add(email)
    return lista_usuarios
