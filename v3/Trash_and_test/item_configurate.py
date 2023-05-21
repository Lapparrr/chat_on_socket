import dearpygui.dearpygui as dpg

dpg.create_context()


def change_button():
    dpg.configure_item("item", enabled=False, label="New Label")


with dpg.window(width=500, height=300):
    dpg.add_button(enabled=True, label="Press me", tag="item",
                   callback=change_button)

    # at a later time, change the item's configuration

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
