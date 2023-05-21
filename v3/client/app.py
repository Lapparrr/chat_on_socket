from socket import AF_INET, socket, SOCK_STREAM

import dearpygui.dearpygui as dpg

from threading import Thread
dpg.create_context()

list_data = []
BUFSIZ = 1024

def send(msg):
    client_socket.send(bytes(msg, "utf8"))


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            list_data.append(msg)
        except OSError:
            break


def start_connection(sender, app_data):
    global client_socket

    HOST = dpg.get_value("HOST_INPUT")
    PORT = int(dpg.get_value("PORT_INPUT"))
    ADDR = (HOST, PORT)
    print('подключаюст', ADDR)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)

    receive_thread = Thread(target=receive)
    receive_thread.start()
    pass


def add_to_listbox(sender, app_data):
    print(sender, app_data)
    msg = dpg.get_value('text1')
    send(msg)
    list_data.append(msg)
    dpg.configure_item('list1', items=list_data)
    dpg.set_value('string_value', value=' ')
    pass


with dpg.font_registry():
    with dpg.font("Assets/NotoSerifCJKjp-Medium.otf", 15) as font1:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

with dpg.value_registry():
    dpg.add_string_value(default_value='entry text', tag='string_value')

with dpg.window(tag="Primary Window"):
    dpg.add_listbox(items=list_data, width=-1, num_items=10, tag='list1')
    dpg.add_input_text(width=-1, tag='text1', on_enter=True,
                       callback=add_to_listbox, source="string_value")
    dpg.bind_font(font1)

with dpg.window(tag='Connection Window'):
    dpg.add_text('Введите Хост')
    dpg.add_input_text(tag='HOST_INPUT')
    dpg.add_text('Введите порт')
    dpg.add_input_text(tag='PORT_INPUT')
    dpg.add_button(label='Подключиться', callback=start_connection)

dpg.show_font_manager()
dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
