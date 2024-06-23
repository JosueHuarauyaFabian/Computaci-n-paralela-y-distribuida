import zmq
import datetime
import time

def gather_client():
    node_id = input("Enter node ID: ")
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://localhost:5558")

    for i in range(10):
        send_time = datetime.datetime.now()
        message = f"Data from node {node_id}: {i} {send_time.strftime('%Y-%m-%d %H:%M:%S.%f')}"
        print(f"Sending: {message}")
        socket.send_string(message)
        time.sleep(1)

if __name__ == "__main__":
    gather_client()