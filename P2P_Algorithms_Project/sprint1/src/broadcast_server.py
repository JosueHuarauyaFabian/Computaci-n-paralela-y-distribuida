import zmq
import time

def broadcast_server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")

    while True:
        message = f"Hello to all nodes {time.time()}"
        print(f"Broadcasting: {message}")
        socket.send_string(message)
        time.sleep(1)

if __name__ == "__main__":
    broadcast_server()
