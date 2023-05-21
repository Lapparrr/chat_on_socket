#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break





def on_closing(event=None):
    my_msg.set("{quit}")
    send()

class App:

    def __init__(self, root: tkinter.Tk):
        root.title('Messenger')

        msg_frame = tkinter.Frame(root)
        msg = tkinter.StringVar()
        msg.set("Введите ваше сообщение здесь")

        scrollbar = tkinter.Scrollbar(msg_frame)
        msg_list = tkinter.Listbox(msg_frame, height=15, width=50,
                                   yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        msg_list.pack()
        msg_frame.pack()

        entry_field = tkinter.Entry(root, textvariable=msg)
        entry_field.bind("<Return>", send)
        entry_field.pack()

        send_button = tkinter.Button(root, text="отправить", command=app.send)
        send_button.pack()
        root.protocol("WM_DELETE_WINDOW", on_closing)



def send(self, event=None):
    msg = my_msg.get()
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

HOST = input('Введите хост: ')
PORT = input('Введите порт: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()