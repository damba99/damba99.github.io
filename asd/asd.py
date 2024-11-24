import json

# Ruta del archivo SQL de entrada
sql_file_path = r"C:\Users\bauer\OneDrive\Escritorio\Nueva carpeta\damba99.github.io\asd\estado.sql"

# Leer el archivo SQL con codificación utf-8
try:
    with open(sql_file_path, 'r', encoding='utf-8') as file:
        # Leer todas las líneas
        sql_data = file.readlines()
except UnicodeDecodeError:
    print("Error de codificación al intentar leer el archivo.")
    exit(1)

# Lista para guardar los datos convertidos a JSON
json_data = []

# Procesar cada línea del archivo SQL
for line in sql_data:
    # Limpiar la línea y eliminar paréntesis
    line = line.strip().replace('(', '').replace(')', '').replace(',', '')
    
    # Separar por comas
    parts = line.split()
    
    # Crear un diccionario con los datos
    entry = {
        "id": parts[0],
        "pais_id": parts[1],
        "nombre": ' '.join(parts[2:])
    }
    
    # Añadir al JSON
    json_data.append(entry)

# Escribir el JSON a un archivo
json_file_path = r"C:\Users\bauer\OneDrive\Escritorio\Nueva carpeta\damba99.github.io\asd\estado.json"
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

print(f"Archivo JSON guardado en {json_file_path}")
