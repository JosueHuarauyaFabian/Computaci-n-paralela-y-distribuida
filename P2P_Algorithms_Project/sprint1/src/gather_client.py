import zmq
import time

def gather_client(node_id):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")

    for i in range(10):
        message = f"Data from node {node_id}: {i} {time.time()}"
        print(f"Sending: {message}")
        socket.send_string(message)
        reply = socket.recv_string()
        print(f"Received reply: {reply}")
        time.sleep(1)

if __name__ == "__main__":
    node_id = input("Enter node ID: ")
    gather_client(node_id)
