#EJERCICIO10
'''Analiza la estrategia de prefetching de datos en un entorno paralelo'''

# Importamos la clase ThreadPoolExecutor del módulo concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import random
import numpy as np
# Función que define el comportamiento del trabajador encargado de realizar el prefetching
def prefetching_worker(array, indices, prefetch_distance):
    # Iteramos sobre los índices, realizando prefetching y acceso a los elementos
    for i in range(len(indices) - prefetch_distance):
        # Realizamos el prefetching, accediendo a un elemento del arreglo prefetch_distance posiciones adelante
        _ = array[indices[i + prefetch_distance]]  # Prefetch
        # Accedemos y modificamos el elemento del arreglo en la posición actual
        array[indices[i]] += 1  # Access

# Establecemos el tamaño del arreglo (un millón de elementos)
size = 10**6
# Creamos un arreglo de un millón de ceros
array = np.zeros(size)
# Creamos una lista con los índices del arreglo (0 a 999,999)
indices = list(range(size))
# Mezclamos aleatoriamente los índices
random.shuffle(indices)
# Establecemos la distancia de prefetching en 10
prefetch_distance = 10

# Creamos un ThreadPoolExecutor con un máximo de 4 hilos trabajadores
with ThreadPoolExecutor(max_workers=4) as executor:
    # Dividimos la lista indices en 4 partes iguales
    # y enviamos cada parte a un hilo trabajador utilizando executor.submit
    futures = [executor.submit(prefetching_worker, array, indices[i::4], prefetch_distance) for i in range(4)]
    # Esperamos a que todas las tareas enviadas a los hilos trabajadores se completen
    for future in futures:
        future.result()

# Imprimimos un mensaje indicando que el prefetching se ha completado
print(f"Prefetching completado")