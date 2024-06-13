import zmq
import sys
import multiprocessing

def client(port):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{port}")

    for request in range(10):
        print(f"Sending request to port {port}: {request}")
        socket.send(b"Hello")
        message = socket.recv()
        print(f"Received reply from port {port}: {message}")

if __name__ == "__main__":
    ports = [5555, 5556]
    processes = []
    for port in ports:
        process = multiprocessing.Process(target=client, args=(port,))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
