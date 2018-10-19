
# Created by Jake Stephens


class Control():


    def __init__(self, model, view):
        self.__model                          = model
        self.__view                           = view
        self.__view.archive_button["command"] = self.archive
        self.__view.clear_button["command"]   = self.clear
        self.__view.confirm_button["command"] = self.confirm
        self.__view.cancel_button["command"]  = self.cancel


    def archive(self):
        print("TODO: Control.archive()")


    def confirm(self):
        print("TODO: Control.confirm()")


    def cancel(self):
        self.__view.text_field["state"] = "normal"
        self.__view.text_field.delete("1.0", "end")
        self.__view.text_field["state"] = "disabled"
        self.unlock_fields()
        print("MORE TODO: Control.cancel()")


    def clear(self):
        self.__view.current_entry.delete("0", "end")
        self.__view.target_entry.delete("0", "end")
        self.__view.date_entry.delete("0", "end")
        self.__view.text_field["state"] = "normal"
        self.__view.text_field.delete("1.0", "end")
        self.__view.text_field["state"] = "disabled"


    def __lock_fields(self):
        self.__view.current_entry["state"]  = "disabled"
        self.__view.target_entry["state"]   = "disabled"
        self.__view.date_entry["state"]     = "disabled"
        self.__view.archive_button["state"] = "disabled"
        self.__view.clear_button["state"]   = "disabled"
        self.__view.confirm_button["state"] = "normal"
        self.__view.cancel_button["state"]  = "normal"


    def __unlock_fields(self):
        self.__view.current_entry["state"]  = "normal"
        self.__view.target_entry["state"]   = "normal"
        self.__view.date_entry["state"]     = "normal"
        self.__view.archive_button["state"] = "normal"
        self.__view.clear_button["state"]   = "normal"
        self.__view.confirm_button["state"] = "disable"
        self.__view.cancel_button["state"]  = "disable"