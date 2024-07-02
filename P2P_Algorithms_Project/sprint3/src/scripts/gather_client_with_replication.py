import zlib
import zmq
import time
import random
import sys
import threading

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

def gather_client_with_replication(node_id, replicas):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
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

if __name__ == "__main__":
    node_id = int(sys.argv[1])
    replicas = sys.argv[2:]
    gather_client_with_replication(node_id, replicas)
