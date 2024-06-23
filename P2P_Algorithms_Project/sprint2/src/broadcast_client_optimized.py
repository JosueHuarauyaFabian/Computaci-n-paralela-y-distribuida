import zlib
import zmq

def broadcast_client():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    while True:
        compressed_message = socket.recv()
        message = zlib.decompress(compressed_message).decode()
        print(f"Received broadcast: {message}")

if __name__ == "__main__":
    broadcast_client()
