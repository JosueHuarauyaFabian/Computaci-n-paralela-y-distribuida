import zmq
import time
import sys
import multiprocessing

def server(port):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{port}")

    while True:
        message = socket.recv()
        print(f"Received request on port {port}: {message}")
        time.sleep(1)
        socket.send(b"World")

if __name__ == "__main__":
    ports = [5555, 5556]
    processes = []
    for port in ports:
        process = multiprocessing.Process(target=server, args=(port,))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
