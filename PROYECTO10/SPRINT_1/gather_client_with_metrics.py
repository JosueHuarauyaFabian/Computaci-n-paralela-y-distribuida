import zmq
import datetime
import time

def gather_client(node_id):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://localhost:5558")

    for i in range(10):
        send_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        message = f"Data from node {node_id}: {i} {send_time}"
        print(f"Sending: {message}")
        socket.send_string(message)
        time.sleep(1)

if __name__ == "__main__":
    node_id = input("Enter node ID: ")
    gather_client(node_id)
