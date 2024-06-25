#!/bin/bash

# Asegúrate de matar procesos anteriores
kill $(lsof -t -i:5556) 2>/dev/null

# Ejecutar el servidor Gather
python3 scripts/gather_server_with_replication.py &

# Ejecutar varios clientes Gather
for i in {1..5}
do
    python3 scripts/gather_client_with_replication.py $i &
done
