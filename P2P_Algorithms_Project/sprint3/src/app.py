import signal
import sys
from flask import Flask, render_template, jsonify, Blueprint
import threading
import subprocess
import zlib
import zmq
import time
import random

app = Flask(__name__)

data = {
    "latency": 0,
    "bandwidth": 0
}

# Define el blueprint para las métricas
metrics_bp = Blueprint('metrics_bp', __name__)

@metrics_bp.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify(data)

app.register_blueprint(metrics_bp, url_prefix='/metrics')

@app.route('/')
def index():
    return render_template('index.html')

def replicate_data(message, replicas):
    for replica in replicas:
        context = zmq.Context.instance()
        socket = context.socket(zmq.REQ)
        try:
            socket.connect(f"tcp://{replica}")
            compressed_data = zlib.compress(message.encode())
            socket.send(compressed_data)
            reply = socket.recv_string()
            print(f"Replication reply: {reply}")
        finally:
            socket.close()

def gather_server_with_replication(replicas, port=5556):
    context = zmq.Context.instance()
    socket = context.socket(zmq.REP)
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

def gather_client_with_replication(node_id, replicas, port=5556):
    context = zmq.Context.instance()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{port}")
    while True:
        latency = random.uniform(20, 100)  # Simulating latency
        bandwidth = random.uniform(10, 100)  # Simulating bandwidth
        message = f"{latency},{bandwidth}"
        compressed_message = zlib.compress(message.encode())
        socket.send(compressed_message)
        reply = socket.recv_string()
        print(f"Received reply: {reply}")
        threading.Thread(target=replicate_data, args=(message, replicas)).start()
        time.sleep(1)

def run_gather_server():
    gather_server_with_replication([], port=5556)

def run_gather_client(client_id):
    gather_client_with_replication(client_id, [], port=5556)

def signal_handler(sig, frame):
    print('Stopping threads...')
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    
    # Asegúrate de matar procesos anteriores que utilizan el puerto 5556
    subprocess.run(["kill $(lsof -t -i:5556) 2>/dev/null"], shell=True)
    
    # Iniciar el servidor gather en un hilo separado
    server_thread = threading.Thread(target=run_gather_server)
    server_thread.start()

    # Iniciar los clientes gather en hilos separados
    for i in range(1, 6):
        client_thread = threading.Thread(target=run_gather_client, args=(i,))
        client_thread.start()

    app.run(debug=True)
