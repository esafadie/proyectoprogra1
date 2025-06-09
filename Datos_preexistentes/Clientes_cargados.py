cliente_cargado = [
    ["CL001", "Lucía Fernández", "1123456789"],
    ["CL002", "Martín Gómez", "1134567890"],
    ["CL003", "Sofía Martínez", "1145678901"],
    ["CL004", "Diego Rivas", "1156789012"],
    ["CL005", "Valentina López", "1167890123"]
]
try:
    with open("cliente_cargado.txt", "w", encoding="utf-8") as archivo: #Crear achivo de texto
        # Escribir encabezado
        archivo.write(f"{'ID':<8} {'Nombre':<25} {'Teléfono':<15}\n")
        archivo.write("-" * 50 + "\n")
        # Escribir datos
        for cliente in cliente_cargado:
            archivo.write(f"{cliente[0]:<8} {cliente[1]:<25} {cliente[2]:<15}\n")
    print("Archivo 'cliente_cargado.txt' creado correctamente.")
except Exception as e:
    print("Ocurrió un error al crear el archivo:", e)