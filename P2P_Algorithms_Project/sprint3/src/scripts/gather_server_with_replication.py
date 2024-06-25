import zlib
import zmq
import threading
import sys

data = {
    "latency": 0,
    "bandwidth": 0
}

def replicate_data(data, replicas):
    for replica in replicas:
        context = zmq.Context.instance()
        socket = context.socket(zmq.REQ)
        try:
            socket.connect(f"tcp://{replica}")
            compressed_data = zlib.compress(data.encode())
            socket.send(compressed_data)
            reply = socket.recv_string()
            print(f"Replication reply: {reply}")
        finally:
            socket.close()

def gather_server_with_replication(replicas):
    context = zmq.Context.instance()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    try:
        while True:
            compressed_message = socket.recv()
            message = zlib.decompress(compressed_message).decode()
            print(f"Received data: {message}")
            latency, bandwidth = map(float, message.split(","))
            data["latency"] = latency
            data["bandwidth"] = bandwidth
            threading.Thread(target=replicate_data, args=(message, replicas)).start()
            socket.send_string("ACK")
    finally:
        socket.close()

if __name__ == "__main__":
    replicas = sys.argv[1:]
    gather_server_with_replication(replicas)
