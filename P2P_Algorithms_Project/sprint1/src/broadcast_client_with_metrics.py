import zmq
import datetime
from dateutil import parser

def broadcast_client():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5557")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    while True:
        message = socket.recv_string()
        print(f"Received broadcast: {message}")
        # Parse the message to extract time and calculate latency
        try:
            send_time_str = message.split()[-1]
            send_time = parser.parse(send_time_str)
            recv_time = datetime.datetime.now()
            latency = (recv_time - send_time).total_seconds()
            print(f"Latency: {latency:.6f} seconds")
        except Exception as e:
            print(f"Error parsing time from message: {e}, full message: {message}")

if __name__ == "__main__":
    broadcast_client()
