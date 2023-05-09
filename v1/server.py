import socket
import threading

PORT = 8050
ADDRESS = '0.0.0.0'

broadcast_list = []


def broadcast(message):
    for client in broadcast_list:
        client.send(message.encode())


def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        print(f"Received message : {message}")
        broadcast(message)


def thread_accept(soc):
    while True:
        soc.listen()
        client, client_address = soc.accept()
        broadcast_list.append(client)
        start_listening_thread(client)


def start_listening_thread(client):
    client_thread = threading.Thread(
        target=listen_thread,
        args=(client,)  # the list of argument for the function
    )
    client_thread.start()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ADDRESS, PORT))
    thread_accept(s)


