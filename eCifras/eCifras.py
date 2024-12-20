import time
from mpmath import mp
from tqdm import tqdm
import sys

def calcular_e_gb(tamano_gb):
    # Convertir tamaño en GB a bytes
    tamano_bytes = int(tamano_gb * (1024**3))  # 1 GB = 1024^3 bytes
    digitos = tamano_bytes - 2  # Restar los caracteres "2."
    
    # Configurar la precisión en dígitos
    mp.dps = digitos  # Precisión en dígitos decimales
    
    # Calcular e con la precisión requerida
    print(f"Calculando {digitos} dígitos de e (~{tamano_gb} GB)...")
    e = str(mp.e)  # Convertir e a cadena

    # Establecer el bloque de escritura
    bloque = 10**6  # Escribir en bloques de 1 millón de caracteres
    total_bloques = len(e) // bloque + (1 if len(e) % bloque != 0 else 0)
    
    # Abrir archivo para escritura
    with open("e_1gb.txt", "w") as archivo:
        start_time = time.time()  # Tiempo de inicio
        # Barra de progreso usando tqdm
        for i in tqdm(range(total_bloques), desc="Guardando cifras", file=sys.stdout, ncols=100):
            inicio = i * bloque
            fin = inicio + bloque
            archivo.write(e[inicio:fin])  # Escribir un bloque al archivo

            # Calcular el tiempo transcurrido y estimar el tiempo restante
            elapsed_time = time.time() - start_time
            time_per_block = elapsed_time / (i + 1)  # Promedio por bloque
            remaining_blocks = total_bloques - (i + 1)
            remaining_time = time_per_block * remaining_blocks
            
            # Mostrar la cuenta regresiva
            minutes, seconds = divmod(int(remaining_time), 60)
            print(f"\rTiempo restante: {minutes:02}:{seconds:02}", end="")  # Actualizar la línea con \r
            
        print()  # Nueva línea al final de la barra

    print(f"Cálculo completado: {len(e) - 2} dígitos escritos en 'e_1gb.txt'.")

# Calcular 0.0001 GB de cifras de e y guardarlo en un archivo
calcular_e_gb(.01)
