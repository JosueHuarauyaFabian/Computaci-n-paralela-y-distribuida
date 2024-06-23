import zlib
import zmq
import sys
import threading

def replicate_data(data, replicas):
    for replica in replicas:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(f"tcp://{replica}")
        compressed_data = zlib.compress(data.encode())
        socket.send(compressed_data)
        reply = socket.recv_string()
        print(f"Replication reply: {reply}")

def gather_client_with_replication(node_id, replicas):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    for i in range(10):
        message = f"Data from node {node_id}: {i}"
        compressed_message = zlib.compress(message.encode())
        socket.send(compressed_message)
        reply = socket.recv_string()
        print(f"Received reply: {reply}")
        threading.Thread(target=replicate_data, args=(message, replicas)).start()

if __name__ == "__main__":
    node_id = int(sys.argv[1])
    replicas = sys.argv[2:]
    gather_client_with_replication(node_id, replicas)
