#EJERCICIO7
'''Implementa un patrón productor-consumidor usando multiprocessing.
Queue en Python. Crea varios procesos productores que pongan datos en 
la cola y varios procesos consumidores que lean y procesen esos datos.'''

# Importamos los módulos necesarios
from multiprocessing import Process, Queue
import time
import random

# Función que define el comportamiento de los productores
def producer(queue):
    # Genera 10 números aleatorios
    for _ in range(10):
        # Genera un número aleatorio entre 1 y 100
        item = random.randint(1, 100)
        # Coloca el número en la cola compartida
        queue.put(item)
        # Imprime el número generado
        print(f"Produced {item}")
        # Espera un tiempo aleatorio antes de generar el siguiente número
        time.sleep(random.random())

# Función que define el comportamiento de los consumidores
def consumer(queue):
    # Bucle infinito
    while True:
        # Extrae un elemento de la cola compartida
        item = queue.get()
        # Si el elemento es None (valor centinela), sale del bucle
        if item is None:
            break
        # Imprime el elemento consumido
        print(f"Consumed {item}")
        # Espera un tiempo aleatorio antes de consumir el siguiente elemento
        time.sleep(random.random())

# Punto de entrada del programa
if __name__ == "__main__":
    # Crea una instancia de la cola compartida
    queue = Queue()

    # Crea dos procesos productores y les pasa la cola como argumento
    producers = [Process(target=producer, args=(queue,)) for _ in range(2)]
    # Crea dos procesos consumidores y les pasa la cola como argumento
    consumers = [Process(target=consumer, args=(queue,)) for _ in range(2)]

    # Inicia los procesos productores
    for p in producers:
        p.start()

    # Inicia los procesos consumidores
    for c in consumers:
        c.start()

    # Espera a que todos los procesos productores terminen
    for p in producers:
        p.join()

    # Agrega valores centinela None a la cola para indicar a los consumidores que deben salir
    for _ in consumers:
        queue.put(None)

    # Espera a que todos los procesos consumidores terminen
    for c in consumers:
        c.join()