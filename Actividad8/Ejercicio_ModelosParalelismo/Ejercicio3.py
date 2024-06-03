import dask.dataframe as dd

# Función para procesar archivos CSV en paralelo y calcular el promedio de una columna específica
def parallel_csv_processing(file_paths):
    # Leer varios archivos CSV en paralelo con Dask
    df = dd.read_csv(file_paths)
    # Calcular el promedio de la columna 'target_column' y computar el resultado
    average_value = df['target_column'].mean().compute()
    return average_value

# Lista de rutas de archivos CSV
file_paths = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv']

# Ejecutar la función de procesamiento paralelo y calcular el promedio
average = parallel_csv_processing(file_paths)
print(f"Average value: {average}")
