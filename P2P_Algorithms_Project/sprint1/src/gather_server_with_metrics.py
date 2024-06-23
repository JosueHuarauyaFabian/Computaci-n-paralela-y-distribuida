import zmq
import datetime
from dateutil import parser

def gather_server():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://*:5558")

    while True:
        message = socket.recv_string()
        try:
            _, send_time_str = message.rsplit(' ', 1)
            send_time = parser.parse(send_time_str)
            recv_time = datetime.datetime.now()
            latency = (recv_time - send_time).total_seconds() * 1000  # Convertir a milisegundos
            print(f"Received: {message}, Latency: {latency:.2f} ms")
        except ValueError as e:
            print(f"Error parsing time from message: {e}, full message: {message}")

if __name__ == "__main__":
    gather_server()
