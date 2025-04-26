import re

def carga_usuario():
    usuario = input("Digite su Usuario (Formato: US001) ")
    while not re.match(r'^US[0-9]{3}$', usuario):
        usuario = input("Digite un usuario (Formato: US001)")
    print()
    return
