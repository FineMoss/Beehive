
# Created by Jake Stephens


class Control():

    # create reference to the model and the view
    def __init__(self, model, view):
        self.__model = model
        self.__view  = view
        self.__map_buttons()

    # maps the buttons to the commands
    def __map_buttons(self):
        self.__view.archive_button["command"] = self.__archive
        self.__view.clear_button["command"]   = self.__clear
        self.__view.confirm_button["command"] = self.__confirm
        self.__view.cancel_button["command"]  = self.__cancel

    # command for archive button
    def __archive(self):
        print("TODO: Control.archive()")

    # command for confirm button
    def __confirm(self):
        print("TODO: Control.confirm()")

    # command for cancel button
    def __cancel(self):
        self.__view.text_field["state"] = "normal"
        self.__view.text_field.delete("1.0", "end")
        self.__view.text_field["state"] = "disabled"
        self.__unlock_fields()
        print("MORE TODO: Control.cancel()")

    # command for clear button
    def __clear(self):
        self.__view.current_entry.delete("0", "end")
        self.__view.target_entry.delete("0", "end")
        self.__view.date_entry.delete("0", "end")
        self.__view.text_field["state"] = "normal"
        self.__view.text_field.delete("1.0", "end")
        self.__view.text_field["state"] = "disabled"

    # helper function
    def __lock_fields(self):
        self.__view.current_entry["state"]  = "disabled"
        self.__view.target_entry["state"]   = "disabled"
        self.__view.date_entry["state"]     = "disabled"
        self.__view.archive_button["state"] = "disabled"
        self.__view.clear_button["state"]   = "disabled"
        self.__view.confirm_button["state"] = "normal"
        self.__view.cancel_button["state"]  = "normal"

    # helper fuction
    def __unlock_fields(self):
        self.__view.current_entry["state"]  = "normal"
        self.__view.target_entry["state"]   = "normal"
        self.__view.date_entry["state"]     = "normal"
        self.__view.archive_button["state"] = "normal"
        self.__view.clear_button["state"]   = "normal"
        self.__view.confirm_button["state"] = "disable"
        self.__view.cancel_button["state"]  = "disable"