#EJERCICIO8
'''Usa mpi4py para implementar un broadcast donde un proceso envía 
datos a todos los demás procesos en el comunicador.'''
# Importamos el módulo MPI de la biblioteca mpi4py
from mpi4py import MPI

# Creamos un objeto comunicador global que representa la comunicación entre todos los procesos
comm = MPI.COMM_WORLD

# Obtenemos el identificador de rango (rank) del proceso actual dentro del comunicador
rank = comm.Get_rank()

# Si el rango es 0 (proceso raíz), definimos un diccionario de datos
if rank == 0:
    data = {'key1': 'value1', 'key2': 'value2'}
# Si el rango no es 0, inicializamos data como None
else:
    data = None

# Realizamos una operación de broadcast para enviar los datos desde el proceso raíz a todos los demás procesos
data = comm.bcast(data, root=0)

# Cada proceso imprime su rango y los datos recibidos después del broadcast
print(f"Rank {rank} received data: {data}")