from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

import dearpygui.dearpygui as dpg

dpg.create_context()

list_data = []
BUFSIZ = 1024


# class StateApp:
#     def __init__(self):
#         self.chats = []
#         self.states = {}
#         self.current_state = None
#
#     def get_state(self):
#         return self.current_state
#
#     def add_state(self, state):
#         if state not in self.states:
#
#     def set_state(self, state):
#         self.


class Connection:
    def __init__(self, ADDR):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(ADDR)
        receive_thread = Thread(target=self.receive)
        receive_thread.start()
        self.msgs = []

    def send(self, msg):
        self.client_socket.send(bytes(msg, "utf8"))

    def receive(self):
        while True:
            try:
                msg = self.client_socket.recv(BUFSIZ).decode("utf8")
                self.msgs.append(msg)
            except OSError:
                break
    pass


class App:
    def __init__(self):
        dpg.create_context()
        self.welcome_window()
        dpg.show_font_manager()
        dpg.create_viewport(title='Custom Title', width=600, height=200)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()



    def welcome_window(self):
        with dpg.window(tag='Primary Window') as primary_window:
            print(primary_window)
            dpg.add_tab_bar(label='hello work', tag=dpg.generate_uuid())
            dpg.add_tab_button(label='+', callback=self.new_tab, )
            dpg.add_button(label='hello', parent='tab1')
            dpg.add_button(label='World', parent='tab2')


    def connection_window(self, tab: str):
        pass

    def new_tab(self):
        dpg.add_tab(label='Chat', tag=dpg.generate_uuid())
        pass




app = App()


# def add_to_listbox(sender, app_data):
#     print(sender, app_data)
#     msg = dpg.get_value('text1')
#     send(msg)
#     dpg.configure_item('list1', items=list_data)
#     dpg.set_value('string_value', value=' ')
#     pass
#
#
# with dpg.font_registry():
#     with dpg.font("Assets/NotoSerifCJKjp-Medium.otf", 15) as font1:
#         dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
#         dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
#
# with dpg.value_registry():
#     dpg.add_string_value(default_value='entry text', tag='string_value')
#
# with dpg.window(tag="Primary Window"):
#     dpg.add_listbox(items=list_data, width=-1, num_items=10, tag='list1')
#     dpg.add_input_text(width=-1, tag='text1', on_enter=True,
#                        callback=add_to_listbox, source="string_value")
#     dpg.bind_font(font1)
#
# with dpg.window(tag='Connection Window'):
#     dpg.add_text('Введите Хост')
#     dpg.add_input_text(tag='HOST_INPUT')
#     dpg.add_text('Введите порт')
#     dpg.add_input_text(tag='PORT_INPUT')
#     dpg.add_button(label='Подключиться', callback=start_connection)
#
