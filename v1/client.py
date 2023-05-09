# client.py
import socket
import threading

host = "localhost"  # "127.0.1.1"
port = 8050


def thread_sending(soc):
    while True:
        message_to_send = input()
        soc.send(message_to_send.encode())


def thread_receiving(soc):
    while True:
        message = soc.recv(1024).decode()
        print(message)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    thread_send = threading.Thread(target=thread_sending, args=(s,))
    thread_receive = threading.Thread(target=thread_receiving, args=(s,))
    thread_send.start()
    thread_receive.start()
