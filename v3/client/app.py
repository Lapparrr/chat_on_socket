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
        self.msgs = []
        receive_thread = Thread(target=self.receive)
        receive_thread.start()

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
        self.cons = {}
        self.msg = {}

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
        with dpg.window(tag='Primary Window'):
            dpg.add_tab_bar(label='hello work', tag='tab_bar')
            self.new_tab()
            dpg.add_tab_button(label='+', callback=self.new_tab,
                               parent='tab_bar', trailing=True)

    def send_msg(self, sender, app_data):
        tab = dpg.get_item_parent(sender)
        listbox_id = dpg.get_item_children(tab, 1)[0]
        self.cons[tab].send(app_data)
        dpg.configure_item(listbox_id, items=self.cons[tab].msgs)

    def connection_window(self, sender, app_data):
        parent = dpg.get_item_parent(sender)
        ids = dpg.get_item_children(parent, 1)
        host = dpg.get_value(ids[1])
        port = int(dpg.get_value(ids[3]))
        dpg.delete_item(children_only=True, item=parent)
        con = Connection((host, port))
        self.cons[parent] = con

        with dpg.value_registry():
            tag_string = dpg.generate_uuid()
            dpg.add_string_value(default_value='entry text',
                                 tag=tag_string)
        dpg.add_listbox(self.cons[parent].msgs, width=-1, num_items=10,
                        parent=parent)
        dpg.add_input_text(width=-1, tag='text1', on_enter=True,
                           callback=self.send_msg,
                           source=tag_string, parent=parent)

    def new_tab(self):
        with dpg.tab(parent='tab_bar', label='Chat',
                     tag=dpg.generate_uuid()) as tab:
            tag_host_input = dpg.generate_uuid()
            tag_port_input = dpg.generate_uuid()
            dpg.add_text('Input HOST')
            dpg.add_input_text(tag=tag_host_input)
            dpg.add_text("Input PORT")
            dpg.add_input_text(tag=tag_port_input)
            dpg.add_button(label='Connect', callback=self.connection_window)
        pass


app = App()

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
#
#     dpg.bind_font(font1)
#
# with dpg.window(tag='Connection Window'):
#     dpg.add_text('Введите Хост')
#     dpg.add_input_text(tag='HOST_INPUT')
#     dpg.add_text('Введите порт')
#     dpg.add_input_text(tag='PORT_INPUT')
#     dpg.add_button(label='Подключиться', callback=start_connection)
#
