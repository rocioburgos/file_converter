########################
## Convierte un archivo csv a xlsx
## pip install pandas openpyxl    
##########################
import pandas as pd
import os

def csv_to_excel(input_file, excel_file=None):
    try:
          # Detectar la extensión del archivo
        file_extension = os.path.splitext(input_file)[1].lower()

        # Leer el archivo según su extensión
        if file_extension == ".csv":
            df = pd.read_csv(input_file, delimiter=",")  # CSV con delimitador ","
        elif file_extension == ".txt":
            df = pd.read_csv(input_file, delimiter=",", engine="python")  # TXT con delimitador ","
        else:
            print("Error: El archivo debe ser .csv o .txt")
            return
 
        # Si no se especifica un nombre para el archivo de salida, usa el mismo nombre con .xlsx
        if not excel_file:
            excel_file = input_file.replace(file_extension, ".xlsx")

        # Guardar el DataFrame en un archivo Excel sin el índice
        df.to_excel(excel_file, index=False, engine='openpyxl')

        print(f"Archivo convertido exitosamente: {excel_file}")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    csv_file = input("Ingrese la ruta del archivo (.csv o .txt): ")
    csv_to_excel(csv_file)
