import zlib
import zmq

def gather_client(node_id):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    for i in range(10):
        message = f"Data from node {node_id}: {i}"
        compressed_message = zlib.compress(message.encode())
        socket.send(compressed_message)
        reply = socket.recv_string()
        print(f"Received reply: {reply}")

if __name__ == "__main__":
    import sys
    node_id = int(sys.argv[1])
    gather_client(node_id)
