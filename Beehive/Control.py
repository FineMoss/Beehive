
# Created by Jake Stephens


class Control():


    def __init__(self, frame):
        self.__frame                           = frame
        self.__frame.archive_button["command"] = self.archive
        self.__frame.clear_button["command"]   = self.clear
        self.__frame.confirm_button["command"] = self.confirm
        self.__frame.cancel_button["command"]  = self.cancel


    def archive(self):
        print("TODO: Control.archive()")


    def confirm(self):
        print("TODO: Control.confirm()")


    def cancel(self):
        self.text_field["state"] = "normal"
        self.text_field.delete("1.0", "end")
        self.text_field["state"] = "disabled"
        self.unlock_fields()
        print("MORE TODO: Control.cancel()")


    def clear(self):
        self.__frame.current_entry.delete("0", "end")
        self.__frame.target_entry.delete("0", "end")
        self.__frame.date_entry.delete("0", "end")
        self.__frame.text_field["state"] = "normal"
        self.__frame.text_field.delete("1.0", "end")
        self.__frame.text_field["state"] = "disabled"


    def __lock_fields(self):
        self.__frame.current_entry["state"]  = "disabled"
        self.__frame.target_entry["state"]   = "disabled"
        self.__frame.date_entry["state"]     = "disabled"
        self.__frame.archive_button["state"] = "disabled"
        self.__frame.clear_button["state"]   = "disabled"
        self.__frame.confirm_button["state"] = "normal"
        self.__frame.cancel_button["state"]  = "normal"


    def __unlock_fields(self):
        self.__frame.current_entry["state"]  = "normal"
        self.__frame.target_entry["state"]   = "normal"
        self.__frame.date_entry["state"]     = "normal"
        self.__frame.archive_button["state"] = "normal"
        self.__frame.clear_button["state"]   = "normal"
        self.__frame.confirm_button["state"] = "disable"
        self.__frame.cancel_button["state"]  = "disable"