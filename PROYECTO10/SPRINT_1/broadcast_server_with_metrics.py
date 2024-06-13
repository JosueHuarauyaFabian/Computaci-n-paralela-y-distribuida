import zmq
import time
import datetime
import psutil

def broadcast_server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5557")
    net_io_start = psutil.net_io_counters()

    start_time = time.time()

    while True:
        topic = "broadcast"
        message = f"Hello to all nodes {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}"
        print(f"Broadcasting: {message}")
        socket.send_string(f"{topic} {message}")
        time.sleep(1)

        net_io_current = psutil.net_io_counters()
        total_time = time.time() - start_time
        bytes_sent = net_io_current.bytes_sent - net_io_start.bytes_sent
        print(f"Bytes sent: {bytes_sent}, Time elapsed: {total_time:.2f} seconds")

if __name__ == "__main__":
    broadcast_server()
