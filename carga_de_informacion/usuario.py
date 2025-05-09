import re

def carga_usuarios():
    emails_cargados = set()  # Para evitar emails repetidos

    nombre = input("Nombre del usuario: ")
    email = input("Ingrese el email del usuario: ")

    # Validamos que el email sea correcto y no repetido
    while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) or email in emails_cargados:
        email = input("Email invalido o repetido. Ingrese otro: ")

    usuario = {"email": email, "nombre": nombre}
    emails_cargados.add(email)

    print(f"Bienvenido {nombre}")
    return usuario
