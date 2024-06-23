import zmq
import time
import datetime

def broadcast_server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5557")

    while True:
        send_time = datetime.datetime.now()
        message = f"Broadcast message {send_time.strftime('%Y-%m-%d %H:%M:%S.%f')}"
        socket.send_string(message)
        print(f"Broadcasting: {message}")
        time.sleep(1)  # Adjust the sleep time as necessary

if __name__ == "__main__":
    broadcast_server()

