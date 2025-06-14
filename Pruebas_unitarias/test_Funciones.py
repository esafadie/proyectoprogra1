from Funciones import cargar_clientes,dar_de_baja_clientes

import re
import builtins
import os

ids_cargados = set()


# Pruebas Unitarias de Cargar Clientes ===

def test_id_valido():
    archivo = "clientes_test.txt"
    if os.path.exists(archivo):
        os.remove(archivo)

    entradas = iter(["CL001", "Juan Pérez", "123456789"])
    original_input = builtins.input
    builtins.input = lambda _: next(entradas)

    cargar_clientes(archivo)

    with open(archivo, "r", encoding="UTF-8") as f:
        lineas = f.readlines()
        assert lineas[-1].strip() == "CL001;Juan Pérez;123456789"

    os.remove(archivo)
    builtins.input = original_input


def test_id_invalido_luego_valido():
    archivo = "clientes_test.txt"
    if os.path.exists(archivo):
        os.remove(archivo)

    entradas = iter(["XX01", "CL002", "Ana Gómez", "987654321"])
    original_input = builtins.input
    builtins.input = lambda _: next(entradas)

    cargar_clientes(archivo)

    with open(archivo, "r", encoding="UTF-8") as f:
        lineas = f.readlines()
        assert lineas[-1].strip() == "CL002;Ana Gómez;987654321"

    os.remove(archivo)
    builtins.input = original_input


def test_id_repetido():
    archivo = "clientes_test.txt"
    if os.path.exists(archivo):
        os.remove(archivo)

    # Pre-cargar un ID válido
    ids_cargados.clear()
    ids_cargados.add("CL003")

    entradas = iter(["CL004", "Mario Gómez", "1122334455"])
    original_input = builtins.input
    builtins.input = lambda _: next(entradas)

    cargar_clientes(archivo)

    with open(archivo, "r", encoding="UTF-8") as f:
        lineas = f.readlines()
        assert lineas[-1].strip() == "CL004;Mario Gómez;1122334455"

    os.remove(archivo)
    builtins.input = original_input


#Pruebas unitarias de Dar de Bja Clientes

import os
import builtins

def test_dar_de_baja_clientes():
    archivo_test = "test_clientes.txt"

    datos_iniciales = [
        "CL001;Juan Perez;123456789\n",
        "CL002;Maria Gomez;987654321\n",
        "CL003;Carlos Diaz;555555555\n"
    ]

    with open(archivo_test, "w", encoding="UTF-8") as f:
        f.writelines(datos_iniciales)

    def mock_input(_):
        return "CL002"

    original_input = builtins.input
    builtins.input = mock_input

    try:
        dar_de_baja_clientes(archivo_test)

        with open(archivo_test, "r", encoding="UTF-8") as f:
            lineas = f.readlines()

        assert all("CL002" not in linea for linea in lineas)
        assert any("CL001" in linea for linea in lineas)
        assert any("CL003" in linea for linea in lineas)

    finally:
        builtins.input = original_input
        os.remove(archivo_test)
