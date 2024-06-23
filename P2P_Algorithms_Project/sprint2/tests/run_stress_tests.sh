#!/bin/bash

# Incrementar el límite de archivos abiertos
ulimit -n 10000

# Lanzar el servidor Gather con replicación
python ../src/gather_server_with_replication.py localhost:5557 localhost:5558 &

# Lanzar nodos clientes Gather
for i in {1..50}
do
    python ../src/gather_client_with_replication.py $i localhost:5557 localhost:5558 &
done

# Lanzar el servidor Broadcast
python ../src/broadcast_server_optimized.py &

# Lanzar nodos clientes Broadcast
for i in {1..50}
do
    python ../src/broadcast_client_optimized.py &
done
