########################
## Convierte un archivo csv a xlsx
## pip install -r requirements.txt    
## modo de uso : python convertidor.py path_archivo_csv/txt.csv
##               python csv_to_excel.py archivo.txt -o salida.xlsx
#excel : 39sg
# pandas: 28.95 seg
# spark 46.35seg
##########################
import pandas as pd
import os
import argparse 

def convert_to_excel(input_file, excel_file=None):
    try:
          # Detectar la extensión del archivo
        file_extension = os.path.splitext(input_file)[1].lower()

        # Leer el archivo según su extensión
        if file_extension == ".csv":
            df = pd.read_csv(input_file, delimiter="|")  # CSV con delimitador ","
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

def main():
   
    """Función principal para ejecutar desde la consola."""
    parser = argparse.ArgumentParser(description="Convierte archivos CSV o TXT a Excel (.xlsx)")
    parser.add_argument("input_file", help="Ruta del archivo de entrada (.csv o .txt)")
    parser.add_argument("-o", "--output", help="Ruta del archivo de salida (.xlsx)", default=None)

    args = parser.parse_args()
    convert_to_excel(args.input_file, args.output)

if __name__ == "__main__":
    
    main()
