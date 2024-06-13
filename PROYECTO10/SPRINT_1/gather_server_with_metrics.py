import zmq
import time
import datetime

def gather_server():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://*:5558")

    while True:
        message = socket.recv_string()
        receive_time = datetime.datetime.now()
        try:
            data, send_time_str = message.rsplit(" ", 1)
            send_time = datetime.datetime.strptime(send_time_str, "%Y-%m-%d %H:%M:%S.%f")
            latency = (receive_time - send_time).total_seconds()
            print(f"Gathered data: {data}, Latency: {latency:.6f} seconds")
        except ValueError as e:
            print(f"Error parsing time from message: {e}, full message: {message}")

if __name__ == "__main__":
    gather_server()
