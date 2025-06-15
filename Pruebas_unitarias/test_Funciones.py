from Funciones import cargar_cliente,dar_de_baja_cliente

import re


ids_cargados = set()


# Pruebas Unitarias de Cargar Clientes ===

def test_cargar_valido():
    archivo = "clientes_test.txt"
    open(archivo, "w").close()  # limpiar
    ids = set()
    resultado = cargar_cliente("CL001", "Juan Perez", "123456789", archivo, ids)
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
    assert resultado == "Cliente cargado"
    assert contenido == "CL001;Juan Perez;123456789"

def test_cargar_id_invalido():
    archivo = "clientes_test.txt"
    open(archivo, "w").close()
    ids = set()
    resultado = cargar_cliente("XX01", "Ana", "111", archivo, ids)
    assert resultado == "ID inválido"

def test_cargar_id_repetido():
    archivo = "clientes_test.txt"
    open(archivo, "w").close()
    ids = {"CL001"}
    resultado = cargar_cliente("CL001", "Juan Perez", "123456789", archivo, ids)
    assert resultado == "ID repetido"

def test_dar_de_baja_cliente():
    archivo = "clientes_test.txt"
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("CL001;Juan;123\nCL002;Ana;456\n")
    resultado = dar_de_baja_cliente("CL002", archivo)
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
    assert resultado == "Cliente eliminado"
    assert "CL001" in contenido
    assert "CL002" not in contenido
