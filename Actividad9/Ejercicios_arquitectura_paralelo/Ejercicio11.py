#EJERCICIO 
'''Usa MPI para recolectar y combinar los resultados de datos procesados en 
paralelo utilizando OpenMP en cada nodo.''' #https://pypi.org/project/mpi4py/

# Importamos el módulo MPI de la biblioteca mpi4py para utilizar MPI en Python
from mpi4py import MPI

# Importamos la clase Thread del módulo threading para crear hilos de ejecución paralelos
from threading import Thread

# Definimos una función que calcula el cuadrado de un valor y lo almacena en una lista de resultados
def compute_square(value, result_list, index):
   result_list[index] = value ** 2

# Creamos un objeto Comm que representa el comunicador global de MPI (incluye todos los procesos)
comm = MPI.COMM_WORLD

# Obtenemos el rango (identificador) del proceso actual dentro del comunicador
rank = comm.Get_rank()

# Obtenemos el número total de procesos en el comunicador
size = comm.Get_size()

# Inicializamos la variable data como None
data = None

# Si el proceso actual es el proceso raíz (rango 0)
if rank == 0:
   # Creamos una lista de números del 1 al 100
   data = list(range(1, 101))
   
   # Calculamos el tamaño del segmento de datos que se asignará a cada proceso
   segment_size = len(data) // size
   
   # Dividimos la lista de datos en segmentos más pequeños, uno para cada proceso
   data_segments = [data[i * segment_size:(i + 1) * segment_size] for i in range(size)]

# Si el proceso actual no es el proceso raíz, establecemos data_segments como None
else:
   data_segments = None

# Utilizamos la operación scatter de MPI para distribuir los segmentos de datos a los diferentes procesos
# El proceso raíz (rango 0) envía los segmentos, y cada proceso recibe su segmento correspondiente
data_segment = comm.scatter(data_segments, root=0)

# Creamos una lista vacía para almacenar los resultados del cálculo del cuadrado para el segmento de datos asignado a este proceso
results = [0] * len(data_segment)

# Creamos una lista vacía para almacenar los hilos de ejecución
threads = []

# Iteramos sobre el segmento de datos asignado a este proceso
for i in range(len(data_segment)):
   '''Creamos un hilo de ejecución que llama a la función compute_square con el valor 
   actual del segmento de datos, la lista de resultados y el índice correspondiente'''
   t = Thread(target=compute_square, args=(data_segment[i], results, i))
   
   # Agregamos el hilo creado a la lista de hilos
   threads.append(t)
   
   # Iniciamos la ejecución del hilo
   t.start()

# Esperamos a que todos los hilos terminen su ejecución
for t in threads:
   t.join()

# Utilizamos la operación gather de MPI para recolectar los resultados de todos los procesos en el proceso raíz (rango 0)
gathered_results = comm.gather(results, root=0)

if rank == 0:
    # Si el proceso actual es el proceso raíz (rango 0)
    
    # Creamos una nueva lista 'final_results' combinando todas las sublistas de 'gathered_results'
    # 'gathered_results' es una lista de listas, donde cada sublista contiene los resultados de un proceso
    # La comprensión de listas 'item for sublist in gathered_results for item in sublist' itera sobre cada sublista
    # y luego sobre cada elemento de esa sublista, creando una nueva lista 'final_results' con todos los elementos
    final_results = [item for sublist in gathered_results for item in sublist]
    
    # Imprimimos la lista 'final_results', que contiene todos los resultados combinados de todos los procesos
    print(f"Final results: {final_results}")
