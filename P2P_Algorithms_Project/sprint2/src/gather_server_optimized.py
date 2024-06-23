import zlib
import zmq

def gather_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    while True:
        compressed_message = socket.recv()
        message = zlib.decompress(compressed_message).decode()
        print(f"Received data: {message}")
        socket.send_string("ACK")

if __name__ == "__main__":
    gather_server()
