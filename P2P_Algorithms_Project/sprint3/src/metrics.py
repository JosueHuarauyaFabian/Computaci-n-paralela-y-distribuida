import zlib
import zmq
import threading
import socket as py_socket
from flask import Blueprint, jsonify

metrics = Blueprint('metrics', __name__)

# Datos simulados para pruebas
data = {
    "latency": 0,
    "bandwidth": 0
}

# Función para replicar datos a los nodos de réplica
def replicate_data(data, replicas):
    for replica in replicas:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        try:
            socket.connect(f"tcp://{replica}")
            compressed_data = zlib.compress(data.encode())
            socket.send(compressed_data)
            reply = socket.recv_string()
            print(f"Replication reply: {reply}")
        finally:
            socket.close()

# Función para verificar si el puerto está en uso
def is_port_in_use(port):
    with py_socket.socket(py_socket.AF_INET, py_socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

# Simulación de recepción de datos de latencia y ancho de banda desde los clientes
def gather_server_with_replication(replicas, port=5556):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    
    if is_port_in_use(port):
        print(f"Port {port} is already in use.")
        return

    socket.bind(f"tcp://*:{port}")
    try:
        while True:
            compressed_message = socket.recv()
            message = zlib.decompress(compressed_message).decode()
            print(f"Received data: {message}")
            latency, bandwidth = map(float, message.split(","))
            data["latency"] = latency
            data["bandwidth"] = bandwidth
            threading.Thread(target=replicate_data, args=(message, replicas)).start()
            socket.send_string("ACK")
    finally:
        socket.close()

# Ruta de la API para obtener las métricas
@metrics.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify(data)

# Iniciar el servidor Gather en un hilo separado
replicas = []  # Define tus réplicas aquí
threading.Thread(target=gather_server_with_replication, args=(replicas,), daemon=True).start()
