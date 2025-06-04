import re

def carga_usuarios():

    nombre = input("Nombre del usuario: ")
    email = input("Ingrese el email del usuario: ")

    # Validamos que el email sea correcto y no repetido
    while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        email = input("Email invalido o repetido. Ingrese otro: ")

    usuario = {"email": email, "nombre": nombre}

    print(f"Bienvenido {nombre}")
    return usuario
