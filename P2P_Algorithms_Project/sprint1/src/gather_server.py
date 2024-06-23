import zmq
import time

def gather_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")

    while True:
        message = socket.recv_string()
        print(f"Received data: {message}")
        socket.send_string(f"ACK {time.time()}")

if __name__ == "__main__":
    gather_server()
