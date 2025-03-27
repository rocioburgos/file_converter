########################
## Convierte un archivo csv a xlsx
## pip install -r requirements.txt    
## modo de uso : python convertidor.py path_archivo_csv/txt.csv
##               python csv_to_excel.py archivo.txt -o salida.xlsx
#excel : 39sg
# pandas: 28.95 seg
# spark 46.35seg
##########################

from pyspark.sql import SparkSession
import pandas as pd
import os
import argparse

def convert_to_excel_spark(input_file, excel_file=None, delimiter=None):
    """Convierte archivos CSV o TXT en Excel usando PySpark."""
    try:
        # Crear sesión de Spark 
        spark = SparkSession.builder.appName("CSVtoExcel").getOrCreate()

        # Detectar la extensión del archivo
        file_extension = os.path.splitext(input_file)[1].lower()

        # Leer el archivo con Spark
        if file_extension in [".csv", ".txt"]:
            if delimiter:
                df_spark = spark.read.option("header", "true").option("delimiter", delimiter).csv(input_file, mode="DROPMALFORMED")
            else:
                df_spark = spark.read.option("header", "true").option("delimiter", ",").csv(input_file, mode="DROPMALFORMED")
        else:
            print("❌ Error: El archivo debe ser .csv o .txt")
            return

        # Convertir el DataFrame de Spark a Pandas (para guardarlo como Excel)
        df_pandas = df_spark.toPandas()

        # Si no se especifica un nombre de salida, usa el mismo nombre con .xlsx
        if not excel_file:
            excel_file = input_file.replace(file_extension, ".xlsx")

        # Guardar el DataFrame en un archivo Excel sin índice
        df_pandas.to_excel(excel_file, index=False, engine='openpyxl')

        print(f"✅ Archivo convertido exitosamente: {excel_file}")

    except Exception as e:
        print(f"❌ Error al procesar el archivo: {e}")

def main():
    """Función principal para ejecutar desde la consola."""
    parser = argparse.ArgumentParser(description="Convierte archivos CSV o TXT a Excel (.xlsx) usando Spark")
    parser.add_argument("input_file", help="Ruta del archivo de entrada (.csv o .txt)")
    parser.add_argument("-o", "--output", help="Ruta del archivo de salida (.xlsx)", default=None)
    parser.add_argument("-d", "--delimiter", help="Delimitador del archivo de entrada ", default=',')

    args = parser.parse_args()
    convert_to_excel_spark(args.input_file, args.output, args.delimiter)

if __name__ == "__main__":
    main() 