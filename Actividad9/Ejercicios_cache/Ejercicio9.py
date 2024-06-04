#EJERCICIO9
'''Implementa una política de reemplazo aleatorio para una 
caché y simula el acceso a los datos.'''

# Importamos el módulo random para generar números aleatorios
import random

# Definimos la clase RandomCache
class RandomCache:
    # El método __init__ es el constructor de la clase
    def __init__(self, capacity):
        # Almacenamos la capacidad máxima de la caché
        self.capacity = capacity
        # Inicializamos un diccionario vacío para almacenar los elementos de la caché
        self.cache = {}

    # El método get se utiliza para obtener el valor asociado a una clave en la caché
    def get(self, key):
        # Utilizamos el método get del diccionario self.cache para buscar el valor correspondiente a la clave key
        # Si la clave no se encuentra en la caché, se devuelve -1 como valor predeterminado
        return self.cache.get(key, -1)

    # El método put se utiliza para almacenar un par clave-valor en la caché
    def put(self, key, value):
        # Verificamos si la clave key ya está en la caché
        if key not in self.cache:
            # Si la clave no está en la caché, verificamos si la caché ha alcanzado su capacidad máxima
            if len(self.cache) >= self.capacity:
                # Si la caché está llena, seleccionamos una clave de manera aleatoria
                evict = random.choice(list(self.cache.keys()))
                # Eliminamos la clave seleccionada aleatoriamente de la caché
                del self.cache[evict]
        # Almacenamos el nuevo par clave-valor en la caché
        self.cache[key] = value

# Simulación de acceso
# Creamos una instancia de RandomCache con una capacidad de 3 elementos
cache = RandomCache(3)
# Definimos una lista de operaciones de put (almacenar) y get (obtener) que se realizarán en la caché
operations = [("put", 1, "data1"), ("put", 2, "data2"), ("put", 3, "data3"), ("get", 1),
              ("put", 4, "data4"), ("get", 2), ("put", 5, "data5"), ("get", 3), ("get", 1)]

# Iteramos sobre cada operación en la lista operations
for op in operations:
    # Si la operación es "put" (almacenar)
    if op[0] == "put":
        # Llamamos al método put de la caché con la clave op[1] y el valor op[2]
        cache.put(op[1], op[2])
        # Imprimimos un mensaje indicando la operación realizada
        print(f"Put: {op[1]} -> {op[2]}")
    # Si la operación es "get" (obtener)
    elif op[0] == "get":
        # Llamamos al método get de la caché con la clave op[1]
        result = cache.get(op[1])
        # Imprimimos un mensaje indicando la operación y el resultado
        print(f"Get: {op[1]} -> {result}")
    # Después de cada operación, imprimimos el estado actual de la caché
    print(f"Estado de la caché: {list(cache.cache.items())}")