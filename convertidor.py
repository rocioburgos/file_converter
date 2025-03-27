########################
## Convierte un archivo csv a xlsx
## 
##########################
import pandas as pd

def csv_to_excel(csv_file, excel_file=None):
    try:
        # Leer el CSV con delimitador ","
        df = pd.read_csv(csv_file, delimiter=",")

        # Si no se especifica un nombre para el archivo de salida, usa el mismo nombre con .xlsx
        if not excel_file:
            excel_file = csv_file.replace('.csv', '.xlsx')

        # Guardar el DataFrame en un archivo Excel sin el índice
        df.to_excel(excel_file, index=False, engine='openpyxl')

        print(f"Archivo convertido exitosamente: {excel_file}")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    csv_file = input("Ingrese la ruta del archivo CSV: ")
    csv_to_excel(csv_file)
