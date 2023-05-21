import dearpygui.dearpygui as dpg

dpg.create_context()


def add_button():
    global new_button1, new_button2
    new_button1 = dpg.add_button(label='New Button',
                                 before='delete_button',
                                 tag='new_button1')
    new_button2 = dpg.add_button(label='New Button 2', parent='window23',
                                 tag='new_button2')


def delete_children():
    dpg.delete_item('window23', children_only=True)


def delete_buttons():
    dpg.delete_item('new_button1')
    dpg.delete_item('new_button2')


with dpg.window(label='Window1', pos=(0, 0)) as window1:
    dpg.add_button(label='add Buttons', callback=add_button)
    dpg.add_button(label='Delete Buttons', callback=delete_buttons,
                   tag='delete_button')

    slider_int = dpg.add_slider_int(label='Clide to the left', width=100)
    slider_float = dpg.add_slider_float(label='Slide to the right', width=100)
    print(
        f"Printing item tag's: {window1}, {slider_int},"
        f" {slider_float}")
    pass
button2 = dpg.add_button(label="Don't forget me!", parent=window1,
                         callback=delete_children)
with dpg.window(label='Window2', pos=(100, 0), tag='window23'):
    pass

dpg.create_viewport(title='Custom Title', width=600, height=200)

dpg.setup_dearpygui()

dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()
