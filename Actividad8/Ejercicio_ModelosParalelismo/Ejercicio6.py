import concurrent.futures
import os

# Función para contar las palabras en un archivo
def count_words_in_file(file_path):
    # Abrir el archivo en modo lectura
    with open(file_path, 'r', encoding='utf-8') as file:
        # Leer el contenido del archivo
        text = file.read()
    # Contar las palabras dividiendo el texto por espacios
    word_count = len(text.split())
    # Retornar una tupla con la ruta del archivo y el conteo de palabras
    return (file_path, word_count)

# Función para contar las palabras en múltiples archivos en paralelo
def parallel_word_count(file_paths):
    results = {}  # Diccionario para almacenar los resultados
    # Usar ThreadPoolExecutor para ejecutar tareas en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Crear un diccionario de tareas futuras
        future_to_file = {executor.submit(count_words_in_file, file_path): file_path for file_path in file_paths}
        # A medida que las tareas se completen, obtener los resultados
        for future in concurrent.futures.as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                # Obtener el resultado de la tarea completada
                file_path, count = future.result()
                # Almacenar el resultado en el diccionario
                results[file_path] = count
            except Exception as exc:
                # Manejar cualquier excepción que ocurra durante la ejecución de la tarea
                print(f"{file_path} generated an exception: {exc}")
    # Retornar el diccionario con los resultados
    return results

# Lista de archivos de ejemplo descargados
file_paths = ["/home/josue-huarauya/Documentos/CPyD/Computaci-n-paralela-y-distribuida/Actividad8/Ejercicio_ModelosParalelismo/Frankenstein.txt",
              "/home/josue-huarauya/Documentos/CPyD/Computaci-n-paralela-y-distribuida/Actividad8/Ejercicio_ModelosParalelismo/Moby_Dick.txt", 
              "/home/josue-huarauya/Documentos/CPyD/Computaci-n-paralela-y-distribuida/Actividad8/Ejercicio_ModelosParalelismo/Romeo_Julieta.txt"]

# Ejecutar la función de conteo de palabras en paralelo
word_counts = parallel_word_count(file_paths)
print(word_counts)