import concurrent.futures
import os

# Definir la función para contar palabras en un archivo
def count_words_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    word_count = len(text.split())
    return (file_path, word_count)

# Definir la función para contar palabras en paralelo
def parallel_word_count(file_paths):
    results = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(count_words_in_file, file_path): file_path for file_path in file_paths}
        for future in concurrent.futures.as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                file_path, count = future.result()
                results[file_path] = count
            except Exception as exc:
                print(f"{file_path} generated an exception: {exc}")
    return results

# Lista de archivos de ejemplo descargados
file_paths = ["/home/josue-huarauya/Documentos/CPyD/Computaci-n-paralela-y-distribuida/Actividad8/Ejercicio_ModelosParalelismo/Frankenstein.txt",
              "/home/josue-huarauya/Documentos/CPyD/Computaci-n-paralela-y-distribuida/Actividad8/Ejercicio_ModelosParalelismo/Moby_Dick.txt", 
              "/home/josue-huarauya/Documentos/CPyD/Computaci-n-paralela-y-distribuida/Actividad8/Ejercicio_ModelosParalelismo/Romeo_Julieta.txt"]

# Ejecutar la función de conteo de palabras en paralelo
word_counts = parallel_word_count(file_paths)
print(word_counts)