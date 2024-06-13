import zmq
import time

def gather_server():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://*:5557")

    while True:
        message = socket.recv_string()
        print(f"Gathered data: {message}")

if __name__ == "__main__":
    gather_server()
