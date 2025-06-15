from Funciones import eliminar_por_id

productos = [
    {"ID": "PR001", "nombre": "Remera", "proveedor": "Diego Ramirez", "stock": 439},
    {"ID": "PR006", "nombre": "Medias", "proveedor": "Santiago Frias", "stock": 300},
    {"ID": "PR502", "nombre": "Pantalones", "proveedor": "Natalia Ramirez", "stock": 40},
    {"ID": "PR014", "nombre": "Guantes", "proveedor": "Natalia", "stock": 23},
    {"ID": "PR203", "nombre": "Gorros", "proveedor": "Joaquin Gimenez", "stock": 10},
    {"ID": "PR033", "nombre": "Zapatillas", "proveedor": "Ramiro Alvarez", "stock": 4}
]

def test_eliminar_producto_existente():
    resultado = eliminar_por_id(productos.copy(), "PR014")
    assert len(resultado) == 5
    assert all(p["ID"] != "PR014" for p in resultado)

def test_eliminar_producto_inexistente():
    resultado = eliminar_por_id(productos.copy(), "PR999")
    assert len(resultado) == 6
    assert resultado == productos

def test_eliminar_primer_producto():
    resultado = eliminar_por_id(productos.copy(), "PR001")
    assert len(resultado) == 5
    assert all(p["ID"] != "PR001" for p in resultado)

def test_eliminar_ultimo_producto():
    resultado = eliminar_por_id(productos.copy(), "PR033")
    assert len(resultado) == 5
    assert all(p["ID"] != "PR033" for p in resultado)
