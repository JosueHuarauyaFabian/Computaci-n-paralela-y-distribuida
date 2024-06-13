import zmq
import time

def broadcast_server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")

    while True:
        topic = "broadcast"
        message = "Hello to all nodes"
        print(f"Broadcasting: {message}")
        socket.send_string(f"{topic} {message}")
        time.sleep(1)

if __name__ == "__main__":
    broadcast_server()
