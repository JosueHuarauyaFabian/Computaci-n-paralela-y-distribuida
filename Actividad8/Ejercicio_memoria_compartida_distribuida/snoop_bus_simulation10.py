import threading
import time

# Memoria compartida simulada
shared_memory = [0] * 10
# Lista para registrar las operaciones en el bus
bus_operations = []
# Cerradura para sincronizar el acceso al bus
bus_lock = threading.Lock()

# Clase Cache para simular una caché de CPU
class Cache:
    def __init__(self, id):
        self.id = id
        self.cache = [0] * 10  # Inicializa la caché con 10 ceros

    # Método para leer un valor de la caché
    def read(self, index):
        with bus_lock:  # Adquiere el bloqueo del bus
            bus_operations.append((self.id, 'read', index))  # Registra la operación de lectura
        return self.cache[index]

    # Método para escribir un valor en la caché
    def write(self, index, value):
        with bus_lock:  # Adquiere el bloqueo del bus
            bus_operations.append((self.id, 'write', index, value))  # Registra la operación de escritura
        self.cache[index] = value  # Escribe el valor en la caché

    # Método para realizar snooping (monitorización) de las operaciones en el bus
    def snoop(self):
        while True:
            with bus_lock:  # Adquiere el bloqueo del bus
                if bus_operations:  # Si hay operaciones en el bus
                    op = bus_operations.pop(0)  # Toma la primera operación en la lista
                    if op[1] == 'write':  # Si es una operación de escritura
                        self.cache[op[2]] = op[3]  # Actualiza la caché con el valor escrito
            time.sleep(0.01)  # Espera un breve periodo antes de continuar

# Función para simular una tarea de CPU que escribe y luego lee desde la caché
def cpu_task(cache, index, value):
    cache.write(index, value)  # Escribe un valor en la caché
    print(f"CPU {cache.id} wrote {value} at index {index}")
    time.sleep(1)  # Espera un segundo
    read_value = cache.read(index)  # Lee el valor de la caché
    print(f"CPU {cache.id} read {read_value} from index {index}")

# Función principal para configurar y ejecutar las simulaciones
def main():
    caches = [Cache(i) for i in range(4)]  # Crea cuatro cachés de CPU
    threads = []

    # Inicia un hilo para la función snoop de cada caché
    for cache in caches:
        t = threading.Thread(target=cache.snoop)
        t.daemon = True  # Marca el hilo como un hilo daemon para que termine cuando el programa principal termine
        t.start()

    # Inicia un hilo para la tarea de CPU de cada caché
    for i, cache in enumerate(caches):
        t = threading.Thread(target=cpu_task, args=(cache, i % 10, i))
        threads.append(t)
        t.start()

    # Espera a que todos los hilos de tarea de CPU terminen
    for t in threads:
        t.join()

# Punto de entrada del script
if __name__ == "__main__":
    main()