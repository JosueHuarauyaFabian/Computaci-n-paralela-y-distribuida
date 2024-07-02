import zlib
import zmq
import time

def broadcast_server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    while True:
        message = "Hello to all nodes"
        compressed_message = zlib.compress(message.encode())
        socket.send(compressed_message)
        print(f"Broadcasting: {message}")
        time.sleep(1)

if __name__ == "__main__":
    broadcast_server()
