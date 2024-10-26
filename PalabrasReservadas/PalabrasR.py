import csv
import keyword
from collections import Counter

# Especifica la ruta del archivo
archivo_py = "C:\\Users\\alzuk\\OneDrive\\Escritorio\\Probabilidad\\PalabrasReservadas\\generic.py"


# Obtener las palabras reservadas de Python
palabras_reservadas = set(keyword.kwlist)

# Contar las palabras reservadas en el archivo
contador_reservadas = Counter()

# Leer y contar las palabras reservadas en el archivo
with open(archivo_py, 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        palabras = linea.split()
        for palabra in palabras:
            if palabra in palabras_reservadas:
                contador_reservadas[palabra] += 1

# Guardar los resultados en un archivo CSV
ruta_csv = "PalabrasReservadas\conteoPR.csv"
with open(ruta_csv, mode="w", newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Palabra_Reservada", "Frecuencia"])
    for palabra, frecuencia in contador_reservadas.items():
        escritor_csv.writerow([palabra, frecuencia])

print(f"El conteo se ha guardado en '{ruta_csv}'")
