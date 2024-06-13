import zmq
import datetime

def broadcast_client():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5557")
    socket.setsockopt_string(zmq.SUBSCRIBE, "broadcast")

    while True:
        message = socket.recv_string()
        receive_time = datetime.datetime.now()
        try:
            _, content, send_time_str = message.rsplit(" ", 2)  # Usar rsplit para dividir correctamente
            send_time = datetime.datetime.strptime(send_time_str, "%Y-%m-%d %H:%M:%S.%f")
            latency = (receive_time - send_time).total_seconds()
            print(f"Received: {content}, Latency: {latency:.6f} seconds")
        except ValueError as e:
            print(f"Error parsing time from message: {e}, full message: {message}")

if __name__ == "__main__":
    broadcast_client()
