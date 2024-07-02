import signal
import sys
from flask import Flask, render_template, jsonify, request
import threading
import zlib
import zmq

app = Flask(__name__)

data = {
    "latency": 0,
    "bandwidth": 0,
    "nodes": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics/metrics', methods=['GET'])
def get_metrics():
    return jsonify(data)

@app.route('/add_node', methods=['POST'])
def add_node():
    node_address = request.json.get('address')
    if node_address and node_address not in data["nodes"]:
        data["nodes"].append(node_address)
        return jsonify(success=True)
    return jsonify(success=False)

def gather_server_with_replication(replicas):
    context = zmq.Context.instance()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
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

def replicate_data(data, replicas):
    for replica in replicas:
        context = zmq.Context.instance()
        socket = context.socket(zmq.REQ)
        try:
            socket.connect(f"tcp://{replica}")
            compressed_data = zlib.compress(data.encode())
            socket.send(compressed_data)
            reply = socket.recv_string()
            print(f"Replication reply: {reply}")
        finally:
            socket.close()

def signal_handler(sig, frame):
    print('Stopping threads...')
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    replicas = []  # Define tus réplicas aquí
    server_thread = threading.Thread(target=gather_server_with_replication, args=(replicas,))
    server_thread.start()
    app.run(debug=True)
